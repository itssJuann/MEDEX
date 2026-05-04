RX_BASE = """
<svg viewBox="0 0 400 480" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">
  <!-- Warm anatomical illustration background -->
  <rect width="400" height="480" fill="#f6f1ec"/>
  <text x="200" y="14" text-anchor="middle" fill="#c0b0a0" font-size="8" font-family="sans-serif" font-weight="600">TÓRAX — ILUSTRACIÓN ANATÓMICA</text>

  <!-- Body silhouette (skin tone) -->
  <path d="M88 90 Q52 198 48 350 Q54 422 106 454 Q150 474 200 476 Q250 474 294 454 Q346 422 352 350 Q348 198 312 90 Q286 78 248 72 Q200 68 152 72 Q114 78 88 90 Z" fill="#ede4d8" stroke="#c8b8a4" stroke-width="1.5"/>
  <!-- Neck -->
  <rect x="185" y="18" width="30" height="74" rx="13" fill="#ede4d8" stroke="#c8b8a4" stroke-width="1.2"/>

  <!-- ── CLAVICLES (cortical bone, ivory) ── -->
  <path d="M200 98 Q163 87,130 98 Q105 108,88 126" stroke="#e2d4bc" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M200 98 Q237 87,270 98 Q295 108,312 126" stroke="#e2d4bc" stroke-width="7" fill="none" stroke-linecap="round"/>
  <!-- Cortical highlight -->
  <path d="M200 98 Q163 87,130 98 Q105 108,88 126" stroke="#f0e8d4" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M200 98 Q237 87,270 98 Q295 108,312 126" stroke="#f0e8d4" stroke-width="3" fill="none" stroke-linecap="round"/>

  <!-- ── SPINE (vertebral column) ── -->
  <rect x="192" y="102" width="16" height="368" rx="4" fill="#c8b898" stroke="#b0a080" stroke-width="1"/>
  {spine_elements}

  <!-- ── TRACHEA ── -->
  <rect x="192" y="34" width="16" height="120" rx="7" fill="#f4ede8" stroke="#d4c4bc" stroke-width="2"/>
  <rect x="195" y="37" width="10" height="114" rx="4" fill="#e8ddd6"/>
  <!-- Tracheal cartilage rings -->
  <line x1="192" y1="50"  x2="208" y2="50"  stroke="#c4b4aa" stroke-width="1.5"/>
  <line x1="192" y1="62"  x2="208" y2="62"  stroke="#c4b4aa" stroke-width="1.5"/>
  <line x1="192" y1="74"  x2="208" y2="74"  stroke="#c4b4aa" stroke-width="1.5"/>
  <line x1="192" y1="86"  x2="208" y2="86"  stroke="#c4b4aa" stroke-width="1.5"/>
  <line x1="192" y1="98"  x2="208" y2="98"  stroke="#c4b4aa" stroke-width="1.5"/>
  <line x1="192" y1="110" x2="208" y2="110" stroke="#c4b4aa" stroke-width="1.5"/>
  <line x1="192" y1="122" x2="208" y2="122" stroke="#c4b4aa" stroke-width="1.5"/>
  <line x1="192" y1="134" x2="208" y2="134" stroke="#c4b4aa" stroke-width="1.5"/>
  <!-- Carina + main bronchi -->
  <circle cx="200" cy="154" r="5" fill="#d4c0b8" stroke="#c0acaa" stroke-width="1"/>
  <path d="M198 154 Q180 163,164 176" stroke="#d4c4bc" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M202 154 Q220 163,236 176" stroke="#d4c4bc" stroke-width="5" fill="none" stroke-linecap="round"/>

  <!-- ── LEFT LUNG (patient's left = image left; 2 lobes + cardiac notch) ── -->
  <path d="M148 50 C112 52,70 82,52 128 C34 174,32 246,40 316
           C46 368,62 408,88 430 C108 446,136 456,162 456
           Q182 456,188 440 L188 382
           C186 356,180 330,174 304 C168 278,168 252,172 234
           C176 218,188 206,188 194 C188 176,184 146,178 120
           C172 96,164 68,148 50 Z"
        fill="#e8a89e" stroke="#c48880" stroke-width="2.5"/>
  <!-- Lower lobe (slightly deeper tint) -->
  <path d="M42 316 C46 368,62 408,88 430 C108 446,136 456,162 456 Q182 456,188 440
           L188 382 C174 390,148 392,122 382 C94 370,66 348,50 322 Z"
        fill="#d89888" stroke="none" opacity="0.4"/>
  <!-- Oblique fissure (left lung: upper → lower lobe) -->
  <path d="M50 308 Q96 290,150 268 Q180 256,188 244"
        stroke="#c48880" stroke-width="2" fill="none" stroke-dasharray="8,4" opacity="0.7"/>
  <!-- Left pulmonary hila -->
  <ellipse cx="168" cy="226" rx="15" ry="11" fill="#d48272" opacity="0.65"/>
  <!-- Bronchial tree (faint, visible through parenchyma) -->
  <path d="M164 176 Q160 202,158 232" stroke="#d4a898" stroke-width="3.5" fill="none" opacity="0.4"/>
  <path d="M158 232 Q146 264,128 294" stroke="#d4a898" stroke-width="2.5" fill="none" opacity="0.3"/>
  <path d="M158 232 Q166 270,168 314" stroke="#d4a898" stroke-width="2" fill="none" opacity="0.3"/>
  <!-- Pleural outline (outer surface) -->
  <path d="M148 50 C112 52,70 82,52 128 C34 174,32 246,40 316 C46 368,62 408,88 430"
        stroke="#b87868" stroke-width="1" fill="none" opacity="0.6"/>

  <!-- ── RIGHT LUNG (patient's right = image right; 3 lobes) ── -->
  <path d="M252 50 C288 52,330 82,348 128 C366 174,368 246,360 316
           C354 368,338 408,312 430 C292 446,264 456,238 456
           Q218 456,212 440 L212 370
           C212 326,214 286,214 250 C214 216,218 184,222 160
           C226 136,234 104,242 80 C246 66,250 54,252 50 Z"
        fill="#e8a89e" stroke="#c48880" stroke-width="2.5"/>
  <!-- Lower lobe -->
  <path d="M360 316 C354 368,338 408,312 430 C292 446,264 456,238 456 Q218 456,212 440
           L212 370 C228 378,258 382,288 376 C320 368,348 348,362 326 Z"
        fill="#d89888" stroke="none" opacity="0.4"/>
  <!-- Horizontal fissure (upper → middle lobe) -->
  <path d="M214 230 Q262 224,312 220 Q338 218,356 226"
        stroke="#c48880" stroke-width="2" fill="none" stroke-dasharray="8,4" opacity="0.7"/>
  <!-- Oblique fissure (upper/middle → lower) -->
  <path d="M360 310 Q306 286,254 262 Q226 250,214 236"
        stroke="#c48880" stroke-width="2" fill="none" stroke-dasharray="8,4" opacity="0.7"/>
  <!-- Right pulmonary hila -->
  <ellipse cx="232" cy="220" rx="15" ry="11" fill="#d48272" opacity="0.65"/>
  <!-- Bronchial tree -->
  <path d="M236 176 Q240 202,242 230" stroke="#d4a898" stroke-width="3.5" fill="none" opacity="0.4"/>
  <path d="M242 230 Q256 264,274 294" stroke="#d4a898" stroke-width="2.5" fill="none" opacity="0.3"/>
  <path d="M242 230 Q236 270,234 312" stroke="#d4a898" stroke-width="2" fill="none" opacity="0.3"/>
  <!-- Pleural outline -->
  <path d="M252 50 C288 52,330 82,348 128 C366 174,368 246,360 316 C354 368,338 408,312 430"
        stroke="#b87868" stroke-width="1" fill="none" opacity="0.6"/>

  <!-- ── HEART (anatomical cardiac silhouette) ── -->
  <!-- Pericardium + myocardium -->
  <path d="M197 164
           C210 158,224 168,226 188 C228 212,220 254,214 296
           C208 336,204 374,198 400 C192 420,182 432,168 432
           C152 432,134 416,124 392 C114 366,116 320,124 282
           C130 250,144 220,156 198 C164 180,176 160,186 154
           C192 150,196 160,197 164 Z"
        fill="#cc2233" stroke="#aa1122" stroke-width="2.5"/>
  <!-- Right ventricle (anterior face, lighter red) -->
  <path d="M197 164 C206 170,212 188,212 212 C212 240,206 272,202 298
           C198 320,196 348,196 372 C182 376,166 372,154 362
           C142 350,136 328,134 304 C130 280,136 254,144 230
           C152 210,164 192,178 178 C186 170,192 162,197 164 Z"
        fill="#ee4455" stroke="none" opacity="0.45"/>
  <!-- Interventricular groove (LAD territory) -->
  <path d="M192 172 Q184 224,180 284 Q176 336,174 384"
        stroke="#cc0022" stroke-width="2" fill="none" opacity="0.5"/>
  <!-- Left anterior descending artery (LAD) -->
  <path d="M192 172 Q178 200,170 240 Q164 276,163 320"
        stroke="#ff5566" stroke-width="2" fill="none" opacity="0.6"/>
  <!-- Right coronary artery -->
  <path d="M198 170 Q212 192,218 228 Q220 248,216 268"
        stroke="#ff5566" stroke-width="1.5" fill="none" opacity="0.5"/>

  <!-- ── GREAT VESSELS (top of heart) ── -->
  <!-- Ascending aorta -->
  <path d="M198 162 C200 146,206 132,202 118 Q198 106,198 98"
        stroke="#cc2233" stroke-width="14" stroke-linecap="round" fill="none"/>
  <path d="M198 162 C200 146,206 132,202 118 Q198 106,198 98"
        stroke="#ee4455" stroke-width="8"  stroke-linecap="round" fill="none"/>
  <!-- Aortic arch (curves left) -->
  <path d="M198 98 Q190 88,180 92 Q170 96,166 108 Q162 120,170 126"
        stroke="#cc2233" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M198 98 Q190 88,180 92 Q170 96,166 108 Q162 120,170 126"
        stroke="#ee4455" stroke-width="6"  fill="none" stroke-linecap="round"/>
  <!-- Pulmonary trunk (to left from heart) -->
  <path d="M184 162 Q174 152,170 154 Q164 158,170 166"
        stroke="#aa3355" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M184 162 Q174 152,170 154 Q164 158,170 166"
        stroke="#cc4466" stroke-width="5"  fill="none" stroke-linecap="round"/>
  <!-- Superior vena cava (right side, slightly blue) -->
  <path d="M207 162 Q210 146,208 132 Q206 120,204 108"
        stroke="#667799" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M207 162 Q210 146,208 132 Q206 120,204 108"
        stroke="#8899bb" stroke-width="4" fill="none" stroke-linecap="round"/>

  <!-- ── DIAPHRAGM ── -->
  <!-- Right dome (higher, more convex) -->
  <path d="M44 400 Q100 440,164 450 Q188 455,196 453"
        stroke="#c0b090" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M44 400 Q100 440,164 450 Q188 455,196 453"
        stroke="#d4c8a8" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <!-- Left dome (slightly lower) -->
  <path d="M204 453 Q212 455,236 450 Q300 440,356 400"
        stroke="#b8a880" stroke-width="4.5" fill="none" stroke-linecap="round"/>
  <path d="M204 453 Q212 455,236 450 Q300 440,356 400"
        stroke="#ccc0a0" stroke-width="2.2" fill="none" stroke-linecap="round"/>
  <!-- Costophrenic angles (sharp and clear) -->
  <path d="M44 400 Q42 420,52 434" stroke="#b0a080" stroke-width="2" fill="none"/>
  <path d="M356 400 Q358 420,348 434" stroke="#b0a080" stroke-width="2" fill="none"/>
  <!-- Liver silhouette (right subdiaphragmatic, subtle) -->
  <path d="M196 453 Q248 456,298 446 Q326 438,354 418 L356 400
           Q324 430,278 440 Q234 450,196 453 Z"
        fill="#c8a888" opacity="0.22"/>
  <!-- Gastric air bubble (left, below left dome) -->
  <ellipse cx="236" cy="462" rx="24" ry="12" fill="#e8e0d4" stroke="#c8c0b0" stroke-width="1" opacity="0.5"/>

  <!-- ── RIBS ── -->
  {ribs}

  <!-- ── FINDINGS ── -->
  {findings}
</svg>
"""

