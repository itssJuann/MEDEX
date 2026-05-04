from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from data import PATHOLOGIES
from learning_data import LEARNING
from differentials import DIFFERENTIALS
from algorithms import ALGORITHMS
from clinical_images import CLINICAL_IMAGES
from anatomy import ORGANS
from quizzes import QUIZZES
from database import get_db, engine, Base
from auth import hash_password, verify_password, create_token, get_current_user
import models

Base.metadata.create_all(bind=engine)


ADMIN_SECRET = "medex-admin-2024"   # share this code with educators/moderators

def _is_admin(user_id: int, db: Session) -> bool:
    """user_id == 1 is always admin; others only if in admin_users table."""
    if user_id == 1:
        return True
    return db.query(models.AdminUser).filter(models.AdminUser.user_id == user_id).first() is not None

app = FastAPI(title="MediClinic API")

import os as _os

_FRONTEND = _os.getenv("FRONTEND_URL", "*")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[_FRONTEND] if _FRONTEND != "*" else ["*"],
    allow_credentials=_FRONTEND != "*",
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Schemas ----------

class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str

class LoginSchema(BaseModel):
    email: str
    password: str

# ---------- Auth routes ----------

@app.post("/register", status_code=201)
def register(body: RegisterSchema, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == body.email).first():
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")
    user = models.User(
        name=body.name,
        email=body.email,
        hashed_password=hash_password(body.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_token(user.email)
    return {"token": token, "id": user.id, "name": user.name, "email": user.email, "is_admin": _is_admin(user.id, db)}

@app.post("/login")
def login(body: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == body.email).first()
    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos.")
    token = create_token(user.email)
    return {"token": token, "id": user.id, "name": user.name, "email": user.email, "is_admin": _is_admin(user.id, db)}

@app.get("/me")
def me(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return {"id": current_user.id, "name": current_user.name, "email": current_user.email, "is_admin": _is_admin(current_user.id, db)}

# ---------- User settings routes (protected) ----------

class UpdateProfileSchema(BaseModel):
    name: str

class UpdatePasswordSchema(BaseModel):
    current_password: str
    new_password: str

class AdminClaimSchema(BaseModel):
    code: str

@app.post("/admin/claim")
def claim_admin(body: AdminClaimSchema, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if body.code.strip() != ADMIN_SECRET:
        raise HTTPException(status_code=400, detail="Código de administrador incorrecto.")
    existing = db.query(models.AdminUser).filter(models.AdminUser.user_id == current_user.id).first()
    if not existing:
        db.add(models.AdminUser(user_id=current_user.id))
        db.commit()
    return {"ok": True, "is_admin": True, "id": current_user.id, "name": current_user.name, "email": current_user.email}

@app.put("/me")
def update_profile(body: UpdateProfileSchema, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if not body.name.strip():
        raise HTTPException(status_code=400, detail="El nombre no puede estar vacío.")
    current_user.name = body.name.strip()
    db.commit()
    return {"name": current_user.name, "email": current_user.email}

@app.put("/me/password")
def update_password(body: UpdatePasswordSchema, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if not verify_password(body.current_password, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="La contraseña actual es incorrecta.")
    if len(body.new_password) < 6:
        raise HTTPException(status_code=400, detail="La nueva contraseña debe tener al menos 6 caracteres.")
    current_user.hashed_password = hash_password(body.new_password)
    db.commit()
    return {"ok": True}

# ---------- Progress routes (protected) ----------

RESULT_RANK = {"success": 2, "warning": 1, "failure": 0}

class ProgressSchema(BaseModel):
    module_type: str = "case"
    item_id: str
    result: str

def _key(module_type: str, item_id: str) -> str:
    """Encode module+item into the pathology_id column."""
    return item_id if module_type == "case" else f"{module_type}:{item_id}"

def _decode(pathology_id: str) -> dict:
    """Decode back from pathology_id column."""
    if ":" in pathology_id:
        mt, iid = pathology_id.split(":", 1)
        return {"module_type": mt, "item_id": iid}
    return {"module_type": "case", "item_id": pathology_id}

@app.post("/progress", status_code=200)
def save_progress(body: ProgressSchema, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if body.result not in RESULT_RANK:
        raise HTTPException(status_code=400, detail="Resultado inválido.")
    from datetime import datetime
    key = _key(body.module_type, body.item_id)
    existing = db.query(models.Progress).filter(
        models.Progress.user_id == current_user.id,
        models.Progress.pathology_id == key,
    ).first()
    if existing:
        existing.attempts += 1
        if RESULT_RANK[body.result] > RESULT_RANK[existing.best_result]:
            existing.best_result = body.result
        existing.updated_at = datetime.utcnow()
    else:
        db.add(models.Progress(
            user_id=current_user.id,
            pathology_id=key,
            best_result=body.result,
        ))
    db.commit()
    return {"ok": True}

@app.get("/progress")
def get_progress(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    rows = db.query(models.Progress).filter(
        models.Progress.user_id == current_user.id
    ).all()
    return [
        {
            **_decode(r.pathology_id),
            "pathology_id": r.pathology_id,
            "best_result":  r.best_result,
            "attempts":     r.attempts,
        }
        for r in rows
    ]

# ---------- Quiz routes (public) ----------

@app.get("/quizzes")
def get_quizzes():
    return [
        {
            "id": q["id"],
            "title": q["title"],
            "system": q["system"],
            "difficulty": q["difficulty"],
            "description": q["description"],
            "question_count": q["question_count"],
        }
        for q in QUIZZES
    ]

@app.get("/quizzes/{quiz_id}")
def get_quiz(quiz_id: str):
    q = next((q for q in QUIZZES if q["id"] == quiz_id), None)
    if not q:
        raise HTTPException(status_code=404, detail="Quiz no encontrado.")
    return q

# ---------- Anatomy routes (public) ----------

@app.get("/anatomy")
def get_anatomy():
    return [
        {
            "id": o["id"],
            "name": o["name"],
            "system": o["system"],
            "color": o["color"],
            "svg_zone": o["svg_zone"],
            "pathology_count": len(o["pathologies"]),
        }
        for o in ORGANS
    ]

@app.get("/anatomy/{organ_id}")
def get_anatomy_organ(organ_id: str):
    organ = next((o for o in ORGANS if o["id"] == organ_id), None)
    if not organ:
        raise HTTPException(status_code=404, detail="Órgano no encontrado.")
    # Enrich pathologies with case data
    enriched = []
    for p in organ["pathologies"]:
        case = next((c for c in PATHOLOGIES if c["id"] == p["id_case"]), None)
        enriched.append({
            **p,
            "difficulty": case["difficulty"] if case else "Intermedio",
            "summary": case["summary"] if case else "",
        })
    return {**organ, "pathologies": enriched}

# ---------- Clinical image routes (public) ----------

@app.get("/clinical-images")
def get_clinical_images():
    return [
        {
            "id": c["id"],
            "title": c["title"],
            "modality": c["modality"],
            "system": c["system"],
            "difficulty": c["difficulty"],
            "presentation": c["presentation"],
            "question_count": len(c["questions"]),
        }
        for c in CLINICAL_IMAGES
    ]

@app.get("/clinical-images/{image_id}")
def get_clinical_image(image_id: str):
    c = next((c for c in CLINICAL_IMAGES if c["id"] == image_id), None)
    if not c:
        raise HTTPException(status_code=404, detail="Caso no encontrado.")
    return c

# ---------- Algorithm routes (public) ----------

@app.get("/algorithms")
def get_algorithms():
    return [
        {
            "id": a["id"],
            "title": a["title"],
            "specialty": a["specialty"],
            "difficulty": a["difficulty"],
            "description": a["description"],
            "guideline": a["guideline"],
            "node_count": len(a["nodes"]),
        }
        for a in ALGORITHMS
    ]

@app.get("/algorithms/{algo_id}")
def get_algorithm(algo_id: str):
    a = next((a for a in ALGORITHMS if a["id"] == algo_id), None)
    if not a:
        raise HTTPException(status_code=404, detail="Algoritmo no encontrado.")
    return a

# ---------- Differential routes (public) ----------

@app.get("/differentials")
def get_differentials():
    return [
        {
            "id": d["id"],
            "title": d["title"],
            "system": d["system"],
            "difficulty": d["difficulty"],
            "presentation": d["presentation"],
            "diagnosis_count": len(d["diagnoses"]),
        }
        for d in DIFFERENTIALS
    ]

@app.get("/differentials/{diff_id}")
def get_differential(diff_id: str):
    d = next((d for d in DIFFERENTIALS if d["id"] == diff_id), None)
    if not d:
        raise HTTPException(status_code=404, detail="Caso no encontrado.")
    return d

# ---------- Pathology routes (public) ----------

@app.get("/pathologies")
def get_pathologies():
    return [
        {
            "id": p["id"],
            "name": p["name"],
            "system": p["system"],
            "difficulty": p["difficulty"],
            "summary": p["summary"],
        }
        for p in PATHOLOGIES
    ]

@app.get("/pathologies/{pathology_id}")
def get_pathology(pathology_id: str):
    p = next((p for p in PATHOLOGIES if p["id"] == pathology_id), None)
    if not p:
        raise HTTPException(status_code=404, detail="Patología no encontrada.")
    return {**p, "learning": LEARNING.get(pathology_id)}

# ---------- Comment routes ----------

COMMENT_TYPES = {"duda", "perla", "correccion"}

class CommentSchema(BaseModel):
    type: str
    content: str

@app.get("/pathologies/{pathology_id}/comments")
def get_comments(pathology_id: str, db: Session = Depends(get_db)):
    rows = (
        db.query(models.Comment, models.User.name)
        .join(models.User, models.Comment.user_id == models.User.id)
        .filter(models.Comment.pathology_id == pathology_id)
        .order_by(models.Comment.created_at.asc())
        .all()
    )
    return [
        {
            "id":           c.id,
            "user_id":      c.user_id,
            "user_name":    name,
            "type":         c.type,
            "content":      c.content,
            "created_at":   c.created_at.isoformat(),
        }
        for c, name in rows
    ]

@app.post("/pathologies/{pathology_id}/comments", status_code=201)
def post_comment(
    pathology_id: str,
    body: CommentSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if body.type not in COMMENT_TYPES:
        raise HTTPException(status_code=400, detail="Tipo inválido.")
    if not body.content.strip():
        raise HTTPException(status_code=400, detail="El contenido no puede estar vacío.")
    comment = models.Comment(
        user_id=current_user.id,
        pathology_id=pathology_id,
        type=body.type,
        content=body.content.strip(),
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return {
        "id":         comment.id,
        "user_id":    comment.user_id,
        "user_name":  current_user.name,
        "type":       comment.type,
        "content":    comment.content,
        "created_at": comment.created_at.isoformat(),
    }

@app.delete("/comments/{comment_id}", status_code=200)
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado.")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="No puedes eliminar este comentario.")
    db.delete(comment)
    db.commit()
    return {"ok": True}

# ---------- Community cases routes ----------

VALID_SYSTEMS     = {"Cardiovascular","Respiratorio","Digestivo","Neurológico","Endocrino","Infeccioso","Renal"}
VALID_DIFFICULTIES = {"Básico","Intermedio","Avanzado"}

class CommunityCaseSchema(BaseModel):
    title:        str
    system:       str
    difficulty:   str
    summary:      str
    presentation: str
    questions:    list   # list of question dicts
    diagnosis:    str
    pearl:        str = ""

class ModerateSchema(BaseModel):
    action:  str   # "approve" | "reject"
    note:    str = ""

def _fmt_community(c: models.CommunityCase, author_name: str, include_questions: bool = False) -> dict:
    import json as _json
    base = {
        "id":           c.id,
        "user_id":      c.user_id,
        "author":       author_name,
        "title":        c.title,
        "system":       c.system,
        "difficulty":   c.difficulty,
        "summary":      c.summary,
        "status":       c.status,
        "mod_note":     c.mod_note,
        "created_at":   c.created_at.isoformat(),
    }
    if include_questions:
        base["presentation"] = c.presentation
        base["questions"]    = _json.loads(c.questions)
        base["diagnosis"]    = c.diagnosis
        base["pearl"]        = c.pearl or ""
    return base

@app.post("/community-cases", status_code=201)
def create_community_case(
    body: CommunityCaseSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    import json as _json
    if body.system not in VALID_SYSTEMS:
        raise HTTPException(status_code=400, detail="Sistema inválido.")
    if body.difficulty not in VALID_DIFFICULTIES:
        raise HTTPException(status_code=400, detail="Dificultad inválida.")
    if not body.title.strip() or not body.presentation.strip() or not body.diagnosis.strip():
        raise HTTPException(status_code=400, detail="Faltan campos obligatorios.")
    if len(body.questions) < 2:
        raise HTTPException(status_code=400, detail="El caso debe tener al menos 2 preguntas.")
    case = models.CommunityCase(
        user_id=current_user.id,
        title=body.title.strip(),
        system=body.system,
        difficulty=body.difficulty,
        summary=body.summary.strip(),
        presentation=body.presentation.strip(),
        questions=_json.dumps(body.questions, ensure_ascii=False),
        diagnosis=body.diagnosis.strip(),
        pearl=body.pearl.strip(),
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    return {"id": case.id, "status": case.status}

@app.get("/community-cases")
def list_community_cases(db: Session = Depends(get_db)):
    rows = (
        db.query(models.CommunityCase, models.User.name)
        .join(models.User, models.CommunityCase.user_id == models.User.id)
        .filter(models.CommunityCase.status == "approved")
        .order_by(models.CommunityCase.created_at.desc())
        .all()
    )
    return [_fmt_community(c, name) for c, name in rows]

@app.get("/community-cases/pending")
def list_pending_cases(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if not _is_admin(current_user.id, db):
        raise HTTPException(status_code=403, detail="Solo el moderador puede ver casos pendientes.")
    rows = (
        db.query(models.CommunityCase, models.User.name)
        .join(models.User, models.CommunityCase.user_id == models.User.id)
        .filter(models.CommunityCase.status == "pending")
        .order_by(models.CommunityCase.created_at.asc())
        .all()
    )
    return [_fmt_community(c, name, include_questions=True) for c, name in rows]

@app.get("/community-cases/mine")
def list_my_cases(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    rows = (
        db.query(models.CommunityCase, models.User.name)
        .join(models.User, models.CommunityCase.user_id == models.User.id)
        .filter(models.CommunityCase.user_id == current_user.id)
        .order_by(models.CommunityCase.created_at.desc())
        .all()
    )
    return [_fmt_community(c, name) for c, name in rows]

@app.get("/community-cases/{case_id}")
def get_community_case(case_id: int, db: Session = Depends(get_db)):
    row = (
        db.query(models.CommunityCase, models.User.name)
        .join(models.User, models.CommunityCase.user_id == models.User.id)
        .filter(models.CommunityCase.id == case_id, models.CommunityCase.status == "approved")
        .first()
    )
    if not row:
        raise HTTPException(status_code=404, detail="Caso no encontrado.")
    c, name = row
    return _fmt_community(c, name, include_questions=True)

@app.post("/community-cases/{case_id}/moderate", status_code=200)
def moderate_case(
    case_id: int,
    body: ModerateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if not _is_admin(current_user.id, db):
        raise HTTPException(status_code=403, detail="Solo el moderador puede moderar casos.")
    if body.action not in ("approve", "reject"):
        raise HTTPException(status_code=400, detail="Acción inválida.")
    case = db.query(models.CommunityCase).filter(models.CommunityCase.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Caso no encontrado.")
    case.status   = "approved" if body.action == "approve" else "rejected"
    case.mod_note = body.note.strip() or None
    db.commit()
    return {"ok": True, "status": case.status}
