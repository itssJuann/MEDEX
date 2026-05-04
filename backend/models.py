from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String, nullable=False)
    email           = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Comment(Base):
    __tablename__ = "comments"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id"), nullable=False)
    pathology_id = Column(String, nullable=False, index=True)
    type         = Column(String, nullable=False)   # duda | perla | correccion
    content      = Column(String, nullable=False)
    created_at   = Column(DateTime, default=datetime.utcnow)

class AdminUser(Base):
    """Users with moderation/admin privileges."""
    __tablename__ = "admin_users"

    id      = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

class CommunityCase(Base):
    """Cases created by users, reviewed before going live."""
    __tablename__ = "community_cases"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id"), nullable=False)
    title        = Column(String, nullable=False)
    system       = Column(String, nullable=False)
    difficulty   = Column(String, nullable=False)
    summary      = Column(String, nullable=False)
    presentation = Column(String, nullable=False)
    questions    = Column(String, nullable=False)   # JSON string
    diagnosis    = Column(String, nullable=False)
    pearl        = Column(String, nullable=True)
    status       = Column(String, default="pending")  # pending | approved | rejected
    mod_note     = Column(String, nullable=True)
    created_at   = Column(DateTime, default=datetime.utcnow)

class Progress(Base):
    """
    Stores progress for ALL modules.
    pathology_id format:
      - Cases:          "infarto-agudo-miocardio"
      - Other modules:  "differential:dolor-toracico-agudo"
                        "algorithm:manejo-sepsis-shock"
                        "image:ecg-iamcest"
                        "quiz:cardio-urgente"
    This works with the original DB schema — no migration needed.
    """
    __tablename__ = "progress"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id"), nullable=False)
    pathology_id = Column(String, nullable=False)
    best_result  = Column(String, nullable=False)
    attempts     = Column(Integer, default=1)
    updated_at   = Column(DateTime, default=datetime.utcnow)
