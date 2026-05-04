"""
Learning content for each pathology: pathophysiology flow, treatment phases,
complications and clinical pearls. Merged into /pathologies/{id} responses.
"""

LEARNING = {
    "infarto-agudo-miocardio": {
        "pathophysiology": {
            "summary": "Oclusión aguda de una arteria coronaria por rotura de placa aterosclerótica con trombosis sobreañadida, que interrumpe el flujo sanguíneo y genera necrosis miocárdica progresiva.",
            "flow": [
                {"label": "Placa vulnerable", "detail": "Núcleo lipídico grande + cápsula fibrosa adelgazada por inflamación crónica"},
                {"label": "Rotura de placa", "detail": "Estrés mecánico o inflamatorio → fisura de la cápsula fibrosa"},
                {"label": "Trombosis aguda", "detail": "Colágeno subendotelial expuesto → activación plaquetaria + cascada de coagulación"},
                {"label": "Oclusión coronaria", "detail": "Trombo ocluye la luz → cese del flujo sanguíneo distal"},
                {"label": "Isquemia → necrosis", "detail": ">20 min sin flujo = muerte celular irreversible (endocardio → epicardio, ola de necrosis)"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Primeros 10 min", "color": "red",
                 "actions": ["ECG 12 derivaciones urgente", "Monitorización + vía IV + analítica", "Aspirina 300 mg VO masticada", "Oxígeno si SpO₂ <90%"]},
                {"name": "Antitrombótico", "color": "orange",
                 "actions": ["Ticagrelor 180 mg VO (o clopidogrel 600 mg)", "Heparina no fraccionada 70 UI/kg IV", "Nitratos sublinguales si dolor y TA normal"]},
                {"name": "Reperfusión <90 min", "color": "yellow",
                 "actions": ["ICPP (angioplastia primaria) — de elección si disponible en <120 min", "Trombolisis si ICPP no accesible a tiempo", "Stent en arteria responsable"]},
                {"name": "Alta y crónico", "color": "green",
                 "actions": ["DAPT 12 meses (AAS + ticagrelor/clopidogrel)", "Betabloqueante (metoprolol/carvedilol)", "IECA o ARA II", "Estatina alta intensidad (rosuvastatina 20-40 mg)"]},
            ]
        },
        "complications": [
            {"name": "Fibrilación ventricular", "severity": "alta", "description": "Principal causa de muerte extrahospitalaria. Requiere desfibrilación inmediata (si VF primaria, pronóstico bueno post-ICPP)."},
            {"name": "Shock cardiogénico", "severity": "alta", "description": "Mortalidad >50%. IAM extenso con disfunción sistólica severa. Requiere soporte inotrópico o balón de contrapulsación."},
            {"name": "Ruptura de pared libre", "severity": "alta", "description": "Catastrófica. 3-7 días post-IAM. Hemopericardio y taponamiento. Mortalidad casi universal sin cirugía urgente."},
            {"name": "Insuficiencia cardíaca aguda", "severity": "media", "description": "Edema pulmonar por disfunción sistólica del VI. Clasificación de Killip I-IV orienta pronóstico."},
            {"name": "Pericarditis / Dressler", "severity": "baja", "description": "Síndrome de Dressler: fiebre + dolor pleurítico semanas post-IAM. Responde a AINEs."},
        ],
        "pearls": [
            "Tiempo puerta-balón <90 min: cada 30 minutos de retraso aumenta la mortalidad a 30 días un 7.5%.",
            "El ECG puede ser normal en las primeras horas — troponina se eleva 3-4 h después del inicio del dolor.",
            "No morfina de rutina: retrasa absorción intestinal de antiagregantes orales (evidencia CRUSADE).",
            "IAM inferior (II, III, aVF): siempre derivar V4R para descartar compromiso del ventrículo derecho.",
            "La doble antiagregación 12 meses protege el stent — suspender sin indicación cardiológica es peligroso.",
        ],
        "related_differential": "dolor-toracico-agudo",
        "related_quiz": "cardio-urgente"
    },

    "neumonia-adquirida-comunidad": {
        "pathophysiology": {
            "summary": "Infección del parénquima pulmonar adquirida fuera del hospital, generalmente por Streptococcus pneumoniae, que produce consolidación alveolar e inflamación exudativa.",
            "flow": [
                {"label": "Inóculo bacteriano", "detail": "Microaspiración de secreciones orofaríngeas colonizadas (S. pneumoniae, H. influenzae, atípicos)"},
                {"label": "Fallo de defensas", "detail": "Supera las defensas locales (cilios, macrófagos alveolares, IgA secretora)"},
                {"label": "Respuesta inflamatoria", "detail": "Citoquinas (IL-6, TNF-α) → vasodilatación, exudado + neutrófilos hacia alvéolo"},
                {"label": "Consolidación", "detail": "Alvéolos llenos de exudado fibrino-purulento → opacidad radiológica (broncograma aéreo)"},
                {"label": "Repercusión sistémica", "detail": "Bacteriemia ± SIRS → fiebre, escalofríos, alteración estado general"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Estratificación (CRB-65 / PSI)", "color": "blue",
                 "actions": ["CRB-65: 0-1 → ambulatorio; 2 → hospitalizar; 3-4 → UCI considerar", "SpO₂, FR, TA, estado mental", "RxTx PA + lateral"]},
                {"name": "Antibiótico (ambulatorio)", "color": "orange",
                 "actions": ["Amoxicilina 1g/8h x7d (neumococo)", "Azitromicina 500 mg/día x5d (atípicos, alergia penicilina)", "Amox-clavulánico si comorbilidades"]},
                {"name": "Antibiótico (hospitalizado)", "color": "red",
                 "actions": ["Ampicilina-sulbactam IV + azitromicina IV (o levofloxacino)", "Piperacilina-tazobactam si aspiración sospechada", "Oseltamivir si influenza"]},
                {"name": "Soporte y seguimiento", "color": "green",
                 "actions": ["O₂ para SpO₂ ≥94%", "Hidratación IV si necesario", "RxTx control a las 6-8 semanas (descartar neoplasia)"]},
            ]
        },
        "complications": [
            {"name": "Sepsis / Shock séptico", "severity": "alta", "description": "Bacteriemia con disfunción orgánica. Mortalidad >20%. Cultivos e inicio precoz de ATB."},
            {"name": "Insuficiencia respiratoria aguda", "severity": "alta", "description": "SDRA en NAC grave bilateral. Requiere ventilación mecánica en UCI."},
            {"name": "Derrame pleural complicado / Empiema", "severity": "media", "description": "Líquido pleural purulento. Requiere drenaje torácico + ATB."},
            {"name": "Absceso pulmonar", "severity": "media", "description": "Necrosis focal con cavitación. Más frecuente en aspiración. Metronidazol + amoxicilina prolongados."},
            {"name": "Neumonía organizada", "severity": "baja", "description": "Fallo en la resolución → tejido de granulación en alvéolos. Responde a corticoides."},
        ],
        "pearls": [
            "El broncograma aéreo (bronquios oscuros dentro de la consolidación) confirma proceso alveolar, no intersticial.",
            "S. pneumoniae es el germen más frecuente en adultos inmunocompetentes, pero no se aísla en el 50% de los casos.",
            "La RxTx puede tardar 12-24h en mostrar la consolidación — si la clínica es clara, tratar igual.",
            "CRB-65 ≥2 = hospitalización: Confusion, Respiratory rate ≥30, Blood pressure <90/60, age ≥65.",
            "Vacunación antineumocócica reduce internación por NAC un 30-40% en >65 años.",
        ],
        "related_differential": "disnea-aguda-hipoxemia",
        "related_quiz": "respiratorio-critico"
    },

    "acv-isquemico": {
        "pathophysiology": {
            "summary": "Oclusión arterial cerebral (embólica o trombótica) que genera isquemia en el territorio dependiente: zona de infarto central (irreversible) rodeada de penumbra (recuperable con reperfusión precoz).",
            "flow": [
                {"label": "Origen del émbolo / trombo", "detail": "Cardioembólico (FA, valvulopatía), aterotrombótico (carótida, arco aórtico) o lacunar (pequeño vaso)"},
                {"label": "Oclusión arterial", "detail": "Émbolo o trombo obstruye arteria cerebral (ACM más frecuente)"},
                {"label": "Cascada isquémica", "detail": "↓ ATP → despolarización neuronal, entrada masiva Ca²⁺ → excitotoxicidad por glutamato"},
                {"label": "Necrosis central", "detail": "Núcleo con flujo <10 mL/100g/min → necrosis irreversible en minutos"},
                {"label": "Penumbra isquémica", "detail": "Zona con flujo 10-20 mL/100g/min → disfuncional pero recuperable — ventana terapéutica"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Prehospitalario (0-60 min)", "color": "red",
                 "actions": ["Activar código ictus", "FAST: Face/Arm/Speech/Time", "Glucemia (descartar hipoglucemia)", "No dar nada VO, vía IV, monitorización"]},
                {"name": "Urgencias (60-90 min)", "color": "orange",
                 "actions": ["TC cerebral urgente (descartar hemorragia)", "Analítica + coagulación", "TA: bajar solo si >185/110 (si candidato a trombolisis)", "NIHSS para cuantificar déficit"]},
                {"name": "Reperfusión (<4.5 h del inicio)", "color": "yellow",
                 "actions": ["Alteplase 0.9 mg/kg IV si elegible (sin contraindicaciones)", "Trombectomía mecánica si oclusión proximal (ACM/carótida) hasta 24 h en seleccionados", "Aspirina 300 mg si no se tromboliza"]},
                {"name": "Unidad de Ictus", "color": "green",
                 "actions": ["Control glucemia (objetivo 140-180 mg/dL)", "Fiebre → antitérmicos (empeora pronóstico)", "Anticoagulación si FA (inicio diferido)", "Rehabilitación precoz"]},
            ]
        },
        "complications": [
            {"name": "Transformación hemorrágica", "severity": "alta", "description": "Sangrado dentro del infarto post-trombolisis (1-6%). Factor de riesgo: infarto grande, HTA, anticoagulación previa."},
            {"name": "Edema cerebral maligno", "severity": "alta", "description": "Infartos extensos de ACM → pico 48-72h. Puede requerir hemicraniectomía descompresiva."},
            {"name": "Neumonía aspirativa", "severity": "media", "description": "Disfagia post-ictus → aspiración. Principal causa de mortalidad tardía. Evaluación fonoaudiológica."},
            {"name": "TVP / TEP", "severity": "media", "description": "Inmovilización + lesión endotelial → trombosis venosa. Heparina profiláctica precoz."},
            {"name": "Epilepsia post-ictus", "severity": "baja", "description": "5-10% de los casos, especialmente en infartos corticales. Puede ser la presentación tardía."},
        ],
        "pearls": [
            "Tiempo puerta-aguja (TC → trombolisis) debe ser <60 min — el tiempo es cerebro: 1.9 millones de neuronas/min.",
            "La TC inicial es NORMAL en la mayoría de infartos agudos (<6h) — sirve para descartar hemorragia.",
            "La hipoglucemia puede simular un ACV — siempre medir glucemia antes del diagnóstico.",
            "FAST ampliado a BE-FAST: Balance, Eyes, Face, Arm, Speech, Time.",
            "La penumbra isquémica es el objetivo terapéutico: con reperfusión a tiempo, se recupera función.",
        ],
        "related_differential": "cefalea-thunderclap",
        "related_quiz": "neuroemergencias"
    },

    "shock-septico": {
        "pathophysiology": {
            "summary": "Respuesta inflamatoria sistémica descontrolada a la infección que produce vasodilatación masiva, disfunción de la microcirculación e insuficiencia multiorgánica.",
            "flow": [
                {"label": "Foco infeccioso", "detail": "Bacterias gram(-) (LPS) o gram(+) (ácido lipoteicoico) → activación de TLR macrofágicos"},
                {"label": "Tormenta de citoquinas", "detail": "TNF-α, IL-1, IL-6 → respuesta inflamatoria sistémica (SIRS)"},
                {"label": "Vasodilatación", "detail": "NO → vasoplegia → hipotensión distribucional refractaria a volumen"},
                {"label": "Disfunción microcirculatoria", "detail": "Coagulopatía + trombos en pequeños vasos → isquemia de órganos (CID)"},
                {"label": "Fallo multiorgánico", "detail": "Riñón (IRA), pulmón (SDRA), corazón (miocardiopatía séptica), hígado, cerebro"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Primera hora (bundle 1h)", "color": "red",
                 "actions": ["Hemocultivos x2 ANTES de antibióticos", "Lactato (>2 mmol/L = hipoperfusión)", "Acceso IV + cristaloides 30 mL/kg en 3h si hipotensión/lactato >4", "Antibióticos de amplio espectro <1h"]},
                {"name": "Vasopresores (si MAP <65)", "color": "orange",
                 "actions": ["Norepinefrina: vasopresor de primera línea", "Vasopresina si NE >0.25 mcg/kg/min", "Hidrocortisona 200 mg/día si refractario", "Objetivo: MAP ≥65 mmHg, lactato <2"]},
                {"name": "Control del foco", "color": "yellow",
                 "actions": ["Drenaje de colecciones en <6-12h si accesible", "Retirada de catéteres potencialmente infectados", "Ecografía/TC para localizar foco"]},
                {"name": "Soporte orgánico", "color": "green",
                 "actions": ["Ventilación mecánica protectora si SDRA (VT 6 mL/kg)", "Hemodiálisis si IRA con indicación", "Hemoderivados: Hb >7 g/dL", "Profilaxis TVP + úlcera gástrica"]},
            ]
        },
        "complications": [
            {"name": "SDRA", "severity": "alta", "description": "Daño alveolar difuso bilateral. PaO₂/FiO₂ <100 = grave. Ventilación mecánica con VT bajo."},
            {"name": "IRA oligúrica", "severity": "alta", "description": "Necrosis tubular aguda por hipoperfusión + nefrotóxicos. Diuresis <0.5 mL/kg/h."},
            {"name": "CID", "severity": "alta", "description": "Coagulación intravascular diseminada. TP alargado, fibrinógeno bajo, trombocitopenia."},
            {"name": "Miocardiopatía séptica", "severity": "media", "description": "Depresión reversible de la función sistólica del VI por citoquinas. Eco precoz."},
            {"name": "Encefalopatía séptica", "severity": "media", "description": "Alteración del nivel de conciencia sin foco neurológico. Mortalidad x3 si presente."},
        ],
        "pearls": [
            "Bundle 1h (surviving sepsis 2018): lactato + hemocultivos + ATB + cristaloides + vasopresores si MAP <65.",
            "Lactato >4 mmol/L = shock séptico independientemente de la TA — mortalidad >40%.",
            "La fuente del shock séptico más frecuente es pulmonar (30%) > abdominal (25%) > urinario (15%).",
            "La norepinefrina es el vasopresor de primera línea — no la dopamina (más efectos adversos cardíacos).",
            "ATB dentro de la primera hora reduce la mortalidad ~7% por cada hora de retraso.",
        ],
        "related_differential": "fiebre-confusion-adulto-mayor",
        "related_quiz": "errores-frecuentes-urgencias"
    },

    "cetoacidosis-diabetica": {
        "pathophysiology": {
            "summary": "Déficit absoluto o relativo de insulina que activa la lipolisis y cetogénesis, generando acidosis metabólica con anión gap elevado e hiperglucemia con diuresis osmótica.",
            "flow": [
                {"label": "Déficit de insulina", "detail": "DM1 (absoluto) o DM2 con estrés severo (relativo) → glucagón no contrarrestado"},
                {"label": "Hiperglucemia", "detail": "↑ gluconeogénesis hepática + ↓ captación periférica → glucemia >250 mg/dL"},
                {"label": "Cetogénesis", "detail": "Lipolisis → AGL → β-oxidación → acetil-CoA → cuerpos cetónicos (AcAc, β-OH-butirato)"},
                {"label": "Acidosis metabólica", "detail": "Acumulación de ácidos cetónicos → pH <7.30, HCO₃ <15, AG elevado"},
                {"label": "Deshidratación severa", "detail": "Glucosuria → diuresis osmótica → déficit 5-7 L de agua libre + Na, K, Mg, PO₄"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Reanimación hídrica", "color": "blue",
                 "actions": ["SF 0.9% 1L en primera hora", "500 mL/h las primeras 4h, luego 250 mL/h", "Cambiar a SF 0.45% si Na >145 mEq/L", "Bicarbonato solo si pH <6.9"]},
                {"name": "Insulina regular IV", "color": "orange",
                 "actions": ["Iniciar DESPUÉS de K >3.5 mEq/L", "Bolo 0.1 UI/kg IV, luego perfusión 0.1 UI/kg/h", "Objetivo: reducir glucemia 50-70 mg/dL/h", "No parar insulina hasta cerrar cetosis (HCO₃ >18)"]},
                {"name": "Reposición de potasio", "color": "yellow",
                 "actions": ["K <3.5: 40 mEq/h IV antes de insulina", "K 3.5-5.5: 20-40 mEq/h junto con insulina", "K >5.5: no reponer, controlar c/2h", "El K cae precipitadamente con la insulina — monitorizar"]},
                {"name": "Monitorización y transición", "color": "green",
                 "actions": ["Glucemia c/1h, K c/2h, cetonas c/4h", "Cuando glucemia <200 + iniciar dextrosa al 5%", "Transición a insulina SC cuando coma + tolera VO + cetosis cerrada", "Buscar y tratar factor desencadenante"]},
            ]
        },
        "complications": [
            {"name": "Edema cerebral", "severity": "alta", "description": "Más frecuente en niños. Corrección demasiado rápida de la hiperosmolaridad. Manitol urgente."},
            {"name": "Hipopotasemia severa", "severity": "alta", "description": "Insulina desplaza K al intracelular. Arritmias mortales si no se repone. K antes de insulina."},
            {"name": "Hipoglucemia iatrogénica", "severity": "media", "description": "Exceso de insulina sin ajuste al bajar glucemia. Monitorización horaria obligatoria."},
            {"name": "Hipofosfatemia", "severity": "baja", "description": "Reponer si <1 mg/dL con síntomas (debilidad, hemólisis). No reponer rutinariamente."},
            {"name": "Trombosis venosa", "severity": "media", "description": "Estado procoagulante + deshidratación → TVP. Heparina profiláctica si inmovilización."},
        ],
        "pearls": [
            "Tres criterios de CAD: glucemia >250, pH <7.30 (o HCO₃ <15), cetonas positivas en orina/sangre.",
            "El K sérico puede estar normal o alto en CAD — pero el K corporal total SIEMPRE está depletado.",
            "No iniciar insulina si K <3.5 — riesgo de arritmia fatal por hipopotasemia severa.",
            "La cetosis NO cierra con glucemia <200: seguir insulina + agregar dextrosa para evitar hipoglucemia.",
            "El bicarbonato solo en pH <6.9 — en pH 6.9-7.1 la acidosis responde a la corrección hídrica e insulina.",
        ],
        "related_differential": None,
        "related_quiz": "urgencias-metabolicas"
    },

    "insuficiencia-cardiaca-aguda": {
        "pathophysiology": {
            "summary": "Incapacidad aguda del corazón para mantener el gasto cardíaco necesario, generando congestión retrógrada (edema pulmonar) e hipoperfusión anterógrada.",
            "flow": [
                {"label": "Disfunción cardíaca", "detail": "Sistólica (↓FE <40%) o diastólica (FE preservada) ± precipitante agudo"},
                {"label": "↑ Presión telediastólica VI", "detail": "Fallo de bomba → sangre se acumula en VI → presión hidrostática en capilar pulmonar"},
                {"label": "Trasudación alveolar", "detail": "Presión capilar pulmonar >25 mmHg → trasudado en alvéolo → edema pulmonar"},
                {"label": "Hipoxemia", "detail": "Alvéolos inundados → shunt intrapulmonar → PaO₂ ↓ → disnea, crepitantes, SpO₂ baja"},
                {"label": "Activación neurohumoral", "detail": "↓ GC → activación SRAA + SNS → vasoconstricción, retención hidrosalina → empeora congestión"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Emergencia (LMNOP)", "color": "red",
                 "actions": ["L-Lasix (furosemida IV 40-80 mg)", "M-Morfina 2-4 mg IV (ansiedad/precarga)", "N-Nitratos IV/SL si TA >100 mmHg", "O-Oxígeno (SpO₂ ≥94%)", "P-Posición sentado 45°"]},
                {"name": "Soporte ventilatorio", "color": "orange",
                 "actions": ["CPAP/BiPAP si SpO₂ <90% con O₂ a alto flujo", "Reduce intubación 50%", "IOT si Glasgow bajo, apnea, acidosis severa"]},
                {"name": "Vasodilatadores e inotrópicos", "color": "yellow",
                 "actions": ["Nitroglicerina IV: ↓ pre y postcarga", "Nitroprusiato si emergencia hipertensiva severa", "Dobutamina si shock cardiogénico (inotropo)", "Levosimendán: alternativa a dobutamina"]},
                {"name": "Tratamiento crónico", "color": "green",
                 "actions": ["IECA/ARA II (o ARNI: sacubitrilo/valsartán)", "Betabloqueante (carvedilol/bisoprolol)", "MRA (espironolactona/eplerenona)", "SGLT2i (empagliflozina/dapagliflozina)"]},
            ]
        },
        "complications": [
            {"name": "Shock cardiogénico", "severity": "alta", "description": "GC severamente reducido con hipoperfusión orgánica. Mortalidad >50%."},
            {"name": "Insuficiencia renal aguda", "severity": "alta", "description": "Síndrome cardiorrenal tipo 1: bajo gasto → hipoperfusión renal. Diurético con precaución."},
            {"name": "Arritmias malignas", "severity": "alta", "description": "Distensión ventricular + remodelado → TV/FV. Indicación de DAI en FE <35%."},
            {"name": "Tromboembolismo pulmonar", "severity": "media", "description": "Inmovilización + bajo gasto → TVP y TEP. Heparina profiláctica."},
            {"name": "Hiponatremia dilucional", "severity": "media", "description": "Retención de agua libre > Na. Na <130 = peor pronóstico. Restricción hídrica."},
        ],
        "pearls": [
            "Furosemida IV es la piedra angular del edema agudo de pulmón — inicio de acción en 5-15 min.",
            "Los 4 pilares del tratamiento crónico de IC-FEr reducen mortalidad: IECA/ARNI + BB + MRA + SGLT2i.",
            "Líneas B de Kerley en RxTx = presión capilar pulmonar >18 mmHg.",
            "NT-proBNP >900 pg/mL confirma IC como causa de disnea; <300 descarta IC aguda.",
            "Los betabloqueantes SE SUSPENDEN en IC descompensada grave — no se inician hasta estabilización.",
        ],
        "related_differential": "edema-miembros-inferiores",
        "related_quiz": "cardio-urgente"
    },

    "tromboembolia-pulmonar": {
        "pathophysiology": {
            "summary": "Obstrucción de la circulación pulmonar por trombos venosos (TVP) que aumenta la postcarga del VD, generando insuficiencia respiratoria por espacio muerto y potencial colapso hemodinámico.",
            "flow": [
                {"label": "Tríada de Virchow", "detail": "Estasis venosa + lesión endotelial + hipercoagulabilidad → TVP (generalmente en EII)"},
                {"label": "Embolización", "detail": "Trombo se desprende → circulación venosa → AD → VD → arteria pulmonar"},
                {"label": "Obstrucción vascular", "detail": "Aumento brusco de postcarga del VD → dilatación VD + hipoquinesia"},
                {"label": "Espacio muerto", "detail": "Zonas ventiladas sin perfusión → hipoxemia + hipocapnia (taquipnea compensadora)"},
                {"label": "Shock obstructivo", "detail": "TEP masivo: VD falla → cae GC → hipotensión → colapso hemodinámico"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Estratificación de riesgo", "color": "blue",
                 "actions": ["Wells TEP + Dímero D (descartar si probabilidad baja)", "Angio-TC pulmonar si Dímero + o probabilidad alta", "Eco: dilatación VD, McConnell, TAPSE, desviación septal"]},
                {"name": "Anticoagulación inmediata", "color": "orange",
                 "actions": ["HBPM (enoxaparina 1 mg/kg/12h) o HNF si riesgo hemorrágico alto", "ACOD (rivaroxabán o apixabán) si estable y sin cáncer", "Iniciar anticoagulación antes de confirmar si alta probabilidad"]},
                {"name": "TEP de alto riesgo (inestable)", "color": "red",
                 "actions": ["Trombolisis sistémica: alteplase 100 mg IV en 2h", "Embolectomía quirúrgica si trombolisis contraindicada/falla", "Trombectomía percutánea en centros especializados", "Soporte hemodinámico: NE si hipotensión"]},
                {"name": "Alta y crónico", "color": "green",
                 "actions": ["ACOD 3-6 meses (6 meses si primer episodio sin causa reversible)", "Indefinido si TEP recurrente o síndrome antifosfolípido", "Filtro cava si contraindicación absoluta a anticoagulación"]},
            ]
        },
        "complications": [
            {"name": "Shock obstructivo", "severity": "alta", "description": "TEP masivo: hipotensión + hipoxemia + taquicardia. Mortalidad >30%. Trombolisis de emergencia."},
            {"name": "Cor pulmonale agudo", "severity": "alta", "description": "Dilatación y fallo agudo del VD. Desviación septal hacia VI → bajo gasto izquierdo."},
            {"name": "Infarto pulmonar", "severity": "media", "description": "Necrosis del parénquima por oclusión de rama segmentaria. Hemoptisis + dolor pleurítico."},
            {"name": "TEP crónico (HPTEC)", "severity": "media", "description": "Trombos no resueltos → hipertensión pulmonar tromboembólica crónica. Tromboendarterectomía."},
            {"name": "Síndrome post-TEP", "severity": "baja", "description": "Disnea residual y limitación funcional. Hasta 50% de los pacientes."},
        ],
        "pearls": [
            "La mayoría de las TEP provienen de TVP de EII — buscar edema unilateral en la exploración.",
            "Dímero D tiene alto VPN (>95%) pero bajo VPP — solo útil en baja/media probabilidad clínica.",
            "Troponina + elevada + dilatación VD en eco = TEP submasivo — considerar trombolisis o UCIM.",
            "Los ACOD (rivaroxabán, apixabán) han desplazado a la warfarina en la mayoría de los TEP.",
            "El signo de McGinn-White (S1Q3T3) aparece solo en el 10-15% de los TEP — la RxTx suele ser normal.",
        ],
        "related_differential": "hemoptisis",
        "related_quiz": "respiratorio-critico"
    },

    "pancreatitis-aguda": {
        "pathophysiology": {
            "summary": "Activación prematura de enzimas pancreáticas dentro del acino que produce autodigestión del parénquima, con respuesta inflamatoria local y potencialmente sistémica.",
            "flow": [
                {"label": "Factor desencadenante", "detail": "Colelitiasis (40%) → obstrucción de la ampolla de Vater; Alcohol (30%) → efecto tóxico directo"},
                {"label": "Activación del tripsinógeno", "detail": "Tripsinógeno se convierte en tripsina prematuramente dentro del acino"},
                {"label": "Autodigestión", "detail": "Tripsina activa otras proenzimas (fosfolipasa, elastasa) → necrosis acinar"},
                {"label": "Inflamación local", "detail": "Citoquinas (IL-1, IL-6, TNF-α) → edema peripancreático, necrosis peri/pancreática"},
                {"label": "Respuesta sistémica", "detail": "Citoquinas sistémicas → SIRS → SDRA, IRA, CID (pancreatitis grave)"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Reanimación hídrica agresiva", "color": "blue",
                 "actions": ["Ringer lactato 250-500 mL/h primeras 12-24h (preferible sobre SF)", "Objetivo: diuresis >0.5 mL/kg/h, Hto 35-44%", "Reducir velocidad si signos de sobrecarga"]},
                {"name": "Analgesia y soporte", "color": "orange",
                 "actions": ["Tramadol/morfina IV titulada", "NPO si vómitos persistentes", "Dieta enteral precoz si tolera (protege barrera intestinal)", "NPT solo si vía enteral imposible >5 días"]},
                {"name": "Manejo del foco biliar", "color": "yellow",
                 "actions": ["CPRE urgente (<24h) si colangitis + coledocolitiasis", "CPRE programada (<72h) si pancreatitis biliar grave sin colangitis", "Colecistectomía en el mismo ingreso (PA leve)"]},
                {"name": "Complicaciones", "color": "red",
                 "actions": ["Necrosis infectada: ATB (imipenem/meropenem) + drenaje diferido", "Pseudoquiste: drenaje si sintomático o >6 cm", "UCI si fallo orgánico"]},
            ]
        },
        "complications": [
            {"name": "Necrosis pancreática infectada", "severity": "alta", "description": "Principal causa de mortalidad tardía (semanas). Fiebre persistente + PCR elevada. ATB + drenaje."},
            {"name": "SDRA", "severity": "alta", "description": "Mediadores inflamatorios sistémicos → daño alveolar difuso. Requiere VM protectora en UCI."},
            {"name": "Fallo multiorgánico", "severity": "alta", "description": "Pancreatitis grave con SIRS sostenido. Mortalidad 30-50%."},
            {"name": "Pseudoquiste pancreático", "severity": "media", "description": "Colección encapsulada de jugo pancreático. Drenaje si sintomático o >6 cm después de 4 semanas."},
            {"name": "Ascitis pancreática", "severity": "media", "description": "Rotura del conducto pancreático → fuga hacia la cavidad peritoneal. Amilasa muy elevada en líquido."},
        ],
        "pearls": [
            "Criterios de Ranson o BISAP al ingreso predicen gravedad — BISAP ≥2 = mortalidad significativa.",
            "El Ringer lactato es superior al SF 0.9% en pancreatitis aguda — reduce la acidosis hiperclorémica.",
            "La nutrición enteral (SNG/SNY) es mejor que la parenteral — mantiene la barrera intestinal.",
            "Lipasa es más específica que amilasa para pancreatitis — amilasa se normaliza antes.",
            "La CPRE urgente solo en pancreatitis biliar con colangitis — no reduce gravedad de la PA sin colangitis.",
        ],
        "related_differential": "dolor-hipocondrio-derecho",
        "related_quiz": "abdomen-agudo"
    },

    "apendicitis-aguda": {
        "pathophysiology": {
            "summary": "Obstrucción de la luz apendicular (por fecalito, hiperplasia linfoide o parásitos) que genera distensión, isquemia progresiva e infección bacteriana con riesgo de perforación.",
            "flow": [
                {"label": "Obstrucción luminal", "detail": "Fecalito (60%), hiperplasia linfoide (viral, jóvenes), parásito o tumor"},
                {"label": "Distensión y presión", "detail": "Secreciones acumuladas + flora bacteriana proliferante → distensión progresiva"},
                {"label": "Isquemia parietal", "detail": "↑ presión intraluminal → compromiso del drenaje venoso y luego arterial"},
                {"label": "Invasión bacteriana", "detail": "Bacterias intestinales invaden la pared isquémica → inflamación transmural"},
                {"label": "Perforación", "detail": "Necrosis de pared → perforación libre (peritonitis) o contenida (absceso periapendicular)"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Diagnóstico y estabilización", "color": "blue",
                 "actions": ["Score de Alvarado ≥7: alta probabilidad", "Eco abdominal (primera línea); TC si dudoso", "Analítica: leucocitosis con desviación izquierda", "NPO + vía IV + analgesia (no retrasa diagnóstico)"]},
                {"name": "Apendicitis no complicada", "color": "orange",
                 "actions": ["Apendicectomía laparoscópica de elección", "ATB perioperatorio dosis única (cefazolina)", "Alta 24-48h post-cirugía laparoscópica", "ATB como alternativa a cirugía en casos seleccionados"]},
                {"name": "Apendicitis complicada (perforación)", "color": "red",
                 "actions": ["ATB IV: piperacilina-tazobactam o carbapenémico", "Apendicectomía urgente", "Drenaje abdominal si absceso en lavado peritoneal", "Duración ATB según respuesta clínica"]},
                {"name": "Post-operatorio", "color": "green",
                 "actions": ["Deambulación precoz", "Dieta líquida al reanudar ruido intestinal", "ATB oral hasta afebril + leucocitos normales", "Alta con control cirugía en 1 semana"]},
            ]
        },
        "complications": [
            {"name": "Perforación libre", "severity": "alta", "description": "Peritonitis fecal generalizada. Mortalidad 1-3% adultos, mayor en ancianos. ATB + cirugía urgente."},
            {"name": "Absceso periapendicular", "severity": "media", "description": "Perforación contenida. Puede tratarse con ATB ± drenaje percutáneo + apendicectomía diferida."},
            {"name": "Íleo paralítico", "severity": "media", "description": "Inflamación peritoneal → paresia intestinal post-quirúrgica. Habitual; resuelve en 2-4 días."},
            {"name": "Infección de herida quirúrgica", "severity": "baja", "description": "Más frecuente en apendicitis perforada. Profilaxis ATB perioperatoria reduce incidencia."},
            {"name": "Obstrucción intestinal tardía", "severity": "baja", "description": "Adherencias post-quirúrgicas. Principal causa tardía de OI en adultos con cirugías abdominales previas."},
        ],
        "pearls": [
            "McBurney (2/3 desde ombligo a EID), Blumberg (rebote), Rovsing (dolor EID al palpar EII) aumentan probabilidad.",
            "Score de Alvarado: temperatura + leucocitos + neutrofilia + migración del dolor + anorexia + náuseas + rebote + defensa.",
            "La TC tiene sensibilidad 94-98% y especificidad 95-97% — de elección en adultos con diagnóstico dudoso.",
            "La apendicitis en embarazo: duele más alto (útero desplaza apéndice). Eco o RM sin radiación ionizante.",
            "ATB solo como alternativa a cirugía: funciona en 70% a 1 año pero recurrencia del 20-40% en 5 años.",
        ],
        "related_differential": "dolor-abdominal-fid",
        "related_quiz": "abdomen-agudo"
    },

    "meningitis-bacteriana": {
        "pathophysiology": {
            "summary": "Infección bacteriana de las meninges (piamadre y aracnoides) con respuesta inflamatoria en el LCR que puede producir vasculitis cerebral, hidrocefalia e hipertensión intracraneal.",
            "flow": [
                {"label": "Colonización / Bacteriemia", "detail": "N. meningitidis (jóvenes), S. pneumoniae (adultos/mayores), L. monocytogenes (inmunodeprimidos/>50 años)"},
                {"label": "Invasión meníngea", "detail": "Bacterias cruzan la BHE → espacio subaracnoideo → LCR sin defenses inmune locales"},
                {"label": "Respuesta inflamatoria en LCR", "detail": "Citoquinas → neutrófilos → exudado purulento → obstrucción flujo LCR"},
                {"label": "Edema y HIC", "detail": "Edema citotóxico + vasogénico → ↑PIC → cefalea, vómitos, alteración de conciencia"},
                {"label": "Vasculitis + daño neuronal", "detail": "Inflamación vascular → trombosis → infarto cerebral; Endotoxinas → daño neuronal directo"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Primeros 30 min (urgencia extrema)", "color": "red",
                 "actions": ["ATB INMEDIATO si sospecha clínica (no esperar punción)", "Dexametasona 0.15 mg/kg IV ANTES o CON primera dosis de ATB", "Vía IV + analítica urgente + hemocultivos x2"]},
                {"name": "Punción lumbar", "color": "orange",
                 "actions": ["Si no hay signos de HIC, papiledema ni déficit focal: PL ANTES del ATB", "Si hay contraindicación: TC previo + ATB SIN esperar PL", "LCR: turbio, glucosa ↓, proteínas ↑, neutrófilos >1000/mm³"]},
                {"name": "Antibiótico empírico", "color": "yellow",
                 "actions": ["<50 años sin inmunosupresión: Ceftriaxona 2g/12h IV", ">50 años o inmunosuprimido: + Ampicilina 2g/4h (Listeria)", "Alérgico a penicilina: meropenem + vancomicina", "Ajustar según cultivo de LCR y antibiograma"]},
                {"name": "Manejo de HIC", "color": "green",
                 "actions": ["Cabeza 30° + habitación tranquila", "Manitol 0.25-0.5 g/kg si deterioro neurológico", "Control glucemia", "Profilaxis anticonvulsivante si crisis"]},
            ]
        },
        "complications": [
            {"name": "Ventriculitis / Empiema subdural", "severity": "alta", "description": "Extensión de la infección. Requiere drenaje neuroquirúrgico + ATB prolongados."},
            {"name": "Infarto cerebral", "severity": "alta", "description": "Vasculitis séptica de arterias cerebrales → ictus. Peor pronóstico neurológico."},
            {"name": "Hidrocefalia", "severity": "alta", "description": "Obstrucción del flujo de LCR por exudado. Puede requerir derivación ventriculoperitoneal."},
            {"name": "Sordera neurosensorial", "severity": "media", "description": "Daño del VIII par. Más frecuente en neumococo. Dexametasona reduce incidencia."},
            {"name": "CID / Púrpura fulminante", "severity": "alta", "description": "Neisseria meningitidis → sepsis grave + CID → necrosis de extremidades. Mortalidad >50%."},
        ],
        "pearls": [
            "La tríada clásica (fiebre + cefalea + rigidez de nuca) solo aparece en el 44% de los casos — no esperar la tríada completa.",
            "Dexametasona ANTES o CON la primera dosis de ATB reduce mortalidad y secuelas neurológicas (evidencia clase I).",
            "PL contraindicada si: PIC muy elevada, déficit focal, papiledema, GCS <10 → TC primero.",
            "Kernig (+): dolor al extender rodilla con cadera en 90°; Brudzinski: flexión de rodillas al flexionar el cuello.",
            "La profilaxis con rifampicina o ciprofloxacino está indicada para contactos íntimos de meningococo.",
        ],
        "related_differential": "cefalea-thunderclap",
        "related_quiz": "neuroemergencias"
    },

    "crisis-asmatica": {
        "pathophysiology": {
            "summary": "Exacerbación aguda del asma por broncoespasmo, edema de la mucosa e hipersecreción de moco que aumentan la resistencia de la vía aérea y generan hiperinsuflación dinámica.",
            "flow": [
                {"label": "Desencadenante", "detail": "Alérgenos, infecciones virales (rinovirus), irritantes, AINE, estrés, ejercicio"},
                {"label": "Inflamación bronquial", "detail": "Mastocitos + eosinófilos + Th2 → histamina, leucotrienos, IL-4/5/13"},
                {"label": "Broncoespasmo", "detail": "Contracción del músculo liso bronquial → obstrucción del flujo espiratorio"},
                {"label": "Edema + moco", "detail": "Edema de la mucosa + hipersecreción → obstrucción adicional → atelectasias"},
                {"label": "Hiperinsuflación + hipoxemia", "detail": "Aire atrapado → ↑ volumen residual → trabajo respiratorio ↑ + V/Q alterado → hipoxemia"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Crisis leve-moderada", "color": "orange",
                 "actions": ["SABA (salbutamol MDI 4-8 puffs c/20 min x3 o nebulizado)", "Ipratropio + SABA en crisis moderada-grave", "Corticoide sistémico: prednisona 40-60 mg VO o metilprednisolona IV", "O₂ para SpO₂ ≥94%"]},
                {"name": "Crisis grave", "color": "red",
                 "actions": ["SABA + ipratropio nebulizados continuos", "Sulfato de magnesio 2g IV en 20 min", "Metilprednisolona IV 1-2 mg/kg", "Heliox si disponible", "UCIM: preparar para VMI si deterioro"]},
                {"name": "Ventilación mecánica (si necesario)", "color": "red",
                 "actions": ["Estrategia 'permissive hypercapnia'", "FR baja, VT bajo, tiempo espiratorio largo (I:E 1:3-4)", "PEEP intrínseca: cuidado con hiperinsuflación", "Ketamina + propofol: broncodilatadores como sedación"]},
                {"name": "Alta y prevención", "color": "green",
                 "actions": ["ICS: pilar del tratamiento preventivo", "LABA + ICS en escalones 3-5 (GINA)", "Identificar y evitar desencadenantes", "Plan de acción escrito al alta"]},
            ]
        },
        "complications": [
            {"name": "Asma casi fatal / Paro respiratorio", "severity": "alta", "description": "SpO₂ <92% que no responde a tratamiento. Alteración de conciencia → IOT urgente."},
            {"name": "Neumotórax", "severity": "alta", "description": "Hiperinsuflación extrema → rotura de bullae. Hipersonoridad + asimetría → drenaje urgente."},
            {"name": "Neumonía sobreañadida", "severity": "media", "description": "Obstrucción + hipersecreción → infección secundaria. ATB si fiebre + infiltrado radiológico."},
            {"name": "Insuficiencia respiratoria hipercápnica", "severity": "alta", "description": "Agotamiento muscular → hipercapnia progresiva. PCO₂ que sube = signo de alarma tardía."},
            {"name": "Miopatía por corticoides", "severity": "baja", "description": "Corticoides sistémicos prolongados → debilidad de los músculos respiratorios."},
        ],
        "pearls": [
            "Silencio auscultatorio en asma grave = pulmón muy obstruido con mínimo flujo de aire — signo de alarma.",
            "El PCO₂ 'normal' (35-45) en asma aguda GRAVE es un signo de alarma — el paciente debería estar hipocápnico.",
            "Salbutamol + ipratropio es más eficaz que salbutamol solo en crisis moderada-grave (reduce hospitalización 25%).",
            "El sulfato de magnesio IV tiene evidencia en crisis grave — mecanismo: antagonismo Ca²⁺ en músculo liso bronquial.",
            "GINA 2023: iniciar ICS desde el diagnóstico — los SABA solos sin ICS aumentan riesgo de crisis grave.",
        ],
        "related_differential": "disnea-aguda-hipoxemia",
        "related_quiz": "respiratorio-critico"
    },

    "fibrilacion-auricular": {
        "pathophysiology": {
            "summary": "Actividad eléctrica auricular caótica (350-600/min) por múltiples frentes de onda con reentrada, que produce respuesta ventricular irregular y estasis sanguínea con riesgo embólico.",
            "flow": [
                {"label": "Sustrato estructural", "detail": "Fibrosis auricular, dilatación de AI, HTA crónica, valvulopatía mitral → heterogeneidad eléctrica"},
                {"label": "Disparadores", "detail": "Focos ectópicos en venas pulmonares → extrasístoles auriculares frecuentes"},
                {"label": "Actividad eléctrica caótica", "detail": "Múltiples frentes de onda con reentrada → ausencia de onda P organizada"},
                {"label": "Respuesta ventricular irregular", "detail": "Conducción AV aleatoria → RR irregularmente irregular"},
                {"label": "Estasis auricular → trombo", "detail": "Orejuela izquierda sin contracción efectiva → estasis → trombo → embolia sistémica"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Control de frecuencia", "color": "blue",
                 "actions": ["Metoprolol 5 mg IV lento (o VO 25-50 mg)", "Diltiazem IV si IC no deprimida", "Digoxina si IC con FE baja", "Objetivo: FC 80-110 lpm (110 en síntomas severos)"]},
                {"name": "Control de ritmo", "color": "orange",
                 "actions": ["Cardioversión eléctrica si inestable hemodinámicamente", "Flecainida o propafenona si <48h + sin cardiopatía estructural", "Amiodarona si cardiopatía estructural + control de ritmo deseado", "Ablación FA si recurrente y sintomática"]},
                {"name": "Anticoagulación (CHA₂DS₂-VASc)", "color": "yellow",
                 "actions": ["Hombres ≥2 / Mujeres ≥3: anticoagulación indicada", "ACOD de elección (rivaroxabán, apixabán, dabigatrán)", "AVK (warfarina) si valvulopatía reumática / válvula mecánica", "No antiagregantes solos — no reducen ictus en FA"]},
                {"name": "Cardioversión programada", "color": "green",
                 "actions": ["Si >48h: anticoagular 3-4 semanas antes o ETE para descartar trombo en AI", "ACOD al menos 4 semanas post-cardioversión", "Tratar factores modificables: HTA, apnea del sueño, alcohol, peso"]},
            ]
        },
        "complications": [
            {"name": "Ictus / ACV embólico", "severity": "alta", "description": "Riesgo anual 5x mayor que sin FA. Trombo en orejuela izquierda → embolia cerebral. Indicación de anticoagulación."},
            {"name": "Insuficiencia cardíaca por taquicardiomiopatía", "severity": "alta", "description": "FA persistente con FC elevada → remodelado ventricular reversible. Control de frecuencia + cardioversión."},
            {"name": "Síncope", "severity": "media", "description": "Pausa post-cardioversión o respuesta ventricular muy lenta. Descartar síndrome taquicardia-bradicardia (sick sinus)."},
            {"name": "Hemorragia bajo anticoagulación", "severity": "media", "description": "Riesgo HAS-BLED. Los ACODs tienen menor riesgo de hemorragia intracraneal que warfarina."},
            {"name": "Embolismo periférico", "severity": "media", "description": "Isquemia aguda de extremidades, mesenterio o riñones. Menos frecuente que el ictus."},
        ],
        "pearls": [
            "CHA₂DS₂-VASc: CHF/FE baja=1, HTA=1, Edad≥75=2, DM=1, ACV previo=2, Vasculopatía=1, Edad65-74=1, Sexo femenino=1.",
            "La FA es la causa más frecuente de ictus cardioembólico — anticoagular es la intervención más eficaz.",
            "Los ACOD no requieren monitorización y tienen menor riesgo de HIC vs warfarina.",
            "Cardioversión en FA <48h: anticoagulación directa post-cardioversión 4 semanas como mínimo.",
            "Abordar los factores de riesgo modifica el curso natural: control de HTA, reducción de peso, abstinencia de alcohol.",
        ],
        "related_differential": "palpitaciones-agudas",
        "related_quiz": "cardio-urgente"
    },

    "hipoglucemia-severa": {
        "pathophysiology": {
            "summary": "Descenso de glucemia <54 mg/dL con síntomas adrenérgicos y neuroglucogénicos, causado por exceso de insulina, déficit de aporte glucídico o insuficiencia suprarrenal.",
            "flow": [
                {"label": "Caída de glucemia", "detail": "Insulina relativa o absoluta > aporte → glucemia <70 mg/dL (alerta), <54 (clínica)"},
                {"label": "Respuesta adrenérgica", "detail": "Glucemia <70 → adrenalina, glucagón → temblor, taquicardia, diaforesis, palpitaciones"},
                {"label": "Neuroglucogenia", "detail": "Cerebro agota glucosa → cefalea, mareo, visión borrosa, confusión"},
                {"label": "Neuroglucopenia grave", "detail": "Glucemia <40 → convulsiones, pérdida de conciencia (neurona sin energía)"},
                {"label": "Daño neurológico", "detail": "Hipoglucemia prolongada → muerte neuronal irreversible (similar a hipoxia)"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Paciente consciente", "color": "orange",
                 "actions": ["Regla '15-15': 15g de carbohidratos (150 mL zumo/refresco/3 terrones azúcar)", "Controlar glucemia a los 15 min", "Repetir si <100 mg/dL", "Comida con carbohidratos complejos para evitar rebote"]},
                {"name": "Paciente inconsciente", "color": "red",
                 "actions": ["Glucosa IV: 20-50 mL de dextrosa al 50% (SG50%) en bolo", "O Glucagón 1 mg SC/IM si no hay vía IV (DM1)", "Monitorizar glucemia c/15 min", "Identificar causa y evitar recurrencia"]},
                {"name": "Hipoglucemia por sulfonilureas", "color": "yellow",
                 "actions": ["Observación hospitalaria 24-48h (vida media larga)", "Dextrosa IV continua + monitorización", "Octreotida si recurrente grave (inhibe insulina)"]},
                {"name": "Investigación y prevención", "color": "green",
                 "actions": ["Revisar dosis de insulina/ADO", "Educación: reconocer síntomas precoces", "Glucagón de emergencia en casa (kit para familiares)", "Ajuste de objetivos glucémicos en hipoglucemia recurrente"]},
            ]
        },
        "complications": [
            {"name": "Daño neurológico permanente", "severity": "alta", "description": "Hipoglucemia prolongada → necrosis cortical. Más riesgo en ancianos y episodios nocturnos."},
            {"name": "Arritmias cardíacas", "severity": "alta", "description": "Hipoglucemia → liberación adrenérgica → prolongación QT → arritmias ventriculares."},
            {"name": "Caídas y traumatismos", "severity": "media", "description": "Confusión o pérdida de conciencia → traumatismo craneal. Riesgo en ancianos."},
            {"name": "Hipoglucemia inadvertida", "severity": "alta", "description": "Neuropatía autonómica o hipoglucemias repetidas → pérdida de síntomas adrenérgicos de alarma."},
            {"name": "ACV / IAM desencadenado", "severity": "media", "description": "Vasoespasmo + hipercoagulabilidad por respuesta adrenérgica extrema."},
        ],
        "pearls": [
            "La regla del '15-15' es el pilar del tratamiento ambulatorio — 15g CHO + control en 15 min.",
            "El glucagón NO funciona en hipoglucemias por sulfonilureas ni en desnutrición severa (sin glucógeno hepático).",
            "Hipoglucemia nocturna: diana HbA1c >7.5% en pacientes con hipoglucemias frecuentes inadvertidas.",
            "El cerebro consume el 25% de la glucosa total — es el órgano más sensible a la hipoglucemia.",
            "SG50% irrita venas — diluir a SG10% si hay tiempo o usar vía central/intraósea.",
        ],
        "related_differential": None,
        "related_quiz": "urgencias-metabolicas"
    },

    "insuficiencia-renal-aguda": {
        "pathophysiology": {
            "summary": "Deterioro agudo de la función renal (↑ creatinina ≥0.3 mg/dL en 48h o ≥1.5x basal en 7 días) por hipoperfusión, daño tubular directo u obstrucción.",
            "flow": [
                {"label": "Prerrenal (55%)", "detail": "Hipoperfusión renal → sin daño tubular aún (reversible con volumen)"},
                {"label": "Intrarrenal (40%)", "detail": "NTA (isquémica o nefrotóxica): daño del epitelio tubular → obstrucción de la nefrona"},
                {"label": "Obstructiva (5%)", "detail": "Obstrucción del tracto urinario → ↑ presión en nefrona → ↓ FG (reversible con drenaje)"},
                {"label": "↓ FG → acumulación", "detail": "Creatinina, urea, K, ácidos, agua → uremia, hiperpotasemia, acidosis, sobrecarga de volumen"},
                {"label": "Disfunción tubular", "detail": "Incapacidad de concentrar orina, regular electrolitos y excretar ácidos → FRA establecida"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Identificar causa y eliminarla", "color": "blue",
                 "actions": ["Prerrenal: volumen IV (cristaloides 500 mL en 30 min si no sobrecargado)", "NTA: retirar nefrotóxicos (AINEs, aminoglucósidos, contrastes)", "Obstructiva: sondaje vesical + ecografía renal urgente"]},
                {"name": "Manejo de complicaciones", "color": "red",
                 "actions": ["Hiperpotasemia severa (K >6.5): gluconato Ca²⁺ IV + insulina + glucosa + bicarbonato", "Acidosis severa (pH <7.1): bicarbonato IV", "Sobrecarga hídrica: furosemida IV (si FRA oligúrica)"]},
                {"name": "Indicaciones de hemodiálisis urgente", "color": "red",
                 "actions": ["Hiperpotasemia refractaria al tratamiento médico", "Acidosis severa refractaria (pH <7.1)", "Sobrecarga hídrica con edema pulmonar", "Encefalopatía urémica o pericarditis urémica"]},
                {"name": "Prevención y nefroprotección", "color": "green",
                 "actions": ["N-acetilcisteína + hidratación precontraste en nefropatía por contraste", "Evitar AINEs en pacientes con FG <60", "Ajuste de dosis de fármacos según FG", "Dieta baja en K y P si oliguria"]},
            ]
        },
        "complications": [
            {"name": "Hiperpotasemia severa", "severity": "alta", "description": "K >6.5 → arritmias ventriculares letales. ECG: QRS ancho, onda T picuda, onda P aplanada."},
            {"name": "Acidosis metabólica", "severity": "alta", "description": "↓ excreción de H⁺ + ↑ ácidos endógenos → respiración de Kussmaul, arritmias."},
            {"name": "Sobrecarga hídrica / EAP", "severity": "alta", "description": "Sin diuresis → acumulación de agua → edema pulmonar. Diálisis si furosemida ineficaz."},
            {"name": "IRA crónica (FRC)", "severity": "media", "description": "FRA prolongado o recurrente → fibrosis tubulointersticial → ERC permanente."},
            {"name": "Infección (sepsis)", "severity": "alta", "description": "FRA + inmunosupresión urémica → infecciones de catéter, urinarias, pulmonares."},
        ],
        "pearls": [
            "Criterios KDIGO de FRA: ↑ creatinina ≥0.3 mg/dL en 48h, ó ≥1.5x basal en 7 días, ó diuresis <0.5 mL/kg/h por 6h.",
            "Índice FeNa: <1% = prerrenal (túbulo intacto retiene Na); >2% = intrarrenal (NTA, túbulo lesionado).",
            "El gluconato de Ca²⁺ IV cardioprotege pero NO baja el K — necesita insulina+glucosa para efecto hipopotasémico.",
            "Los AINEs bloquean PGE₂ renal (vasodilatación aferente) → precipitan FRA prerrenal en cirróticos/ICC/deshidratados.",
            "La mioglobinuria post-rabdomiólisis: orina marrón + CK >5000 → NTA por mioglobina → hiperhidratación alcalinizante.",
        ],
        "related_differential": "hematuria-macroscopica",
        "related_quiz": "urgencias-metabolicas"
    },

    "hemorragia-digestiva-alta": {
        "pathophysiology": {
            "summary": "Sangrado del tracto digestivo proximal al ángulo de Treitz, principalmente por úlcera péptica (55%) o varices esofagogástricas (20%), con potencial compromiso hemodinámico.",
            "flow": [
                {"label": "Erosión o rotura vascular", "detail": "Úlcera péptica: erosión de H. pylori + AINEs; Varices: HTPortal → varices frágiles"},
                {"label": "Sangrado intraluminal", "detail": "Hematemesis (sangre roja o en poso de café) y/o melenas"},
                {"label": "Pérdida de volumen", "detail": "Hipovolemia → taquicardia → hipotensión → shock si >30% del volumen sanguíneo"},
                {"label": "Activación neurohumoral", "detail": "SRAA + SNS → vasoconstricción → hipoperfusión de órganos diana"},
                {"label": "Complicaciones orgánicas", "detail": "Encefalopatía hepática (carga nitrogenada) si varices; IRA prerrenal; isquemia miocárdica"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Reanimación inicial", "color": "red",
                 "actions": ["2 vías IV gruesas + analítica urgente + grupo sanguíneo", "Cristaloides en bolo si hipotensión", "Transfusión si Hb <7 (u 8 en cardiopatía)", "Sonda nasogástrica si diagnóstico incierto"]},
                {"name": "Fármacos", "color": "orange",
                 "actions": ["IBP: omeprazol 80 mg IV en bolo + 8 mg/h en perfusión (úlcera péptica)", "Somatostatina/octreotida IV si sospecha varices", "Antibiótico profiláctico (ceftriaxona) si cirrosis", "Eritromicina IV 250 mg previo a endoscopia (vaciar estómago)"]},
                {"name": "Endoscopia urgente (<12h)", "color": "yellow",
                 "actions": ["Dentro de 24h si estable; <12h si inestable o criterios de Rockford alto", "Úlcera: inyección adrenalina + termocoagulación/clipaje", "Varices: ligadura con bandas elásticas de primera elección"]},
                {"name": "Refractario", "color": "red",
                 "actions": ["TIPS si varices refractarias a tratamiento endoscópico", "Cirugía si úlcera sangrante refractaria", "Embolización arterial si candidato quirúrgico de alto riesgo"]},
            ]
        },
        "complications": [
            {"name": "Shock hipovolémico", "severity": "alta", "description": "Pérdida >30% del volumen circulante → TAS <90, FC >120, oliguria. Transfusión masiva."},
            {"name": "Resangrado", "severity": "alta", "description": "20% en úlceras Forrest Ia-IIa. Alto riesgo de mortalidad. IBP + endoscopia precoz."},
            {"name": "Encefalopatía hepática", "severity": "alta", "description": "Carga nitrogenada intestinal por sangre → hiperamonemia en cirróticos. Lactulosa + rifaximina."},
            {"name": "Isquemia miocárdica", "severity": "alta", "description": "Anemia aguda + hipotensión → demanda > oferta de O₂ al miocardio. ECG + troponina."},
            {"name": "Aspiración", "severity": "media", "description": "Hematemesis masiva → aspiración. Intubación orotraqueal si riesgo de broncoaspiración."},
        ],
        "pearls": [
            "Score de Rockford/Blatchford pre-endoscopia: si 0 = muy bajo riesgo, alta precoz; ≥6 = alto riesgo, ingreso UCI.",
            "IBP en perfusión continua post-endoscopia reduce resangrado un 50% en úlceras de alto riesgo.",
            "La melena puede aparecer con solo 50-100 mL de sangre en el tubo digestivo proximal.",
            "La somatostatina reduce el flujo esplácnico y las varices NO necesitan esperar la endoscopia — iniciar inmediato.",
            "No transfundir libremente: Hb objetivo 7-8 g/dL — transfusión liberal en cirrosis aumenta resangrado y mortalidad.",
        ],
        "related_differential": "dolor-hipocondrio-derecho",
        "related_quiz": "abdomen-agudo"
    },

    "anafilaxia": {
        "pathophysiology": {
            "summary": "Reacción alérgica sistémica grave mediada por IgE que produce liberación masiva de mediadores de mastocitos y basófilos, con vasodilatación sistémica e inflamación de la vía aérea.",
            "flow": [
                {"label": "Sensibilización previa", "detail": "Primera exposición al alergeno → producción de IgE específica → fijación en mastocitos"},
                {"label": "Re-exposición", "detail": "Alergeno une IgE en mastocitos → entrecruzamiento → degranulación"},
                {"label": "Liberación de mediadores", "detail": "Histamina, triptasa, leucotrienos, PGD₂ → vasodilatación + broncoespasmo + edema"},
                {"label": "Respuesta sistémica", "detail": "Vasodilatación masiva → hipotensión; Edema de vía aérea → obstrucción; Urticaria/angioedema"},
                {"label": "Shock anafiláctico", "detail": "Distribución del volumen + fuga capilar → hipotensión refractaria → colapso vascular"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Adrenalina INMEDIATA (1ª línea)", "color": "red",
                 "actions": ["Epinefrina 0.3-0.5 mg IM en cara anterolateral del muslo (concentración 1:1000)", "Repetir c/5-15 min si no hay respuesta", "NO se retrasa por ausencia de vía IV ni para dar antihistamínico primero", "En paro cardíaco: adrenalina 1 mg IV (1:10000)"]},
                {"name": "Soporte hemodinámico", "color": "orange",
                 "actions": ["Posición decúbito + MMII elevados (excepción: disnea → sentado)", "Cristaloides 1-2L IV rápido si hipotensión", "Adrenalina IV en perfusión si refractario a IM"]},
                {"name": "Vía aérea", "color": "yellow",
                 "actions": ["O₂ de alto flujo (10-15 L/min)", "Broncodilatadores (salbutamol) si broncoespasmo predominante", "Cricotirotomía si edema supraglótico que impide IOT"]},
                {"name": "Adyuvantes (2ª línea, nunca en lugar de adrenalina)", "color": "green",
                 "actions": ["Antihistamínico H1: difenhidramina IV (no sustituye adrenalina)", "Corticoide: metilprednisolona 1-2 mg/kg IV (previene fase tardía)", "Glucagón IV si paciente con betabloqueantes (evita respuesta a adrenalina)", "Observación 6-12h por riesgo de reacción bifásica"]},
            ]
        },
        "complications": [
            {"name": "Reacción bifásica", "severity": "alta", "description": "Reaparición de síntomas 1-72h después de resolución aparente. Observación mínima 6-12h."},
            {"name": "Paro cardiorrespiratorio", "severity": "alta", "description": "Hipoxia + vasodilatación + arritmias. RCP estándar + adrenalina 1 mg IV c/3-5 min."},
            {"name": "Obstrucción de vía aérea", "severity": "alta", "description": "Edema supraglótico → estridor → IOT urgente. Cricotirotomía si IOT imposible."},
            {"name": "Miocardiopatía de Takotsubo", "severity": "media", "description": "Disfunción transitoria del VI por catecolaminas. ECG + troponina + eco."},
            {"name": "Hipotensión refractaria", "severity": "alta", "description": "Adrenalina IM + IV + volumen + glucagón si betabloqueado. Vasopresina como rescate."},
        ],
        "pearls": [
            "La adrenalina IM es el tratamiento de primera línea — los antihistamínicos NO salvan vidas en anafilaxia.",
            "El muslo anterolateral (IM) absorbe adrenalina 2x más rápido que el deltoides.",
            "Si el paciente toma betabloqueantes: la adrenalina puede no responder — glucagón 1-2 mg IV como alternativa.",
            "Prescribir adrenalina autoinyectable (EpiPen) al alta y educar sobre técnica de uso al paciente y familia.",
            "La anafilaxia no requiere exposición previa documentada — puede ocurrir en primera exposición (vía alternativa IgE-independiente).",
        ],
        "related_differential": None,
        "related_quiz": "errores-frecuentes-urgencias"
    },

    "status-epileptico": {
        "pathophysiology": {
            "summary": "Crisis epiléptica que dura más de 5 minutos o dos crisis sin recuperación de conciencia entre ellas, con excitotoxicidad neuronal progresiva si no se controla en 30 minutos.",
            "flow": [
                {"label": "Crisis epiléptica", "detail": "Descarga neuronal sincrónica excesiva por desequilibrio GABA/glutamato"},
                {"label": "Fallo en la detención", "detail": ">5 min: mecanismos inhibitorios (GABA-A) se internalizan → dificultad para cortar"},
                {"label": "Excitotoxicidad", "detail": "Acumulación de glutamato → entrada masiva de Ca²⁺ → muerte neuronal (hipocampo)"},
                {"label": "Alteraciones sistémicas", "detail": "Hipoxia, acidosis láctica, hipoglucemia, hipertermia, rabdomiólisis, hipoventilación"},
                {"label": "Daño neurológico", "detail": ">30 min sin tratar → necrosis neuronal irreversible, especialmente hipocampal"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "0-5 min: primera línea", "color": "orange",
                 "actions": ["Benzodiacepina IV: lorazepam 0.1 mg/kg IV (o diazepam 0.15-0.2 mg/kg IV)", "Sin vía IV: midazolam bucal/intranasal 0.2 mg/kg o diazepam rectal", "O₂, vía IV, glucemia (descartar hipoglucemia)", "Posición lateral de seguridad"]},
                {"name": "5-20 min: segunda línea", "color": "red",
                 "actions": ["Fenitoína IV 18-20 mg/kg en 20 min (con monitorización ECG)", "Levetiracetam IV 30-60 mg/kg (mejor tolerado)", "Valproato IV 25-45 mg/kg si origen generalizado o focal desconocido", "Fenobarbital IV 15-20 mg/kg si falla fenitoína/LEV"]},
                {"name": "20-40 min: refractario (UCI)", "color": "red",
                 "actions": ["Midazolam IV en perfusión continua (titulación EEG)", "Propofol IV (cuidado en niños)", "Pentobarbital/tiopental si super-refractario", "Objetivo: brote-supresión en EEG"]},
                {"name": "Manejo etiológico", "color": "green",
                 "actions": ["Buscar desencadenante: glucemia, iones, TC cerebral, PL si sospecha meningitis", "Thiamina IV si sospecha deficit (alcohólico, desnutrido)", "Antibióticos si posible meningitis", "Tratar causa subyacente (ACV, tumor, metabolismo)"]},
            ]
        },
        "complications": [
            {"name": "Daño neuronal hipóxico", "severity": "alta", "description": "Hipoxemia + hipoglucemia durante la crisis → muerte neuronal. O₂ y glucosa urgentes."},
            {"name": "Hipoxia / Broncoaspiración", "severity": "alta", "description": "Pérdida de conciencia + hipertonía → obstrucción y broncoaspiración. Posición lateral."},
            {"name": "Rabdomiólisis / IRA", "severity": "alta", "description": "Contracciones musculares intensas → CK elevada → mioglobinuria → NTA."},
            {"name": "Hipertermia", "severity": "media", "description": "Actividad muscular sostenida → T°>40°C → daño sistémico adicional. Refrigerar activamente."},
            {"name": "Inestabilidad hemodinámica", "severity": "media", "description": "Crisis prolongada → acidosis + hipoxia → colapso cardiovascular. Monitorización ICU."},
        ],
        "pearls": [
            "5 minutos = umbral de tratamiento — no esperar los '30 minutos de definición' clásica para actuar.",
            "Benzodiacepinas son la primera línea — lorazepam IV es ligeramente más efectivo que diazepam IV.",
            "La benzodiacepina intranasal/bucal tiene la misma eficacia que IV y es más rápida de administrar fuera del hospital.",
            "Levetiracetam IV ha desplazado a fenitoína por mejor perfil de seguridad (sin riesgo de arritmia).",
            "Siempre medir glucemia — la hipoglucemia causa estatus epiléptico y es fácilmente reversible con dextrosa.",
        ],
        "related_differential": "cefalea-thunderclap",
        "related_quiz": "neuroemergencias"
    },

    "colecistitis-aguda": {
        "pathophysiology": {
            "summary": "Inflamación aguda de la vesícula biliar, generalmente por obstrucción del cístico por un cálculo, que produce distensión, isquemia parietal e infección bacteriana secundaria.",
            "flow": [
                {"label": "Obstrucción del cístico", "detail": "Cálculo en el cuello o conducto cístico → bilis estancada en la vesícula"},
                {"label": "Distensión vesicular", "detail": "Acumulación de bilis + secreciones → ↑ presión intravesicular"},
                {"label": "Isquemia parietal", "detail": "Compresión de la microvascularización → isquemia de la mucosa"},
                {"label": "Inflamación + infección", "detail": "E. coli, Klebsiella, Enterococcus → inflamación transmural → fiebre + leucocitosis"},
                {"label": "Complicaciones", "detail": "Gangrenosa → perforación → peritonitis biliar o absceso perivesicular"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Estabilización inicial", "color": "blue",
                 "actions": ["NPO + analgesia (AINE + opiáceos)", "Cristaloides IV", "Criterios de Tokyo: clasificar gravedad (I-III)", "Eco abdominal: signo de Murphy ecográfico, pared engrosada >4mm, líquido perivesicular"]},
                {"name": "Antibióticos", "color": "orange",
                 "actions": ["Moderada: amoxicilina-clavulánico IV o cefalosporina 2ª generación", "Grave/complicada: piperacilina-tazobactam + metronidazol", "Duración: hasta colecistectomía + 24h post-cirugía (leve/moderada)"]},
                {"name": "Colecistectomía laparoscópica", "color": "yellow",
                 "actions": ["De elección en las primeras 72h (preferible <24h)", "Reduce hospitalización vs cirugía diferida", "Conversión a abierta si complicaciones graves", "Drenaje percutáneo si Tokyo III (muy grave) no candidato a cirugía"]},
                {"name": "Colecistitis acalculosa / crónica", "color": "green",
                 "actions": ["UCI (séptico, postcirugía): sospechar acalculosa → eco urgente", "CPRE si coledocolitiasis asociada", "Control ambulatorio si Tokyo I + buena respuesta ATB"]},
            ]
        },
        "complications": [
            {"name": "Colecistitis gangrenosa", "severity": "alta", "description": "Necrosis de la pared vesicular. Mayor riesgo de perforación. Requiere cirugía urgente."},
            {"name": "Perforación vesicular", "severity": "alta", "description": "Peritonitis biliar local o generalizada. Mortalidad elevada. Drenaje + cirugía urgente."},
            {"name": "Colangitis ascendente", "severity": "alta", "description": "Infección del árbol biliar (coledocolitiasis + infección). Tríada de Charcot + CPRE urgente."},
            {"name": "Fístula colecistointestinal", "severity": "media", "description": "Erosión hacia intestino adyacente. Puede causar íleo biliar (cálculo grande en íleon terminal)."},
            {"name": "Absceso perivesicular", "severity": "media", "description": "Perforación contenida. Drenaje percutáneo guiado por TC + ATB IV."},
        ],
        "pearls": [
            "Criterios de Tokyo para gravedad: I (leve) = responde ATB; II (moderada) = cirugía <72h; III (grave) = disfunción orgánica.",
            "El signo de Murphy ecográfico (dolor bajo la sonda en FCS) tiene VPP >90% para colecistitis.",
            "La colecistectomía laparoscópica precoz (<24h) reduce hospitalización y complicaciones vs cirugía diferida.",
            "La colecistitis acalculosa (sin cálculos) ocurre en pacientes críticos, post-cirugía o con ayuno prolongado.",
            "Coledocolitiasis (ictericia + colangitis): CPRE antes de la colecistectomía.",
        ],
        "related_differential": "dolor-hipocondrio-derecho",
        "related_quiz": "abdomen-agudo"
    },

    "iamsest": {
        "pathophysiology": {
            "summary": "Síndrome coronario agudo sin elevación del ST por oclusión subtotal o distal de una arteria coronaria o estenosis crítica con isquemia subendocárdica, que incluye angina inestable y NSTEMI.",
            "flow": [
                {"label": "Placa aterosclerótica inestable", "detail": "Erosión o rotura parcial de placa → trombo no oclusivo (diferencia con IAMCEST)"},
                {"label": "Reducción de flujo coronario", "detail": "Trombo parcial + vasospasmo → isquemia subendocárdica (NSTEMI) o síntomas sin necrosis (AI)"},
                {"label": "Necrosis subendocárdica", "detail": "NSTEMI: necrosis de la capa más interna (mayor demanda metabólica, más vulnerable)"},
                {"label": "Elevación de troponinas", "detail": "Daño de miocitos → troponinas T e I → elevación y posterior normalización"},
                {"label": "Riesgo de oclusión total", "detail": "Trombo inestable puede progresar → IAMCEST; microémbolos distales → daño difuso"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Antiisquemia inicial", "color": "blue",
                 "actions": ["Nitratos sublinguales/IV si persiste dolor y TA normal", "Betabloqueante VO si FC >60 y sin contraindicaciones", "O₂ si SpO₂ <90%", "Morfina IV si dolor severo (con cautela)"]},
                {"name": "Antitrombótico", "color": "orange",
                 "actions": ["Aspirina 300 mg VO carga + 100 mg/día mantenimiento", "Ticagrelor 180 mg carga (o clopidogrel 600 mg)", "Anticoagulación: fondaparinux SC o enoxaparina SC", "HNF IV si coronariografía precoz"]},
                {"name": "Estratificación y coronariografía", "color": "yellow",
                 "actions": ["GRACE score: bajo (<108) = invasiva electiva; alto (>140) = invasiva precoz <24h", "Inmediata (<2h) si inestabilidad hemodinámica o eléctrica severa", "TIMI score alternativo para riesgo"]},
                {"name": "Alta y crónico", "color": "green",
                 "actions": ["DAPT 12 meses", "Betabloqueante + IECA + estatina alta intensidad", "Rehabilitación cardíaca", "Modificación de FRCV"]},
            ]
        },
        "complications": [
            {"name": "Progresión a IAMCEST", "severity": "alta", "description": "Trombo inestable ocluye completamente la arteria. Monitorización ECG continua."},
            {"name": "Arritmias", "severity": "alta", "description": "TV/FV si isquemia extensa. FA nueva frecuente. Taquicardias por reentrada peri-cicatriz."},
            {"name": "Insuficiencia cardíaca aguda", "severity": "media", "description": "FRCV múltiples + isquemia activa → disfunción sistólica aguda."},
            {"name": "Reestenosis intrastent", "severity": "media", "description": "Proliferación de neointima en stent metálico. Stent liberador de fármaco reduce incidencia."},
            {"name": "Hemorragia por antitrombóticos", "severity": "media", "description": "Triple terapia (DAPT + ACO) = alto riesgo hemorrágico. Mínimo tiempo de triple terapia."},
        ],
        "pearls": [
            "NSTEMI vs Angina Inestable: ambos sin elevación del ST, pero NSTEMI tiene troponinas elevadas.",
            "El cambio dinámico del ST o inversión de la onda T con angina = SCASEST hasta que se demuestre lo contrario.",
            "GRACE score >140: coronariografía <24h — reduce mortalidad vs estrategia conservadora.",
            "Fondaparinux es preferido sobre enoxaparina en SCASEST conservador por menor hemorragia.",
            "La troponina ultrasensible se eleva en las primeras 1-2h — permite rule-out más rápido vs troponina convencional.",
        ],
        "related_differential": "dolor-toracico-agudo",
        "related_quiz": "cardio-urgente"
    },

    "epoc-exacerbado": {
        "pathophysiology": {
            "summary": "Empeoramiento agudo de los síntomas respiratorios del EPOC que requiere cambio de tratamiento, generalmente por infección respiratoria que genera hipersecreción, broncoespasmo y hiperinsuflación dinámica.",
            "flow": [
                {"label": "Factor desencadenante", "detail": "Infección viral (rinovirus 50%) o bacteriana (H. influenzae, S. pneumoniae, M. catarrhalis) → inflamación aguda"},
                {"label": "Inflamación bronquial aguda", "detail": "Neutrófilos + citoquinas → hipersecreción de moco + edema de mucosa"},
                {"label": "Obstrucción de la vía aérea", "detail": "Broncoespasmo + secreciones → ↑ resistencia al flujo espiratorio → atrapamiento de aire"},
                {"label": "Hiperinsuflación dinámica", "detail": "Fallo en vaciado pulmonar → aumento VR → aplana diafragma → ineficiencia muscular"},
                {"label": "Insuficiencia respiratoria", "detail": "Hipoxemia (V/Q alterado) + ↑ PaCO₂ (hipoventilación relativa + muscular) → acidosis respiratoria"},
            ]
        },
        "treatment": {
            "phases": [
                {"name": "Broncodilatadores (1ª línea)", "color": "orange",
                 "actions": ["SABA: salbutamol 2.5-5 mg nebulizado c/4-6h", "SAMA: ipratropio 0.5 mg nebulizado c/6-8h", "Combinación más efectiva que cada uno solo en exacerbación", "Teofilina IV solo si refractario a nebulizaciones"]},
                {"name": "Corticoides sistémicos", "color": "orange",
                 "actions": ["Prednisona 40 mg/día x5 días VO", "Metilprednisolona IV si no tolera VO", "Reduce tiempo de hospitalización y fracaso terapéutico", "No prolongar >5-7 días — sin beneficio adicional"]},
                {"name": "Antibióticos (si indicación)", "color": "yellow",
                 "actions": ["Si: disnea + ↑ expectoración + cambio color esputo (criterios de Anthonisen)", "Amoxicilina-clavulánico VO 7 días (leve-moderada)", "Levofloxacino/azitromicina si P. aeruginosa poco probable", "Piperacilina-tazobactam IV si P. aeruginosa sospechada (FEV₁<30%)"]},
                {"name": "Soporte ventilatorio", "color": "red",
                 "actions": ["O₂ controlado: SpO₂ 88-92% (evitar hipercapnia por efecto Haldane)", "VNI (BiPAP) si pH 7.25-7.35 con PaCO₂ >45 → reduce IOT 50%", "IOT si Glasgow bajo, apnea, fracaso de VNI", "Fisioterapia respiratoria + movilización precoz"]},
            ]
        },
        "complications": [
            {"name": "Insuficiencia respiratoria hipercápnica aguda", "severity": "alta", "description": "PaCO₂ >55 + pH <7.25 = VMI. VNI primero si consciente y cooperador."},
            {"name": "Cor pulmonale agudo descompensado", "severity": "alta", "description": "HTP crónica + hipoxemia aguda → fallo VD. Hipotensión + signos de bajo gasto derecho."},
            {"name": "Neumotórax espontáneo secundario", "severity": "alta", "description": "Bullae en EPOC grave + presiones altas en VMI → rotura. Drenaje urgente."},
            {"name": "TEP en EPOC exacerbado", "severity": "alta", "description": "El 25% de las exacerbaciones 'infecciosas' pueden ser TEP. Sospecha si no responde a ATB."},
            {"name": "Arritmias cardíacas", "severity": "media", "description": "Hipoxemia + betaagonistas + teofilina → FA, TSV. Corregir O₂ y electrolitos."},
        ],
        "pearls": [
            "O₂ en EPOC: objetivo SpO₂ 88-92%, NO 100% — el exceso de O₂ bloquea la vasoconstricción hipóxica y agrava la hipercapnia.",
            "La VNI (BiPAP) en exacerbación grave reduce la necesidad de IOT en un 50% y la mortalidad hospitalaria.",
            "Antibiótico solo si cumple ≥2 criterios de Anthonisen: ↑ disnea + ↑ volumen expectoración + cambio color.",
            "El EPOC grave tiene 50% de mortalidad a 5 años — es crucial el plan anticipado de cuidados.",
            "Radiografía de tórax en toda exacerbación — hasta un 25% tiene causa alternativa (TEP, neumonía, neumotórax).",
        ],
        "related_differential": "disnea-aguda-hipoxemia",
        "related_quiz": "respiratorio-critico"
    },
}
