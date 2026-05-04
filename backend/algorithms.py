ALGORITHMS = [
    {
        "id": "dolor-toracico-urgencias",
        "title": "Manejo del Dolor Torácico en Urgencias",
        "specialty": "Urgencias",
        "difficulty": "Intermedio",
        "description": "Algoritmo de evaluación y manejo inicial del dolor torácico agudo basado en guías ESC 2023.",
        "guideline": "ESC 2023 / AHA/ACC",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente presenta inestabilidad hemodinámica?",
                "context": "TA sistólica <90 mmHg, shock, o arritmia maligna (TV/FV).",
                "options": [
                    {"id": "si", "label": "Sí — inestable", "next": "n_emergencia"},
                    {"id": "no", "label": "No — estable", "next": "n2"}
                ]
            },
            "n_emergencia": {
                "type": "terminal",
                "severity": "critical",
                "title": "Activar código de emergencia inmediato",
                "text": "Paciente inestable con dolor torácico — manejo de emergencia sin demora.",
                "details": [
                    "Monitoreo continuo ECG, TA, SatO2",
                    "Acceso venoso x2 calibre grueso",
                    "O2 si SatO2 <90%",
                    "ECG de 12 derivaciones en <10 minutos",
                    "Desfibrilador al lado del paciente",
                    "Avisar a cardiología de guardia de inmediato"
                ],
                "pearl": "En el paciente inestable, el diagnóstico y el tratamiento van en paralelo. No esperar estudios para iniciar maniobras de estabilización."
            },
            "n2": {
                "type": "question",
                "text": "¿El ECG muestra elevación del ST ≥1mm en ≥2 derivaciones contiguas o BRIHH nuevo?",
                "context": "Realizar ECG en menos de 10 minutos desde el ingreso. El BRIHH nuevo se trata como IAMCEST.",
                "options": [
                    {"id": "si", "label": "Sí → IAMCEST", "next": "n_iamcest_tiempo"},
                    {"id": "no", "label": "No", "next": "n3"}
                ]
            },
            "n_iamcest_tiempo": {
                "type": "question",
                "text": "¿La angioplastia primaria (ICPP) está disponible en menos de 120 minutos desde el diagnóstico?",
                "context": "Tiempo puerta-balón objetivo: <90 minutos. Si el centro no tiene hemodinamia, calcular tiempo de traslado.",
                "options": [
                    {"id": "si", "label": "Sí — ICPP accesible en tiempo", "next": "n_icpp"},
                    {"id": "no", "label": "No — ICPP no disponible en tiempo", "next": "n_trombolisis"}
                ]
            },
            "n_icpp": {
                "type": "terminal",
                "severity": "critical",
                "title": "Activar protocolo ICPP — Angioplastia primaria",
                "text": "IAMCEST con ICPP accesible en tiempo. Esta es la estrategia de reperfusión de elección.",
                "details": [
                    "Doble antiagregación: AAS 300mg + ticagrelor 180mg (o prasugrel) inmediato",
                    "Anticoagulación: heparina no fraccionada 70-100 UI/kg IV",
                    "Activar sala de hemodinamia — tiempo es músculo",
                    "Tiempo puerta-balón objetivo: <90 minutos",
                    "Oxígeno solo si SatO2 <90%",
                    "Morfina si dolor intenso (con precaución — puede reducir absorción de antiagregantes)"
                ],
                "pearl": "Cada 30 minutos de retraso en la ICPP aumenta la mortalidad a 30 días en un 7.5%. El único objetivo es abrir la arteria lo más rápido posible."
            },
            "n_trombolisis": {
                "type": "question",
                "text": "¿Hay contraindicaciones absolutas para la trombolisis?",
                "context": "Contraindicaciones absolutas: ACV hemorrágico previo, ACV isquémico en los últimos 6 meses, neoplasia SNC, cirugía mayor/trauma en últimas 3 semanas, sangrado activo, disección aórtica.",
                "options": [
                    {"id": "no", "label": "No hay contraindicaciones", "next": "n_trombo_ok"},
                    {"id": "si", "label": "Sí hay contraindicaciones", "next": "n_trombo_contra"}
                ]
            },
            "n_trombo_ok": {
                "type": "terminal",
                "severity": "warning",
                "title": "Trombolisis farmacológica — Objetivo <30 min desde el diagnóstico",
                "text": "IAMCEST sin posibilidad de ICPP en tiempo y sin contraindicaciones. Iniciar trombolisis.",
                "details": [
                    "Alteplase 15mg IV bolo → 0.75mg/kg en 30 min → 0.5mg/kg en 60 min (máx 100mg total)",
                    "Heparina no fraccionada concomitante",
                    "Monitoreo ECG continuo — buscar criterios de reperfusión (resolución ST ≥50%)",
                    "Si no hay reperfusión a los 90 min → traslado urgente para ICPP de rescate",
                    "Trasladar a centro con hemodinamia dentro de las 24h para coronariografía"
                ],
                "pearl": "La trombolisis debe iniciarse en <30 minutos desde el diagnóstico (tiempo puerta-aguja). Si hay reperfusión exitosa, coronariografía electiva en 3-24 horas. Si falla: ICPP de rescate inmediata."
            },
            "n_trombo_contra": {
                "type": "terminal",
                "severity": "critical",
                "title": "IAMCEST sin opción de reperfusión estándar — Traslado urgente",
                "text": "Contraindicaciones absolutas a la trombolisis y sin ICPP disponible en tiempo. Situación crítica.",
                "details": [
                    "Traslado urgente al centro con hemodinamia más cercano aunque supere los 120 min",
                    "La reperfusión tardía es mejor que ninguna reperfusión en la mayoría de los casos",
                    "Antiagregación y anticoagulación igualmente",
                    "Considerar balón de contrapulsación intraaórtica si hay shock",
                    "Consulta urgente con cardiología intervencionista"
                ],
                "pearl": "Incluso fuera del tiempo ideal, la ICPP hasta las 12 horas del inicio de síntomas tiene beneficio si el paciente sigue con dolor o inestabilidad. La ventana no es absoluta."
            },
            "n3": {
                "type": "question",
                "text": "¿La troponina de alta sensibilidad está elevada sobre el percentil 99?",
                "context": "Solicitar troponina al ingreso. Si es negativa, repetir a las 1-2h (protocolo 0h/1h o 0h/2h según el ensayo disponible).",
                "options": [
                    {"id": "si", "label": "Sí — troponina elevada", "next": "n4_grace"},
                    {"id": "no", "label": "No — troponina normal", "next": "n5_riesgo"}
                ]
            },
            "n4_grace": {
                "type": "question",
                "text": "¿El score GRACE es mayor a 140 puntos (alto riesgo)?",
                "context": "Score GRACE incluye: edad, FC, TA sistólica, creatinina, Killip, parada cardíaca, desviación ST, troponina elevada.",
                "options": [
                    {"id": "si", "label": "Sí — GRACE >140 (alto riesgo)", "next": "n_iamsest_alto"},
                    {"id": "no", "label": "No — GRACE ≤140 (riesgo intermedio)", "next": "n_iamsest_intermedio"}
                ]
            },
            "n_iamsest_alto": {
                "type": "terminal",
                "severity": "warning",
                "title": "IAMSEST de ALTO riesgo — Estrategia invasiva precoz (<24h)",
                "text": "Troponina elevada + GRACE >140. Coronariografía dentro de las 24 horas.",
                "details": [
                    "DAAT inmediata: AAS 300mg + ticagrelor 180mg",
                    "Anticoagulación: fondaparinux 2.5mg SC o enoxaparina",
                    "Betabloqueante si no hay contraindicaciones",
                    "Coronariografía en <24 horas (estrategia invasiva precoz)",
                    "Monitoreo continuo — riesgo de progresión a IAMCEST"
                ],
                "pearl": "En IAMSEST de alto riesgo, la estrategia invasiva precoz (<24h) reduce muerte e IAM en comparación con el manejo conservador. El GRACE score ≥140 es el umbral de intervención."
            },
            "n_iamsest_intermedio": {
                "type": "terminal",
                "severity": "warning",
                "title": "IAMSEST riesgo intermedio — Estrategia invasiva en <72h",
                "text": "Troponina elevada con GRACE ≤140. Coronariografía dentro de las 72 horas.",
                "details": [
                    "DAAT: AAS + ticagrelor o clopidogrel",
                    "Anticoagulación con enoxaparina o fondaparinux",
                    "Coronariografía en <72 horas",
                    "Ecocardiograma para evaluar función ventricular",
                    "Alta con seguimiento cardiológico estrecho si no hay criterios de hospitalización"
                ],
                "pearl": "El IAMSEST de riesgo intermedio se beneficia de la coronariografía en 48-72h. El riesgo de progresión a IAMCEST justifica la hospitalización y el monitoreo continuo."
            },
            "n5_riesgo": {
                "type": "question",
                "text": "¿El dolor tiene características de alto riesgo? (típico, en reposo, progresivo, cambios ECG transitorios)",
                "context": "Dolor típico: opresivo, irradiado, con diaforesis. Cambios ECG: inversión de T, depresión ST transitoria.",
                "options": [
                    {"id": "si", "label": "Sí — características de alto riesgo", "next": "n_angina_inestable"},
                    {"id": "no", "label": "No — dolor atípico o bajo riesgo", "next": "n_ambulatorio"}
                ]
            },
            "n_angina_inestable": {
                "type": "terminal",
                "severity": "warning",
                "title": "Angina Inestable — Hospitalización y estudio",
                "text": "Dolor típico con troponina normal. No descarta síndrome coronario agudo. Requiere observación.",
                "details": [
                    "Hospitalización para monitoreo y repetición de troponinas seriadas",
                    "AAS 100mg + anticoagulación con enoxaparina",
                    "ECG seriados cada 6-8h",
                    "Prueba de esfuerzo o imagen (eco estrés, SPECT) si troponinas persisten negativas",
                    "Coronariografía si la prueba funcional es positiva"
                ],
                "pearl": "La angina inestable (troponina negativa, sin elevación ST) y el IAMSEST comparten fisiopatología pero difieren en que en la AI no hay necrosis detectable. El manejo inicial es similar pero el pronóstico es algo mejor."
            },
            "n_ambulatorio": {
                "type": "terminal",
                "severity": "success",
                "title": "Bajo riesgo — Alta con seguimiento ambulatorio",
                "text": "Troponina negativa, ECG normal, dolor atípico. Probabilidad baja de síndrome coronario agudo.",
                "details": [
                    "Completar protocolo de troponinas a las 3h (si no se hizo protocolo acelerado)",
                    "Si troponinas negativas y ECG normal: alta con seguimiento en 72h",
                    "Prueba de esfuerzo ambulatoria si hay factores de riesgo cardiovascular",
                    "Indicar señales de alarma para volver a urgencias",
                    "AAS solo si hay clara indicación por factores de riesgo"
                ],
                "pearl": "El score HEART (History, ECG, Age, Risk factors, Troponin) identifica pacientes de bajo riesgo que pueden darse de alta de forma segura. Score ≤3 = mortalidad a 6 semanas <2%."
            }
        }
    },
    {
        "id": "manejo-sepsis-shock",
        "title": "Manejo de Sepsis y Shock Séptico",
        "specialty": "Urgencias / UCI",
        "difficulty": "Avanzado",
        "description": "Protocolo basado en la campaña Surviving Sepsis Campaign 2021 para el reconocimiento y manejo temprano de la sepsis.",
        "guideline": "Surviving Sepsis Campaign 2021",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿Hay sospecha de infección activa?",
                "context": "Fiebre/hipotermia, leucocitosis/leucopenia, signos locales de infección, foco identificable.",
                "options": [
                    {"id": "si", "label": "Sí — sospecha de infección", "next": "n2"},
                    {"id": "no", "label": "No — buscar otro diagnóstico", "next": "n_no_sepsis"}
                ]
            },
            "n_no_sepsis": {
                "type": "terminal",
                "severity": "info",
                "title": "Sin sospecha de infección",
                "text": "Si no hay foco infeccioso claro, considerar diagnósticos alternativos de disfunción orgánica aguda.",
                "details": [
                    "Síndrome inflamatorio no infeccioso (pancreatitis, vasculitis, quemaduras)",
                    "Shock cardiogénico, hemorrágico u obstructivo",
                    "Crisis adrenal",
                    "Intoxicación o síndrome serotoninérgico"
                ],
                "pearl": "El SIRS (taquicardia, fiebre, leucocitosis, taquipnea) sin foco infeccioso no es sepsis. La sepsis requiere infección + disfunción orgánica (definición Sepsis-3)."
            },
            "n2": {
                "type": "question",
                "text": "¿Hay disfunción orgánica aguda? (SOFA ≥2 puntos sobre el basal)",
                "context": "Disfunción orgánica: confusión aguda, creatinina >2mg/dL, bilirrubina >2mg/dL, plaquetas <100k, hipotensión, lactato >2mmol/L, SatO2 <90%.",
                "options": [
                    {"id": "si", "label": "Sí — hay disfunción orgánica → SEPSIS", "next": "n3_lactato"},
                    {"id": "no", "label": "No — sin disfunción orgánica", "next": "n_infeccion_simple"}
                ]
            },
            "n_infeccion_simple": {
                "type": "terminal",
                "severity": "info",
                "title": "Infección sin criterios de Sepsis",
                "text": "Infección activa sin disfunción orgánica. Manejo antibiótico según foco y monitoreo estrecho.",
                "details": [
                    "Cultivos antes de iniciar antibiótico",
                    "Antibiótico dirigido al foco sospechado",
                    "Monitoreo para detección precoz de deterioro",
                    "Reevaluar en 6-12h para detectar progresión a sepsis",
                    "Hidratación según estado de volumen"
                ],
                "pearl": "La infección sin disfunción orgánica no cumple criterios de sepsis (Sepsis-3). Sin embargo, el riesgo de progresión obliga al monitoreo estrecho y el tratamiento antibiótico precoz."
            },
            "n3_lactato": {
                "type": "question",
                "text": "¿El lactato sérico es ≥2 mmol/L?",
                "context": "Medir lactato inmediatamente al identificar sepsis. Lactato ≥4 mmol/L con hipotensión = shock séptico.",
                "options": [
                    {"id": "si_alto", "label": "Lactato ≥4 mmol/L + hipotensión → SHOCK SÉPTICO", "next": "n4_shock"},
                    {"id": "si_inter", "label": "Lactato 2-4 mmol/L — hipoperfusión", "next": "n4_sepsis_fluidos"},
                    {"id": "no", "label": "Lactato <2 mmol/L", "next": "n4_sepsis_antibio"}
                ]
            },
            "n4_shock": {
                "type": "question",
                "text": "¿Se ha iniciado el bundle de 1 hora de la Surviving Sepsis Campaign?",
                "context": "Bundle de 1h: lactato, hemocultivos x2, antibiótico de amplio espectro, bolo de cristaloides 30mL/kg, vasopresores si hipotensión persiste.",
                "options": [
                    {"id": "no", "label": "No — iniciar bundle ahora", "next": "n_bundle"},
                    {"id": "si", "label": "Sí — bundle iniciado", "next": "n5_respuesta_fluidos"}
                ]
            },
            "n_bundle": {
                "type": "terminal",
                "severity": "critical",
                "title": "SHOCK SÉPTICO — Iniciar Bundle de 1 Hora AHORA",
                "text": "Cada hora de retraso aumenta la mortalidad un 7%. Ejecutar en paralelo, no secuencialmente.",
                "details": [
                    "1️⃣ MEDIR: Lactato sérico urgente",
                    "2️⃣ CULTIVAR: Hemocultivos x2 (aerobio + anaerobio) ANTES del antibiótico",
                    "3️⃣ ANTIBIÓTICO: Amplio espectro según foco en <1 hora (ej: pip-tazo + vancomicina)",
                    "4️⃣ FLUIDOS: Bolo de cristaloides 30mL/kg en 30 minutos",
                    "5️⃣ VASOPRESORES: Norepinefrina si TA media <65 pese a fluidos",
                    "📍 UCI: Ingreso urgente para monitoreo invasivo"
                ],
                "pearl": "El antibiótico es lo más urgente. Si el cultivo no se puede tomar en <45 minutos, dar el antibiótico sin esperarlo. La demora en el antibiótico mata; la demora en el cultivo no."
            },
            "n5_respuesta_fluidos": {
                "type": "question",
                "text": "¿La TA media es ≥65 mmHg después de los fluidos?",
                "context": "Si después de 30mL/kg de cristaloides la TA media sigue <65 mmHg, iniciar vasopresores.",
                "options": [
                    {"id": "si", "label": "Sí — responde a fluidos", "next": "n_responde_fluidos"},
                    {"id": "no", "label": "No — sigue hipotensa", "next": "n_vasopresores"}
                ]
            },
            "n_responde_fluidos": {
                "type": "terminal",
                "severity": "warning",
                "title": "Sepsis respondedora a fluidos — Continuar monitoreo en UCI",
                "text": "TA media ≥65 tras fluidoterapia. Continuar el bundle y buscar el control del foco.",
                "details": [
                    "Repetir lactato en 2h — objetivo: clearance >10% (o lactato <2)",
                    "Ajustar antibiótico al antibiograma en 48-72h",
                    "Buscar y controlar el foco (drenaje de absceso, retirada de catéter, etc.)",
                    "Evitar sobrecarga de fluidos — balance hídrico neutro o negativo después de la fase inicial",
                    "Corticoides (hidrocortisona 200mg/día) si refractario a vasopresores"
                ],
                "pearl": "El clearance de lactato ≥10% en 2 horas es un marcador de respuesta al tratamiento. Si el lactato no cae, buscar foco no controlado o insuficiencia adrenal."
            },
            "n_vasopresores": {
                "type": "terminal",
                "severity": "critical",
                "title": "Shock séptico refractario a fluidos — Vasopresores",
                "text": "Iniciar norepinefrina para mantener TA media ≥65 mmHg. Considerar hidrocortisona.",
                "details": [
                    "Norepinefrina: vasopresor de primera línea, iniciar por vía central o intraósea",
                    "Si norepinefrina >0.25 mcg/kg/min: agregar vasopresina 0.03 UI/min",
                    "Hidrocortisona 200mg/día IV si shock refractario a 2 vasopresores",
                    "Acceso venoso central + línea arterial para monitoreo continuo",
                    "Objetivo: TA media ≥65, diuresis ≥0.5mL/kg/h, lactato en descenso"
                ],
                "pearl": "La dopamina ya no es el vasopresor de primera línea en sepsis (mayor tasa de arritmias). La norepinefrina tiene mayor seguridad y eficacia. La vasopresina se agrega como ahorradora de catecolaminas."
            },
            "n4_sepsis_fluidos": {
                "type": "terminal",
                "severity": "warning",
                "title": "Sepsis con hipoperfusión — Bundle de 1 hora",
                "text": "Lactato 2-4 mmol/L indica hipoperfusión tisular. Iniciar manejo completo.",
                "details": [
                    "Hemocultivos x2 antes del antibiótico",
                    "Antibiótico de amplio espectro en <1 hora",
                    "Bolo de cristaloides 30mL/kg",
                    "Monitoreo de TA cada 15 minutos",
                    "Repetir lactato en 2h — objetivo: clearance ≥10%",
                    "Considerar ingreso a UCI para monitoreo"
                ],
                "pearl": "El lactato entre 2-4 mmol/L identifica pacientes con hipoperfusión oculta que pueden progresar a shock. La intervención precoz en este estadio previene la evolución a shock séptico."
            },
            "n4_sepsis_antibio": {
                "type": "terminal",
                "severity": "warning",
                "title": "Sepsis sin hipoperfusión — Tratamiento y monitoreo",
                "text": "Sepsis con lactato normal. Tratamiento antibiótico precoz y monitoreo para detectar deterioro.",
                "details": [
                    "Hemocultivos x2 antes del antibiótico",
                    "Antibiótico dirigido al foco sospechado en <1 hora",
                    "Hidratación IV según estado de volumen",
                    "Monitoreo horario de signos vitales",
                    "Repetir lactato en 2-4h",
                    "Control del foco infeccioso"
                ],
                "pearl": "La sepsis sin hipoperfusión tiene mejor pronóstico pero sigue siendo una emergencia. El antibiótico en la primera hora reduce la mortalidad incluso en estos casos menos graves."
            }
        }
    },
    {
        "id": "algoritmo-tep",
        "title": "Diagnóstico y Manejo del TEP",
        "specialty": "Urgencias / Medicina Interna",
        "difficulty": "Avanzado",
        "description": "Algoritmo diagnóstico y terapéutico del tromboembolismo pulmonar según guías ESC 2019.",
        "guideline": "ESC 2019",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente presenta inestabilidad hemodinámica?",
                "context": "TA sistólica <90 mmHg, caída de TA ≥40mmHg, necesidad de vasopresores o paro cardíaco.",
                "options": [
                    {"id": "si", "label": "Sí — TEP de alto riesgo (masivo)", "next": "n_alto_riesgo"},
                    {"id": "no", "label": "No — hemodinámicamente estable", "next": "n2_wells"}
                ]
            },
            "n_alto_riesgo": {
                "type": "question",
                "text": "¿Hay tiempo para realizar TC angiografía pulmonar (TCAP)?",
                "context": "Si el paciente está en paro o su estado es crítico, la trombolisis puede indicarse sin confirmación tomográfica.",
                "options": [
                    {"id": "si", "label": "Sí — realizar TCAP urgente", "next": "n_tcap_urgente"},
                    {"id": "no", "label": "No — paro o deterioro extremo", "next": "n_trombo_empirica"}
                ]
            },
            "n_trombo_empirica": {
                "type": "terminal",
                "severity": "critical",
                "title": "TEP masivo con paro — Trombolisis empírica",
                "text": "Sin tiempo para confirmar diagnóstico. Trombolisis empírica ante alta sospecha clínica.",
                "details": [
                    "Alteplase 50mg IV en 2 minutos (en paro cardíaco)",
                    "RCP si paro cardiorrespiratorio — no es contraindicación",
                    "Heparina no fraccionada después de la trombolisis",
                    "Si hay ecocardiograma a pie de cama: VD dilatado + disfunción = confirma sospecha",
                    "Considerar embolectomía quirúrgica si trombolisis contraindicada"
                ],
                "pearl": "En paro cardíaco por TEP masivo sospechado, la trombolisis empírica sin diagnóstico confirmado es aceptable. La RCP no es contraindicación para la trombolisis. Si funciona, continuar RCP 60-90 minutos para permitir efecto."
            },
            "n_tcap_urgente": {
                "type": "terminal",
                "severity": "critical",
                "title": "TEP de alto riesgo confirmado — Trombolisis sistémica",
                "text": "TCAP confirma TEP masivo en paciente inestable. Trombolisis sistémica de urgencia.",
                "details": [
                    "Alteplase 100mg IV en 2 horas (régimen estándar)",
                    "Suspender heparina durante la infusión de alteplase",
                    "Reiniciar heparina 2h después de alteplase cuando TTPA <80 seg",
                    "UCI para monitoreo post-trombolisis",
                    "Si trombolisis contraindicada: embolectomía quirúrgica o trombectomía percutánea"
                ],
                "pearl": "La trombolisis sistémica en TEP masivo reduce la mortalidad pero tiene riesgo hemorrágico del 10% (HIC 2%). Está indicada solo en shock/paro. En TEP submasivo (VD disfuncionante sin shock) no reduce mortalidad pero sí sangrado — no está recomendada de rutina."
            },
            "n2_wells": {
                "type": "question",
                "text": "¿Cuál es la probabilidad pre-test según el Score de Wells?",
                "context": "Wells: TVP clínica (+3), diagnóstico alternativo menos probable (+3), FC >100 (+1.5), inmovilización/cirugía en 4 sem (+1.5), TVP/TEP previo (+1.5), hemoptisis (+1), neoplasia activa (+1).",
                "options": [
                    {"id": "alta", "label": "Wells >6 — Probabilidad ALTA", "next": "n_tcap_directo"},
                    {"id": "moderada", "label": "Wells 2-6 — Probabilidad MODERADA", "next": "n_dimero_moderado"},
                    {"id": "baja", "label": "Wells <2 — Probabilidad BAJA", "next": "n_dimero_bajo"}
                ]
            },
            "n_tcap_directo": {
                "type": "question",
                "text": "¿La TC angiografía pulmonar confirma el TEP?",
                "context": "Con Wells >6, ir directo a TCAP sin dímero D (el dímero no sirve para descartar en alta probabilidad).",
                "options": [
                    {"id": "si", "label": "Sí — TEP confirmado", "next": "n_clasificar_gravedad"},
                    {"id": "no", "label": "No — TCAP negativo", "next": "n_no_tep"}
                ]
            },
            "n_dimero_moderado": {
                "type": "question",
                "text": "¿El dímero D es positivo (>500 ng/mL o ajustado por edad)?",
                "context": "En >50 años usar dímero ajustado por edad: edad × 10 ng/mL. Ej: paciente de 70 años → umbral 700 ng/mL.",
                "options": [
                    {"id": "si", "label": "Sí — dímero elevado → TCAP", "next": "n_tcap_directo"},
                    {"id": "no", "label": "No — dímero negativo → TEP descartado", "next": "n_no_tep"}
                ]
            },
            "n_dimero_bajo": {
                "type": "question",
                "text": "¿El dímero D es negativo (<500 ng/mL o ajustado por edad)?",
                "context": "En probabilidad baja, el dímero negativo descarta TEP con valor predictivo negativo >99%.",
                "options": [
                    {"id": "si", "label": "Sí — dímero negativo → TEP descartado", "next": "n_no_tep"},
                    {"id": "no", "label": "No — dímero positivo → TCAP", "next": "n_tcap_directo"}
                ]
            },
            "n_no_tep": {
                "type": "terminal",
                "severity": "success",
                "title": "TEP descartado — Buscar diagnóstico alternativo",
                "text": "El algoritmo excluye TEP con seguridad. Buscar otras causas de los síntomas.",
                "details": [
                    "No iniciar anticoagulación por sospecha de TEP",
                    "Considerar diagnósticos alternativos: NAC, pleuritis, musculoesquelético, ICC",
                    "Si la sospecha clínica es muy alta pese a la TCAP negativa: consultar con radiología",
                    "En caso de duda: eco con Doppler venoso para descartar TVP"
                ],
                "pearl": "La TCAP negativa en alta probabilidad clínica es un resultado discordante. Se debe revisar la calidad del estudio, considerar TEP subsegmentario (no detectado) y valorar con el radiólogo si la imagen es diagnóstica."
            },
            "n_clasificar_gravedad": {
                "type": "question",
                "text": "¿Hay disfunción ventricular derecha en la imagen Y troponina elevada?",
                "context": "Disfunción VD: VD/VI >0.9 en TCAP o eco, BNP elevado. TEP submasivo = VD disfuncionante sin shock.",
                "options": [
                    {"id": "si", "label": "Sí — TEP submasivo (alto riesgo intermedio)", "next": "n_submasivo"},
                    {"id": "no", "label": "No — TEP de bajo riesgo", "next": "n_bajo_riesgo"}
                ]
            },
            "n_submasivo": {
                "type": "terminal",
                "severity": "warning",
                "title": "TEP Submasivo — Anticoagulación + monitoreo intensivo",
                "text": "TEP con disfunción VD sin shock. Anticoagulación plena y monitoreo estrecho por riesgo de deterioro.",
                "details": [
                    "Anticoagulación: HBPM o NACO (apixabán o rivaroxabán) — NO trombolisis de rutina",
                    "Monitoreo en unidad de cuidados intermedios o UCI",
                    "Ecocardiograma seriado para detectar deterioro hemodinámico",
                    "Si deteriora a shock: trombolisis o trombectomía de rescate",
                    "Troponina seriada para monitorizar daño miocárdico",
                    "Duración anticoagulación: mínimo 3-6 meses"
                ],
                "pearl": "La trombolisis en TEP submasivo (disfunción VD sin shock) reduce la progresión a deterioro hemodinámico pero aumenta el sangrado mayor sin reducir mortalidad — no se recomienda de rutina. Solo si hay deterioro a shock."
            },
            "n_bajo_riesgo": {
                "type": "terminal",
                "severity": "success",
                "title": "TEP de bajo riesgo — Anticoagulación y alta posible",
                "text": "TEP sin disfunción VD ni elevación de troponina. Buen pronóstico. Considerar manejo ambulatorio.",
                "details": [
                    "NACO de elección: apixabán 10mg/12h x7 días → 5mg/12h, o rivaroxabán 15mg/12h x21 días → 20mg/día",
                    "Score HESTIA o sPESI para evaluar criterios de alta precoz",
                    "Si sPESI=0 y sin contraindicaciones: alta en <24h con seguimiento ambulatorio",
                    "Duración: 3 meses si factor de riesgo transitorio, indefinido si no provocado",
                    "Estudio de trombofilia si <50 años o TEP no provocado recurrente"
                ],
                "pearl": "Los NACOs han reemplazado a la heparina + warfarina en el TEP de bajo/intermedio riesgo. Son igual de eficaces, más seguros y sin necesidad de controles de INR. El apixabán y rivaroxabán pueden iniciarse sin heparina previa."
            }
        }
    },
    {
        "id": "manejo-shock-agudo",
        "title": "Clasificación y Manejo del Shock",
        "specialty": "Urgencias / UCI",
        "difficulty": "Avanzado",
        "description": "Algoritmo para identificar el tipo de shock y orientar el tratamiento inicial basado en el mecanismo fisiopatológico.",
        "guideline": "SCCM / ESC",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿Hay hipotensión sostenida con signos de hipoperfusión?",
                "context": "TA sistólica <90mmHg o MAP <65mmHg + al menos uno: lactato >2, confusión, oliguria <0.5mL/kg/h, extremidades frías.",
                "options": [
                    {"id": "si", "label": "Sí — criterios de shock presentes", "next": "n2_tipo"},
                    {"id": "no", "label": "No — sin shock", "next": "n_no_shock"}
                ]
            },
            "n_no_shock": {
                "type": "terminal",
                "severity": "success",
                "title": "Sin criterios de shock — Vigilancia",
                "text": "No cumple criterios de shock. Monitoreo para detectar deterioro precozmente.",
                "details": [
                    "Monitorizar TA, FC, diuresis, lactato cada 1-2h",
                    "Identificar la causa del deterioro hemodinámico leve",
                    "Hidratación según respuesta y contexto clínico",
                    "Si hay hipotensión sin hipoperfusión: puede ser constitucional o por medicamentos"
                ],
                "pearl": "La hipotensión sin hipoperfusión no es shock. El shock se define por hipoperfusión tisular, no solo por cifras de TA. Un paciente con TA 85/50 sin lactato elevado ni signos de hipoperfusión puede no estar en shock."
            },
            "n2_tipo": {
                "type": "question",
                "text": "¿Cuál es la presentación hemodinámica predominante?",
                "context": "Evaluar: temperatura de extremidades, ingurgitación yugular, auscultación, contexto clínico, respuesta a fluidos.",
                "options": [
                    {"id": "distributivo", "label": "Extremidades calientes + vasodilatación (distributivo)", "next": "n3_distributivo"},
                    {"id": "cardiogenico", "label": "Extremidades frías + IY elevada + crepitantes (cardiogénico)", "next": "n3_cardiogenico"},
                    {"id": "hipovolemico", "label": "Extremidades frías + IY plana + sin crepitantes (hipovolémico)", "next": "n3_hipovolemico"},
                    {"id": "obstructivo", "label": "Extremidades frías + IY elevada + sin crepitantes (obstructivo)", "next": "n3_obstructivo"}
                ]
            },
            "n3_distributivo": {
                "type": "question",
                "text": "¿Cuál es la causa más probable del shock distributivo?",
                "context": "Séptico: foco infeccioso identificado. Anafiláctico: exposición a alérgeno + urticaria/angioedema. Neurogénico: trauma medular.",
                "options": [
                    {"id": "septico", "label": "Séptico — foco infeccioso", "next": "n_septico"},
                    {"id": "anafilactico", "label": "Anafiláctico — exposición a alérgeno", "next": "n_anafilactico"},
                    {"id": "neurogénico", "label": "Neurogénico — trauma medular", "next": "n_neurogénico"}
                ]
            },
            "n_septico": {
                "type": "terminal",
                "severity": "critical",
                "title": "Shock Séptico — Bundle de 1 hora",
                "text": "Ver algoritmo de Sepsis para manejo completo. Puntos clave:",
                "details": [
                    "Hemocultivos x2 → antibiótico amplio espectro en <1h",
                    "Bolo cristaloides 30mL/kg en 30 minutos",
                    "Norepinefrina si TA media <65 tras fluidos",
                    "Lactato y clearance de lactato en 2h",
                    "Buscar y controlar el foco infeccioso"
                ],
                "pearl": "El shock séptico es el más frecuente en UCI. Norepinefrina es el vasopresor de primera línea. La hidrocortisona se agrega cuando se necesitan dosis altas de norepinefrina (>0.25 mcg/kg/min)."
            },
            "n_anafilactico": {
                "type": "terminal",
                "severity": "critical",
                "title": "Shock Anafiláctico — Adrenalina IM INMEDIATA",
                "text": "La adrenalina es el único tratamiento que revierte el shock anafiláctico. No hay contraindicaciones.",
                "details": [
                    "Adrenalina 0.5mg IM en muslo anterolateral — PRIMERA ACCIÓN",
                    "Repetir cada 5-15 min si no hay respuesta",
                    "Posición: decúbito con piernas elevadas (si no hay angioedema/disnea)",
                    "SF 1000-2000mL IV rápido para la hipotensión",
                    "Si shock refractario: adrenalina IV en infusión (0.1-0.5 mcg/kg/min)",
                    "Antihistamínico + corticoide DESPUÉS de la adrenalina (no en lugar de)"
                ],
                "pearl": "El error más fatal en anafilaxia es no dar adrenalina o darla tarde. Los antihistamínicos y corticoides NO revierten el shock anafiláctico — son adyuvantes para prevenir la fase tardía."
            },
            "n_neurogénico": {
                "type": "terminal",
                "severity": "warning",
                "title": "Shock Neurogénico — Fluidos + Vasopresores + Inmovilización",
                "text": "Pérdida del tono simpático por lesión medular ≥T6. Bradicardia + hipotensión paradójica.",
                "details": [
                    "Cristaloides con precaución (riesgo de edema medular por sobrecarga)",
                    "Norepinefrina o fenilefrina para restaurar el tono vascular",
                    "Atropina si hay bradicardia sintomática",
                    "Inmovilización de columna si no está asegurada",
                    "Objetivo: TA media ≥85-90mmHg en lesión medular aguda (mayor que en otros shocks)"
                ],
                "pearl": "El shock neurogénico tiene la paradoja de bradicardia con hipotensión (sin taquicardia compensadora por lesión simpática). En otros shocks hay taquicardia compensadora. Esta diferencia es clave para identificarlo."
            },
            "n3_cardiogenico": {
                "type": "question",
                "text": "¿Cuál es la causa probable del shock cardiogénico?",
                "context": "IAM: contexto coronario. Miocarditis: viral, joven. Valvular: soplo, historia. Tamponamiento: IY muy elevada, ruidos apagados, pulso paradójico.",
                "options": [
                    {"id": "iam", "label": "IAM / síndrome coronario agudo", "next": "n_cardiogenico_iam"},
                    {"id": "tamponade", "label": "Tamponamiento cardíaco", "next": "n_tamponade"},
                    {"id": "otro", "label": "Miocarditis / valvulopatía aguda", "next": "n_cardiogenico_otro"}
                ]
            },
            "n_cardiogenico_iam": {
                "type": "terminal",
                "severity": "critical",
                "title": "Shock Cardiogénico por IAM — Revascularización urgente",
                "text": "El shock por IAM tiene 40-50% de mortalidad. La revascularización urgente es la única medida que cambia el pronóstico.",
                "details": [
                    "ICPP urgente como prioridad absoluta — no esperar estabilización hemodinámica",
                    "Balón de contrapulsación intraaórtica si disponible",
                    "Dobutamina 5-20 mcg/kg/min como inotrópico (si TA lo permite)",
                    "Norepinefrina para mantener TA mínima que permita perfusión coronaria",
                    "NO dar fluidos agresivos — puede empeorar el edema pulmonar",
                    "UCI cardiológica urgente"
                ],
                "pearl": "En shock por IAM, la ICPP urgente reduce la mortalidad a 6 meses del 65% al 46%. Cada minuto de retraso empeora el pronóstico. No esperar estabilización antes de la revascularización — la revascularización ES la estabilización."
            },
            "n_tamponade": {
                "type": "terminal",
                "severity": "critical",
                "title": "Tamponamiento Cardíaco — Pericardiocentesis urgente",
                "text": "Tríada de Beck: hipotensión + ingurgitación yugular + ruidos cardíacos apagados. Emergencia.",
                "details": [
                    "Pericardiocentesis guiada por eco — drenaje de urgencia",
                    "NO dar diuréticos ni vasodilatadores (empeorarán el shock)",
                    "Fluidos IV pueden mantener el llenado mientras se prepara el drenaje",
                    "Ecocardiograma urgente: colapso diastólico de VD + VCI dilatada sin colapso",
                    "Si no hay eco: pericardiocentesis clínica guiada por ECG"
                ],
                "pearl": "El tamponamiento es el único shock que empeora dramáticamente con la respiración espontánea profunda. El pulso paradójico (caída >10mmHg de TA sistólica en inspiración) es su signo clásico. El eco a pie de cama lo diagnostica en 30 segundos."
            },
            "n_cardiogenico_otro": {
                "type": "terminal",
                "severity": "critical",
                "title": "Shock Cardiogénico no isquémico — Soporte e investigación",
                "text": "Miocarditis fulminante o valvulopatía aguda. Alta mortalidad. Soporte hemodinámico y diagnóstico urgente.",
                "details": [
                    "Ecocardiograma urgente para diagnóstico etiológico",
                    "Dobutamina como inotrópico de primera línea",
                    "Considerar soporte mecánico: IABP, Impella, ECMO venoarterial",
                    "En miocarditis fulminante por autoinmune: corticoides e inmunoglobulina",
                    "Traslado urgente a centro con capacidad de soporte ventricular mecánico"
                ],
                "pearl": "La miocarditis fulminante en jóvenes puede requerir ECMO como puente a la recuperación (la miocarditis fulminante tiene paradójicamente mejor pronóstico a largo plazo que la miocarditis aguda no fulminante, si se sobrevive la fase aguda)."
            },
            "n3_hipovolemico": {
                "type": "question",
                "text": "¿La causa de la hipovolemia es hemorrágica?",
                "context": "Hemorrágico: trauma, HDA, hemoperitoneo. No hemorrágico: deshidratación, vómitos, diarrea, tercer espacio.",
                "options": [
                    {"id": "si", "label": "Sí — shock hemorrágico", "next": "n_hemorragico"},
                    {"id": "no", "label": "No — deshidratación / pérdidas", "next": "n_deshidratacion"}
                ]
            },
            "n_hemorragico": {
                "type": "terminal",
                "severity": "critical",
                "title": "Shock Hemorrágico — Control del sangrado es la prioridad",
                "text": "Los fluidos son temporales. El control del foco hemorrágico es el tratamiento definitivo.",
                "details": [
                    "Control físico del sangrado: presión directa, torniquete, cirugía de control de daños",
                    "Activar protocolo de transfusión masiva: PG:PFC:Plaquetas = 1:1:1",
                    "Ácido tranexámico 1g IV en <3h del trauma (reduce mortalidad)",
                    "Evitar hipotermia, acidosis y coagulopatía ('tríada de la muerte')",
                    "TA objetivo permisiva: sistólica 80-90 mmHg (salvo TCE que requiere ≥90)",
                    "Cirugía/radiología intervencionista urgente para control definitivo"
                ],
                "pearl": "La 'hipotensión permisiva' (TA sistólica 80-90mmHg) en shock hemorrágico evita empeorar la coagulopatía dilucional. La excepción es el TCE concomitante, donde se necesita TA más alta para mantener la presión de perfusión cerebral."
            },
            "n_deshidratacion": {
                "type": "terminal",
                "severity": "warning",
                "title": "Shock Hipovolémico no hemorrágico — Reposición de volumen",
                "text": "Pérdidas por vómitos, diarrea, quemaduras o tercer espacio. Responde bien a fluidos.",
                "details": [
                    "Cristaloides IV: Ringer lactato de preferencia (más fisiológico que SF en grandes volúmenes)",
                    "Bolo inicial 500-1000mL y reevaluar respuesta",
                    "Corrección de electrolitos: K+, Na+, Mg++",
                    "Tratar la causa de las pérdidas (antieméticos, antidiarreicos, IBP)",
                    "Monitorizar diuresis como indicador de respuesta",
                    "Considerar sonda vesical para monitoreo estricto"
                ],
                "pearl": "El SF (suero fisiológico 0.9%) en grandes volúmenes produce acidosis hiperclorémica. El Ringer lactato es más fisiológico para la reposición de grandes volúmenes. La excepción es la hipercalemia o alcalosis metabólica donde el SF puede ser preferible."
            },
            "n3_obstructivo": {
                "type": "question",
                "text": "¿Cuál es la causa más probable del shock obstructivo?",
                "context": "TEP masivo: hipoxemia súbita. Neumotórax a tensión: desviación traqueal, sin murmullo en un lado. Tamponamiento: ruidos apagados, IY elevada.",
                "options": [
                    {"id": "tep", "label": "TEP masivo — disnea, hipoxemia, post-quirúrgico", "next": "n_tep_shock"},
                    {"id": "neumo", "label": "Neumotórax a tensión — trauma, ventilación mecánica", "next": "n_neumo_tension"},
                    {"id": "tamponade2", "label": "Tamponamiento — ruidos apagados, IY muy elevada", "next": "n_tamponade"}
                ]
            },
            "n_tep_shock": {
                "type": "terminal",
                "severity": "critical",
                "title": "TEP Masivo con Shock — Trombolisis sistémica",
                "text": "TEP de alto riesgo. Trombolisis sin demora si no hay contraindicaciones absolutas.",
                "details": [
                    "Alteplase 100mg IV en 2 horas o 50mg en 15 min si paro inminente",
                    "Heparina no fraccionada antes de la trombolisis, suspender durante la infusión",
                    "O2 de alto flujo + soporte ventilatorio si precisa",
                    "Si trombolisis contraindicada: embolectomía quirúrgica o trombectomía percutánea",
                    "Eco a pie de cama: VD dilatado + septum paradójico = confirma TEP masivo"
                ],
                "pearl": "El shock obstructivo por TEP masivo es la única indicación de trombolisis en TEP. En TEP sin shock, la trombolisis aumenta el sangrado sin reducir la mortalidad. La diferencia entre 'TEP con shock' y 'TEP sin shock' determina completamente la estrategia."
            },
            "n_neumo_tension": {
                "type": "terminal",
                "severity": "critical",
                "title": "Neumotórax a Tensión — Descompresión inmediata",
                "text": "Emergencia que mata en minutos. Descompresión sin esperar confirmación radiológica si la sospecha es alta.",
                "details": [
                    "Aguja: 2° espacio intercostal, línea medioclavicular, borde superior de la costilla inferior",
                    "Inmediatamente después: toracocentesis con tubo en 5° espacio, línea axilar media",
                    "No esperar RxTx si hay compromiso hemodinámico grave",
                    "En ventilación mecánica: neumotórax a tensión es más frecuente y fulminante",
                    "Diagnóstico clínico: ausencia unilateral de murmullo + desviación traqueal contralateral + shock"
                ],
                "pearl": "El neumotórax a tensión mata por colapso cardiovascular, no por hipoxemia. La descompresión con aguja en el 2° EIC en segundos puede salvar la vida mientras se prepara el tubo de tórax. No esperar imagen en el paciente en shock."
            }
        }
    },
    {
        "id": "hipertension-arterial-urgencias",
        "title": "Manejo de HTA en Urgencias",
        "specialty": "Urgencias / Medicina Interna",
        "difficulty": "Básico",
        "description": "Algoritmo para clasificar y manejar la hipertensión arterial en el servicio de urgencias. Diferenciación entre urgencia y emergencia hipertensiva.",
        "guideline": "ESH/ESC 2023",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿La TA sistólica es ≥180 mmHg o diastólica ≥120 mmHg?",
                "context": "Confirmar con 2 lecturas en reposo de 5 minutos. Descartar error de medición (manguito incorrecto, brazo incorrecto).",
                "options": [
                    {"id": "si", "label": "Sí — HTA severa ≥180/120", "next": "n2_danio"},
                    {"id": "no", "label": "No — HTA no severa", "next": "n_hta_leve"}
                ]
            },
            "n_hta_leve": {
                "type": "terminal",
                "severity": "info",
                "title": "HTA no severa — Manejo ambulatorio",
                "text": "TA elevada sin criterios de urgencia ni emergencia. No requiere tratamiento IV urgente.",
                "details": [
                    "Optimizar tratamiento antihipertensivo oral habitual",
                    "Identificar y tratar causas de descompensación: dolor, ansiedad, abandono del tratamiento",
                    "Control en consulta de medicina en 1-2 semanas",
                    "No bajar la TA bruscamente — puede causar hipoperfusión",
                    "Educación sobre adherencia al tratamiento"
                ],
                "pearl": "La HTA 160/100 sin síntomas en urgencias no requiere tratamiento IV urgente. La reducción brusca de la TA puede ser más peligrosa que la HTA moderada crónica. El objetivo es la normalización gradual en semanas."
            },
            "n2_danio": {
                "type": "question",
                "text": "¿Hay evidencia de daño agudo de órgano diana?",
                "context": "Órganos diana: cerebro (encefalopatía, ACV, HSA), corazón (IAM, disección, EAP), riñón (creatinina en ascenso), retina (exudados, hemorragias, papiledema), eclampsia.",
                "options": [
                    {"id": "si", "label": "Sí → EMERGENCIA HIPERTENSIVA", "next": "n3_tipo_emergencia"},
                    {"id": "no", "label": "No → URGENCIA HIPERTENSIVA", "next": "n_urgencia"}
                ]
            },
            "n_urgencia": {
                "type": "terminal",
                "severity": "warning",
                "title": "Urgencia Hipertensiva — Reducción gradual oral",
                "text": "TA ≥180/120 sin daño de órgano diana. No requiere tratamiento IV. Reducir TA en horas.",
                "details": [
                    "Captopril 25mg sublingual o VO (inicio en 15-30 min)",
                    "Labetalol 200mg VO si no hay contraindicación",
                    "Objetivo: reducir TA un 25% en las primeras 2-6 horas",
                    "Observación 2-4h en urgencias",
                    "Alta con ajuste de tratamiento antihipertensivo y control en 24-72h",
                    "Investigar causa de descompensación: abandono, dolor, AINE, cocaína"
                ],
                "pearl": "La urgencia hipertensiva NO es una emergencia. No requiere tratamiento IV ni hospitalización. La reducción de TA debe ser gradual (objetivo: 25% en las primeras horas, normalización en días-semanas). La reducción brusca puede causar ACV isquémico por hipoperfusión cerebral."
            },
            "n3_tipo_emergencia": {
                "type": "question",
                "text": "¿Cuál es el órgano diana afectado?",
                "context": "La elección del antihipertensivo IV depende del órgano comprometido.",
                "options": [
                    {"id": "cerebral", "label": "SNC — encefalopatía, ACV hemorrágico", "next": "n_emergencia_cerebral"},
                    {"id": "cardiaco", "label": "Corazón — EAP, IAM, disección aórtica", "next": "n_emergencia_cardiaca"},
                    {"id": "renal", "label": "Riñón — creatinina en ascenso, proteinuria", "next": "n_emergencia_renal"},
                    {"id": "eclampsia", "label": "Eclampsia / preeclampsia severa", "next": "n_eclampsia"}
                ]
            },
            "n_emergencia_cerebral": {
                "type": "terminal",
                "severity": "critical",
                "title": "Emergencia Hipertensiva con Afección Neurológica",
                "text": "Manejo diferenciado según la patología neurológica específica.",
                "details": [
                    "Encefalopatía hipertensiva: labetalol o nicardipino IV, objetivo reducir MAP 25% en 1h",
                    "ACV hemorrágico: objetivo TA <140 mmHg sistólica (si TA >180 al ingreso)",
                    "ACV isquémico agudo (sin trombolisis): no tratar salvo TA >220/120",
                    "ACV isquémico + trombolisis: TA <185/110 antes y <180/105 durante 24h post-tPA",
                    "EVITAR nitroprusiato en patología neurológica (aumenta presión intracraneal)"
                ],
                "pearl": "En ACV isquémico agudo NO trombolizado, la hipertensión es un mecanismo compensador para mantener la perfusión de la penumbra isquémica. Tratar solo si TA >220/120 mmHg. Bajar la TA puede extender el infarto."
            },
            "n_emergencia_cardiaca": {
                "type": "terminal",
                "severity": "critical",
                "title": "Emergencia Hipertensiva Cardíaca",
                "text": "EAP hipertensivo, IAM o disección aórtica. Cada uno requiere manejo específico.",
                "details": [
                    "EAP hipertensivo: nitroglicerina IV + furosemida IV + VNI (CPAP)",
                    "IAM: nitroglicerina IV + betabloqueante + IECA, ICPP urgente",
                    "Disección aórtica tipo A: labetalol o esmolol IV, objetivo TA sistólica <120mmHg, cirugía urgente",
                    "Disección aórtica tipo B: betabloqueante IV, objetivo FC 60 y TA <120/80",
                    "EVITAR hidralazina en disección (taquicardia refleja aumenta el estrés de la pared)"
                ],
                "pearl": "La disección aórtica requiere la reducción de TA más agresiva de todas las emergencias hipertensivas: objetivo sistólica <120mmHg. El labetalol es ideal porque reduce simultáneamente la TA y la dP/dt (fuerza de eyección), los dos determinantes de la propagación de la disección."
            },
            "n_emergencia_renal": {
                "type": "terminal",
                "severity": "critical",
                "title": "Emergencia Hipertensiva Renal — Crisis Hipertensiva con Nefropatía",
                "text": "HTA severa con deterioro agudo de la función renal. Microangiopatía trombótica asociada.",
                "details": [
                    "IECA o ARA-II IV — son nefroprotectores en este contexto",
                    "Nicardipino IV como alternativa",
                    "Objetivo: reducir MAP un 25% en las primeras horas",
                    "Monitorizar función renal y electrolitos cada 6h",
                    "Puede requerir diálisis transitoria si la IRA es severa",
                    "Buscar microangiopatía trombótica: frotis de sangre periférica (esquistocitos)"
                ],
                "pearl": "La crisis renal por esclerodermia es una emergencia hipertensiva específica donde los IECAs son el tratamiento de elección incluso con creatinina elevada — son los únicos fármacos que han demostrado mejorar el pronóstico renal en esta entidad específica."
            },
            "n_eclampsia": {
                "type": "terminal",
                "severity": "critical",
                "title": "Preeclampsia Severa / Eclampsia",
                "text": "HTA severa en embarazada ≥20 semanas o puerperio. Riesgo materno-fetal crítico.",
                "details": [
                    "Sulfato de magnesio IV: 4-6g en 20 min → 1-2g/h (previene y trata convulsiones)",
                    "Labetalol IV 20mg → 40mg → 80mg cada 10 min (máx 300mg) o hidralazina 5mg IV",
                    "Objetivo TA: sistólica <160 y diastólica <105 mmHg (no bajar demasiado)",
                    "EVITAR IECA/ARA-II, nitroprusiato (fetotóxicos)",
                    "El único tratamiento definitivo es el PARTO urgente",
                    "Neonatología presente en el parto"
                ],
                "pearl": "El sulfato de magnesio es superior a los anticonvulsivantes clásicos (benzodiacepinas, fenitoína) para prevenir y tratar las convulsiones eclámpsicas. Tiene además efecto vasodilatador. Vigilar toxicidad: pérdida de reflejos osteotendinosos (primero), depresión respiratoria (después). Antídoto: gluconato de calcio."
            }
        }
    },
    {
        "id": "fibrilacion-auricular",
        "title": "Manejo de la Fibrilación Auricular",
        "specialty": "Cardiología / Urgencias",
        "difficulty": "Intermedio",
        "description": "Algoritmo para el manejo inicial de la FA: control de frecuencia, estrategia de ritmo y anticoagulación según guías ESC 2020.",
        "guideline": "ESC 2020",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente presenta inestabilidad hemodinámica por la FA?",
                "context": "Hipotensión sintomática, angina, síncope, o insuficiencia cardíaca aguda atribuibles a la taquiarritmia.",
                "options": [
                    {"id": "si", "label": "Sí — inestable", "next": "n_cardioversion_urgente"},
                    {"id": "no", "label": "No — estable hemodinámicamente", "next": "n2_tiempo"}
                ]
            },
            "n_cardioversion_urgente": {
                "type": "terminal",
                "severity": "critical",
                "title": "Cardioversión Eléctrica Sincronizada Urgente",
                "text": "FA con inestabilidad hemodinámica. La cardioversión eléctrica es la única opción sin importar el tiempo de inicio.",
                "details": [
                    "Sedación/analgesia: midazolam + fentanilo o propofol",
                    "Cardioversión sincronizada: 150-200J bifásico",
                    "Anticoagulación concomitante con heparina IV",
                    "Si fracasa: repetir con mayor energía o agregar antiarrítmico (amiodarona)",
                    "Monitoreo continuo post-cardioversión",
                    "Anticoagulación mínima 4 semanas post-cardioversión independientemente del tiempo de inicio"
                ],
                "pearl": "En FA con inestabilidad hemodinámica, la cardioversión eléctrica urgente NO requiere anticoagulación previa ni ETE. El beneficio de restaurar el ritmo sinusal supera el riesgo embólico. La anticoagulación va después."
            },
            "n2_tiempo": {
                "type": "question",
                "text": "¿El inicio de la FA está documentado en menos de 48 horas?",
                "context": "Si el inicio es incierto o >48h, debe asumirse que puede haber trombo en la orejuela izquierda.",
                "options": [
                    {"id": "si", "label": "Sí — inicio claro <48h", "next": "n3_cardiovertir_precoz"},
                    {"id": "no", "label": "No — >48h o inicio incierto", "next": "n4_anticoag_previa"}
                ]
            },
            "n3_cardiovertir_precoz": {
                "type": "question",
                "text": "¿Cuál es la estrategia preferida en este paciente?",
                "context": "FA <48h: la cardioversión es segura con anticoagulación simultánea. La estrategia depende de síntomas, edad y cardiopatía.",
                "options": [
                    {"id": "ritmo", "label": "Control de ritmo — restaurar sinusal (joven, sintomático, primer episodio)", "next": "n_cardioversion_precoz"},
                    {"id": "frecuencia", "label": "Control de frecuencia — mantener FA (anciano, asintomático, FA permanente)", "next": "n_control_fc"}
                ]
            },
            "n_cardioversion_precoz": {
                "type": "terminal",
                "severity": "info",
                "title": "Cardioversión en FA <48h — Eléctrica o Farmacológica",
                "text": "FA de inicio reciente. Cardioversión segura con anticoagulación concomitante.",
                "details": [
                    "Anticoagulación: NACO dosis plena o heparina IV antes de la cardioversión",
                    "Farmacológica: flecainida 200-300mg VO (sin cardiopatía estructural) o amiodarona IV (con cardiopatía)",
                    "Eléctrica: 150-200J bifásico sincronizado si la farmacológica falla o se prefiere rapidez",
                    "Mantener anticoagulación mínimo 4 semanas post-cardioversión (aturdimiento auricular)",
                    "Calcular CHA₂DS₂-VASc para decisión de anticoagulación crónica",
                    "Investigar causa: hipertiroidismo, alcohol, infección, valvulopatía"
                ],
                "pearl": "La estrategia 'pill in the pocket' (flecainida 200mg en casa al inicio del episodio) es válida para pacientes seleccionados con FA paroxística, sin cardiopatía estructural, que han sido entrenados. Tasa de conversión a sinusal: 60-90% en 6 horas."
            },
            "n4_anticoag_previa": {
                "type": "question",
                "text": "¿El paciente lleva ≥3 semanas con anticoagulación terapéutica O el ETE no muestra trombo?",
                "context": "3 semanas de anticoagulación eficaz permiten la resolución del trombo si existía. ETE con sensibilidad >95% para trombo en orejuela.",
                "options": [
                    {"id": "si", "label": "Sí — anticoagulado ≥3 sem o ETE negativo", "next": "n_cardioversion_diferida"},
                    {"id": "no", "label": "No — sin anticoagulación previa y sin ETE", "next": "n_anticoag_3semanas"}
                ]
            },
            "n_cardioversion_diferida": {
                "type": "terminal",
                "severity": "warning",
                "title": "Cardioversión Diferida — Segura con Anticoagulación Previa",
                "text": "Anticoagulación ≥3 semanas o ETE negativo. Cardioversión segura. Anticoagular mínimo 4 semanas post-cardioversión.",
                "details": [
                    "Cardioversión eléctrica: 150-200J bifásico sincronizado",
                    "O farmacológica: amiodarona IV (con cardiopatía) o flecainida (sin cardiopatía)",
                    "Anticoagulación: continuar al menos 4 semanas post-cardioversión",
                    "CHA₂DS₂-VASc ≥2 en hombres o ≥3 en mujeres → anticoagulación indefinida",
                    "Antiarrítmico de mantenimiento si FA paroxística recurrente: flecainida, propafenona o amiodarona"
                ],
                "pearl": "El CHA₂DS₂-VASc calcula el riesgo embólico ANUAL en FA: C=IC(1), H=HTA(1), A2=edad≥75(2), D=DM(1), S2=ACV previo(2), V=vasculopatía(1), A=edad65-74(1), Sc=sexo femenino(1). Score≥2 en ♂ o ≥3 en ♀ → anticoagulación indefinida."
            },
            "n_anticoag_3semanas": {
                "type": "terminal",
                "severity": "warning",
                "title": "Anticoagular 3 Semanas Antes de Cardioversión",
                "text": "Sin anticoagulación previa y sin ETE. Opciones: anticoagular 3 semanas y luego cardiovertir, o hacer ETE primero.",
                "details": [
                    "Opción A: NACO durante 3 semanas y luego cardioversión + 4 semanas más",
                    "Opción B: ETE urgente — si no hay trombo, cardiovertir de inmediato con anticoagulación simultánea",
                    "Mientras tanto: control de frecuencia con betabloqueante o diltiazem",
                    "Digoxina: solo si hay IC con FE reducida (no como primera línea en general)",
                    "Calcular CHA₂DS₂-VASc para decisión de anticoagulación a largo plazo"
                ],
                "pearl": "El ETE-guiado acorta el tiempo a la cardioversión cuando el paciente está muy sintomático. La estrategia a elegir depende de: disponibilidad del ETE, síntomas del paciente, y factores de riesgo de sangrado vs tromboembolismo."
            },
            "n_control_fc": {
                "type": "terminal",
                "severity": "info",
                "title": "Estrategia de Control de Frecuencia Cardíaca",
                "text": "Objetivo: FC en reposo <110 lpm (control permisivo) o <80 lpm (control estricto si síntomas).",
                "details": [
                    "Primera línea: betabloqueante (metoprolol, bisoprolol, carvedilol) — especialmente con IC",
                    "Alternativa: diltiazem o verapamilo (NO en IC con FE reducida)",
                    "Digoxina: útil en sedentarios con IC; efecto limitado en ejercicio",
                    "FA permanente: anticoagulación según CHA₂DS₂-VASc",
                    "Control permisivo (FC <110 en reposo) es equivalente al control estricto en la mayoría de pacientes (estudio RACE II)",
                    "Ablación del nodo AV + marcapasos si refractaria al tratamiento médico"
                ],
                "pearl": "La estrategia de control de ritmo vs control de frecuencia tiene resultados equivalentes en mortalidad (estudio AFFIRM). Sin embargo, el estudio EAST-AFNET4 demostró que el control de ritmo PRECOZ (<1 año del diagnóstico) reduce eventos cardiovasculares. Inicio precoz del control de ritmo es hoy la tendencia."
            }
        }
    },
    {
        "id": "cetoacidosis-diabetica-protocolo",
        "title": "Protocolo de Cetoacidosis Diabética (CAD)",
        "specialty": "Urgencias / Endocrinología",
        "difficulty": "Intermedio",
        "description": "Manejo paso a paso de la cetoacidosis diabética: hidratación, potasio e insulina en el orden correcto.",
        "guideline": "ADA 2022",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente cumple criterios diagnósticos de CAD?",
                "context": "Criterios: Glucemia >250 mg/dL + cetonas en sangre u orina + acidosis metabólica (pH <7.30 o HCO₃ <15 mEq/L).",
                "options": [
                    {"id": "si", "label": "Sí — cumple los 3 criterios", "next": "n2_gravedad"},
                    {"id": "no", "label": "No — considerar estado hiperosmolar o hiperglucemia simple", "next": "n_no_cad"}
                ]
            },
            "n_no_cad": {
                "type": "terminal",
                "severity": "info",
                "title": "No es CAD — Evaluar Estado Hiperosmolar",
                "text": "Hiperglucemia sin acidosis significativa. Puede ser estado hiperosmolar hiperglucémico (EHH) o hiperglucemia simple.",
                "details": [
                    "EHH: glucemia >600, osmolaridad >320, sin acidosis, sin cetonas significativas (DM2)",
                    "Hiperglucemia simple: sin acidosis ni cetonas, tratar causa desencadenante",
                    "EHH: hidratación agresiva es el pilar (déficit hídrico 8-10L), insulina posterior",
                    "Monitorizar osmolaridad, Na+ corregido y estado neurológico"
                ],
                "pearl": "La diferencia clave entre CAD y EHH: CAD tiene acidosis + cetonas (DM1 predominantemente). EHH tiene hiperosmolaridad severa sin acidosis (DM2). Pueden coexistir. El EHH tiene mayor mortalidad por la hiperosmolaridad extrema."
            },
            "n2_gravedad": {
                "type": "question",
                "text": "¿Cuál es la gravedad de la CAD según el pH?",
                "context": "Leve: pH 7.25-7.30. Moderada: pH 7.00-7.24. Grave: pH <7.00.",
                "options": [
                    {"id": "grave", "label": "Grave — pH <7.00 o HCO₃ <5 mEq/L", "next": "n_cad_grave"},
                    {"id": "leve_mod", "label": "Leve/Moderada — pH ≥7.00", "next": "n3_potasio"}
                ]
            },
            "n_cad_grave": {
                "type": "terminal",
                "severity": "critical",
                "title": "CAD Grave — UCI + Protocolo Agresivo",
                "text": "pH <7.00. Alto riesgo de edema cerebral, arritmias y fallo multiorgánico. Ingreso en UCI.",
                "details": [
                    "Monitoreo continuo: ECG, TA, diuresis horaria, glucemia cada hora",
                    "Bicarbonato solo si pH <6.9: 100mmol en 400mL agua estéril en 2h (con KCl)",
                    "Hidratación: SF 1L en 1h → 500mL/h las siguientes 4h → ajustar",
                    "K+ >3.5: iniciar insulina. K+ <3.5: corregir primero (ver siguiente paso)",
                    "Buscar causa desencadenante: infección, IAM, abandono de insulina",
                    "Sonda vesical para control estricto de diuresis"
                ],
                "pearl": "El edema cerebral es la complicación más temida de la CAD, especialmente en niños. Factores de riesgo: corrección demasiado rápida de la glucemia, exceso de fluidos hipotónicos, bicarbonato. Síntomas: cefalea, cambio de conducta, bradicardia + HTA (reflejo de Cushing)."
            },
            "n3_potasio": {
                "type": "question",
                "text": "¿El K+ sérico es mayor a 3.5 mEq/L?",
                "context": "REGLA CRÍTICA: Nunca iniciar insulina con K+ <3.5. La insulina mueve K+ al intracelular y puede causar hipocalemia fatal.",
                "options": [
                    {"id": "si", "label": "Sí — K+ ≥3.5 → se puede iniciar insulina", "next": "n4_hidratacion"},
                    {"id": "no", "label": "No — K+ <3.5 → reponer primero", "next": "n_reponer_k"}
                ]
            },
            "n_reponer_k": {
                "type": "terminal",
                "severity": "critical",
                "title": "DETENER — Reponer Potasio Antes de Insulina",
                "text": "K+ <3.5 mEq/L. La insulina está CONTRAINDICADA hasta corregir la hipocalemia.",
                "details": [
                    "Cloruro de potasio: 20-40 mEq/h IV hasta K+ >3.5 mEq/L",
                    "Monitoreo ECG continuo durante la reposición",
                    "Solo hidratación IV sin insulina durante la corrección",
                    "Repetir K+ cada 1-2 horas",
                    "Una vez K+ >3.5: iniciar insulina con 20-30 mEq/h de K+ mantenimiento"
                ],
                "pearl": "El K+ en CAD puede estar falsamente normal o elevado al ingreso (acidosis desplaza K+ al extracelular). Una vez que se corrige la acidosis con insulina y fluidos, el K+ cae precipitadamente. Anticipar hipocalemia y reponer de forma proactiva."
            },
            "n4_hidratacion": {
                "type": "question",
                "text": "¿Se ha iniciado la hidratación IV con suero fisiológico?",
                "context": "La hidratación precede a la insulina. El SF restaura el volumen intravascular y reduce la glucemia antes de la insulina.",
                "options": [
                    {"id": "si", "label": "Sí — hidratación iniciada", "next": "n5_insulina"},
                    {"id": "no", "label": "No — iniciar hidratación primero", "next": "n_hidratacion"}
                ]
            },
            "n_hidratacion": {
                "type": "terminal",
                "severity": "warning",
                "title": "Iniciar Hidratación IV — Primer Paso del Protocolo",
                "text": "Orden correcto: 1° Hidratación → 2° Corrección K+ → 3° Insulina.",
                "details": [
                    "SF 0.9%: 1L en la primera hora (bolo de reanimación)",
                    "Seguir: 500mL/h las siguientes 4 horas",
                    "Cambiar a SF 0.45% cuando Na+ corregido sea normal",
                    "Agregar dextrosa 5% cuando glucemia llegue a 200-250 mg/dL",
                    "Objetivo: déficit hídrico estimado 3-6L, reponer en 24-48h",
                    "Una vez iniciada la hidratación: verificar K+ e iniciar insulina"
                ],
                "pearl": "La hidratación sola baja la glucemia 80-100 mg/dL/h en la primera hora por dilución y mejora de la filtración renal. No subestimar el efecto de los fluidos antes de la insulina."
            },
            "n5_insulina": {
                "type": "question",
                "text": "¿La glucemia ha llegado a 200-250 mg/dL con la insulinoterapia?",
                "context": "Cuando la glucemia llega a 250 mg/dL, agregar dextrosa al suero para poder mantener la insulina corriendo hasta resolver la cetoacidosis.",
                "options": [
                    {"id": "si", "label": "Sí — glucemia ≤250 mg/dL", "next": "n_agregar_dextrosa"},
                    {"id": "no", "label": "No — glucemia >250 mg/dL aún", "next": "n_insulina_continuar"}
                ]
            },
            "n_insulina_continuar": {
                "type": "terminal",
                "severity": "info",
                "title": "Continuar Protocolo de Insulina",
                "text": "Insulina en infusión continua hasta resolución de la CAD. El objetivo es resolver la cetosis, no solo la hiperglucemia.",
                "details": [
                    "Insulina regular IV: 0.1 UI/kg/h en infusión continua",
                    "Si glucemia no cae >50 mg/dL en 1h: doblar la dosis de insulina",
                    "Objetivo glucemia: descenso de 50-75 mg/dL por hora",
                    "K+: reponer para mantener entre 4-5 mEq/L (20-40 mEq/h según nivel)",
                    "Controlar glucemia cada hora, K+ cada 2h, GSA cada 2-4h",
                    "Criterios de resolución: pH >7.30, HCO₃ >15, cetonas negativas (no glucemia normal)"
                ],
                "pearl": "El error más común: suspender la insulina porque la glucemia normalizó. La CAD se resuelve cuando el pH y el HCO₃ normalizan, no cuando la glucemia cae. Suspender insulina prematuramente con cetonas aún presentes causa rebote de la CAD."
            },
            "n_agregar_dextrosa": {
                "type": "terminal",
                "severity": "success",
                "title": "Agregar Dextrosa y Continuar Insulina",
                "text": "Glucemia en 250 mg/dL. Agregar dextrosa al suero para mantener la insulina corriendo hasta resolver la cetosis.",
                "details": [
                    "Cambiar a suero con dextrosa 5-10% para mantener glucemia 150-200 mg/dL",
                    "Continuar insulina IV a la misma dosis — NO suspender",
                    "Criterios de resolución: pH >7.30, HCO₃ >15 mEq/L, brecha aniónica normal, cetonas negativas",
                    "Transición a insulina SC: dar dosis de insulina basal SC 1-2h ANTES de suspender la infusión IV",
                    "Alta cuando tolera vía oral, cetonas negativas y puede autoadministrarse insulina",
                    "Identificar y tratar el factor desencadenante"
                ],
                "pearl": "La transición de insulina IV a SC requiere superposición de 1-2 horas. Si se suspende la infusión IV sin insulina SC previa, hay una brecha de cobertura que puede causar recaída de la CAD. Este error ocurre frecuentemente al amanecer cuando cambia el turno de guardia."
            }
        }
    },
    {
        "id": "acv-isquemico-agudo",
        "title": "ACV Isquémico Agudo — Código Ictus",
        "specialty": "Neurología / Urgencias",
        "difficulty": "Avanzado",
        "description": "Algoritmo de activación del código ictus y toma de decisiones para reperfusión en el ACV isquémico agudo.",
        "guideline": "ESO 2021 / AHA/ASA 2019",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿Los síntomas neurológicos focales comenzaron hace menos de 4.5 horas (o last known well <4.5h)?",
                "context": "Si el paciente se despertó con síntomas (wake-up stroke), el LKW es cuando se fue a dormir. Considerar RMN con DWI/FLAIR para ampliar ventana.",
                "options": [
                    {"id": "si", "label": "Sí — dentro de la ventana de 4.5h", "next": "n2_tc"},
                    {"id": "no", "label": "No — fuera de ventana de tPA convencional", "next": "n_fuera_ventana"}
                ]
            },
            "n_fuera_ventana": {
                "type": "question",
                "text": "¿El tiempo desde el inicio es de 6-24h Y hay imagen vascular que muestra oclusión de gran vaso (OGV)?",
                "context": "Ventana extendida para trombectomía mecánica: 6-24h si hay penumbra isquémica salvable (mismatching clínico-imagen en RMN o perfusión-TC).",
                "options": [
                    {"id": "si", "label": "Sí — oclusión de gran vaso y penumbra salvable", "next": "n_trombectomia_tardia"},
                    {"id": "no", "label": "No — fuera de cualquier ventana terapéutica", "next": "n_manejo_conservador"}
                ]
            },
            "n_trombectomia_tardia": {
                "type": "terminal",
                "severity": "warning",
                "title": "Trombectomía Mecánica en Ventana Extendida (6-24h)",
                "text": "Estudios DAWN y DEFUSE-3 demuestran beneficio de la trombectomía hasta 24h si hay penumbra salvable.",
                "details": [
                    "Imagen de perfusión (TC-perfusión o RMN-DWI/FLAIR) para confirmar penumbra",
                    "Criterios DAWN: discordancia clínico-imagen (déficit grande, infarto pequeño)",
                    "Trombectomía con stent retriever en centro con UCI de ictus",
                    "Antiagregación con AAS 300mg tras confirmar que no habrá tPA",
                    "Control estricto de TA: <180/105 mmHg en el peri-procedimiento"
                ],
                "pearl": "La trombectomía mecánica ha revolucionado el tratamiento del ACV. En OGV, el beneficio es dramático: NNT de 2.6 para independencia funcional. La ventana temporal es secundaria a la viabilidad del tejido — 'time is brain, but brain is the real target'."
            },
            "n_manejo_conservador": {
                "type": "terminal",
                "severity": "info",
                "title": "Manejo Médico del ACV Isquémico — Fuera de Ventana",
                "text": "Sin opciones de reperfusión. Prevención secundaria precoz y manejo de soporte.",
                "details": [
                    "AAS 300mg en las primeras 24-48h (si no hay contraindicaciones hemorrágicas)",
                    "No bajar TA en ACV isquémico agudo salvo >220/120 mmHg (hipoperfusión de la penumbra)",
                    "Estatina de alta intensidad: atorvastatina 80mg desde el día 1",
                    "Monitoreo cardíaco 72h para detectar FA oculta",
                    "Deambulación precoz (24-48h) en ACV no grave",
                    "Inicio de anticoagulación en FA: 4-14 días según tamaño del infarto"
                ],
                "pearl": "El control estricto de la glucemia (objetivo 140-180 mg/dL) en la fase aguda del ACV mejora el pronóstico. La hiperglucemia aumenta el área de infarto. La hipoglucemia (<60 mg/dL) mimetiza el ACV y debe descartarse siempre."
            },
            "n2_tc": {
                "type": "question",
                "text": "¿La TC de cráneo sin contraste muestra hemorragia intracraneal?",
                "context": "La TC debe realizarse en menos de 25 minutos desde el ingreso. La hemorragia es contraindicación absoluta para el tPA.",
                "options": [
                    {"id": "si", "label": "Sí — hemorragia visible en TC", "next": "n_hemorragico"},
                    {"id": "no", "label": "No — TC sin hemorragia (isquémico probable)", "next": "n3_nihss"}
                ]
            },
            "n_hemorragico": {
                "type": "terminal",
                "severity": "critical",
                "title": "ACV Hemorrágico — Manejo Específico",
                "text": "Hemorragia intracraneal confirmada. El tPA está absolutamente contraindicado.",
                "details": [
                    "TA objetivo: <140 mmHg sistólica en las primeras horas (estudio INTERACT2)",
                    "Revertir anticoagulación si estaba anticoagulado: vitamina K + PFC o CCP",
                    "Consulta urgente a neurocirugía: evaluar drenaje si >30mL o hidrocefalia",
                    "Cabecera a 30°, control de glucemia, temperatura y convulsiones",
                    "Ingreso en UCI neurológica o stroke unit",
                    "Repetir TC a las 6h para detectar expansión del hematoma"
                ],
                "pearl": "El 25% de los hematomas se expanden en las primeras horas — factor de mal pronóstico. La reversión urgente de anticoagulación (especialmente con NACOs: andexanet alfa o idarucizumab) y el control agresivo de la TA reducen la expansión."
            },
            "n3_nihss": {
                "type": "question",
                "text": "¿El NIHSS es ≥4 puntos y ≤25 puntos, y no hay contraindicaciones para el tPA?",
                "context": "Contraindicaciones principales: cirugía mayor <3 sem, ACV previo <3 meses, sangrado activo, plaquetas <100k, anticoagulación con INR >1.7 o toma de NACOs en las últimas 48h.",
                "options": [
                    {"id": "si", "label": "Sí — elegible para tPA", "next": "n4_tpa"},
                    {"id": "nihss_bajo", "label": "NIHSS <4 — síntomas menores o en resolución", "next": "n_nihss_bajo"},
                    {"id": "contra", "label": "Contraindicación para tPA", "next": "n_contra_tpa"}
                ]
            },
            "n4_tpa": {
                "type": "question",
                "text": "¿La imagen vascular (AngioTC o AngioRM) muestra oclusión de gran vaso (carótida interna, ACM M1/M2)?",
                "context": "La oclusión de gran vaso indica que además del tPA, se debe considerar trombectomía mecánica (tratamiento combinado).",
                "options": [
                    {"id": "si", "label": "Sí — oclusión de gran vaso", "next": "n_tpa_mas_trombectomia"},
                    {"id": "no", "label": "No — sin oclusión de gran vaso", "next": "n_solo_tpa"}
                ]
            },
            "n_solo_tpa": {
                "type": "terminal",
                "severity": "critical",
                "title": "tPA IV — Tiempo Puerta-Aguja <60 minutos",
                "text": "ACV isquémico sin OGV elegible para trombolisis. El tiempo es el factor más crítico.",
                "details": [
                    "Alteplase 0.9 mg/kg IV (máx 90mg): 10% en bolo → 90% en 60 minutos",
                    "TA pre-tPA: mantener <185/110 mmHg (labetalol o nicardipino si precisa)",
                    "TA post-tPA 24h: <180/105 mmHg",
                    "Sin antiagregantes ni anticoagulantes en las primeras 24h",
                    "TC de control a las 24h antes de iniciar antiagregación",
                    "Monitoreo neurológico cada 15 min durante la infusión"
                ],
                "pearl": "Por cada 15 minutos de reducción en el tiempo puerta-aguja, se salvan 4 semanas de vida saludable (ajustada por discapacidad). El tiempo puerta-aguja objetivo es <60 minutos. El tiempo inicio-aguja es <4.5h."
            },
            "n_tpa_mas_trombectomia": {
                "type": "terminal",
                "severity": "critical",
                "title": "tPA + Trombectomía Mecánica — Tratamiento Combinado",
                "text": "Oclusión de gran vaso: tratamiento combinado tPA IV + trombectomía mecánica es el estándar actual.",
                "details": [
                    "tPA IV: iniciar inmediatamente, NO esperar la trombectomía",
                    "Activar sala de angiografía en paralelo mientras corre el tPA",
                    "Trombectomía: stent retriever en ACM M1/M2 o carótida interna",
                    "Tiempo puerta-punción objetivo: <90 minutos",
                    "En centros sin hemodinamia: tPA y traslado urgente ('drip and ship')",
                    "Resultado: tasa de recanalización >80% vs 40% con tPA solo"
                ],
                "pearl": "En OGV, el tPA solo recanaliza en <30% de los casos. La trombectomía mecánica añadida al tPA aumenta la recanalización al 80-90% y mejora la independencia funcional en 25-30% adicional de pacientes (NNT~2.5)."
            },
            "n_nihss_bajo": {
                "type": "terminal",
                "severity": "warning",
                "title": "ACV Menor o TIA — Manejo Urgente sin tPA",
                "text": "NIHSS <4 o síntomas en resolución. El tPA no está indicado pero el riesgo de ACV completo es alto a corto plazo.",
                "details": [
                    "AAS 300mg + clopidogrel 300mg (doble antiagregación en las primeras 3 semanas — estudio POINT)",
                    "Estudio urgente de la causa: ECG, Holter, ecocardiograma, angioTC de vasos",
                    "Score ABCD2 para estimar riesgo de ACV en 48h",
                    "TIA de alto riesgo (ABCD2 ≥4 o estenosis carotídea): hospitalización urgente",
                    "Estatina de alta intensidad desde el primer día",
                    "No bajar TA agresivamente en la fase aguda"
                ],
                "pearl": "El riesgo de ACV completo en las 48h post-TIA es del 10-20%. El tratamiento antiagregante dual (AAS + clopidogrel) en las primeras 3 semanas reduce ese riesgo en un 30%. Este beneficio se revierte y se convierte en daño si se mantiene más de 3 semanas."
            },
            "n_contra_tpa": {
                "type": "terminal",
                "severity": "warning",
                "title": "Contraindicación para tPA — Evaluar Trombectomía",
                "text": "Sin acceso a trombolisis. Si hay OGV, la trombectomía mecánica sola puede estar indicada.",
                "details": [
                    "Imagen vascular urgente: angioTC para buscar OGV",
                    "Si hay OGV: trombectomía mecánica sin tPA previo (indicación clase I)",
                    "Sin OGV: manejo médico con AAS y estatina",
                    "Anticoagulación solo si hay FA documentada (diferida 4-14 días según tamaño infarto)",
                    "Documentar la contraindicación claramente en la historia"
                ],
                "pearl": "La trombectomía mecánica SIN tPA previo tiene eficacia similar a la combinación tPA+trombectomía en OGV. Los estudios DIRECT-MT y SKIP lo confirmaron. Esto es importante para pacientes con contraindicaciones al tPA o en centros con acceso directo a hemodinamia."
            }
        }
    },
    {
        "id": "status-epileptico-protocolo",
        "title": "Status Epiléptico — Protocolo por Tiempo",
        "specialty": "Neurología / Urgencias",
        "difficulty": "Avanzado",
        "description": "Protocolo escalonado por tiempo para el manejo del status epiléptico convulsivo generalizado.",
        "guideline": "ILAE 2015 / NCS 2012",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿Las convulsiones llevan más de 5 minutos O hay 2 crisis sin recuperación de conciencia entre ellas?",
                "context": "El umbral de 5 minutos define el status epiléptico operacional. Las convulsiones raramente ceden solas después de los 5 minutos.",
                "options": [
                    {"id": "si", "label": "Sí — status epiléptico confirmado", "next": "n2_medidas_basicas"},
                    {"id": "no", "label": "No — convulsión aislada <5 min", "next": "n_crisis_aislada"}
                ]
            },
            "n_crisis_aislada": {
                "type": "terminal",
                "severity": "info",
                "title": "Crisis Epiléptica Aislada — Manejo de Soporte",
                "text": "Convulsión <5 minutos que cedió espontáneamente. No es status epiléptico. Manejo conservador.",
                "details": [
                    "Posición de seguridad: decúbito lateral para evitar broncoaspiración",
                    "O2 suplementario: 4-6L/min por cánula nasal",
                    "Glucemia capilar urgente: descartar hipoglucemia como causa",
                    "No insertar nada en la boca durante la crisis",
                    "Vigilar fase post-ictal (confusión normal 10-30 min)",
                    "Investigar causa: niveles de antiepilépticos, tóxicos, fiebre, metabólico"
                ],
                "pearl": "El 60% de las crisis epilépticas en adultos con epilepsia conocida son por niveles subterapéuticos del antiepiléptico. Siempre medir niveles. La primera crisis en adulto sin epilepsia requiere TC de urgencia y EEG dentro de las 24h."
            },
            "n2_medidas_basicas": {
                "type": "question",
                "text": "¿Se han iniciado las medidas básicas de soporte?",
                "context": "Estas medidas deben iniciarse en paralelo con el tratamiento, nunca en lugar de él.",
                "options": [
                    {"id": "si", "label": "Sí — soporte iniciado", "next": "n3_benzo"},
                    {"id": "no", "label": "No — iniciar soporte urgente", "next": "n_soporte"}
                ]
            },
            "n_soporte": {
                "type": "terminal",
                "severity": "critical",
                "title": "Medidas de Soporte Inmediatas (Minuto 0-5)",
                "text": "Iniciar SIMULTÁNEAMENTE al tratamiento farmacológico, no antes.",
                "details": [
                    "Vía aérea: posición lateral, aspirar secreciones, O2 de alto flujo",
                    "Acceso venoso: 2 vías periféricas calibre 18G",
                    "Glucemia capilar: bolo de dextrosa 50% si glucemia <60 mg/dL",
                    "Tiamina 100mg IV si alcoholismo u otra sospecha de déficit (ANTES de la dextrosa)",
                    "Monitoreo: ECG, SatO2, TA",
                    "Preparar benzodiacepinas para administrar INMEDIATAMENTE"
                ],
                "pearl": "La tiamina ANTES de la dextrosa en alcohólicos: la dextrosa sin tiamina puede precipitar encefalopatía de Wernicke aguda en pacientes con déficit de tiamina. En cualquier duda, dar tiamina primero."
            },
            "n3_benzo": {
                "type": "question",
                "text": "Minuto 5-10: ¿Se ha administrado benzodiacepina de primera línea?",
                "context": "Primera línea: lorazepam IV 4mg (o diazepam IV 10mg). Si no hay acceso IV: diazepam rectal 10-20mg o midazolam IM 10mg o intranasal 5mg.",
                "options": [
                    {"id": "si_cede", "label": "Sí — las convulsiones cedieron", "next": "n_benzo_exito"},
                    {"id": "si_no_cede", "label": "Sí — NO cedieron (refractario a BZD)", "next": "n4_segunda_linea"},
                    {"id": "no", "label": "No — administrar BZD ahora", "next": "n_dar_benzo"}
                ]
            },
            "n_dar_benzo": {
                "type": "terminal",
                "severity": "critical",
                "title": "Administrar Benzodiacepina — Primera Línea",
                "text": "Las BZD son el único tratamiento de primera línea del status epiléptico. Sin excepciones.",
                "details": [
                    "Con acceso IV: lorazepam 4mg IV (o diazepam 10mg IV) — puede repetirse 1 vez a los 5 min",
                    "Sin acceso IV: midazolam 10mg IM (igual de eficaz que lorazepam IV — estudio RAMPART)",
                    "Alternativa sin IV: diazepam rectal 10-20mg, midazolam intranasal 5mg",
                    "Máximo 2 dosis de BZD — más dosis aumentan depresión respiratoria sin eficacia",
                    "Preparar segunda línea en paralelo si la BZD no cede las convulsiones"
                ],
                "pearl": "El midazolam IM es tan eficaz como el lorazepam IV para terminar el status, con la ventaja de no requerir acceso venoso (crucial en pacientes pediátricos y extrahospitalario). El estudio RAMPART (2012) estableció la equivalencia."
            },
            "n_benzo_exito": {
                "type": "terminal",
                "severity": "success",
                "title": "Status Controlado con BZD — Mantenimiento y Estudio",
                "text": "Las BZD terminaron el status. Iniciar antiepiléptico de mantenimiento e investigar la causa.",
                "details": [
                    "Antiepiléptico de mantenimiento IV: levetiracetam 1500mg IV o valproato 30mg/kg IV",
                    "EEG urgente: descartar status no convulsivo post-ictal",
                    "TC de cráneo: buscar causa estructural (masa, hemorragia)",
                    "Analítica: electrolitos, glucemia, función renal, niveles de antiepilépticos",
                    "Si fiebre o rigidez de nuca: punción lumbar para descartar meningitis/encefalitis",
                    "Monitoreo neurológico cada 15 min durante 2h"
                ],
                "pearl": "El status epiléptico no convulsivo (SENC) puede seguir al status convulsivo aunque las convulsiones hayan cesado clínicamente. La única forma de descartarlo es el EEG. El SENC produce daño neuronal sin manifestación motora visible."
            },
            "n4_segunda_linea": {
                "type": "question",
                "text": "Minuto 10-30: ¿Se ha administrado un antiepiléptico de segunda línea?",
                "context": "Segunda línea (igual eficacia — estudio ESETT): levetiracetam 60mg/kg IV, valproato 40mg/kg IV, o fenitoína 20mg/kg IV. Elegir según contexto clínico.",
                "options": [
                    {"id": "si_cede", "label": "Sí — las convulsiones cedieron con la segunda línea", "next": "n_benzo_exito"},
                    {"id": "si_no_cede", "label": "Sí — NO cedieron → STATUS REFRACTARIO", "next": "n5_refractario"},
                    {"id": "no", "label": "No — administrar segunda línea ahora", "next": "n_segunda_linea"}
                ]
            },
            "n_segunda_linea": {
                "type": "terminal",
                "severity": "critical",
                "title": "Segunda Línea (Minuto 10-30) — Los Tres Tienen Igual Eficacia",
                "text": "Elegir según contexto. El estudio ESETT (2019) demostró eficacia equivalente de los tres.",
                "details": [
                    "Levetiracetam: 60mg/kg (máx 4.5g) IV en 15 min — PRIMERA ELECCIÓN (menos interacciones, más seguro)",
                    "Valproato: 40mg/kg (máx 3g) IV en 10 min — EVITAR en embarazo y hepatopatía",
                    "Fenitoína/fosfenitoína: 20mg/kg IV lento (máx 50mg/min) — EVITAR en arritmias",
                    "Labetalol para TA si hay HTA durante la administración",
                    "Si no hay respuesta en 10 min: status refractario → intubación y anestesia"
                ],
                "pearl": "El estudio ESETT (NEJM 2019) fue un hito: levetiracetam, valproato y fenitoína tienen eficacia equivalente (~47% de éxito) en el status refractario a BZD. La elección depende del paciente, no de una jerarquía de eficacia. Levetiracetam tiene el mejor perfil de seguridad."
            },
            "n5_refractario": {
                "type": "terminal",
                "severity": "critical",
                "title": "Status Refractario (>30 min) — Anestesia General + UCI",
                "text": "Status que no cede a BZD + segunda línea. Requiere intubación y anestesia general bajo monitoreo EEG continuo.",
                "details": [
                    "Intubación orotraqueal: secuencia rápida con ketamina (efecto anticonvulsivo) + succinilcolina",
                    "Propofol infusión: 1-2mg/kg bolo → 2-10mg/kg/h (monitoreo de propofol infusion syndrome)",
                    "O midazolam infusión: 0.2mg/kg bolo → 0.05-0.4mg/kg/h",
                    "O pentobarbital si fallo de los anteriores",
                    "EEG CONTINUO: objetivo supresión de brotes (burst suppression)",
                    "UCI neurológica: buscar causa tratable (encefalitis autoinmune, tóxicos)"
                ],
                "pearl": "En el status superrefractario (>24h con anestesia), buscar activamente causas tratables: encefalitis autoinmune (anti-NMDA, anti-LGI1, etc.) con LCR y anticuerpos. El tratamiento inmunomodulador (corticoides, IGIV, plasmaféresis) puede salvar la vida en estos casos."
            }
        }
    },
    {
        "id": "protocolo-anafilaxia",
        "title": "Protocolo de Anafilaxia",
        "specialty": "Urgencias / Alergología",
        "difficulty": "Básico",
        "description": "Reconocimiento y manejo de la anafilaxia. La adrenalina IM es el primer tratamiento y no debe retrasarse.",
        "guideline": "WAO 2020 / EAACI",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente cumple criterios diagnósticos de anafilaxia?",
                "context": "Criterio 1: inicio agudo con afección de PIEL + SCV o respiratorio tras exposición probable a alérgeno. Criterio 2: 2 o más sistemas afectados tras exposición. Criterio 3: hipotensión tras alérgeno conocido.",
                "options": [
                    {"id": "si", "label": "Sí — anafilaxia probable", "next": "n2_adrenalina"},
                    {"id": "dudoso", "label": "Reacción alérgica leve/moderada (solo urticaria)", "next": "n_alergia_leve"}
                ]
            },
            "n_alergia_leve": {
                "type": "terminal",
                "severity": "info",
                "title": "Reacción Alérgica Leve — Antihistamínico ± Corticoide",
                "text": "Sin compromiso hemodinámico ni respiratorio. Manejo con antihistamínicos.",
                "details": [
                    "Difenhidramina 25-50mg IV/IM O cetirizina 10mg VO",
                    "Si hay urticaria extensa: dexametasona 8mg IV o prednisona 40mg VO",
                    "Vigilar 2-4h por riesgo de progresión a anafilaxia",
                    "Alta con antihistamínico oral 3-5 días y corticoide 3 días",
                    "Referir a alergología para identificar el alérgeno"
                ],
                "pearl": "Una reacción alérgica puede progresar a anafilaxia incluso 30-60 minutos después de la exposición. La observación de al menos 2 horas en urgencias es mandatoria incluso en reacciones aparentemente leves."
            },
            "n2_adrenalina": {
                "type": "question",
                "text": "¿Se ha administrado adrenalina IM en el muslo anterolateral?",
                "context": "PRIMERA ACCIÓN en toda anafilaxia. No hay contraindicaciones absolutas. No esperar para canalizar vía venosa ni dar antihistamínicos primero.",
                "options": [
                    {"id": "no", "label": "No — administrar AHORA", "next": "n_dar_adrenalina"},
                    {"id": "si", "label": "Sí — adrenalina administrada", "next": "n3_respuesta"}
                ]
            },
            "n_dar_adrenalina": {
                "type": "terminal",
                "severity": "critical",
                "title": "ADRENALINA IM — Primera y Única Acción Urgente",
                "text": "Sin excusas, sin demora. La adrenalina IM en el muslo salva vidas. Todo lo demás es secundario.",
                "details": [
                    "Adrenalina 0.3-0.5mg IM en muslo anterolateral (adultos)",
                    "Niños: 0.01mg/kg IM (máx 0.5mg)",
                    "Puede repetirse cada 5-15 minutos si no hay respuesta",
                    "El muslo permite absorción más rápida que el deltoides",
                    "LUEGO: posición (decúbito + piernas elevadas si hipotensión), O2, acceso venoso, SF IV"
                ],
                "pearl": "Los dos errores mortales en anafilaxia: 1) No dar adrenalina o darla tarde. 2) Usar adrenalina IV sin monitoreo (puede causar arritmias letales). La vía IM es la correcta en el 99% de los casos. La vía IV se reserva para paro cardíaco o shock refractario a múltiples dosis IM."
            },
            "n3_respuesta": {
                "type": "question",
                "text": "¿El paciente responde a la primera dosis de adrenalina en 5-15 minutos?",
                "context": "Respuesta: mejoría de la TA, reducción del estridor/broncoespasmo, mejora de la urticaria.",
                "options": [
                    {"id": "si", "label": "Sí — mejoría evidente", "next": "n4_observacion"},
                    {"id": "no", "label": "No — sin respuesta suficiente", "next": "n_segunda_adrenalina"}
                ]
            },
            "n_segunda_adrenalina": {
                "type": "question",
                "text": "¿Se han administrado medidas de soporte y segunda dosis de adrenalina?",
                "context": "Shock anafiláctico refractario: puede requerir adrenalina IV en infusión.",
                "options": [
                    {"id": "no", "label": "No — administrar segunda dosis + soporte", "next": "n_soporte_anafilaxia"},
                    {"id": "si_shock", "label": "Sí — sigue en shock refractario", "next": "n_shock_refractario"}
                ]
            },
            "n_soporte_anafilaxia": {
                "type": "terminal",
                "severity": "critical",
                "title": "Segunda Dosis de Adrenalina + Soporte Hemodinámico",
                "text": "Anafilaxia resistente a la primera dosis. Escalar el tratamiento.",
                "details": [
                    "Segunda dosis adrenalina 0.5mg IM a los 5-15 min",
                    "SF 500-1000mL IV rápido (shock anafiláctico = shock distributivo)",
                    "O2 de alto flujo: 10-15 L/min por mascarilla con reservorio",
                    "Salbutamol nebulizado si broncoespasmo prominente",
                    "Difenhidramina 50mg IV + ranitidina 50mg IV (bloqueo H1+H2)",
                    "Dexametasona 8mg IV (previene la fase tardía — efecto en 4-6h)"
                ],
                "pearl": "Los antihistamínicos y corticoides son ADYUVANTES, no tratamiento principal. Tratar el shock primero con adrenalina + fluidos. Los antihistamínicos solo tratan el prurito y la urticaria, no el shock ni el edema laríngeo."
            },
            "n_shock_refractario": {
                "type": "terminal",
                "severity": "critical",
                "title": "Shock Anafiláctico Refractario — Adrenalina IV",
                "text": "Anafilaxia resistente a múltiples dosis IM. Requiere adrenalina IV en infusión con monitoreo continuo.",
                "details": [
                    "Adrenalina IV: 0.1-0.5 mcg/kg/min en infusión (NUNCA bolo IV rápido salvo paro)",
                    "Monitoreo ECG continuo durante adrenalina IV (riesgo de arritmias)",
                    "Glucagón 1-2mg IV/IM si el paciente toma betabloqueantes (revierte el efecto del betabloqueo)",
                    "Azul de metileno 1.5mg/kg IV si shock vasodilatador refractario",
                    "UCI para soporte vasopresor e inotrópico",
                    "Descartar componente de angioedema de vías aéreas: intubación precoz si estridor"
                ],
                "pearl": "En pacientes con betabloqueantes, la anafilaxia puede ser refractaria a la adrenalina porque el betabloqueo antagoniza los receptores beta. El glucagón (que actúa por receptores independientes de los beta) puede 'rescatar' estos casos. Siempre preguntar por betabloqueantes en anafilaxia refractaria."
            },
            "n4_observacion": {
                "type": "terminal",
                "severity": "warning",
                "title": "Anafilaxia Controlada — Observación Obligatoria 4-8 Horas",
                "text": "Buena respuesta inicial. La reacción bifásica ocurre en el 20% — observación mínima de 4 horas.",
                "details": [
                    "Monitoreo: TA, FC, SatO2 cada 15-30 min durante la observación",
                    "Difenhidramina + ranitidina + corticoide IV (previenen fase tardía)",
                    "Alta solo si: estable 4h, sin síntomas residuales, acompañado",
                    "Al alta: autoinyector de adrenalina (EpiPen) + entrenamiento en su uso",
                    "Pulsera de alergia + plan de acción escrito",
                    "Derivación obligatoria a alergología para identificación del alérgeno"
                ],
                "pearl": "La reacción bifásica ocurre en 1-20% de las anafilaxias: el paciente mejora y recae 1-72h después sin nueva exposición. Factor de riesgo principal: anafilaxia grave inicial y demora en la adrenalina. El corticoide reduce (no elimina) este riesgo."
            }
        }
    },
    {
        "id": "hemorragia-digestiva-alta",
        "title": "Manejo de la Hemorragia Digestiva Alta",
        "specialty": "Urgencias / Gastroenterología",
        "difficulty": "Intermedio",
        "description": "Algoritmo para la evaluación y manejo inicial de la hemorragia digestiva alta: estabilización, estratificación de riesgo y timing de la endoscopia.",
        "guideline": "BSG 2021 / ESGE",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente presenta inestabilidad hemodinámica?",
                "context": "TA sistólica <90 mmHg, FC >100 lpm, signos de hipoperfusión (palidez, diaforesis, confusión) o hemoglobina <7 g/dL.",
                "options": [
                    {"id": "si", "label": "Sí — inestable → resucitación urgente", "next": "n_resucitacion"},
                    {"id": "no", "label": "No — estable hemodinámicamente", "next": "n2_estratificacion"}
                ]
            },
            "n_resucitacion": {
                "type": "question",
                "text": "¿Se han iniciado las medidas de resucitación?",
                "context": "En HDA con shock: resucitación PRIMERO, endoscopia DESPUÉS. Endoscopiar a un paciente inestable aumenta la mortalidad.",
                "options": [
                    {"id": "si", "label": "Sí — resucitado, ahora estable", "next": "n2_estratificacion"},
                    {"id": "no", "label": "No — iniciar resucitación ahora", "next": "n_dar_resucitacion"}
                ]
            },
            "n_dar_resucitacion": {
                "type": "terminal",
                "severity": "critical",
                "title": "Resucitación Urgente Antes de la Endoscopia",
                "text": "Shock hemorrágico. Estabilizar antes de la endoscopia.",
                "details": [
                    "2 vías periféricas calibre 16-18G + muestra para hemograma, coagulación, grupo y reserva",
                    "SF o Ringer lactato: bolo 500mL en 15 min, repetir según respuesta",
                    "Transfusión: umbral Hb <7 g/dL (o <8 en cardiopatía isquémica)",
                    "Omeprazol 80mg IV en bolo → 8mg/h en infusión (antes de la endoscopia)",
                    "Posición: decúbito lateral izquierdo si vómitos para evitar broncoaspiración",
                    "Avisar a gastroenterología: endoscopia urgente (<12h) en alto riesgo"
                ],
                "pearl": "El objetivo transfusional en HDA es Hb 7-8 g/dL, NO más alto. La transfusión liberal aumenta la mortalidad en HDA variceal (aumenta la presión portal). La excepción es la cardiopatía isquémica activa donde el umbral es Hb <8 g/dL."
            },
            "n2_estratificacion": {
                "type": "question",
                "text": "¿El score de Glasgow-Blatchford (GBS) es mayor a 1?",
                "context": "GBS incluye: BUN, Hb, TA sistólica, FC, melena, síncope, hepatopatía, ICC. GBS 0-1 = bajo riesgo (puede no necesitar endoscopia urgente).",
                "options": [
                    {"id": "alto", "label": "GBS >1 — alto riesgo (requiere endoscopia)", "next": "n3_timing"},
                    {"id": "bajo", "label": "GBS 0-1 — bajo riesgo", "next": "n_bajo_riesgo_hda"}
                ]
            },
            "n_bajo_riesgo_hda": {
                "type": "terminal",
                "severity": "success",
                "title": "Bajo Riesgo — Manejo Ambulatorio Posible",
                "text": "GBS 0-1: muy bajo riesgo de necesitar intervención. Puede manejarse ambulatoriamente.",
                "details": [
                    "Endoscopia electiva ambulatoria en 24-72h",
                    "Omeprazol oral 40mg cada 12h",
                    "Instrucciones de alarma: volver si hay hematemesis, melena abundante, mareo",
                    "Suspender AINEs, aspirina si no es cardioprotectora",
                    "H. pylori: test en aliento o antígeno fecal al alta",
                    "No requiere hospitalización si hay seguimiento garantizado"
                ],
                "pearl": "El score de Glasgow-Blatchford predice la necesidad de intervención endoscópica. GBS=0 tiene VPN del 99% para necesidad de intervención. Este es el único score validado para decidir alta segura desde urgencias en HDA."
            },
            "n3_timing": {
                "type": "question",
                "text": "¿Hay signos de sangrado activo grave (hematemesis masiva, sangre roja por SNG, shock refractario)?",
                "context": "El sangrado activo masivo requiere endoscopia de emergencia (<6h). El alto riesgo sin sangrado activo requiere endoscopia urgente (<24h).",
                "options": [
                    {"id": "si", "label": "Sí — sangrado activo masivo → endoscopia <6h", "next": "n_endoscopia_emergencia"},
                    {"id": "no", "label": "No — estabilizado → endoscopia <24h", "next": "n_endoscopia_urgente"}
                ]
            },
            "n_endoscopia_emergencia": {
                "type": "terminal",
                "severity": "critical",
                "title": "Endoscopia de Emergencia (<6 horas)",
                "text": "Sangrado activo masivo. Endoscopia de emergencia con paciente estabilizado.",
                "details": [
                    "Eritromicina 250mg IV 30-60 min antes (vacía el estómago — mejora visibilidad)",
                    "Intubación orotraqueal antes de la endoscopia si encefalopatía o alto riesgo de aspiración",
                    "Hallazgo Forrest Ia/Ib: hemostasia combinada (adrenalina + clip o electrocoagulación)",
                    "Varices esofágicas: ligadura endoscópica o esclerosis + terlipresina IV",
                    "Solicitar cirugía de guardia disponible: si endoscopia falla → cirugía o radiología intervencionista"
                ],
                "pearl": "La eritromicina pre-endoscópica (procinético) vacía el estómago de coágulos en 20-30 minutos y mejora dramáticamente la calidad de la visión endoscópica. Su uso rutinario en HDA antes de la endoscopia es una práctica establecida con nivel de evidencia IA."
            },
            "n_endoscopia_urgente": {
                "type": "terminal",
                "severity": "warning",
                "title": "Endoscopia Urgente (<24 horas)",
                "text": "Alto riesgo estabilizado. Endoscopia dentro de las primeras 24 horas.",
                "details": [
                    "Omeprazol 80mg IV bolo → 8mg/h en infusión continua mientras se espera la endoscopia",
                    "Eritromicina 250mg IV 30-60 min antes de la endoscopia (si se puede planificar)",
                    "Endoscopia: clasificar según Forrest (Ia-IIb = hemostasia; IIc-III = solo IBP)",
                    "Post-hemostasia Forrest Ia/Ib: IBP IV 72h + no reiniciar AINEs",
                    "Biopsia para H. pylori: tratar si positivo (reduce recurrencia del 70% al 5%)",
                    "Alta cuando: sin resangrado en 72h, tolerancia oral, Hb estable"
                ],
                "pearl": "La hemostasia endoscópica combinada (adrenalina perilesional + clip mecánico) es superior a la monoterapia. La adrenalina sola tiene tasa de resangrado del 15-20% en Forrest Ia. El clip añadido la reduce al 5%. El IBP IV post-hemostasia es el estándar para úlcera de alto riesgo."
            }
        }
    },
    {
        "id": "neutropenia-febril",
        "title": "Neutropenia Febril Oncológica",
        "specialty": "Oncología / Urgencias",
        "difficulty": "Avanzado",
        "description": "Manejo de la neutropenia febril en paciente oncológico según estratificación de riesgo. El antibiótico precoz salva vidas.",
        "guideline": "IDSA 2010 / ESMO",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente cumple criterios de neutropenia febril?",
                "context": "Definición: neutrófilos <500/mm³ (o <1000 con tendencia a bajar a <500) + temperatura única >38.3°C o >38°C por más de 1 hora.",
                "options": [
                    {"id": "si", "label": "Sí — neutropenia febril confirmada", "next": "n2_mascc"},
                    {"id": "no", "label": "No — fiebre sin neutropenia", "next": "n_no_nf"}
                ]
            },
            "n_no_nf": {
                "type": "terminal",
                "severity": "info",
                "title": "No es Neutropenia Febril — Evaluar Causa de Fiebre",
                "text": "Fiebre sin neutropenia en paciente oncológico. Evaluar según el contexto.",
                "details": [
                    "Fiebre tumoral: diagnóstico de exclusión, puede responder a AINE",
                    "Infección con neutrófilos normales: manejo antibiótico según foco",
                    "Fiebre por transfusión o medicamentos: resolución espontánea en 4-8h",
                    "Siempre considerar la inmunosupresión relativa del paciente oncológico"
                ],
                "pearl": "El umbral de fiebre en el paciente oncológico inmunosuprimido es de 38°C (no 38.5°C como en el paciente general). Un solo registro de 38.3°C es suficiente para activar el protocolo de neutropenia febril."
            },
            "n2_mascc": {
                "type": "question",
                "text": "¿El score de MASCC es ≥21 puntos (bajo riesgo)?",
                "context": "MASCC: sin hipotensión(5) + sin EPOC(4) + tumor sólido o no infección fúngica previa(4) + sin deshidratación(3) + ambulatorio al inicio(3) + edad <60 años(2) + sin síntomas severos(3).",
                "options": [
                    {"id": "bajo", "label": "MASCC ≥21 — Bajo riesgo", "next": "n3_bajo_riesgo"},
                    {"id": "alto", "label": "MASCC <21 — Alto riesgo", "next": "n3_alto_riesgo"}
                ]
            },
            "n3_alto_riesgo": {
                "type": "question",
                "text": "¿Hay signos de infección grave o foco identificado?",
                "context": "Infección grave: sepsis, neumonía, infección de catéter con bacteriemia, celulitis extensa.",
                "options": [
                    {"id": "si", "label": "Sí — sepsis o foco grave identificado", "next": "n_nf_sepsis"},
                    {"id": "no", "label": "No — fiebre sin foco claro", "next": "n_nf_alto_sin_foco"}
                ]
            },
            "n_nf_sepsis": {
                "type": "terminal",
                "severity": "critical",
                "title": "Neutropenia Febril de Alto Riesgo con Sepsis",
                "text": "Máxima urgencia. Antibiótico de amplio espectro antipseudomónico en la primera hora.",
                "details": [
                    "Hemocultivos x2 (periférico + catéter central si lo tiene) ANTES del antibiótico",
                    "Antibiótico: cefepima 2g IV/8h o piperacilina-tazobactam 4.5g IV/6h o meropenem 1g IV/8h",
                    "Agregar vancomicina 15-25mg/kg IV si: infección de catéter, neumonía, inestabilidad",
                    "Agregar cobertura antifúngica (caspofungina) si fiebre persiste >96h sin foco o colonización por Candida",
                    "G-CSF (filgrastim) si neutropenia profunda prolongada",
                    "Hospitalización en aislamiento inverso obligatoria"
                ],
                "pearl": "La mortalidad de la neutropenia febril con sepsis sin antibiótico en la primera hora es del 20-30%. Con antibiótico en <60 min cae al 5-7%. La Pseudomonas aeruginosa puede matar en <24h en neutropenia profunda — la cobertura antipseudomónica no es opcional."
            },
            "n_nf_alto_sin_foco": {
                "type": "terminal",
                "severity": "warning",
                "title": "Neutropenia Febril de Alto Riesgo — Hospitalización + Antibiótico IV",
                "text": "Alto riesgo sin sepsis establecida. Hospitalización obligatoria con antibiótico IV.",
                "details": [
                    "Hemocultivos x2 antes del antibiótico (en <30 minutos desde el triage)",
                    "Cefepima 2g IV/8h como primera línea (antipseudomónica)",
                    "Estudio del foco: RxTx, uroanálisis, considerar TC según síntomas",
                    "Evaluar a las 48-72h: si mejoría clínica y afebril → considerar desescalada a oral",
                    "Si fiebre persiste >96h: TCs para buscar foco oculto + considerar antifúngico empírico",
                    "Duración mínima: hasta neutrófilos >500/mm³ Y afebril 48h"
                ],
                "pearl": "El estudio de imagen en la neutropenia febril con fiebre persistente: la TC de tórax de alta resolución detecta aspergilosis pulmonar invasiva (infiltrados en halo) cuando la RxTx es normal. Iniciar voriconazol si hay nódulos con halo en neutropenia prolongada."
            },
            "n3_bajo_riesgo": {
                "type": "question",
                "text": "¿El paciente puede recibir tratamiento oral y tiene seguimiento garantizado en 24h?",
                "context": "Criterios adicionales para manejo ambulatorio: sin fallo renal/hepático, sin mucositis grado 3-4, estado general conservado, acompañante.",
                "options": [
                    {"id": "si", "label": "Sí — candidato a manejo oral ambulatorio", "next": "n_nf_oral"},
                    {"id": "no", "label": "No — hospitalizar aunque sea bajo riesgo", "next": "n_nf_alto_sin_foco"}
                ]
            },
            "n_nf_oral": {
                "type": "terminal",
                "severity": "info",
                "title": "Neutropenia Febril de Bajo Riesgo — Manejo Oral Ambulatorio",
                "text": "MASCC ≥21. Puede manejarse con antibióticos orales y seguimiento ambulatorio estrecho.",
                "details": [
                    "Ciprofloxacino 500-750mg VO/12h + amoxicilina-clavulánico 875mg VO/8h (cobertura oral amplia)",
                    "Hemocultivos antes del alta (puede tomarse en urgencias)",
                    "Instrucciones claras: regresar URGENTE si deterioro, nueva fiebre o síntomas respiratorios",
                    "Control en 24h obligatorio (puede ser telefónico + presencial si hay fiebre)",
                    "Si fiebre persiste >48h con tratamiento oral: hospitalización y cambio a IV",
                    "G-CSF profiláctico para los próximos ciclos de quimioterapia"
                ],
                "pearl": "El manejo ambulatorio de la neutropenia febril de bajo riesgo ha demostrado ser tan seguro como la hospitalización en estudios randomizados. Reduce el riesgo de infección nosocomial, mejora la calidad de vida y reduce costos. El MASCC ≥21 es la herramienta validada para seleccionar estos pacientes."
            }
        }
    },
    {
        "id": "epoc-exacerbado-algoritmo",
        "title": "Exacerbación Grave de EPOC",
        "specialty": "Urgencias / Neumología",
        "difficulty": "Intermedio",
        "description": "Manejo de la exacerbación aguda grave de EPOC con insuficiencia respiratoria hipercápnica. La VNI es el pilar del tratamiento.",
        "guideline": "GOLD 2024 / BTS",
        "start": "n1",
        "nodes": {
            "n1": {
                "type": "question",
                "text": "¿El paciente presenta paro respiratorio o deterioro de conciencia extremo (Glasgow <8)?",
                "context": "Paro respiratorio o coma = intubación inmediata sin pasar por VNI.",
                "options": [
                    {"id": "si", "label": "Sí — paro o coma → intubación inmediata", "next": "n_intubacion_inmediata"},
                    {"id": "no", "label": "No — paciente con trabajo respiratorio pero consciente", "next": "n2_gasometria"}
                ]
            },
            "n_intubacion_inmediata": {
                "type": "terminal",
                "severity": "critical",
                "title": "Intubación Orotraqueal de Emergencia",
                "text": "Paro respiratorio o coma en EPOC. Intubación sin demora.",
                "details": [
                    "Secuencia de intubación rápida: ketamina 1-2mg/kg + succinilcolina 1.5mg/kg",
                    "Ventilación mecánica: VT 6-8mL/kg, FR 12-14/min, PEEP 5cmH2O, FiO2 mínima",
                    "CUIDADO: hiperinsuflación dinámica en EPOC — tiempo espiratorio largo, FR baja",
                    "Objetivo: pH >7.20, PaCO2 similar a la basal crónica (no normalizar bruscamente)",
                    "UCI neumológica o médica con experiencia en EPOC",
                    "El destete será difícil — anticipar traqueotomía si EPOC muy severo"
                ],
                "pearl": "La ventilación mecánica en EPOC tiene alta tasa de dependencia prolongada. Por eso la VNI existe: evitar la intubación en el 60-70% de los casos. Cuando se intuba, el riesgo de no poder extubar es significativo. Comentar con la familia y el paciente (si estaba consciente) antes de intubar."
            },
            "n2_gasometria": {
                "type": "question",
                "text": "¿La gasometría arterial muestra acidosis respiratoria (pH <7.35 y PaCO2 >45 mmHg)?",
                "context": "La hipercapnia con acidosis define la insuficiencia respiratoria hipercápnica — la indicación más fuerte para VNI en EPOC.",
                "options": [
                    {"id": "si", "label": "Sí — acidosis respiratoria hipercápnica", "next": "n3_vni_indicada"},
                    {"id": "no", "label": "No — sin acidosis (pH ≥7.35)", "next": "n_tratamiento_medico"}
                ]
            },
            "n_tratamiento_medico": {
                "type": "terminal",
                "severity": "info",
                "title": "Exacerbación Sin Acidosis — Tratamiento Médico Estándar",
                "text": "EPOC exacerbado sin insuficiencia respiratoria hipercápnica. Manejo médico sin VNI.",
                "details": [
                    "Broncodilatadores: salbutamol 2.5mg + ipratropio 0.5mg nebulizados cada 20 min × 3",
                    "Corticoide sistémico: metilprednisolona 40mg IV/día × 5 días (no más, estudio REDUCE)",
                    "Antibiótico si: esputo purulento, fiebre o radiografía con infiltrado — amoxicilina-clavulánico",
                    "O2 controlado: objetivo SatO2 88-92% (no hipercorregir — supresión del drive hipóxico)",
                    "Repetir GSA en 1-2h si hay dudas sobre la evolución",
                    "Fisioterapia respiratoria: técnicas de higiene bronquial"
                ],
                "pearl": "El corticoide oral en exacerbación de EPOC reduce el tiempo de recuperación y el riesgo de recaída a 30 días. El estudio REDUCE demostró que 5 días son equivalentes a 14 días. Cursos más largos solo aumentan efectos adversos sin beneficio adicional."
            },
            "n3_vni_indicada": {
                "type": "question",
                "text": "¿Hay contraindicaciones para la Ventilación No Invasiva (VNI)?",
                "context": "Contraindicaciones absolutas: paro respiratorio, vómitos incoercibles, obstrucción de vía aérea superior, incapacidad de adaptar mascarilla (trauma facial).",
                "options": [
                    {"id": "no", "label": "No — VNI indicada (iniciar BiPAP)", "next": "n4_bipap"},
                    {"id": "si", "label": "Sí — contraindicación para VNI → intubación", "next": "n_intubacion_inmediata"}
                ]
            },
            "n4_bipap": {
                "type": "question",
                "text": "¿Se ha iniciado BiPAP y cuál es la respuesta en 1-4 horas?",
                "context": "Parámetros iniciales: IPAP 14-16 cmH2O, EPAP 4-6 cmH2O. Evaluar respuesta: pH, PaCO2, FR, confort.",
                "options": [
                    {"id": "no", "label": "No — iniciar BiPAP ahora", "next": "n_iniciar_vni"},
                    {"id": "si_buena", "label": "Sí — buena respuesta (pH mejora, FR baja, confortable)", "next": "n_vni_exito"},
                    {"id": "si_mala", "label": "Sí — mala respuesta (pH sigue <7.25, agitado, fatiga)", "next": "n_fallo_vni"}
                ]
            },
            "n_iniciar_vni": {
                "type": "terminal",
                "severity": "warning",
                "title": "Iniciar BiPAP — Parámetros y Objetivos",
                "text": "VNI indicada. Iniciar de forma inmediata con mascarilla facial completa.",
                "details": [
                    "IPAP inicial: 14-16 cmH2O (ajustar según tolerancia y respuesta)",
                    "EPAP: 4-6 cmH2O (contrarresta auto-PEEP del EPOC)",
                    "FiO2: ajustar para SatO2 88-92% (no más)",
                    "Mascarilla facial completa: mejor tolerancia que nasobucal al inicio",
                    "Explicar al paciente el procedimiento: mejora la tolerancia y el éxito",
                    "GSA de control en 1h y 4h para evaluar respuesta"
                ],
                "pearl": "La VNI en EPOC con acidosis respiratoria tiene nivel de evidencia A: reduce intubación en un 65%, reduce mortalidad hospitalaria y reduce la estadía en UCI. Es una de las intervenciones con mayor nivel de evidencia en medicina intensiva."
            },
            "n_vni_exito": {
                "type": "terminal",
                "severity": "success",
                "title": "VNI Exitosa — Continuar y Planificar Destete",
                "text": "Buena respuesta a BiPAP. Continuar de forma discontinua (con descansos) y planificar el destete.",
                "details": [
                    "VNI continua las primeras 24h, luego descansos progresivos para comer y movilizar",
                    "Tratar causa de la exacerbación: antibiótico si esputo purulento, broncodilatadores, corticoide",
                    "Destete: retirar VNI gradualmente cuando pH >7.35 y PaCO2 en descenso",
                    "No retirar abruptamente — comprobar GSA sin VNI antes del alta",
                    "Considerar VNI domiciliaria nocturna si hipercapnia persistente al alta",
                    "Vacunación (neumococo + gripe) y rehabilitación pulmonar al alta"
                ],
                "pearl": "El destete de la VNI debe ser gradual: primero retirarla durante el día manteniendo de noche, luego evaluar tolerancia sin ella. La retirada brusca es la causa más frecuente de fracaso de la VNI. Una GSA sin VNI antes del alta asegura que el paciente puede ventilar de forma autónoma."
            },
            "n_fallo_vni": {
                "type": "terminal",
                "severity": "critical",
                "title": "Fracaso de VNI — Intubación Electiva",
                "text": "VNI ineficaz. Intubación planificada antes del deterioro a paro respiratorio.",
                "details": [
                    "Intubación electiva (mejor que de emergencia — menor mortalidad)",
                    "Informar al paciente y familia de la decisión clínica",
                    "SRI: ketamina 1.5mg/kg + rocuronio 1.2mg/kg (permite dosis alta de succinilcolina alternativa)",
                    "VMI: FR baja 10-12/min, VT 6-7mL/kg, PEEP 5-8, tiempo espiratorio largo (I:E 1:3-1:4)",
                    "UCI: protocolo de destete precoz — EPOC tiene alta tasa de dependencia ventilatoria",
                    "Comentar objetivos de cuidado con el paciente y familia si EPOC muy avanzado (GOLD IV)"
                ],
                "pearl": "El fracaso de VNI se define: pH no mejora tras 1-2h, FR >25 tras 1h, deterioro neurológico, secreciones no manejables o intolerancia. El criterio más importante es el pH a las 1-2h: si no mejora, intubar de forma planificada antes del deterioro a paro."
            }
        }
    }
]