RIBS = """
  <!-- Ribs: thick ivory arcs with bright cortical highlight, dimming down -->
  <!-- Rib 1 -->
  <path d="M200 122 Q246 118,280 130 Q308 144,318 168" stroke="#ddd0b8" stroke-width="7" fill="none" stroke-linecap="round" opacity="0.7"/>
  <path d="M200 122 Q154 118,120 130 Q92 144,82 168"  stroke="#ddd0b8" stroke-width="7" fill="none" stroke-linecap="round" opacity="0.7"/>
  <path d="M200 122 Q246 118,280 130 Q308 144,318 168" stroke="#f4ecdc" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.6"/>
  <path d="M200 122 Q154 118,120 130 Q92 144,82 168"  stroke="#f4ecdc" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.6"/>
  <!-- Rib 2 -->
  <path d="M200 158 Q250 153,284 167 Q315 182,324 208" stroke="#d8cbb4" stroke-width="6.5" fill="none" stroke-linecap="round" opacity="0.65"/>
  <path d="M200 158 Q150 153,116 167 Q85 182,76 208"  stroke="#d8cbb4" stroke-width="6.5" fill="none" stroke-linecap="round" opacity="0.65"/>
  <path d="M200 158 Q250 153,284 167 Q315 182,324 208" stroke="#ece0cc" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.5"/>
  <path d="M200 158 Q150 153,116 167 Q85 182,76 208"  stroke="#ece0cc" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.5"/>
  <!-- Rib 3 -->
  <path d="M200 194 Q252 189,290 206 Q324 224,330 252" stroke="#d4c8b0" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.6"/>
  <path d="M200 194 Q148 189,110 206 Q76 224,70 252"  stroke="#d4c8b0" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.6"/>
  <!-- Rib 4 -->
  <path d="M200 230 Q254 225,294 244 Q330 265,334 298" stroke="#d0c4ac" stroke-width="5.5" fill="none" stroke-linecap="round" opacity="0.55"/>
  <path d="M200 230 Q146 225,106 244 Q70 265,66 298"  stroke="#d0c4ac" stroke-width="5.5" fill="none" stroke-linecap="round" opacity="0.55"/>
  <!-- Rib 5 -->
  <path d="M200 266 Q254 261,296 282 Q334 304,338 340" stroke="#ccbfa8" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.5"/>
  <path d="M200 266 Q146 261,104 282 Q66 304,62 340"  stroke="#ccbfa8" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.5"/>
  <!-- Rib 6 -->
  <path d="M200 302 Q254 297,298 320 Q336 344,340 380" stroke="#c8bba4" stroke-width="4.5" fill="none" stroke-linecap="round" opacity="0.45"/>
  <path d="M200 302 Q146 297,102 320 Q64 344,60 380"  stroke="#c8bba4" stroke-width="4.5" fill="none" stroke-linecap="round" opacity="0.45"/>
  <!-- Lower costal margin -->
  <path d="M200 336 Q254 331,298 356 Q334 380,338 414" stroke="#c4b8a0" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.4"/>
  <path d="M200 336 Q146 331,102 356 Q66 380,62 414"  stroke="#c4b8a0" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.4"/>
"""

SPINE = """
  <rect x="193" y="120" width="14" height="10" rx="2" fill="#d8c8a8" stroke="#b8a888" stroke-width="0.5"/>
  <rect x="193" y="134" width="14" height="10" rx="2" fill="#d4c4a4" stroke="#b8a888" stroke-width="0.5"/>
  <rect x="193" y="148" width="14" height="10" rx="2" fill="#d0c0a0" stroke="#b4a484" stroke-width="0.5"/>
  <rect x="193" y="162" width="14" height="10" rx="2" fill="#ccbc9c" stroke="#b4a484" stroke-width="0.5"/>
  <rect x="193" y="176" width="14" height="10" rx="2" fill="#c8b898" stroke="#b0a080" stroke-width="0.5"/>
  <rect x="193" y="190" width="14" height="10" rx="2" fill="#c4b494" stroke="#b0a080" stroke-width="0.5"/>
  <rect x="193" y="204" width="14" height="10" rx="2" fill="#c0b090" stroke="#aca07c" stroke-width="0.5"/>
  <rect x="193" y="218" width="14" height="10" rx="2" fill="#bcac8c" stroke="#a89c78" stroke-width="0.5"/>
  <rect x="193" y="232" width="14" height="10" rx="2" fill="#b8a888" stroke="#a49874" stroke-width="0.5"/>
  <rect x="193" y="246" width="14" height="10" rx="2" fill="#b4a484" stroke="#a09470" stroke-width="0.5"/>
  <rect x="193" y="260" width="14" height="10" rx="2" fill="#b0a080" stroke="#9c9070" stroke-width="0.5"/>
  <rect x="193" y="274" width="14" height="10" rx="2" fill="#ac9c7c" stroke="#988c6c" stroke-width="0.5"/>
  <rect x="193" y="288" width="14" height="10" rx="2" fill="#a89878" stroke="#948868" stroke-width="0.5"/>
  <rect x="193" y="302" width="14" height="10" rx="2" fill="#a49474" stroke="#908464" stroke-width="0.5"/>
  <rect x="193" y="316" width="14" height="10" rx="2" fill="#a09070" stroke="#8c8060" stroke-width="0.5"/>
  <rect x="193" y="330" width="14" height="10" rx="2" fill="#9c8c6c" stroke="#887c5c" stroke-width="0.5"/>
  <rect x="193" y="344" width="14" height="10" rx="2" fill="#988868" stroke="#847858" stroke-width="0.5"/>
  <rect x="193" y="358" width="14" height="10" rx="2" fill="#948464" stroke="#807454" stroke-width="0.5"/>
  <rect x="193" y="372" width="14" height="10" rx="2" fill="#908060" stroke="#7c7050" stroke-width="0.5"/>
"""

CLINICAL_IMAGES = [
    {
        "id": "rx-neumonia-lobar",
        "title": "Radiografía de Tórax — Consolidación Lobar",
        "modality": "RxTx",
        "system": "Respiratorio",
        "difficulty": "Básico",
        "presentation": "Paciente femenina de 45 años con 5 días de fiebre de 39°C, tos productiva con expectoración amarillenta y dolor pleurítico en hemitórax derecho. Se solicita radiografía de tórax PA y lateral.",
        "svg": RX_BASE.format(
            spine_elements=SPINE,
            ribs=RIBS,
            findings="""
  <!-- RIGHT LOWER LOBE CONSOLIDATION (hepatized lung = orange-brown) -->
  <!-- Replaces normal pink lung texture in the RLL area (image right = patient's right) -->
  <path d="M216 296 C232 286,264 282,296 288 C326 294,352 312,360 338
           C366 360,358 396,342 418 C324 436,296 448,264 452
           C240 455,218 450,214 438 L214 372
           C214 342,214 316,216 296 Z"
        fill="#c07038" opacity="0.9" stroke="#a05828" stroke-width="2"/>
  <!-- Air bronchogram: dark bronchi visible through solid lung -->
  <path d="M262 294 L258 368" stroke="#e09858" stroke-width="3"   stroke-linecap="round" opacity="0.75"/>
  <path d="M278 290 L276 370" stroke="#e09858" stroke-width="2.5" stroke-linecap="round" opacity="0.7"/>
  <path d="M295 290 L297 366" stroke="#dda060" stroke-width="2"   stroke-linecap="round" opacity="0.65"/>
  <path d="M313 296 L316 358" stroke="#d09050" stroke-width="2"   stroke-linecap="round" opacity="0.55"/>
  <path d="M256 332 Q278 328,304 332" stroke="#e09858" stroke-width="2" fill="none" opacity="0.5"/>
  <path d="M254 354 Q280 350,312 354" stroke="#dda060" stroke-width="1.5" fill="none" opacity="0.45"/>
  <!-- Label -->
  <rect x="228" y="456" width="128" height="18" rx="9" fill="#a05828" opacity="0.9"/>
  <text x="292" y="469" text-anchor="middle" fill="white" font-size="10" font-family="sans-serif" font-weight="bold">LID consolidado</text>
"""
        ),
        "hotspots": [
            {
                "id": "h_consolidacion",
                "x": 71, "y": 74,
                "radius": 14,
                "label": "Consolidación lobar inferior derecha",
                "correct": True,
                "explanation": "Opacidad homogénea en lóbulo inferior derecho (LID) con broncograma aéreo visible. El broncograma (bronquios oscuros dentro de la opacidad blanca) confirma la consolidación alveolar."
            },
            {
                "id": "h_izquierdo",
                "x": 35, "y": 65,
                "radius": 14,
                "label": "Campo pulmonar izquierdo",
                "correct": False,
                "explanation": "El campo pulmonar izquierdo es normal en este caso. La lesión está en el hemitórax derecho."
            },
            {
                "id": "h_superior",
                "x": 65, "y": 35,
                "radius": 12,
                "label": "Lóbulo superior derecho",
                "correct": False,
                "explanation": "El lóbulo superior derecho es normal. La consolidación está en la base pulmonar derecha."
            }
        ],
        "questions": [
            {
                "id": "q1",
                "type": "hotspot",
                "text": "Señala en la imagen dónde está la lesión principal",
                "hint": "Busca una zona más blanca/opaca que el resto del pulmón"
            },
            {
                "id": "q2",
                "type": "mcq",
                "text": "¿Qué patrón radiológico observas en la lesión señalada?",
                "options": [
                    {"id": "a", "text": "Consolidación lobar con broncograma aéreo", "correct": True, "feedback": "Correcto. La opacidad homogénea que ocupa un lóbulo completo con bronquios oscuros visibles dentro de ella (broncograma aéreo) es el patrón clásico de la neumonía lobar."},
                    {"id": "b", "text": "Derrame pleural libre", "correct": False, "feedback": "Incorrecto. El derrame pleural produce opacidad basal con borde superior cóncavo (signo del menisco) y borramiento del ángulo costofrénico. Aquí la opacidad es más homogénea y central."},
                    {"id": "c", "text": "Neumotórax a tensión", "correct": False, "feedback": "Incorrecto. El neumotórax produce hiperclaridad (zona oscura) sin trama vascular, con la línea de la pleura visceral visible. En este caso vemos un aumento de densidad (zona blanca), no una disminución."},
                    {"id": "d", "text": "Masa pulmonar cavitada", "correct": False, "feedback": "Incorrecto. Una masa cavitada tendría un borde definido y una cavidad central (opacidad en anillo). La consolidación tiene bordes lobares y es homogénea."}
                ]
            },
            {
                "id": "q3",
                "type": "mcq",
                "text": "¿Qué signo radiológico específico confirma que el proceso es alveolar y no intersticial?",
                "options": [
                    {"id": "a", "text": "El broncograma aéreo", "correct": True, "feedback": "Correcto. El broncograma aéreo (visualización de los bronquios como líneas oscuras dentro de la opacidad) indica que el alvéolo está ocupado por exudado o líquido pero el bronquio permanece aireado. Es el signo de consolidación alveolar por excelencia."},
                    {"id": "b", "text": "El signo de la silueta", "correct": False, "feedback": "El signo de la silueta (borramiento del borde cardíaco o diafragmático) indica contacto entre la lesión y la estructura, pero no diferencia el proceso alveolar del intersticial."},
                    {"id": "c", "text": "Las líneas B de Kerley", "correct": False, "feedback": "Las líneas B de Kerley son líneas horizontales finas en la periferia pulmonar que indican edema intersticial (ICC). No son específicas de consolidación alveolar."}
                ]
            }
        ],
        "resolution": "Neumonía lobar del lóbulo inferior derecho. El diagnóstico radiológico se establece por la consolidación lobar con broncograma aéreo. En el contexto clínico (fiebre, tos, dolor pleurítico) confirma la neumonía bacteriana. El germen más frecuente en adultos inmunocompetentes es el Streptococcus pneumoniae.",
        "pearl": "Perla radiológica: El broncograma aéreo es el signo más específico de consolidación alveolar. Indica que el alvéolo está lleno de material (pus, líquido, sangre, células tumorales) pero el bronquio permanece abierto y aireado. Está presente en neumonía, edema pulmonar alveolar, contusión pulmonar y linfoma pulmonar."
    },
    {
        "id": "rx-neumotorax",
        "title": "Radiografía de Tórax — Neumotórax",
        "modality": "RxTx",
        "system": "Respiratorio",
        "difficulty": "Básico",
        "presentation": "Paciente masculino de 22 años, delgado y alto, sin antecedentes. Consulta por disnea brusca y dolor pleurítico izquierdo de inicio súbito hace 2 horas. Sin traumatismo. FR 22 rpm, SatO2 94%.",
        "svg": RX_BASE.format(
            spine_elements=SPINE,
            ribs=RIBS,
            findings="""
  <!-- AIR SPACE (pleural cavity filled with air = very pale blue) -->
  <!-- Covers the lateral portion of the left lung field -->
  <path d="M40 316 C32 246,34 174,52 128 C70 84,112 54,148 50
           C162 68,170 96,176 120 C182 144,188 174,188 194
           L154 226 C130 240,104 262,88 296
           C70 328,54 352,46 368 Z"
        fill="#daeaf8" stroke="#a8c8e8" stroke-width="1.5" opacity="0.92"/>
  <!-- COLLAPSED LEFT LUNG (atelectatic = darker, pushed medially) -->
  <path d="M152 226 C170 218,186 210,188 202 L188 382
           C180 406,164 428,140 440 C118 450,96 444,82 428
           C68 410,66 382,72 356 C78 334,94 312,108 298
           C124 282,140 258,152 240 Z"
        fill="#c89090" stroke="#a87070" stroke-width="2"/>
  <!-- Visceral pleural line (bright edge of collapsed lung) -->
  <path d="M84 110 Q78 134,74 160 Q66 196,56 228 Q48 260,48 296 Q48 322,52 358"
        stroke="#6699cc" stroke-width="3" fill="none"/>
  <!-- Mediastinal shift indicator -->
  <path d="M200 200 L216 200" stroke="#cc8800" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="218" y="204" fill="#cc8800" font-size="9" font-family="sans-serif" font-weight="600">→ shift</text>
  <!-- Label -->
  <rect x="32" y="456" width="146" height="18" rx="9" fill="#446699" opacity="0.9"/>
  <text x="105" y="469" text-anchor="middle" fill="white" font-size="10" font-family="sans-serif" font-weight="bold">Neumotórax izq.</text>
"""
        ),
        "hotspots": [
            {
                "id": "h_neumo",
                "x": 22, "y": 50,
                "radius": 15,
                "label": "Neumotórax izquierdo",
                "correct": True,
                "explanation": "Zona hiperlúcida (muy oscura/negra) en el hemitórax izquierdo lateral, sin trama vascular pulmonar. La línea pleural visceral delimita el borde del pulmón colapsado."
            },
            {
                "id": "h_derecho",
                "x": 70, "y": 55,
                "radius": 14,
                "label": "Hemitórax derecho",
                "correct": False,
                "explanation": "El hemitórax derecho muestra trama vascular normal. El neumotórax está en el lado izquierdo."
            }
        ],
        "questions": [
            {
                "id": "q1",
                "type": "hotspot",
                "text": "¿En qué hemitórax está el neumotórax? Señálalo",
                "hint": "Busca una zona muy oscura sin vasos pulmonares"
            },
            {
                "id": "q2",
                "type": "mcq",
                "text": "¿Cuál es el signo radiológico definitorio del neumotórax?",
                "options": [
                    {"id": "a", "text": "Línea pleural visceral con ausencia de trama vascular lateral a ella", "correct": True, "feedback": "Correcto. La línea pleural visceral (línea fina paralela a la pared torácica) con ausencia de trama vascular pulmonar lateral es el signo diagnóstico del neumotórax. El espacio entre la línea y la pared torácica contiene solo aire."},
                    {"id": "b", "text": "Opacidad homogénea con broncograma aéreo", "correct": False, "feedback": "Incorrecto. Eso es el patrón de consolidación (neumonía). El neumotórax produce hiperclaridad (zona más oscura), no opacidad."},
                    {"id": "c", "text": "Borramiento del ángulo costofrénico con menisco", "correct": False, "feedback": "Incorrecto. Eso es el derrame pleural. El neumotórax produce hiperclaridad en el ápex o la región lateral sin trama vascular."}
                ]
            },
            {
                "id": "q3",
                "type": "mcq",
                "text": "Este paciente (22 años, delgado, alto, sin traumatismo) corresponde al tipo de neumotórax:",
                "options": [
                    {"id": "a", "text": "Espontáneo primario — sin enfermedad pulmonar subyacente", "correct": True, "feedback": "Correcto. El neumotórax espontáneo primario afecta típicamente a varones jóvenes, delgados y altos. Se produce por rotura de pequeñas bullas apicales subpleurales. Sin enfermedad pulmonar de base."},
                    {"id": "b", "text": "Espontáneo secundario — por EPOC o asma subyacente", "correct": False, "feedback": "Incorrecto. El neumotórax secundario complica enfermedades pulmonares previas (EPOC, FQ, Marfan, PCP). Este paciente joven sin antecedentes corresponde al tipo primario."},
                    {"id": "c", "text": "Traumático — por contusión torácica", "correct": False, "feedback": "Incorrecto. El neumotórax traumático requiere un mecanismo de traumatismo torácico o procedimiento invasivo. Este paciente no refiere trauma."}
                ]
            }
        ],
        "resolution": "Neumotórax espontáneo primario izquierdo moderado. La línea pleural visceral visible con ausencia de trama vascular lateral confirma el diagnóstico. Tratamiento según tamaño: observación (<2cm), aspiración simple o tubo de drenaje (>2cm o sintomático). Recidiva en el 30% sin pleurodesis.",
        "pearl": "Perla radiológica: El neumotórax a tensión es una emergencia — el pulmón colapsado desplaza el mediastino hacia el lado opuesto y comprime el retorno venoso. Signo clave: desviación traqueal y mediastínica contralateral. Tratamiento inmediato: descompresión con aguja en 2° EIC línea medioclavicular, sin esperar la RxTx."
    },
    {
        "id": "rx-icc",
        "title": "Radiografía de Tórax — Insuficiencia Cardíaca",
        "modality": "RxTx",
        "system": "Cardiovascular",
        "difficulty": "Básico",
        "presentation": "Paciente masculino de 72 años con IC crónica conocida. Consulta por disnea progresiva en los últimos 3 días, ortopnea y edema en extremidades inferiores. SatO2 88%, FC 105 lpm.",
        "svg": RX_BASE.format(
            spine_elements=SPINE,
            ribs=RIBS,
            findings="""
  <!-- ENLARGED HEART (cardiomegaly — bigger silhouette overlaid on base heart) -->
  <path d="M200 148
           C218 140,240 154,244 180 C248 210,238 258,230 308
           C222 356,216 398,208 426 C200 446,188 458,172 458
           C154 458,132 440,120 412 C108 382,110 330,118 286
           C124 250,140 216,156 194 C166 178,178 154,190 148
           C196 145,199 146,200 148 Z"
        fill="#dd3344" stroke="#bb1122" stroke-width="2.5"/>
  <!-- Enlarged right ventricular face -->
  <path d="M200 148 C212 158,222 180,224 210 C226 242,218 278,214 308
           C210 334,208 360,208 386 C192 394,174 392,160 380
           C146 368,138 344,136 318 C132 292,140 262,150 238
           C160 216,174 196,188 180 C194 168,198 152,200 148 Z"
        fill="#ee5566" stroke="none" opacity="0.4"/>
  <!-- Dilated LAD artery on surface -->
  <path d="M196 158 Q178 206,170 256 Q164 296,163 338"
        stroke="#ff6677" stroke-width="2.5" fill="none" opacity="0.65"/>

  <!-- PULMONARY EDEMA — bilateral lower zone haziness (blue-gray) -->
  <!-- Right lower zone -->
  <path d="M214 308 C232 300,270 296,312 304 C348 312,366 332,362 360
           C358 384,336 402,304 410 C274 418,242 416,216 406
           L214 384 C214 356,214 330,214 308 Z"
        fill="#b8c8dc" opacity="0.55"/>
  <!-- Left lower zone -->
  <path d="M100 336 C76 346,46 364,44 390 C42 408,60 422,84 432
           C104 440,130 444,156 444 C170 444,184 440,188 432
           L188 406 C174 408,152 408,130 400 C112 392,104 368,100 336 Z"
        fill="#b8c8dc" opacity="0.5"/>

  <!-- Kerley B lines (horizontal short lines in lower lateral zones) -->
  <line x1="340" y1="360" x2="366" y2="358" stroke="#7899aa" stroke-width="2" opacity="0.8"/>
  <line x1="340" y1="372" x2="364" y2="370" stroke="#7899aa" stroke-width="2" opacity="0.75"/>
  <line x1="338" y1="384" x2="362" y2="382" stroke="#7899aa" stroke-width="1.5" opacity="0.7"/>
  <line x1="42" y1="366" x2="68" y2="364" stroke="#7899aa" stroke-width="2" opacity="0.8"/>
  <line x1="42" y1="378" x2="66" y2="376" stroke="#7899aa" stroke-width="2" opacity="0.75"/>
  <line x1="44" y1="390" x2="66" y2="388" stroke="#7899aa" stroke-width="1.5" opacity="0.65"/>

  <!-- CTR label -->
  <rect x="116" y="456" width="168" height="18" rx="9" fill="#880011" opacity="0.9"/>
  <text x="200" y="469" text-anchor="middle" fill="white" font-size="10" font-family="sans-serif" font-weight="bold">Cardiomegalia + Edema pulmonar</text>
"""
        ),
        "hotspots": [
            {
                "id": "h_cardiomegalia",
                "x": 46, "y": 65,
                "radius": 18,
                "label": "Cardiomegalia",
                "correct": True,
                "explanation": "La silueta cardíaca está significativamente agrandada. El índice cardiotorácico (ICT = diámetro cardíaco / diámetro torácico) supera 0.55, confirmando cardiomegalia."
            },
            {
                "id": "h_kerley",
                "x": 18, "y": 75,
                "radius": 10,
                "label": "Líneas B de Kerley",
                "correct": True,
                "explanation": "Líneas horizontales finas en la periferia pulmonar basal — representan edema intersticial en los septos interlobulillares. Signo de congestión pulmonar."
            },
            {
                "id": "h_apex",
                "x": 40, "y": 30,
                "radius": 10,
                "label": "Ápex pulmonar derecho",
                "correct": False,
                "explanation": "Los ápices pulmonares son normales en esta imagen. Los hallazgos de ICC están en la silueta cardíaca y las bases pulmonares."
            }
        ],
        "questions": [
            {
                "id": "q1",
                "type": "hotspot",
                "text": "¿Qué estructura está claramente agrandada? Señálala",
                "hint": "Compara el tamaño de la sombra central blanca con el ancho del tórax"
            },
            {
                "id": "q2",
                "type": "mcq",
                "text": "El índice cardiotorácico (ICT) normal en adultos en una RxTx PA es:",
                "options": [
                    {"id": "a", "text": "≤0.50 en PA — mayor en AP (portátil)", "correct": True, "feedback": "Correcto. El ICT normal en RxTx PA es ≤0.50. En proyección AP (portátil) el corazón se magnifica y el límite sube a 0.55. Siempre indicar la proyección al interpretar la silueta cardíaca."},
                    {"id": "b", "text": "≤0.65 independientemente de la proyección", "correct": False, "feedback": "Incorrecto. 0.65 ya sería cardiomegalia significativa. El límite normal es ≤0.50 en PA."},
                    {"id": "c", "text": "≤0.40 — cualquier cosa mayor indica patología", "correct": False, "feedback": "Incorrecto. 0.40 es muy restrictivo. Un ICT hasta 0.50 en PA se considera normal."}
                ]
            },
            {
                "id": "q3",
                "type": "mcq",
                "text": "Las líneas B de Kerley en la periferia pulmonar basal indican:",
                "options": [
                    {"id": "a", "text": "Edema intersticial — congestión de los septos interlobulillares", "correct": True, "feedback": "Correcto. Las líneas B de Kerley son líneas horizontales finas (1-2cm) en la periferia pulmonar basal que representan engrosamiento de los septos interlobulillares por edema. Son un signo de ICC con presión en cuña >18 mmHg."},
                    {"id": "b", "text": "Fibrosis pulmonar establecida", "correct": False, "feedback": "Incorrecto. La fibrosis produce un patrón reticular o en panal más grueso y permanente. Las líneas de Kerley en ICC son reversibles con el tratamiento del edema."},
                    {"id": "c", "text": "Consolidación alveolar por neumonía", "correct": False, "feedback": "Incorrecto. La neumonía produce consolidación (opacidad densa, homogénea) con broncograma aéreo. Las líneas B son líneas finas horizontales periféricas sin consolidación alveolar."}
                ]
            }
        ],
        "resolution": "Insuficiencia cardíaca descompensada con patrón clásico: cardiomegalia (ICT >0.55), redistribución vascular (dilatación de vasos en lóbulos superiores), líneas B de Kerley (edema intersticial) y edema alveolar bilateral. El tratamiento con diuréticos IV resolverá estos hallazgos radiológicos en 24-48 horas.",
        "pearl": "Perla radiológica: La RxTx en ICC sigue un patrón secuencial según la presión en cuña: 1) Redistribución vascular hacia lóbulos superiores (>18 mmHg), 2) Líneas B de Kerley — edema intersticial (>22 mmHg), 3) Edema alveolar bilateral 'en alas de mariposa' (>28 mmHg). Permite estimar la presión de llenado sin cateterismo."
    },
    {
        "id": "ecg-iamcest",
        "title": "ECG — Infarto con Elevación del ST",
        "modality": "ECG",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "presentation": "Paciente masculino de 58 años con dolor retroesternal opresivo de 90 minutos de evolución, irradiado al brazo izquierdo. Diaforesis profusa. TA 145/90, FC 92 lpm. Se realiza ECG de urgencia.",
        "svg": """<svg viewBox="0 0 600 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">
  <rect width="600" height="380" fill="#f5f0e8"/>
  <g stroke="#e8c8c8" stroke-width="0.3">
    <line x1="0" y1="10" x2="600" y2="10"/><line x1="0" y1="20" x2="600" y2="20"/><line x1="0" y1="30" x2="600" y2="30"/>
    <line x1="0" y1="40" x2="600" y2="40"/><line x1="0" y1="50" x2="600" y2="50"/><line x1="0" y1="60" x2="600" y2="60"/>
    <line x1="0" y1="70" x2="600" y2="70"/><line x1="0" y1="80" x2="600" y2="80"/><line x1="0" y1="90" x2="600" y2="90"/>
    <line x1="0" y1="100" x2="600" y2="100"/><line x1="0" y1="110" x2="600" y2="110"/>
    <line x1="0" y1="120" x2="600" y2="120"/><line x1="0" y1="130" x2="600" y2="130"/>
    <line x1="0" y1="140" x2="600" y2="140"/><line x1="0" y1="150" x2="600" y2="150"/>
    <line x1="0" y1="160" x2="600" y2="160"/><line x1="0" y1="170" x2="600" y2="170"/>
    <line x1="0" y1="180" x2="600" y2="180"/><line x1="0" y1="190" x2="600" y2="190"/>
    <line x1="0" y1="200" x2="600" y2="200"/><line x1="0" y1="210" x2="600" y2="210"/>
    <line x1="0" y1="220" x2="600" y2="220"/><line x1="0" y1="230" x2="600" y2="230"/>
    <line x1="0" y1="240" x2="600" y2="240"/><line x1="0" y1="250" x2="600" y2="250"/>
    <line x1="0" y1="260" x2="600" y2="260"/><line x1="0" y1="270" x2="600" y2="270"/>
    <line x1="0" y1="280" x2="600" y2="280"/><line x1="0" y1="290" x2="600" y2="290"/>
    <line x1="0" y1="300" x2="600" y2="300"/><line x1="0" y1="310" x2="600" y2="310"/>
    <line x1="0" y1="320" x2="600" y2="320"/><line x1="0" y1="330" x2="600" y2="330"/>
    <line x1="0" y1="340" x2="600" y2="340"/><line x1="0" y1="350" x2="600" y2="350"/>
    <line x1="0" y1="360" x2="600" y2="360"/><line x1="0" y1="370" x2="600" y2="370"/>
  </g>
  <g stroke="#e8c8c8" stroke-width="0.8">
    <line x1="0" y1="0" x2="0" y2="380"/><line x1="50" y1="0" x2="50" y2="380"/>
    <line x1="100" y1="0" x2="100" y2="380"/><line x1="150" y1="0" x2="150" y2="380"/>
    <line x1="200" y1="0" x2="200" y2="380"/><line x1="250" y1="0" x2="250" y2="380"/>
    <line x1="300" y1="0" x2="300" y2="380"/><line x1="350" y1="0" x2="350" y2="380"/>
    <line x1="400" y1="0" x2="400" y2="380"/><line x1="450" y1="0" x2="450" y2="380"/>
    <line x1="500" y1="0" x2="500" y2="380"/><line x1="550" y1="0" x2="550" y2="380"/>
    <line x1="600" y1="0" x2="600" y2="380"/>
  </g>
  <text x="8" y="55" fill="#444" font-size="9" font-family="monospace" font-weight="bold">I</text>
  <path d="M18 60 L28 60 L30 50 L33 72 L35 60 L38 60 L40 35 L42 85 L45 60 L53 60 L55 52 L57 60 L68 60 L70 50 L73 72 L75 60 L78 60 L80 35 L82 85 L85 60 L93 60 L95 52 L97 60 L108 60 L110 50 L113 72 L115 60 L118 60 L120 35 L122 85 L125 60 L133 60 L135 52 L137 60 L148 60 L150 50 L153 72 L155 60" stroke="#1a1a8a" stroke-width="1.5" fill="none"/>
  <text x="8" y="115" fill="#444" font-size="9" font-family="monospace" font-weight="bold">II</text>
  <path d="M18 120 L28 120 L30 108 L33 132 L35 120 L38 120 L40 92 L42 148 L45 120 L53 120 L55 112 L57 120 L68 120 L70 108 L73 132 L75 120 L78 120 L80 92 L82 148 L85 120 L93 120 L95 112 L97 120 L108 120 L110 108 L113 132 L115 120 L118 120 L120 92 L122 148 L125 120 L133 120 L135 112 L137 120 L148 120 L150 108 L153 132 L155 120" stroke="#1a1a8a" stroke-width="1.5" fill="none"/>
  <text x="8" y="175" fill="#444" font-size="9" font-family="monospace" font-weight="bold">V1</text>
  <path d="M18 178 L28 178 L30 174 L33 190 L35 178 L38 178 L40 195 L42 158 L44 175 L47 165 L55 168 L57 178 L68 178 L70 174 L73 190 L75 178 L78 178 L80 195 L82 158 L84 175 L87 165 L95 168 L97 178 L108 178 L110 174 L113 190 L115 178 L118 178 L120 195 L122 158 L124 175 L127 165 L135 168 L137 178 L148 178 L150 174 L153 190 L155 178" stroke="#1a1a8a" stroke-width="1.5" fill="none"/>
  <text x="8" y="235" fill="#dd2222" font-size="9" font-family="monospace" font-weight="bold">V2</text>
  <path d="M18 238 L28 238 L30 234 L33 250 L35 224 L40 218 L42 260 L44 222 L50 218 L55 218 L68 238 L70 234 L73 250 L75 224 L80 218 L82 260 L84 222 L90 218 L95 218 L108 238 L110 234 L113 250 L115 224 L120 218 L122 260 L124 222 L130 218 L135 218 L148 238 L150 234 L153 250 L155 224" stroke="#dd2222" stroke-width="2" fill="none"/>
  <text x="8" y="295" fill="#dd2222" font-size="9" font-family="monospace" font-weight="bold">V3</text>
  <path d="M18 298 L28 298 L30 294 L33 310 L35 284 L40 278 L42 320 L44 282 L50 278 L55 278 L68 298 L70 294 L73 310 L75 284 L80 278 L82 320 L84 282 L90 278 L95 278 L108 298 L110 294 L113 310 L115 284 L120 278 L122 320 L124 282 L130 278 L135 278 L148 298 L150 294 L153 310 L155 284" stroke="#dd2222" stroke-width="2" fill="none"/>
  <text x="8" y="355" fill="#dd2222" font-size="9" font-family="monospace" font-weight="bold">V4</text>
  <path d="M18 358 L28 358 L30 354 L33 368 L35 344 L40 336 L42 378 L44 340 L50 336 L55 336 L68 358 L70 354 L73 368 L75 344 L80 336 L82 378 L84 340 L90 336 L95 336 L108 358 L110 354 L113 368 L115 344 L120 336 L122 378 L124 340 L130 336 L135 336 L148 358 L150 354 L153 368 L155 344" stroke="#dd2222" stroke-width="2" fill="none"/>
  <path d="M160 180 L600 180" stroke="#ddd" stroke-width="0.5" stroke-dasharray="4,4"/>
  <text x="162" y="178" fill="#dd2222" font-size="9" font-family="monospace">↑ ST elevado V1-V4</text>
  <rect x="156" y="205" width="440" height="1" fill="#dd2222" opacity="0.4"/>
  <text x="162" y="203" fill="#666" font-size="8" font-family="monospace">línea isoeléctrica</text>
  <path d="M165 238 L240 238 L242 234 L246 252 L248 224 L253 218 L258 218 L263 238 L265 238 L310 238 L312 234 L316 252 L318 224 L323 218 L328 218 L333 238 L335 238 L380 238 L382 234 L386 252 L388 224 L393 218 L398 218 L403 238 L405 238 L450 238 L452 234 L456 252 L458 224 L463 218 L468 218 L473 238 L475 238 L520 238 L522 234 L526 252 L528 224 L533 218 L538 218 L543 238 L545 238 L590 238" stroke="#dd2222" stroke-width="2" fill="none"/>
  <text x="290" y="22" text-anchor="middle" fill="#333" font-size="11" font-family="monospace" font-weight="bold">ECG — 25mm/s   10mm/mV</text>
</svg>""",
        "hotspots": [
            {
                "id": "h_v2v4",
                "x": 55, "y": 63,
                "radius": 18,
                "label": "Elevación del ST en V2-V4",
                "correct": True,
                "explanation": "Las derivaciones V2-V4 (marcadas en rojo) muestran elevación del segmento ST >2mm sobre la línea isoeléctrica. Es el hallazgo diagnóstico del IAMCEST anterior."
            },
            {
                "id": "h_normal",
                "x": 40, "y": 30,
                "radius": 12,
                "label": "Derivaciones I y II (normales)",
                "correct": False,
                "explanation": "Las derivaciones I y II son normales en este ECG. La elevación del ST está localizada en las derivaciones precordiales V1-V4, indicando compromiso de la arteria descendente anterior."
            }
        ],
        "questions": [
            {
                "id": "q1",
                "type": "hotspot",
                "text": "¿En qué derivaciones observas la elevación del segmento ST?",
                "hint": "Busca el segmento entre el QRS y la onda T — ¿está por encima de la línea de base?"
            },
            {
                "id": "q2",
                "type": "mcq",
                "text": "La elevación del ST en V1-V4 indica compromiso de:",
                "options": [
                    {"id": "a", "text": "Arteria Descendente Anterior (DA) — infarto anterior", "correct": True, "feedback": "Correcto. Las derivaciones V1-V4 corresponden a la pared anterior del ventrículo izquierdo, irrigada por la arteria descendente anterior (DA). La elevación del ST en este territorio = IAMCEST anterior, el infarto de mayor tamaño y peor pronóstico."},
                    {"id": "b", "text": "Arteria Circunfleja — infarto lateral", "correct": False, "feedback": "Incorrecto. La circunfleja irriga la pared lateral (V5-V6, I, aVL). El infarto lateral produce elevación del ST en esas derivaciones, no en V1-V4."},
                    {"id": "c", "text": "Arteria Coronaria Derecha — infarto inferior", "correct": False, "feedback": "Incorrecto. La coronaria derecha irriga la pared inferior (II, III, aVF). El infarto inferior produce elevación en esas derivaciones, con imagen en espejo (descenso ST) en V1-V4."}
                ]
            },
            {
                "id": "q3",
                "type": "mcq",
                "text": "¿Qué tiempo máximo debe existir entre el diagnóstico del IAMCEST y la apertura de la arteria (tiempo puerta-balón)?",
                "options": [
                    {"id": "a", "text": "90 minutos si el centro tiene hemodinamia disponible", "correct": True, "feedback": "Correcto. El objetivo de tiempo puerta-balón es <90 minutos cuando la angioplastia primaria (ICPP) está disponible en el centro. Si requiere traslado, el tiempo puerta-balón total no debe superar los 120 minutos."},
                    {"id": "b", "text": "30 minutos — el tiempo es músculo", "correct": False, "feedback": "30 minutos es el objetivo del tiempo puerta-aguja para la trombolisis (no la ICPP). El objetivo para ICPP es <90 minutos, aunque menos tiempo siempre es mejor."},
                    {"id": "c", "text": "3 horas — hay tiempo suficiente si el paciente está estable", "correct": False, "feedback": "Incorrecto. 3 horas es inaceptable. Cada 30 minutos de retraso aumenta la mortalidad a 30 días un 7.5%. El objetivo es <90 minutos para centros con hemodinamia."}
                ]
            }
        ],
        "resolution": "IAMCEST anterior extenso por oclusión de la arteria descendente anterior proximal. La elevación del ST >2mm en V1-V4 con imagen en espejo (descenso ST) en cara inferior confirma el diagnóstico. Activar código IAM: angioplastia primaria en <90 minutos. Antiagregación doble + heparina inmediatas.",
        "pearl": "Perla ECG: La localización del infarto por derivaciones: Anterior (V1-V4) = DA. Lateral (V5-V6, I, aVL) = Circunfleja. Inferior (II, III, aVF) = Coronaria derecha (o circunfleja en dominancia izquierda). El infarto posterior (depresión ST en V1-V2, onda R prominente) se confirma con derivaciones posteriores (V7-V9)."
    },
    {
        "id": "ecg-fibrilacion-auricular",
        "title": "ECG — Fibrilación Auricular",
        "modality": "ECG",
        "system": "Cardiovascular",
        "difficulty": "Básico",
        "presentation": "Paciente femenina de 68 años con HTA y DM. Consulta por palpitaciones irregulares desde hace 6 horas. TA 138/85 mmHg, pulso irregular a 112 lpm. Sin dolor torácico ni disnea significativa.",
        "svg": """<svg viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">
  <rect width="600" height="280" fill="#f5f0e8"/>
  <g stroke="#e8c8c8" stroke-width="0.3">
    <line x1="0" y1="10" x2="600" y2="10"/><line x1="0" y1="20" x2="600" y2="20"/>
    <line x1="0" y1="30" x2="600" y2="30"/><line x1="0" y1="40" x2="600" y2="40"/>
    <line x1="0" y1="50" x2="600" y2="50"/><line x1="0" y1="60" x2="600" y2="60"/>
    <line x1="0" y1="70" x2="600" y2="70"/><line x1="0" y1="80" x2="600" y2="80"/>
    <line x1="0" y1="90" x2="600" y2="90"/><line x1="0" y1="100" x2="600" y2="100"/>
    <line x1="0" y1="110" x2="600" y2="110"/><line x1="0" y1="120" x2="600" y2="120"/>
    <line x1="0" y1="130" x2="600" y2="130"/><line x1="0" y1="140" x2="600" y2="140"/>
    <line x1="0" y1="150" x2="600" y2="150"/><line x1="0" y1="160" x2="600" y2="160"/>
    <line x1="0" y1="170" x2="600" y2="170"/><line x1="0" y1="180" x2="600" y2="180"/>
    <line x1="0" y1="190" x2="600" y2="190"/><line x1="0" y1="200" x2="600" y2="200"/>
    <line x1="0" y1="210" x2="600" y2="210"/><line x1="0" y1="220" x2="600" y2="220"/>
    <line x1="0" y1="230" x2="600" y2="230"/><line x1="0" y1="240" x2="600" y2="240"/>
    <line x1="0" y1="250" x2="600" y2="250"/><line x1="0" y1="260" x2="600" y2="260"/>
    <line x1="0" y1="270" x2="600" y2="270"/>
  </g>
  <g stroke="#e8c8c8" stroke-width="0.8">
    <line x1="0" y1="0" x2="0" y2="280"/><line x1="50" y1="0" x2="50" y2="280"/>
    <line x1="100" y1="0" x2="100" y2="280"/><line x1="150" y1="0" x2="150" y2="280"/>
    <line x1="200" y1="0" x2="200" y2="280"/><line x1="250" y1="0" x2="250" y2="280"/>
    <line x1="300" y1="0" x2="300" y2="280"/><line x1="350" y1="0" x2="350" y2="280"/>
    <line x1="400" y1="0" x2="400" y2="280"/><line x1="450" y1="0" x2="450" y2="280"/>
    <line x1="500" y1="0" x2="500" y2="280"/><line x1="550" y1="0" x2="550" y2="280"/>
  </g>
  <text x="8" y="68" fill="#444" font-size="9" font-family="monospace" font-weight="bold">I</text>
  <path d="M18 70 L35 70 L36 68 L38 72 L39 70 L42 70 L44 66 L46 80 L47 70 L56 70 L57 68 L59 72 L60 70 L64 70 L66 60 L68 82 L70 70 L79 70 L81 68 L83 72 L84 70 L87 70 L89 64 L91 78 L93 70 L100 70 L102 68 L104 72 L106 70 L112 70 L114 60 L116 80 L118 70 L127 70 L129 68 L131 72 L132 70 L136 70 L138 62 L140 80 L142 70 L152 70 L154 68 L156 72 L157 70 L161 70 L163 62 L165 80 L167 70 L172 70" stroke="#1a1a8a" stroke-width="1.5" fill="none"/>
  <text x="8" y="138" fill="#444" font-size="9" font-family="monospace" font-weight="bold">II</text>
  <path d="M18 140 L38 140 L39 136 L41 148 L42 140 L48 140 L50 128 L52 158 L53 140 L62 140 L64 136 L66 148 L67 140 L75 140 L77 126 L79 158 L81 140 L90 140 L92 136 L94 148 L95 140 L102 140 L104 126 L106 156 L108 140 L118 140 L120 136 L122 148 L123 140 L130 140 L132 126 L134 156 L136 140 L148 140 L150 136 L152 148 L153 140 L162 140 L164 126 L166 154 L168 140 L178 140" stroke="#1a1a8a" stroke-width="1.5" fill="none"/>
  <path d="M18 140 L598 140" stroke="#aaa" stroke-width="0.5" stroke-dasharray="2,8"/>
  <text x="185" y="138" fill="#dd8800" font-size="8" font-family="monospace">← sin ondas P visibles →</text>
  <text x="8" y="208" fill="#dd2222" font-size="9" font-family="monospace" font-weight="bold">II tira larga</text>
  <path d="M18 210 L30 210 L31 207 L33 216 L34 210 L38 210 L40 198 L42 224 L43 210 L52 210 L53 207 L55 216 L56 210 L62 210 L64 196 L66 226 L67 210 L79 210 L80 207 L82 216 L83 210 L88 210 L90 198 L92 224 L93 210 L106 210 L107 207 L109 216 L110 210 L115 210 L117 196 L119 226 L120 210 L130 210 L131 207 L133 216 L134 210 L140 210 L142 197 L144 224 L145 210 L157 210 L158 207 L160 216 L161 210 L165 210 L167 197 L169 225 L170 210 L179 210 L180 207 L182 216 L183 210 L192 210 L194 196 L196 226 L197 210 L207 210 L208 207 L210 216 L211 210 L218 210 L220 197 L222 225 L223 210 L234 210 L235 207 L237 216 L238 210 L245 210 L247 196 L249 226 L250 210 L261 210 L262 207 L264 216 L265 210 L272 210 L274 197 L276 225 L277 210 L286 210 L287 207 L289 216 L290 210 L296 210 L298 196 L300 226 L301 210 L312 210 L313 207 L315 216 L316 210 L323 210 L325 197 L327 225 L328 210 L337 210 L338 207 L340 216 L341 210 L350 210 L352 196 L354 226 L355 210 L368 210 L369 207 L371 216 L372 210 L378 210 L380 197 L382 225 L383 210 L394 210 L395 207 L397 216 L398 210 L404 210 L406 197 L408 226 L409 210 L422 210 L423 207 L425 216 L426 210 L435 210 L437 196 L439 226 L440 210 L453 210 L454 207 L456 216 L457 210 L463 210 L465 197 L467 225 L468 210 L480 210 L481 207 L483 216 L484 210 L491 210 L493 196 L495 226 L496 210 L508 210 L509 207 L511 216 L512 210 L521 210 L523 197 L525 225 L526 210 L535 210 L536 207 L538 216 L539 210 L549 210 L551 197 L553 225 L554 210 L566 210 L567 207 L569 216 L570 210 L580 210 L582 196 L584 226 L585 210 L595 210" stroke="#dd2222" stroke-width="2" fill="none"/>
  <line x1="43" y1="195" x2="43" y2="230" stroke="#0000cc" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="67" y1="195" x2="67" y2="230" stroke="#0000cc" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="93" y1="195" x2="93" y2="230" stroke="#0000cc" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="120" y1="195" x2="120" y2="230" stroke="#0000cc" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="145" y1="195" x2="145" y2="230" stroke="#0000cc" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="170" y1="195" x2="170" y2="230" stroke="#0000cc" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="18" y="248" fill="#0000cc" font-size="8" font-family="monospace">↕RR↕  ↕RR↕   ↕RR↕   ↕RR↕    ↕RR↕    ↕RR↕</text>
  <text x="18" y="260" fill="#0000cc" font-size="8" font-family="monospace">528ms  464ms   520ms   486ms   508ms   466ms</text>
  <text x="18" y="272" fill="#666" font-size="8" font-family="monospace">→ Intervalos RR irregulares (FA)</text>
  <text x="300" y="22" text-anchor="middle" fill="#333" font-size="11" font-family="monospace" font-weight="bold">ECG — 25mm/s   10mm/mV</text>
</svg>""",
        "hotspots": [
            {
                "id": "h_sin_p",
                "x": 50, "y": 50,
                "radius": 18,
                "label": "Ausencia de ondas P — línea basal irregular",
                "correct": True,
                "explanation": "La línea basal muestra ondulaciones irregulares (ondas fibrilatorias 'f') en lugar de ondas P bien definidas. La ausencia de ondas P es el signo cardinal de la FA."
            },
            {
                "id": "h_rr",
                "x": 65, "y": 75,
                "radius": 15,
                "label": "Irregularidad de los intervalos RR",
                "correct": True,
                "explanation": "Los complejos QRS son de morfología normal pero los intervalos RR son irregulares (irregularmente irregulares). Es la consecuencia de la conducción AV aleatoria en la FA."
            }
        ],
        "questions": [
            {
                "id": "q1",
                "type": "hotspot",
                "text": "Señala en qué parte del ECG ves el hallazgo más importante para diagnosticar FA",
                "hint": "¿Hay ondas P antes de cada QRS? Busca la línea basal entre los complejos"
            },
            {
                "id": "q2",
                "type": "mcq",
                "text": "¿Cuáles son los dos criterios ECG diagnósticos de la fibrilación auricular?",
                "options": [
                    {"id": "a", "text": "Ausencia de ondas P + intervalos RR irregularmente irregulares", "correct": True, "feedback": "Correcto. La FA se diagnostica por: 1) Ausencia de ondas P definidas (reemplazadas por ondas fibrilatorias 'f' de frecuencia 350-600/min), 2) Respuesta ventricular irregularmente irregular (los RR varían de forma totalmente aleatoria). Los QRS son normalmente estrechos."},
                    {"id": "b", "text": "Ondas P negativas + QRS ancho >120ms", "correct": False, "feedback": "Incorrecto. Las ondas P negativas con QRS ancho corresponden a un ritmo de la unión AV con aberrancia o a taquicardia ventricular. La FA tiene ausencia de P y QRS normalmente estrecho."},
                    {"id": "c", "text": "Ondas en serrucho + frecuencia de 150 lpm regular", "correct": False, "feedback": "Incorrecto. Las ondas en serrucho a 300/min con frecuencia ventricular regular de 150 lpm son el patrón del flutter auricular (relación 2:1), no de la FA."}
                ]
            },
            {
                "id": "q3",
                "type": "mcq",
                "text": "Esta paciente tiene CHA₂DS₂-VASc de 4 (HTA=1, DM=1, edad 65-74=1, sexo femenino=1). ¿Qué indicación tiene?",
                "options": [
                    {"id": "a", "text": "Anticoagulación oral crónica con NACO o AVK", "correct": True, "feedback": "Correcto. CHA₂DS₂-VASc ≥2 en hombres o ≥3 en mujeres (equivalente a ≥2 en hombres después de restar el punto del sexo femenino) indica anticoagulación. Con score 4, el riesgo de ACV es ~4%/año sin anticoagulación. Los NACOs son de elección sobre la warfarina."},
                    {"id": "b", "text": "Solo aspirina 100mg — tiene bajo riesgo embólico", "correct": False, "feedback": "Incorrecto. La aspirina no es eficaz para prevenir el ACV en FA (estudios AFFIRM, SPAF). Con CHA₂DS₂-VASc ≥2, la anticoagulación oral es la indicación, no la antiagregación."},
                    {"id": "c", "text": "No requiere anticoagulación — FA de inicio reciente", "correct": False, "feedback": "Incorrecto. El tiempo de inicio de la FA no modifica la indicación de anticoagulación crónica. El CHA₂DS₂-VASc define el riesgo basal de ACV y la necesidad de anticoagulación independientemente del tiempo de inicio."}
                ]
            }
        ],
        "resolution": "Fibrilación auricular con respuesta ventricular rápida (112 lpm). El ECG muestra los dos criterios diagnósticos: ausencia de ondas P y respuesta ventricular irregularmente irregular. Con CHA₂DS₂-VASc de 4, la anticoagulación oral crónica está indicada. Control de frecuencia con betabloqueante y evaluación de cardioversión según tiempo de inicio.",
        "pearl": "Perla ECG: Diferencia clave FA vs Flutter: FA = irregularmente irregular, sin P, ondas fibrilatorias 'f'. Flutter = regularmente regular a 150 lpm (relación 2:1), ondas F en serrucho en II-III-aVF y V1. La maniobra vagal o adenosina en flutter descenmascara el serrucho sin terminar la arritmia. En FA, también enlentece sin terminarla."
    },
    {
        "id": "tc-hematoma-intracraneal",
        "title": "TC de Cráneo — Hematoma Intracerebral",
        "modality": "TC",
        "system": "Neurológico",
        "difficulty": "Intermedio",
        "presentation": "Paciente masculino de 68 años hipertenso mal controlado. Es traído por su esposa por pérdida brusca de la conciencia hace 30 minutos. Actualmente Glasgow 10, hemiparesia derecha, desviación conjugada de la mirada hacia la izquierda. TA 210/120 mmHg.",
        "svg": """<svg viewBox="0 0 400 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">
  <!-- TC background (dark, as real CT) -->
  <rect width="400" height="420" fill="#101010"/>
  <text x="200" y="18" text-anchor="middle" fill="#555" font-size="9" font-family="monospace">TC CRÁNEO SIN CONTRASTE — CORTE AXIAL</text>
  <!-- Skull (cortical bone = very bright ring) -->
  <ellipse cx="200" cy="218" rx="156" ry="176" fill="none" stroke="#e8e8e8" stroke-width="9"/>
  <ellipse cx="200" cy="218" rx="148" ry="168" fill="none" stroke="#c8c8c8" stroke-width="3"/>
  <!-- Brain parenchyma (gray matter and white matter — gray tones) -->
  <ellipse cx="200" cy="218" rx="145" ry="165" fill="#4a4a4a"/>
  <!-- Cortical gray matter (outer layer, slightly lighter) -->
  <ellipse cx="200" cy="218" rx="145" ry="165" fill="none" stroke="#686868" stroke-width="12"/>
  <!-- White matter (inner, slightly darker) -->
  <ellipse cx="200" cy="215" rx="112" ry="128" fill="#424242"/>
  <!-- Basal ganglia + thalami (bilateral, slightly denser) -->
  <ellipse cx="165" cy="213" rx="36" ry="32" fill="#525252"/>
  <ellipse cx="235" cy="213" rx="36" ry="32" fill="#525252"/>
  <!-- Internal capsule (thin lighter band) -->
  <path d="M185 198 Q200 194 215 198 Q220 212 215 228 Q200 232 185 228 Q180 212 185 198" fill="#484848"/>
  <!-- Cerebral sulci (surface folds visible as dark lines) -->
  <path d="M90 155 Q114 138 138 148" stroke="#383838" stroke-width="2.5" fill="none"/>
  <path d="M262 148 Q286 138 310 155" stroke="#383838" stroke-width="2.5" fill="none"/>
  <path d="M76 218 Q96 202 116 196" stroke="#383838" stroke-width="2" fill="none"/>
  <path d="M284 196 Q304 202 324 218" stroke="#383838" stroke-width="2" fill="none"/>
  <path d="M100 278 Q122 292 148 294" stroke="#363636" stroke-width="2" fill="none"/>
  <path d="M252 294 Q278 292 300 278" stroke="#363636" stroke-width="2" fill="none"/>
  <!-- Falx cerebri (interhemispheric fissure, bright midline) -->
  <line x1="200" y1="56" x2="200" y2="380" stroke="#787878" stroke-width="2" opacity="0.7"/>
  <!-- Lateral ventricles (dark CSF-filled spaces, bilateral) -->
  <path d="M175 175 Q185 165 198 168 Q208 168 212 178 Q215 195 210 205 Q200 210 190 205 Q178 198 175 185 Z" fill="#252525"/>
  <path d="M225 175 Q215 165 202 168 Q192 168 188 178 Q185 195 190 205 Q200 210 210 205 Q222 198 225 185 Z" fill="#252525"/>
  <!-- Third ventricle (midline CSF) -->
  <rect x="196" y="200" width="8" height="30" rx="3" fill="#222"/>
  <!-- Fourth ventricle (posterior fossa) -->
  <ellipse cx="200" cy="298" rx="14" ry="10" fill="#222"/>
  <!-- Cerebellum (posterior fossa, slightly different texture) -->
  <path d="M152 310 Q176 320 200 318 Q224 320 248 310 Q264 296 268 282 Q248 290 200 292 Q152 290 132 282 Q136 296 152 310 Z" fill="#404040" stroke="#505050" stroke-width="1"/>
  <!-- Brainstem -->
  <rect x="190" y="278" width="20" height="38" rx="8" fill="#4a4a4a" stroke="#585858" stroke-width="1"/>

  <!-- ── PATHOLOGY: LEFT HEMISPHERE HEMATOMA (hyper-dense = bright white) ── -->
  <!-- Note: in radiology, left hemisphere = image RIGHT (radiological orientation) -->
  <!-- Large hyperdense hemorrhagic area in left basal ganglia region -->
  <ellipse cx="156" cy="198" rx="44" ry="50" fill="#e0e0e0"/>
  <!-- Hematoma core (densest = brightest) -->
  <ellipse cx="156" cy="198" rx="30" ry="36" fill="#f2f2f2"/>
  <!-- Hemorrhage texture (clot inhomogeneity) -->
  <path d="M136 186 Q146 176 160 180 Q172 184 170 198 Q167 216 156 220 Q144 222 136 214 Q128 204 136 186" fill="#d4d4d4"/>
  <!-- Perilesional edema (subtle darker halo) -->
  <ellipse cx="156" cy="198" rx="56" ry="62" fill="none" stroke="#3a3a3a" stroke-width="6" opacity="0.6"/>
  <!-- Midline shift (dashed line showing deviation) -->
  <line x1="200" y1="140" x2="210" y2="280" stroke="#dd4444" stroke-width="1.5" stroke-dasharray="5,3" opacity="0.8"/>
  <!-- Compressed left ventricle -->
  <path d="M175 175 Q185 168 197 170 Q205 172 206 182 Q204 196 196 200 Q184 202 176 194 Z" fill="#1e1e1e"/>

  <!-- Labels -->
  <line x1="122" y1="198" x2="86" y2="188" stroke="#ffaa00" stroke-width="1.5"/>
  <rect x="22" y="178" width="68" height="28" rx="6" fill="#111" opacity="0.85"/>
  <text x="56" y="191" text-anchor="middle" fill="#ffaa00" font-size="8.5" font-family="sans-serif" font-weight="bold">Hematoma</text>
  <text x="56" y="202" text-anchor="middle" fill="#ffaa00" font-size="8" font-family="sans-serif">hiperdenso</text>
  <!-- Orientation labels -->
  <text x="54" y="234" fill="#888" font-size="9" font-family="monospace">D</text>
  <text x="338" y="234" fill="#888" font-size="9" font-family="monospace">I</text>
  <text x="200" y="406" text-anchor="middle" fill="#555" font-size="8" font-family="monospace">D = derecha del paciente   I = izquierda del paciente</text>
</svg>""",
        "hotspots": [
            {
                "id": "h_hematoma",
                "x": 36, "y": 47,
                "radius": 14,
                "label": "Hematoma hiperdenso en ganglios basales izquierdos",
                "correct": True,
                "explanation": "Área hiperdensa (blanca) en los ganglios basales izquierdos. En TC sin contraste, la sangre aguda es HIPERDENSA (blanca) por el coágulo de hemoglobina. Localización clásica de la hemorragia hipertensiva."
            },
            {
                "id": "h_contralateral",
                "x": 64, "y": 47,
                "radius": 12,
                "label": "Hemisferio derecho",
                "correct": False,
                "explanation": "El hemisferio derecho muestra densidad normal del parénquima cerebral (gris). El hematoma está en el lado izquierdo, lo que explica la hemiparesia derecha (vías motoras se cruzan)."
            }
        ],
        "questions": [
            {
                "id": "q1",
                "type": "hotspot",
                "text": "Señala dónde está la lesión hemorrágica en la TC",
                "hint": "Busca una zona más BLANCA (hiperdensa) que el resto del cerebro"
            },
            {
                "id": "q2",
                "type": "mcq",
                "text": "¿Por qué la sangre aguda aparece HIPERDENSA (blanca) en la TC sin contraste?",
                "options": [
                    {"id": "a", "text": "Por el contenido proteico de la hemoglobina en el coágulo fresco", "correct": True, "feedback": "Correcto. La hiperdensidad de la sangre aguda en TC se debe al contenido proteico elevado de la hemoglobina en el coágulo. La retracción del coágulo concentra las proteínas, aumentando la atenuación de los rayos X. A los 7-10 días se vuelve isodensa y luego hipodensa."},
                    {"id": "b", "text": "Por el calcio que se deposita rápidamente en el hematoma", "correct": False, "feedback": "Incorrecto. La calcificación es un proceso tardío (semanas-meses). La hiperdensidad aguda de la sangre es inmediata y se debe a la hemoglobina, no al calcio."},
                    {"id": "c", "text": "Por el edema circundante que desplaza la densidad relativa", "correct": False, "feedback": "Incorrecto. El edema produce hipodensidad (zonas más oscuras), no hiperdensidad. El halo hipodense que rodea al hematoma agudo SÍ es edema, pero el hematoma en sí es hiperdenso por la hemoglobina."}
                ]
            },
            {
                "id": "q3",
                "type": "mcq",
                "text": "La hemiparesia DERECHA con desviación de mirada hacia la IZQUIERDA indica lesión en:",
                "options": [
                    {"id": "a", "text": "Hemisferio izquierdo — las vías motoras se cruzan en el tronco", "correct": True, "feedback": "Correcto. Las vías piramidales se cruzan en la decusación de las pirámides bulbares: una lesión en el hemisferio IZQUIERDO produce hemiparesia DERECHA. La desviación conjugada de la mirada hacia el lado de la lesión (izquierda) es porque el centro oculomotor frontal 'empuja' los ojos hacia el lado contralateral, y al estar dañado, los ojos se desvían hacia el lado de la lesión."},
                    {"id": "b", "text": "Hemisferio derecho — la lesión desplaza el cerebro hacia el lado opuesto", "correct": False, "feedback": "Incorrecto. Una lesión en el hemisferio derecho produce hemiparesia IZQUIERDA (vías cruzadas) y desviación de mirada hacia la DERECHA. Este paciente tiene hemiparesia derecha y mirada hacia la izquierda → lesión hemisferio izquierdo."},
                    {"id": "c", "text": "Tronco del encéfalo — por compresión de los pares craneales", "correct": False, "feedback": "Incorrecto. Las lesiones del tronco producen síndromes cruzados (paresia facial ipsilateral + hemiparesia contralateral). Este patrón (hemiparesia pura + desviación de mirada) es característico de la hemorragia supratentorial hemisférica."}
                ]
            }
        ],
        "resolution": "Hematoma intracerebral hipertensivo en ganglios basales izquierdos con efecto de masa y desviación del septum pelúcido. La localización en ganglios basales es la más frecuente en la hemorragia hipertensiva (70%). Urgencia: control de TA <140 mmHg sistólica, reverter anticoagulación si aplica, consulta neurocirugía.",
        "pearl": "Perla TC: Evolución de la sangre en TC sin contraste: Aguda (0-7 días) = HIPERDENSA (blanca, >60 UH). Subaguda temprana (7-14 días) = ISODENSA (igual al cerebro, difícil de ver). Subaguda tardía (2-8 semanas) = HIPODENSA (oscura). Crónica (>8 semanas) = HIPODENSA con calcificación periférica posible. Recordar: en pacientes muy anémicos, la sangre aguda puede no ser hiperdensa."
    }
]
