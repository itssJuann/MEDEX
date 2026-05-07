QUIZZES = [
    {
        "id": "cardio-urgente",
        "title": "Cardiología Urgente",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "description": "IAM, insuficiencia cardíaca, arritmias. ¿Sabes cuándo actuar y cómo?",
        "question_count": 8,
        "questions": [
            {
                "id": "q1", "type": "next_step",
                "text": "Paciente de 62 años con dolor retroesternal opresivo de 90 min. ECG: elevación del ST 3mm en V1-V4. ¿Cuál es el siguiente paso inmediato?",
                "options": [
                    {"id": "a", "text": "Solicitar troponinas y esperar resultado antes de actuar", "correct": False,
                     "explanation": "Las troponinas confirman necrosis pero no deben retrasar la reperfusión. El ECG con elevación del ST ya es diagnóstico de IAMCEST — actúa ahora."},
                    {"id": "b", "text": "Activar código IAM y preparar ICPP en <90 minutos", "correct": True,
                     "explanation": "Correcto. Con IAMCEST confirmado por ECG, activas inmediatamente el protocolo de reperfusión. Cada 30 minutos de retraso aumenta la mortalidad un 7.5%."},
                    {"id": "c", "text": "RxTx para descartar disección aórtica primero", "correct": False,
                     "explanation": "La disección aórtica es un diferencial pero la elevación del ST localizada en V1-V4 es muy específica de IAMCEST anterior. La RxTx retrasaría el tratamiento innecesariamente."},
                    {"id": "d", "text": "Iniciar heparina IV y observar evolución 1 hora", "correct": False,
                     "explanation": "La anticoagulación sola no reperfunde la arteria ocluida. En IAMCEST la anticoagulación es adyuvante — la reperfusión mecánica (ICPP) o farmacológica es el tratamiento principal."}
                ]
            },
            {
                "id": "q2", "type": "common_error",
                "text": "En un paciente con IAMCEST que llega al hospital, ¿cuál es el error más frecuente que retrasa el tratamiento?",
                "options": [
                    {"id": "a", "text": "No dar aspirina antes de la coronariografía", "correct": False,
                     "explanation": "No dar aspirina es un error, pero no es el que más retrasa el tratamiento. La aspirina tarda segundos en administrarse."},
                    {"id": "b", "text": "Esperar resultados de laboratorio (troponinas) antes de activar el código IAM", "correct": True,
                     "explanation": "El error más frecuente y costoso. El IAMCEST se diagnostica con ECG (10 minutos). Esperar troponinas puede retrasar 1-2 horas la reperfusión. El ECG es suficiente para activar."},
                    {"id": "c", "text": "Dar morfina para el dolor", "correct": False,
                     "explanation": "La morfina puede enmascarar síntomas y retrasar la absorción de antiagregantes orales (estudios CHAMPION), pero no es la causa principal de demora en la activación del protocolo."},
                    {"id": "d", "text": "No colocar monitor cardíaco desde el inicio", "correct": False,
                     "explanation": "El monitoreo continuo es fundamental pero no es el error que más retrasa la reperfusión."}
                ]
            },
            {
                "id": "q3", "type": "next_step",
                "text": "Post-ICPP exitosa en IAMCEST. El paciente está estable. ¿Qué medicación NO debe faltar al alta?",
                "options": [
                    {"id": "a", "text": "AAS + ticagrelor + betabloqueante + IECA + estatina alta intensidad", "correct": True,
                     "explanation": "Los 5 pilares post-IAM: doble antiagregación (previene trombosis del stent), betabloqueante (reduce mortalidad), IECA (remodelado ventricular), estatina (estabiliza placa). Todos con evidencia clase I."},
                    {"id": "b", "text": "AAS + anticoagulante oral + estatina", "correct": False,
                     "explanation": "La anticoagulación oral sola sin inhibidor P2Y12 no protege el stent. La doble antiagregación (AAS + ticagrelor/clopidogrel) es mandatoria por 12 meses post-stent."},
                    {"id": "c", "text": "AAS + antibiótico profiláctico + IECA", "correct": False,
                     "explanation": "Los antibióticos NO tienen indicación en el IAM no complicado. Esta combinación deja al paciente sin betabloqueante, estatina e inhibidor P2Y12 — 3 pilares esenciales."},
                    {"id": "d", "text": "Solo AAS — el stent ya protege contra la reoclusión", "correct": False,
                     "explanation": "El stent sin doble antiagregación tiene una tasa de trombosis del 5-10% en el primer mes. La monoterapia con AAS es absolutamente insuficiente post-stent farmacoactivo."}
                ]
            },
            {
                "id": "q4", "type": "diagnosis",
                "text": "Paciente con IC crónica que consulta por disnea progresiva, ortopnea, SatO2 88%, TA 165/95 y crepitantes bibasales. ¿Cuál es la primera acción?",
                "options": [
                    {"id": "a", "text": "Cristaloides IV 500mL — puede estar deshidratado por el diurético", "correct": False,
                     "explanation": "Error grave. La clínica grita sobrecarga hídrica (crepitantes, SatO2 88%, ortopnea). Los fluidos IV empeorarán el edema pulmonar. Nunca fluidos en IC congestiva sin indicación clara."},
                    {"id": "b", "text": "Furosemida IV + O2 + monitoreo hemodinámico", "correct": True,
                     "explanation": "Correcto. El pilar del tratamiento de ICAD con congestión es el diurético IV (elimina la sobrecarga), O2 para corregir la hipoxemia y monitoreo para detectar deterioro. La furosemida IV tiene efecto vasodilatador venoso casi inmediato."},
                    {"id": "c", "text": "Intubación orotraqueal — SatO2 88% es peligrosa", "correct": False,
                     "explanation": "La intubación es el último recurso. Con SatO2 88%, el primer escalón es O2 + diurético IV. Si no responde, VNI (CPAP/BiPAP) antes de la intubación. La IOT tiene mortalidad inherente significativa en IC."},
                    {"id": "d", "text": "Betabloqueante IV — la taquicardia empeora la IC", "correct": False,
                     "explanation": "Los betabloqueantes IV están CONTRAINDICADOS en la descompensación aguda con congestión. Pueden precipitar un deterioro hemodinámico severo. Solo se ajustan (no se inician ni se aumentan) los VO en fase estable."}
                ]
            },
            {
                "id": "q5", "type": "common_error",
                "text": "FA con inicio desconocido (>48h posible). ¿Cuál es el error más peligroso?",
                "options": [
                    {"id": "a", "text": "No anticoagular antes de la cardioversión", "correct": True,
                     "explanation": "El error más grave. Sin anticoagulación ≥3 semanas previas o ETE que descarte trombo, la cardioversión puede desalojar un trombo de la orejuela izquierda causando ACV. El riesgo embólico es del 5-7%."},
                    {"id": "b", "text": "Usar metoprolol en lugar de diltiazem para controlar la FC", "correct": False,
                     "explanation": "Ambos son válidos para controlar la FC en FA. La elección depende de comorbilidades (IC con FE reducida: prefiero betabloqueante). No es el error más peligroso."},
                    {"id": "c", "text": "No calcular el CHA₂DS₂-VASc en urgencias", "correct": False,
                     "explanation": "Calcularlo es importante para la anticoagulación crónica, pero el error más inmediatamente peligroso es cardiovertir sin anticoagulación adecuada en FA de inicio incierto."},
                    {"id": "d", "text": "Usar cardioversión eléctrica en lugar de farmacológica", "correct": False,
                     "explanation": "Ambas son opciones válidas. La cardioversión eléctrica tiene mayor tasa de éxito, la farmacológica evita la sedación. El problema no es el método sino hacerla sin anticoagulación en FA de inicio incierto."}
                ]
            },
            {
                "id": "q6", "type": "next_step",
                "text": "Paciente con FA y CHA₂DS₂-VASc = 3. Tiene antecedente de úlcera gástrica hace 2 años (sin sangrado activo). ¿Cuál es la conducta?",
                "options": [
                    {"id": "a", "text": "No anticoagular — alto riesgo de sangrado por la úlcera", "correct": False,
                     "explanation": "La úlcera inactiva no es contraindicación absoluta de anticoagulación. Con CHA₂DS₂-VASc ≥2, el riesgo de ACV (4-6%/año) supera claramente el riesgo hemorrágico en un paciente sin sangrado activo."},
                    {"id": "b", "text": "Aspirina — es más segura que los anticoagulantes", "correct": False,
                     "explanation": "Error conceptual importante: la aspirina NO previene el ACV en FA y tiene riesgo de sangrado similar a los anticoagulantes. No es una alternativa — es simplemente ineficaz para este propósito."},
                    {"id": "c", "text": "NACO + IBP de protección gástrica", "correct": True,
                     "explanation": "Correcto. CHA₂DS₂-VASc ≥2 indica anticoagulación. Los NACOs son de elección (menos sangrado GI que la warfarina con dabigatrán, aunque similar con rivaroxabán/apixabán). Se agrega IBP para protección gástrica dada la historia de úlcera."},
                    {"id": "d", "text": "Evaluar en 3 meses cuando cicatrice la úlcera", "correct": False,
                     "explanation": "La úlcera fue hace 2 años. Esperar innecesariamente 3 meses con FA sin anticoagulación expone al paciente a un riesgo de ACV inaceptable (4-6%/año = ~1% en 3 meses)."}
                ]
            },
            {
                "id": "q7", "type": "complication",
                "text": "¿Cuál es la complicación más temida del IAM en las primeras 48-72 horas?",
                "options": [
                    {"id": "a", "text": "Pericarditis post-IAM (síndrome de Dressler)", "correct": False,
                     "explanation": "El síndrome de Dressler ocurre semanas a meses después del IAM, no en las primeras 48-72h. Es una reacción autoinmune al tejido necrótico."},
                    {"id": "b", "text": "Fibrilación ventricular / arritmias ventriculares malignas", "correct": True,
                     "explanation": "La FV es la causa más frecuente de muerte en las primeras horas del IAM, especialmente prehospitalaria. Ocurre por reentrada en la zona de isquemia-necrosis. Por eso el monitoreo ECG continuo es obligatorio en las primeras 24-48h."},
                    {"id": "c", "text": "Trombosis venosa profunda", "correct": False,
                     "explanation": "La TVP es una complicación tardía por inmovilización, pero no es la más temida en las primeras 48-72h. Las arritmias ventriculares son el peligro inmediato."},
                    {"id": "d", "text": "Insuficiencia renal por contraste de la coronariografía", "correct": False,
                     "explanation": "La nefropatía por contraste es una complicación posible pero raramente grave en pacientes con función renal previa normal. No es la más temida en el IAMCEST agudo."}
                ]
            },
            {
                "id": "q8", "type": "next_step",
                "text": "ECG de urgencia muestra FA con FC 180 lpm. TA 78/50 mmHg. El paciente está sudoroso y con alteración del sensorio. ¿Cuál es el siguiente paso?",
                "options": [
                    {"id": "a", "text": "Metoprolol IV 5mg para controlar la frecuencia", "correct": False,
                     "explanation": "Los betabloqueantes IV están CONTRAINDICADOS en FA con inestabilidad hemodinámica. Pueden empeorar el shock al reducir la contractilidad cardíaca ya comprometida."},
                    {"id": "b", "text": "Amiodarona IV 300mg para convertir el ritmo", "correct": False,
                     "explanation": "La amiodarona IV es una opción en FA estable, pero con hipotensión e inestabilidad, no es la maniobra inicial. Además, la amiodarona tarda en hacer efecto (horas)."},
                    {"id": "c", "text": "Cardioversión eléctrica sincronizada de urgencia", "correct": True,
                     "explanation": "FA con inestabilidad hemodinámica = cardioversión eléctrica inmediata. No importa el tiempo de inicio ni la anticoagulación — la vida está en riesgo. Se sedará brevemente y se cardiovertirá."},
                    {"id": "d", "text": "Anticoagulación IV y esperar estabilización espontánea", "correct": False,
                     "explanation": "Con TA 78/50, shock hemodinámico y alteración del sensorio, esperar no es una opción. La cardioversión es la única medida que puede estabilizar al paciente en minutos."}
                ]
            },
            {
                "id": "q9", "type": "multi",
                "hint": "Piensa en los 5 fármacos con evidencia clase I que reducen mortalidad post-IAM de forma independiente.",
                "text": "¿Cuáles de los siguientes fármacos forman parte del tratamiento obligatorio al alta post-IAMCEST con stent? (Selecciona TODOS los correctos)",
                "multi_explanation": "El tratamiento post-IAM tiene 5 pilares con evidencia clase I: doble antiagregación (AAS + inhibidor P2Y12), betabloqueante (reduce la mortalidad un 23%), IECA/ARA-II (previene el remodelado ventricular) y estatina de alta intensidad (estabiliza la placa). Los antibióticos y los AINEs no tienen ningún papel.",
                "options": [
                    {"id": "a", "text": "AAS 100 mg/día indefinida",                                "correct": True,  "explanation": "Correcto. Antiagregante basal de por vida post-IAM."},
                    {"id": "b", "text": "Ticagrelor o clopidogrel por 12 meses",                    "correct": True,  "explanation": "Correcto. Doble antiagregación 12 meses para prevenir trombosis del stent."},
                    {"id": "c", "text": "Betabloqueante (carvedilol o metoprolol)",                  "correct": True,  "explanation": "Correcto. Reduce mortalidad post-IAM en un 23%."},
                    {"id": "d", "text": "IECA o ARA-II",                                             "correct": True,  "explanation": "Correcto. Previene el remodelado ventricular adverso."},
                    {"id": "e", "text": "Estatina de alta intensidad (atorvastatina 40-80 mg)",      "correct": True,  "explanation": "Correcto. LDL objetivo <55-70 mg/dL post-SCA."},
                    {"id": "f", "text": "Antibiótico profiláctico oral 7 días",                     "correct": False, "explanation": "Incorrecto. Los antibióticos no tienen ninguna indicación en el IAM no complicado."}
                ]
            },
            {
                "id": "q10", "type": "order",
                "hint": "Primero diagnóstico, luego activar el sistema, luego premedicación, luego procedimiento.",
                "text": "Ordena los pasos del manejo del IAMCEST desde el ingreso a urgencias:",
                "correct_order": ["a", "b", "c", "d", "e"],
                "explanation": "El protocolo IAMCEST sigue una secuencia estricta: ECG diagnóstico en <10 min → activar código IAM → premedicación antitrombótica → traslado a hemodinamia → ICPP. El tiempo puerta-balón <90 minutos es el indicador de calidad más importante. Cada eslabón de esta cadena debe hacerse en paralelo para minimizar el tiempo.",
                "items": [
                    {"id": "a", "text": "ECG de 12 derivaciones en menos de 10 minutos desde el ingreso"},
                    {"id": "b", "text": "Activar código IAM y avisar a hemodinamia"},
                    {"id": "c", "text": "Doble antiagregación (AAS + ticagrelor) + heparina IV"},
                    {"id": "d", "text": "Traslado urgente al laboratorio de hemodinamia"},
                    {"id": "e", "text": "Angioplastia primaria (ICPP) con implante de stent"}
                ]
            }
        ]
    },
    {
        "id": "respiratorio-critico",
        "title": "Respiratorio Crítico",
        "system": "Respiratorio",
        "difficulty": "Intermedio",
        "description": "TEP, EPOC, neumotórax, neumonía. Decisiones que no admiten demora.",
        "question_count": 7,
        "questions": [
            {
                "id": "q1", "type": "next_step",
                "text": "Mujer de 55 años, 10 días post-cirugía de cadera, con disnea brusca. Wells calculado: 8 puntos. ¿Cuál es el siguiente paso?",
                "options": [
                    {"id": "a", "text": "Dímero D — si es negativo descarta el TEP", "correct": False,
                     "explanation": "Error de algoritmo. Con Wells >6 (alta probabilidad), el dímero D estará elevado por el contexto postquirúrgico independientemente del TEP. El dímero no sirve para descartar en alta probabilidad — ir directo a TCAP."},
                    {"id": "b", "text": "TC angiografía pulmonar (TCAP) directamente", "correct": True,
                     "explanation": "Correcto. Wells ≥6 = probabilidad alta = TCAP directa. El dímero D solo se usa en probabilidad baja/intermedia para intentar descartar sin imagen. En alta probabilidad, la TCAP es mandatoria."},
                    {"id": "c", "text": "Ecografía cardíaca — buscar cor pulmonale", "correct": False,
                     "explanation": "El eco puede mostrar disfunción del VD compatible con TEP, pero no lo confirma ni lo descarta. La TCAP es el gold standard diagnóstico."},
                    {"id": "d", "text": "Anticoagulación empírica sin más estudios", "correct": False,
                     "explanation": "Con Wells alto y posibilidad de TCAP, no es correcto anticoagular sin diagnóstico confirmado. Existe riesgo de hemorragia quirúrgica reciente. La TCAP confirma en minutos."}
                ]
            },
            {
                "id": "q2", "type": "common_error",
                "text": "Paciente con EPOC grave exacerbado, pH 7.28, PaCO2 68 mmHg. ¿Cuál es el error más frecuente en urgencias?",
                "options": [
                    {"id": "a", "text": "No dar antibióticos si no hay fiebre", "correct": False,
                     "explanation": "En EPOC exacerbado con esputo purulento, los antibióticos están indicados independientemente de la fiebre (que puede estar ausente en los mayores). No es el error más frecuente."},
                    {"id": "b", "text": "Dar O2 al 100% por mascarilla de reservorio", "correct": True,
                     "explanation": "El error más clásico en urgencias. El EPOC hipercápnico tiene drive hipóxico. O2 al 100% suprime ese drive → apnea y narcosis por CO2. El objetivo es SatO2 88-92%, no normalizar. Usar venturi al 24-28%."},
                    {"id": "c", "text": "No dar corticoides sistémicos", "correct": False,
                     "explanation": "Los corticoides sistémicos acortan la recuperación en exacerbación de EPOC y están recomendados. No darlos es un error, pero no produce el daño inmediato que produce el O2 excesivo."},
                    {"id": "d", "text": "Usar salbutamol nebulizado en lugar de MDI", "correct": False,
                     "explanation": "Ambas formas son equivalentes en la exacerbación de EPOC. No es un error significativo."}
                ]
            },
            {
                "id": "q3", "type": "next_step",
                "text": "Joven de 25 años con neumotórax espontáneo izquierdo de 35% en RxTx. Hemodinámicamente estable, SatO2 96%. ¿Cuál es la conducta?",
                "options": [
                    {"id": "a", "text": "Observación solamente — se reabsorbe espontáneamente", "correct": False,
                     "explanation": "La observación es para neumotórax pequeños (<2 cm entre el pulmón y la pared torácica). Un 35% requiere intervención activa."},
                    {"id": "b", "text": "Intubación inmediata — neumotórax requiere ventilación", "correct": False,
                     "explanation": "Intubación innecesaria en un paciente consciente y estable. La presión positiva en un paciente con neumotórax puede convertirlo en neumotórax a tensión."},
                    {"id": "c", "text": "Aspiración simple o tubo de drenaje pleural", "correct": True,
                     "explanation": "Correcto. Neumotórax >2 cm o sintomático en paciente estable: aspiración simple (aguja en 2° EIC LMC) o tubo pleural. La BTS recomienda aspiración como primera opción en jóvenes con primer episodio."},
                    {"id": "d", "text": "Pleurodesis química de urgencia", "correct": False,
                     "explanation": "La pleurodesis se considera para prevenir recidivas después del episodio agudo resuelto. No es el tratamiento de urgencia del neumotórax agudo."}
                ]
            },
            {
                "id": "q4", "type": "diagnosis",
                "text": "Paciente con NAC leve (CURB-65 = 1) que a las 72h de amoxicilina persiste con fiebre 37.8°C pero con menor tos y SatO2 98%. ¿Cuál es la conducta?",
                "options": [
                    {"id": "a", "text": "Cambiar a levofloxacino por falla de tratamiento", "correct": False,
                     "explanation": "Cambio prematuro. La falla de tratamiento se define después de 72h SIN mejoría O con deterioro. Aquí hay mejoría (menos tos, SatO2 normal). La fiebre puede tardar 3-5 días en resolver. Esperar."},
                    {"id": "b", "text": "Hospitalizar — la fiebre indica fracaso terapéutico", "correct": False,
                     "explanation": "La fiebre persistente a las 72h con mejoría de otros parámetros no es fracaso. Hospitalizar innecesariamente expone al paciente a infecciones nosocomiales."},
                    {"id": "c", "text": "Tranquilizar y continuar — respuesta clínica puede tardar hasta 5 días", "correct": True,
                     "explanation": "Correcto. En NAC, la respuesta clínica esperada es mejoría de síntomas en 3-5 días, resolución radiológica en 4-8 semanas. La fiebre puede persistir 72h sin indicar fracaso si hay mejoría clínica global."},
                    {"id": "d", "text": "Agregar azitromicina para cubrir atípicos", "correct": False,
                     "explanation": "Añadir antibiótico sin indicación clara genera resistencia. En NAC leve sin comorbilidades, la amoxicilina cubre el 90% de los neumococos. No hay indicación de cobertura empírica para atípicos en CURB-65 bajo."}
                ]
            },
            {
                "id": "q5", "type": "complication",
                "text": "¿Cuál es la complicación más temida de la trombolisis en el TEP?",
                "options": [
                    {"id": "a", "text": "Hipotensión transitoria por vasodilatación", "correct": False,
                     "explanation": "La hipotensión leve durante la trombolisis es frecuente pero manejable. No es la complicación más temida."},
                    {"id": "b", "text": "Hemorragia intracraneal (HIC)", "correct": True,
                     "explanation": "La HIC ocurre en el 1-3% de los pacientes tratados con trombolisis para TEP. Tiene una mortalidad del 50-70%. Por eso la trombolisis solo está indicada en TEP masivo con shock — el beneficio debe superar claramente este riesgo catastrófico."},
                    {"id": "c", "text": "Recurrencia del TEP por resangrado en el coágulo", "correct": False,
                     "explanation": "La recurrencia de TEP durante la trombolisis es inusual. El mecanismo es la lisis activa del trombo."},
                    {"id": "d", "text": "Trombocitopenia inducida por el alteplase", "correct": False,
                     "explanation": "La trombocitopenia es característica de la heparina (HIT), no del alteplase. El alteplase actúa sobre el plasminógeno, no sobre las plaquetas."}
                ]
            },
            {
                "id": "q6", "type": "next_step",
                "text": "EPOC exacerbado con pH 7.26, PaCO2 72 mmHg. Se inicia BiPAP. A la hora de control: pH 7.28, PaCO2 75 mmHg, paciente agitado. ¿Qué haces?",
                "options": [
                    {"id": "a", "text": "Continuar BiPAP y repetir gasometría en 2 horas más", "correct": False,
                     "explanation": "Con pH que no mejora (sigue <7.30) y PaCO2 en aumento tras 1h de VNI, la VNI está fallando. Esperar más sin escalar es peligroso."},
                    {"id": "b", "text": "Añadir más broncodilatadores nebulizados", "correct": False,
                     "explanation": "Los broncodilatadores son parte del tratamiento base pero no resuelven el fallo de la VNI. Si la VNI falla, hay que escalar a intubación."},
                    {"id": "c", "text": "Intubación orotraqueal planificada antes del deterioro a paro", "correct": True,
                     "explanation": "Correcto. Criterios de fracaso de VNI: pH no mejora tras 1-2h, PaCO2 en ascenso, agitación. La intubación planificada es mejor que la intubación de emergencia en paro. Actúa ahora."},
                    {"id": "d", "text": "Aumentar la IPAP del BiPAP a 20 cmH2O", "correct": False,
                     "explanation": "Ajustar los parámetros de la VNI es razonable si hay intolerancia leve, pero con fracaso claro (pH sin mejoría, PaCO2 aumenta, agitación), los ajustes menores no serán suficientes."}
                ]
            },
            {
                "id": "q7", "type": "common_error",
                "text": "En una NAC confirmada con CURB-65 de 3, ¿cuál es el error más frecuente?",
                "options": [
                    {"id": "a", "text": "Usar amoxicilina oral en lugar de antibiótico IV", "correct": True,
                     "explanation": "CURB-65 ≥3 indica hospitalización y antibiótico IV. Amoxicilina oral no alcanza concentraciones adecuadas en sangre/tejido para una NAC grave. La guía indica ceftriaxona IV + azitromicina (o fluoroquinolona respiratoria) en NAC hospitalaria grave."},
                    {"id": "b", "text": "No solicitar hemocultivos antes del antibiótico", "correct": False,
                     "explanation": "Los hemocultivos son importantes pero no deben retrasar el antibiótico. Se pueden tomar en los primeros minutos mientras se prepara el antibiótico."},
                    {"id": "c", "text": "Dar O2 por cánula nasal en lugar de mascarilla", "correct": False,
                     "explanation": "El dispositivo de O2 se ajusta según la SatO2 y el requerimiento. No es el error más frecuente o grave en la NAC de alto riesgo."},
                    {"id": "d", "text": "No hacer RxTx de control a las 24h", "correct": False,
                     "explanation": "La RxTx de control no se realiza rutinariamente a las 24h sino al alta o a las 4-8 semanas. No es el error habitual en el manejo inicial."}
                ]
            },
            {
                "id": "q8", "type": "multi",
                "hint": "Piensa en cuáles son los criterios que definen la ventana de intubación vs. VNI en el EPOC.",
                "text": "¿Cuáles de las siguientes son indicaciones de VNI (ventilación no invasiva) en la exacerbación grave de EPOC? (Selecciona TODAS las correctas)",
                "multi_explanation": "La VNI está indicada cuando hay acidosis respiratoria hipercápnica (pH 7.25-7.35), disnea severa con uso de músculos accesorios, o FR >25 rpm. Está contraindicada si el paciente no coopera, tiene secreciones abundantes que no puede manejar, o hay paro respiratorio inminente (que requiere intubación directa). La hipoxemia aislada sin hipercapnia es más propia de la NIV en edema pulmonar.",
                "options": [
                    {"id": "a", "text": "pH 7.28 con PaCO2 72 mmHg en paciente alerta",        "correct": True,  "explanation": "Correcto. Acidosis respiratoria hipercápnica sin contraindicaciones es la indicación principal."},
                    {"id": "b", "text": "FR 32 rpm con uso intenso de músculos accesorios",     "correct": True,  "explanation": "Correcto. Trabajo respiratorio elevado con riesgo de fatiga es indicación de VNI precoz."},
                    {"id": "c", "text": "Paciente agitado que no tolera la máscara",              "correct": False, "explanation": "Incorrecto. La agitación severa que impide colocar la máscara es contraindicación de VNI."},
                    {"id": "d", "text": "Disnea grave con hipercapnia en paciente cooperador",   "correct": True,  "explanation": "Correcto. La cooperación del paciente es requisito para la VNI — si el paciente es cooperador, la VNI es la primera línea."},
                    {"id": "e", "text": "Paro respiratorio con apnea",                           "correct": False, "explanation": "Incorrecto. El paro respiratorio requiere intubación inmediata, no VNI."}
                ]
            },
            {
                "id": "q9", "type": "order",
                "hint": "En el TEP: primero sospechar, luego estratificar, luego confirmar, luego tratar.",
                "text": "Ordena el algoritmo diagnóstico-terapéutico correcto ante sospecha de TEP en urgencias:",
                "correct_order": ["a", "b", "c", "d", "e"],
                "explanation": "El manejo del TEP sigue este orden: 1) Sospechar clínicamente (síntomas + factores de riesgo), 2) Calcular score de Wells para probabilidad pretest, 3) Si probabilidad alta → TCAP directamente; si baja/media → dímero D primero, 4) Confirmar con TCAP, 5) Anticoagular según el tipo (masivo, submasivo o de bajo riesgo). Saltarse la estratificación lleva a sobrediagnosticar o infradiagnosticar el TEP.",
                "items": [
                    {"id": "a", "text": "Sospecha clínica: disnea brusca + taquicardia + factor de riesgo"},
                    {"id": "b", "text": "Calcular score de Wells para probabilidad pretest"},
                    {"id": "c", "text": "Si Wells alto: TC angiografía pulmonar directa (sin dímero D)"},
                    {"id": "d", "text": "TCAP confirma TEP bilateral con disfunción VD leve"},
                    {"id": "e", "text": "Anticoagulación con NACO o HBPM (TEP sin shock)"}
                ]
            }
        ]
    },
    {
        "id": "neuroemergencias",
        "title": "Neuroemergencias",
        "system": "Neurológico",
        "difficulty": "Avanzado",
        "description": "ACV, meningitis, status epiléptico. El tiempo es cerebro.",
        "question_count": 6,
        "questions": [
            {
                "id": "q1", "type": "next_step",
                "text": "Paciente con hemiparesia derecha de 2 horas de evolución. NIHSS 8. TC sin contraste: normal. ¿Cuál es el siguiente paso?",
                "options": [
                    {"id": "a", "text": "RMN cerebral — más sensible que la TC para detectar el infarto", "correct": False,
                     "explanation": "La RMN es más sensible pero tarda más. En ACV agudo dentro de la ventana, el tiempo es neurona. Si la TC descartó hemorragia y no hay contraindicaciones, administra tPA sin esperar la RMN."},
                    {"id": "b", "text": "tPA IV si no hay contraindicaciones — dentro de la ventana de 4.5h", "correct": True,
                     "explanation": "Correcto. TC sin hemorragia + NIHSS entre 4-25 + dentro de 4.5h + sin contraindicaciones = tPA IV. Tiempo puerta-aguja objetivo: <60 minutos. Cada 15 minutos de reducción salva semanas de vida saludable."},
                    {"id": "c", "text": "Aspirina 300mg — el tPA tiene demasiados riesgos", "correct": False,
                     "explanation": "La aspirina no es sustituto del tPA en ACV isquémico dentro de ventana. Reduce marginalmente la recurrencia precoz pero no revierte el déficit. NNT del tPA para independencia funcional = 8."},
                    {"id": "d", "text": "Anticoagulación con heparina para prevenir extensión del trombo", "correct": False,
                     "explanation": "La heparina no tiene indicación en el ACV isquémico agudo para reperfusión. Aumenta el riesgo de transformación hemorrágica sin mejorar el pronóstico neurológico."}
                ]
            },
            {
                "id": "q2", "type": "common_error",
                "text": "Paciente con sospecha de meningitis bacteriana. ¿Cuál es el error más frecuente y costoso?",
                "options": [
                    {"id": "a", "text": "No dar dexametasona con el antibiótico", "correct": False,
                     "explanation": "No dar dexametasona es un error (reduce complicaciones neurológicas), pero no es el más costoso en términos de mortalidad."},
                    {"id": "b", "text": "Retrasar el antibiótico para esperar la TC y la punción lumbar", "correct": True,
                     "explanation": "El error más mortal. Cada hora de retraso en el antibiótico aumenta la mortalidad en un 10%. Protocolo correcto: antibiótico PRIMERO (antes de TC y PL si hay urgencia), luego imagen, luego PL. El cultivo es positivo incluso 2-4h después del antibiótico."},
                    {"id": "c", "text": "Usar ceftriaxona en lugar de penicilina", "correct": False,
                     "explanation": "La ceftriaxona es el antibiótico de elección en meningitis bacteriana de causa desconocida (cubre neumococo y meningococo). No es un error."},
                    {"id": "d", "text": "No aislar al paciente desde el ingreso", "correct": False,
                     "explanation": "El aislamiento de gotas en meningococcemia es importante, pero no es el error que más aumenta la mortalidad del paciente."}
                ]
            },
            {
                "id": "q3", "type": "next_step",
                "text": "Status epiléptico tónico-clónico de 12 minutos. Se administró lorazepam 4mg IV hace 5 minutos. Las convulsiones persisten. ¿Cuál es el siguiente paso?",
                "options": [
                    {"id": "a", "text": "Segunda dosis de lorazepam 4mg IV", "correct": False,
                     "explanation": "Máximo 2 dosis de BZD. Más dosis solo aumentan la depresión respiratoria sin beneficio anticonvulsivante adicional. Con convulsiones persistentes tras la primera dosis, pasar a la segunda línea."},
                    {"id": "b", "text": "Levetiracetam IV 60 mg/kg o valproato IV 40 mg/kg (segunda línea)", "correct": True,
                     "explanation": "Correcto. Tras fallo de BZD a los 10-20 min, se pasa a segunda línea. Los tres fármacos (LEV, VPA, fenitoína) tienen eficacia equivalente (estudio ESETT 2019). LEV es de elección por mejor perfil de seguridad."},
                    {"id": "c", "text": "Intubación inmediata — las convulsiones causan hipoxia", "correct": False,
                     "explanation": "La intubación se considera en status refractario (>30 min) o con depresión respiratoria grave. A los 12 min con tratamiento en curso, el siguiente paso es la segunda línea farmacológica."},
                    {"id": "d", "text": "Fenitoína IV 15 mg/kg como primera opción de segunda línea", "correct": False,
                     "explanation": "La fenitoína es una opción válida pero tiene desventajas: requiere infusión lenta (riesgo de arritmias), no da en dextrosada, y el estudio ESETT demostró eficacia equivalente a LEV y VPA pero con peor perfil. LEV es preferible."}
                ]
            },
            {
                "id": "q4", "type": "complication",
                "text": "¿Cuál es la complicación neurológica más frecuente de la meningitis bacteriana neumocócica?",
                "options": [
                    {"id": "a", "text": "Hidrocefalia — obstrucción del flujo de LCR", "correct": False,
                     "explanation": "La hidrocefalia es una complicación posible pero no la más frecuente."},
                    {"id": "b", "text": "Sordera neurosensorial", "correct": True,
                     "explanation": "La sordera neurosensorial es la secuela más frecuente de la meningitis bacteriana, especialmente neumocócica. Ocurre en el 10-30% de los supervivientes. El daño al VIII par es directo (toxinas bacterianas) e inflamatorio. La dexametasona reduce su incidencia."},
                    {"id": "c", "text": "Epilepsia post-meningitis", "correct": False,
                     "explanation": "La epilepsia es una secuela posible (5-10%), pero la sordera neurosensorial es más frecuente en la meningitis neumocócica."},
                    {"id": "d", "text": "Vasculitis cerebral con infarto secundario", "correct": False,
                     "explanation": "El infarto cerebral por vasculitis es una complicación grave pero menos frecuente que la sordera."}
                ]
            },
            {
                "id": "q5", "type": "next_step",
                "text": "ACV isquémico confirmado. NIHSS 14. AngioTC: oclusión de ACM M1 izquierda. Han pasado 3 horas. ¿Cuál es el tratamiento óptimo?",
                "options": [
                    {"id": "a", "text": "Solo tPA IV — la trombectomía es para casos refractarios", "correct": False,
                     "explanation": "En oclusión de gran vaso (OGV), el tPA recanaliza solo en <30% de los casos. La trombectomía combinada con tPA aumenta la recanalización al 80-90% y mejora los resultados funcionales. Es tratamiento combinado, no secuencial."},
                    {"id": "b", "text": "tPA IV + trombectomía mecánica (tratamiento combinado)", "correct": True,
                     "explanation": "Correcto. En OGV dentro de ventana: tratamiento combinado. El tPA se inicia inmediatamente y no retrasa la trombectomía. NNT de la trombectomía para independencia funcional = 2.6 — uno de los mejores NNT de la medicina."},
                    {"id": "c", "text": "Solo trombectomía — el tPA aumenta el riesgo hemorrágico", "correct": False,
                     "explanation": "Los estudios DIRECT-MT y SKIP sugieren no inferioridad de trombectomía sola, pero el tratamiento combinado sigue siendo el estándar cuando no hay contraindicaciones al tPA y el tiempo lo permite."},
                    {"id": "d", "text": "Anticoagulación IV y trombectomía en 24h", "correct": False,
                     "explanation": "La anticoagulación no recanaliza arteria ocluida y tiene riesgo de transformación hemorrágica. La trombectomía debe hacerse urgente (<6h, idealmente <90 min desde el diagnóstico), no en 24 horas."}
                ]
            },
            {
                "id": "q6", "type": "common_error",
                "text": "Paciente con 'peor cefalea de su vida' de inicio brusco. TC de cráneo: normal. ¿Cuál es el error más frecuente?",
                "options": [
                    {"id": "a", "text": "No hacer RMN después de la TC negativa", "correct": False,
                     "explanation": "La RMN es útil en algunos casos pero no es el paso inmediato más importante ni el error más frecuente."},
                    {"id": "b", "text": "Dar el alta porque la TC es normal — 'no tiene nada'", "correct": True,
                     "explanation": "El error más peligroso. La TC tiene sensibilidad del 98% en las primeras 12h para HSA pero baja al 85-90% entre 12-24h. TC normal NO descarta HSA — siempre se requiere punción lumbar si la sospecha es alta. La HSA sin diagnóstico tiene mortalidad muy alta por resangrado."},
                    {"id": "c", "text": "No administrar analgésicos hasta tener el diagnóstico", "correct": False,
                     "explanation": "Retener analgesia sin causa no es correcto. El manejo del dolor no interfiere con el diagnóstico de HSA."},
                    {"id": "d", "text": "Pedir EEG para descartar crisis epiléptica", "correct": False,
                     "explanation": "La cefalea en trueno de inicio en segundos es un patrón diferente a la cefalea postcrítica. El EEG no es el estudio indicado aquí."}
                ]
            },
            {
                "id": "q7", "type": "multi",
                "hint": "El ACV tiene varias contraindicaciones absolutas para trombolisis. Algunas sorprenden.",
                "text": "¿Cuáles de las siguientes son contraindicaciones ABSOLUTAS para trombolisis IV con alteplase en el ACV isquémico? (Selecciona TODAS las correctas)",
                "multi_explanation": "Las contraindicaciones absolutas para tPA en ACV incluyen: hemorragia intracraneal en TC, TA >185/110 no controlable, cirugía o trauma mayor en últimas 2 semanas, ACV o TCE en los últimos 3 meses, y anticoagulación activa. Un ACV de hace 5 años NO es contraindicación. La TA elevada puede controlarse con labetalol antes de dar el tPA.",
                "options": [
                    {"id": "a", "text": "Hemorragia intracraneal en la TC sin contraste",              "correct": True,  "explanation": "Contraindicación absoluta — el tPA empeoraría la hemorragia."},
                    {"id": "b", "text": "TA 185/115 mmHg no controlable con labetalol IV",             "correct": True,  "explanation": "Contraindicación absoluta si no se puede bajar a <185/110 antes del tPA."},
                    {"id": "c", "text": "ACV isquémico hace 5 años (sin secuelas graves)",             "correct": False, "explanation": "No es contraindicación. Solo los ACV en los últimos 3 meses son contraindicación."},
                    {"id": "d", "text": "Cirugía mayor abdominal hace 10 días",                         "correct": True,  "explanation": "Cirugía mayor en las últimas 2 semanas es contraindicación absoluta por riesgo de sangrado en el sitio quirúrgico."},
                    {"id": "e", "text": "Anticoagulación activa con dabigatrán (última dosis hace 24h)", "correct": True,  "explanation": "La anticoagulación activa con dabigatrán es contraindicación. Existe antídoto (idarucizumab), pero su disponibilidad es variable."},
                    {"id": "f", "text": "Glucemia 130 mg/dL",                                           "correct": False, "explanation": "No es contraindicación. El rango permitido es 50-400 mg/dL. La glucemia normal no contraindica el tPA."}
                ]
            },
            {
                "id": "q8", "type": "order",
                "hint": "En el status: benzodiacepinas primero, luego segunda línea, nunca esperes más de 10 minutos entre escalones.",
                "text": "Ordena el protocolo de manejo del status epiléptico convulsivo por tiempo:",
                "correct_order": ["a", "b", "c", "d", "e"],
                "explanation": "El protocolo del status sigue una escalada estricta por tiempo: 0-5min acceso venoso + BZD, si falla a los 10min segunda línea IV (levetiracetam/valproato), si falla a los 20-30min anestesia general con intubación. La clave es no esperar — cada paso tiene 10 minutos de margen máximo. Esperar más destruye neuronas.",
                "items": [
                    {"id": "a", "text": "0-5 min: acceso venoso + O2 + glucemia + lorazepam IV 4mg"},
                    {"id": "b", "text": "5-10 min: si persiste, segunda dosis de benzodiacepina"},
                    {"id": "c", "text": "10-20 min: segunda línea IV — levetiracetam 60 mg/kg o valproato 40 mg/kg"},
                    {"id": "d", "text": "20-30 min: status refractario — intubación + propofol en infusión"},
                    {"id": "e", "text": "Tras control: TC cerebral + EEG + investigar causa del status"}
                ]
            }
        ]
    },
    {
        "id": "urgencias-metabolicas",
        "title": "Urgencias Metabólicas",
        "system": "Endocrino",
        "difficulty": "Intermedio",
        "description": "CAD, hipoglucemia, hiperpotasemia. Electrolitos que matan si no se manejan bien.",
        "question_count": 6,
        "questions": [
            {
                "id": "q1", "type": "next_step",
                "text": "Paciente con CAD: pH 7.20, K+ 3.0 mEq/L. ¿Cuál es el siguiente paso correcto?",
                "options": [
                    {"id": "a", "text": "Iniciar insulina IV inmediatamente para bajar la glucemia", "correct": False,
                     "explanation": "NUNCA insulina con K+ <3.5. La insulina mueve K+ al intracelular — con K+ 3.0 podría caer a 2.0, causando FV. Esta es la regla más importante del protocolo CAD."},
                    {"id": "b", "text": "Reponer K+ IV hasta >3.5 mEq/L, luego iniciar insulina", "correct": True,
                     "explanation": "Correcto. Orden obligatorio: 1) Hidratación, 2) K+ >3.5 mEq/L, 3) Insulina. Con K+ 3.0, reponer agresivamente (20-40 mEq/h con monitoreo ECG) antes de la insulina."},
                    {"id": "c", "text": "Bicarbonato IV para corregir la acidosis rápidamente", "correct": False,
                     "explanation": "El bicarbonato en CAD está contraindicado salvo pH <6.9 con shock. Causa hipokalemia paradójica, alcalosis de rebote y puede producir edema cerebral. La insulina resolverá la acidosis."},
                    {"id": "d", "text": "Esperar resultado del ionograma completo antes de actuar", "correct": False,
                     "explanation": "El K+ es urgente y no puede esperar. Si no hay ionograma disponible en minutos, tratar empíricamente la posible hipokalemia."}
                ]
            },
            {
                "id": "q2", "type": "common_error",
                "text": "Paciente con CAD que lleva 6 horas de tratamiento. Glucemia bajó de 450 a 240 mg/dL. El médico decide suspender la insulina. ¿Por qué es un error?",
                "options": [
                    {"id": "a", "text": "La glucemia debería llegar a <180 antes de suspender", "correct": False,
                     "explanation": "El criterio de resolución de la CAD NO es la glucemia. La glucemia puede normalizarse mientras aún hay cetoacidosis activa."},
                    {"id": "b", "text": "La CAD se resuelve cuando el pH >7.30 y HCO3 >15, no cuando baja la glucemia", "correct": True,
                     "explanation": "Error muy frecuente. La glucemia puede normalizarse horas antes de que la cetoacidosis se resuelva. Suspender la insulina con cetonas aún positivas causa rebote de CAD. Los criterios de resolución son metabólicos: pH >7.30, HCO3 >15, cetonas negativas."},
                    {"id": "c", "text": "El K+ debe estar >4.0 antes de suspender la insulina", "correct": False,
                     "explanation": "El K+ es importante de monitorizar pero no es el criterio para suspender la insulina en CAD."},
                    {"id": "d", "text": "La insulina debe continuarse hasta 24h independientemente de la glucemia", "correct": False,
                     "explanation": "El criterio no es temporal sino metabólico (pH y HCO3). Puede resolverse antes o después de las 24h."}
                ]
            },
            {
                "id": "q3", "type": "next_step",
                "text": "Paciente diabético inconsciente en urgencias. Glucemia capilar: 28 mg/dL. ¿Primer paso?",
                "options": [
                    {"id": "a", "text": "Glucagón 1mg IM — acceso rápido sin vía venosa", "correct": False,
                     "explanation": "Si hay acceso venoso (urgencias), la dextrosa IV es más rápida y fiable. El glucagón IM tarda 10-15 min y no funciona en desnutridos o alcohólicos (sin glucógeno hepático)."},
                    {"id": "b", "text": "Dextrosa al 50% IV 25-50 mL en bolo", "correct": True,
                     "explanation": "Correcto. Con acceso venoso disponible, dextrosa IV es la primera línea: actúa en 2-3 minutos, fiable en cualquier contexto. En urgencias siempre se prioriza la vía IV."},
                    {"id": "c", "text": "Insulina rápida IV — el glucómetro puede haberse equivocado", "correct": False,
                     "explanation": "Jamás. Ante cualquier duda, el principio es 'si está inconsciente y es diabético, sospecha hipoglucemia'. Dar insulina en hipoglucemia es potencialmente mortal."},
                    {"id": "d", "text": "TC cerebral urgente para descartar ACV", "correct": False,
                     "explanation": "Con glucemia de 28 mg/dL, la causa del coma es la hipoglucemia hasta demostrar lo contrario. Tratarla tarda 2 minutos. La TC se hace después si no hay recuperación."}
                ]
            },
            {
                "id": "q4", "type": "next_step",
                "text": "Hiperpotasemia K+ 6.8 mEq/L. ECG: ondas T picudas en V1-V4, QRS ligeramente ensanchado. ¿Cuál es el primer tratamiento?",
                "options": [
                    {"id": "a", "text": "Kayexalato oral — para eliminar el potasio", "correct": False,
                     "explanation": "El Kayexalato (resina de intercambio catiónico) elimina K+ pero tarda horas en actuar. Con cambios ECG, necesitas estabilización de la membrana miocárdica INMEDIATA."},
                    {"id": "b", "text": "Gluconato de calcio IV 10mL al 10% en 2-3 minutos", "correct": True,
                     "explanation": "Correcto. El calcio IV estabiliza la membrana del miocito cardíaco en 1-3 minutos. Es el primer paso cuando hay cambios ECG de hiperpotasemia. No baja el K+ (eso lo hacen insulina+dextrosa, bicarbonato, resinas) pero protege el corazón mientras actúan los demás."},
                    {"id": "c", "text": "Furosemida IV para eliminar el K+ por orina", "correct": False,
                     "explanation": "La furosemida puede ayudar a eliminar K+ pero es lenta (horas) y requiere función renal. No es la primera línea con cambios ECG."},
                    {"id": "d", "text": "Insulina 10UI IV + dextrosa 50mL al 50%", "correct": False,
                     "explanation": "La insulina + dextrosa es la segunda acción (mueve K+ al intracelular en 15-30 min). Pero con cambios ECG activos, el calcio IV debe ser lo primero para proteger el corazón."}
                ]
            },
            {
                "id": "q5", "type": "complication",
                "text": "¿Cuál es la complicación más temida de la corrección rápida de la hiponatremia crónica?",
                "options": [
                    {"id": "a", "text": "Edema cerebral por entrada rápida de agua al cerebro", "correct": False,
                     "explanation": "El edema cerebral ocurre en la hiponatremia aguda no tratada, no en la corrección. En la hiponatremia crónica, el cerebro se ha adaptado — la corrección rápida es el peligro."},
                    {"id": "b", "text": "Mielinolisis pontina central (desmielinización osmótica)", "correct": True,
                     "explanation": "La corrección de hiponatremia crónica >10-12 mEq/L en 24h o >18 mEq/L en 48h puede causar mielinolisis pontina (síndrome de desmielinización osmótica): disartria, disfagia, cuadriplejía, coma. Regla: no más de 8-10 mEq/L por día en hiponatremia crónica."},
                    {"id": "c", "text": "Hipernatremia de rebote por sobrecorrección", "correct": False,
                     "explanation": "La hipernatremia de rebote es posible pero no causa daño neurológico tan específico como la mielinolisis pontina."},
                    {"id": "d", "text": "Insuficiencia cardíaca por sobrecarga de volumen con el suero salino", "correct": False,
                     "explanation": "La sobrecarga de volumen es un riesgo a monitorizar pero no es la complicación más temida y específica de la corrección rápida."}
                ]
            },
            {
                "id": "q6", "type": "common_error",
                "text": "Paciente diabético con náuseas y glucemia de 380 mg/dL. Se va a administrar insulina. ¿Cuál es el error más peligroso?",
                "options": [
                    {"id": "a", "text": "Usar insulina regular en lugar de análogos rápidos", "correct": False,
                     "explanation": "Ambas son opciones válidas en urgencias. La insulina regular IV es de elección en urgencias (mejor control). No es el error más peligroso."},
                    {"id": "b", "text": "No medir el K+ sérico antes de iniciar la insulina", "correct": True,
                     "explanation": "El error más peligroso. La insulina mueve K+ al intracelular. Si el K+ basal está bajo o en el límite, la insulina puede precipitar una hipokalemia grave con arritmias fatales. SIEMPRE medir K+ antes de insulina en hiperglucemia severa."},
                    {"id": "c", "text": "No hidratación IV previa a la insulina", "correct": False,
                     "explanation": "La hidratación antes de la insulina es importante en CAD, pero en hiperglucemia simple sin CAD, la insulina puede ir antes o junto a la hidratación."},
                    {"id": "d", "text": "Usar dosis demasiado alta de insulina (>0.1 UI/kg/h)", "correct": False,
                     "explanation": "Dosis altas de insulina pueden causar hipoglucemia, pero el problema de no medir el K+ previo puede ser más inmediatamente letal."}
                ]
            },
            {
                "id": "q7", "type": "multi",
                "hint": "El protocolo CAD tiene un orden obligatorio. Piensa qué pasa si das insulina con K+ bajo.",
                "text": "En el manejo de la cetoacidosis diabética (CAD), ¿cuáles de los siguientes son CORRECTOS? (Selecciona TODOS los que apliquen)",
                "multi_explanation": "El protocolo CAD: la hidratación va primero (SF 1L/h), luego corregir K+ hasta >3.5, luego insulina. El bicarbonato solo se usa si pH <6.9 con shock. La CAD se resuelve cuando pH >7.30, HCO3 >15 y cetonas negativas — NO cuando la glucemia normaliza. Al llegar a 250 mg/dL se añade dextrosa para mantener la insulina corriendo.",
                "options": [
                    {"id": "a", "text": "La insulina NO debe iniciarse si el K+ sérico es <3.5 mEq/L",          "correct": True,  "explanation": "Correcto. Regla de oro: no insulina con K+ <3.5."},
                    {"id": "b", "text": "El bicarbonato está indicado en todo pH <7.20 en CAD",               "correct": False, "explanation": "Incorrecto. El bicarbonato solo se usa en pH <6.9 con compromiso hemodinámico grave."},
                    {"id": "c", "text": "La CAD se resuelve cuando pH >7.30 y HCO3 >15 y cetonas negativas",  "correct": True,  "explanation": "Correcto. Los criterios de resolución son metabólicos, no glucémicos."},
                    {"id": "d", "text": "Al llegar a glucemia de 250 mg/dL se añade dextrosa para mantener la insulina", "correct": True, "explanation": "Correcto. La dextrosa permite mantener la insulina corriendo (que resuelve la cetosis) sin causar hipoglucemia."},
                    {"id": "e", "text": "La hidratación IV es la primera medida, antes que la insulina",       "correct": True,  "explanation": "Correcto. Hidratación primero para restaurar la precarga y corregir la hiperosmolaridad."}
                ]
            },
            {
                "id": "q8", "type": "order",
                "hint": "Primero estabilizar, luego identificar la causa, luego tratar específicamente.",
                "text": "Ordena el manejo inicial del shock séptico (bundle de la primera hora):",
                "correct_order": ["a", "b", "c", "d", "e"],
                "explanation": "El bundle de 1 hora en sepsis es: 1) Lactato sérico para estratificar, 2) Hemocultivos ANTES del antibiótico, 3) Antibiótico de amplio espectro en la primera hora, 4) Cristaloides 30 mL/kg si hipotensión o lactato >4, 5) Vasopresores si no responde a fluidos. Este orden es crítico — los hemocultivos antes del antibiótico es la secuencia que más se altera en la práctica.",
                "items": [
                    {"id": "a", "text": "Medir lactato sérico"},
                    {"id": "b", "text": "Tomar hemocultivos x2 (antes del antibiótico)"},
                    {"id": "c", "text": "Antibiótico de amplio espectro IV dentro de la primera hora"},
                    {"id": "d", "text": "Cristaloides 30 mL/kg IV si hipotensión o lactato >4 mmol/L"},
                    {"id": "e", "text": "Norepinefrina si TA media <65 mmHg persiste tras fluidos"}
                ]
            }
        ]
    },
    {
        "id": "abdomen-agudo",
        "title": "Abdomen Agudo",
        "system": "Digestivo",
        "difficulty": "Básico",
        "description": "Apendicitis, pancreatitis, colecistitis, hemorragia digestiva. Decisiones quirúrgicas y médicas.",
        "question_count": 6,
        "questions": [
            {
                "id": "q1", "type": "diagnosis",
                "text": "Varón de 25 años con dolor periumbilical que migró a FID, fiebre 38.3°C y score de Alvarado de 8. ¿Cuál es la conducta?",
                "options": [
                    {"id": "a", "text": "TC de abdomen para confirmar antes de la cirugía", "correct": False,
                     "explanation": "Con Alvarado ≥7 y ecografía positiva, la TC es innecesaria y retrasa la cirugía. La TC irradia y añade tiempo. La ecografía es suficiente en jóvenes con clínica típica."},
                    {"id": "b", "text": "Cirugía urgente — apendicectomía laparoscópica", "correct": True,
                     "explanation": "Correcto. Alvarado 8 = alto riesgo. Con ecografía positiva (apéndice >6mm no compresible), la cirugía está indicada directamente. Cada hora de demora aumenta el riesgo de perforación ~5%."},
                    {"id": "c", "text": "Antibióticos IV 24h y observar — manejo no quirúrgico", "correct": False,
                     "explanation": "El manejo no quirúrgico tiene tasa de fracaso del 20-30% y mayor recurrencia. Con Alvarado 8 y ecografía positiva, la cirugía es el estándar con menor morbilidad."},
                    {"id": "d", "text": "Alta con AINE y control en 24h si no mejora", "correct": False,
                     "explanation": "Error grave. El alta con AINEs puede enmascarar la progresión a perforación. Un Alvarado de 8 nunca se va de alta sin evaluación quirúrgica."}
                ]
            },
            {
                "id": "q2", "type": "common_error",
                "text": "Pancreatitis aguda leve (BISAP 1, Balthazar B). ¿Cuál es el error más frecuente?",
                "options": [
                    {"id": "a", "text": "No dar antibióticos profilácticos para prevenir la infección", "correct": False,
                     "explanation": "¡El error es al revés! Los antibióticos profilácticos en pancreatitis leve NO están indicados (no reducen la infección, aumentan resistencias). No darlos es lo correcto."},
                    {"id": "b", "text": "Mantener NPO por 7 días 'para que el páncreas descanse'", "correct": True,
                     "explanation": "Error muy frecuente basado en un concepto obsoleto. La evidencia actual favorece el reinicio de dieta oral precoz (24-48h) cuando el paciente tolera, lo que reduce la estadía y las complicaciones infecciosas por traslocación bacteriana."},
                    {"id": "c", "text": "No solicitar ecografía para buscar la causa biliar", "correct": False,
                     "explanation": "La ecografía es importante para identificar colelitiasis (causa más frecuente), pero no hacerla en el primer día no es el error más frecuente que daña al paciente."},
                    {"id": "d", "text": "Hidratación insuficiente en las primeras horas", "correct": False,
                     "explanation": "La hidratación agresiva precoz sí es importante, pero el error de NPO prolongado innecesario es más frecuente y también causa daño."}
                ]
            },
            {
                "id": "q3", "type": "next_step",
                "text": "Hemorragia digestiva alta: hematemesis + TA 78/52 + FC 130. ¿Cuál es la secuencia correcta?",
                "options": [
                    {"id": "a", "text": "Endoscopia urgente inmediata para ver la fuente de sangrado", "correct": False,
                     "explanation": "Endoscopiar a un paciente inestable es peligroso. El riesgo de broncoaspiración y paro durante la sedación en shock hemorrágico supera el beneficio. Primero estabilizar."},
                    {"id": "b", "text": "Resucitación con cristaloides y transfusión → luego endoscopia en <12h", "correct": True,
                     "explanation": "Correcto. Primero estabilizar: 2 vías periféricas, expansión de volumen, transfusión (umbral Hb <7g/dL), IBP IV. Una vez estable, endoscopia en <12-24h (urgente si alto riesgo, electiva si bajo riesgo)."},
                    {"id": "c", "text": "Cirugía de urgencia — la hemorragia activa requiere laparotomía", "correct": False,
                     "explanation": "La cirugía se reserva para falla de dos intentos de hemostasia endoscópica. La endoscopia tiene éxito en >90% de los casos de úlcera sangrante."},
                    {"id": "d", "text": "Solo IBP IV e ingreso a observación sin transfusión", "correct": False,
                     "explanation": "Con Hb implícitamente baja (shock hemorrágico) y TA 78, los IBP solos no son suficientes. Se necesita resucitación de volumen activa."}
                ]
            },
            {
                "id": "q4", "type": "next_step",
                "text": "Colecistitis aguda grado I (Tokio). Paciente operable. ¿Cuál es el momento quirúrgico óptimo?",
                "options": [
                    {"id": "a", "text": "Cirugía electiva en 6-8 semanas — esperar que ceda la inflamación", "correct": False,
                     "explanation": "Estrategia superada. Diferir 6-8 semanas se asocia a mayor morbilidad por recurrencia (25-30% reingresa antes de la cirugía electiva), mayor dificultad técnica y mayor conversión a laparotomía."},
                    {"id": "b", "text": "Colecistectomía laparoscópica en las primeras 72h del inicio de síntomas", "correct": True,
                     "explanation": "Correcto según guías de Tokio actualizadas. La cirugía precoz en colecistitis grado I-II tiene menor morbilidad, menor estancia hospitalaria y menor costo que la cirugía diferida. Ventana óptima: primeras 24-48h."},
                    {"id": "c", "text": "Drenaje percutáneo de la vesícula y cirugía en 3 meses", "correct": False,
                     "explanation": "El drenaje percutáneo se reserva para pacientes no operables (grado III con fallo orgánico). No es la primera opción en un paciente operable grado I."},
                    {"id": "d", "text": "Solo antibióticos — el 40% se resuelve sin cirugía", "correct": False,
                     "explanation": "El manejo exclusivamente antibiótico tiene alta tasa de recurrencia y no extrae la causa (los cálculos). En pacientes operables, la cirugía es el tratamiento definitivo."}
                ]
            },
            {
                "id": "q5", "type": "complication",
                "text": "¿Cuál es la complicación más grave de la pancreatitis aguda grave (BISAP ≥3)?",
                "options": [
                    {"id": "a", "text": "Pseudoquiste pancreático", "correct": False,
                     "explanation": "El pseudoquiste es frecuente pero raramente letal. Se maneja de forma conservadora o con drenaje endoscópico. No es la complicación más grave."},
                    {"id": "b", "text": "Necrosis pancreática infectada", "correct": True,
                     "explanation": "La necrosis pancreática infectada tiene mortalidad del 30-50% incluso con tratamiento óptimo. Ocurre cuando la necrosis (estéril inicialmente) se contamina con bacterias intestinales. Requiere desbridamiento (endoscópico o quirúrgico) + antibióticos."},
                    {"id": "c", "text": "Hiperglucemia por afectación de los islotes de Langerhans", "correct": False,
                     "explanation": "La hiperglucemia es frecuente pero manejable y raramente mortal en el contexto de la pancreatitis aguda."},
                    {"id": "d", "text": "Íleo paralítico prolongado", "correct": False,
                     "explanation": "El íleo es una complicación frecuente y molesta pero no es la más grave. Se resuelve con manejo conservador en la mayoría de los casos."}
                ]
            },
            {
                "id": "q6", "type": "common_error",
                "text": "Paciente con HDA por úlcera duodenal (Forrest Ia, hemostasia endoscópica exitosa). ¿Cuál es el error más frecuente al alta?",
                "options": [
                    {"id": "a", "text": "Alta a las 24h post-hemostasia sin IBP IV 72h", "correct": True,
                     "explanation": "Para úlcera Forrest Ia/Ib, las guías recomiendan IBP IV en infusión continua 72h post-hemostasia (80mg bolo + 8mg/h). El alta precoz sin este protocolo multiplica el riesgo de resangrado del 5% al 20%."},
                    {"id": "b", "text": "No investigar H. pylori", "correct": False,
                     "explanation": "No investigar H. pylori es un error (presente en el 70-90% de las úlceras duodenales, su erradicación previene la recurrencia), pero no produce daño inmediato post-hemostasia como el alta precoz."},
                    {"id": "c", "text": "Reintroducir dieta oral en 24h", "correct": False,
                     "explanation": "La dieta oral se puede reintroducir a las 24h post-endoscopia en úlceras tratadas sin sangrado activo. No es un error."},
                    {"id": "d", "text": "No repetir la endoscopia en 24h", "correct": False,
                     "explanation": "La endoscopia de control rutinaria no está indicada en la actualidad si la hemostasia inicial fue exitosa. No hacerla no es un error."}
                ]
            },
            {
                "id": "q7", "type": "multi",
                "hint": "En la pancreatitis aguda, dos cosas son fundamentales las primeras 12-24h. Los antibióticos y la TC son para casos específicos.",
                "text": "¿Cuáles de los siguientes son CORRECTOS en el manejo de la pancreatitis aguda leve? (Selecciona TODOS los que apliquen)",
                "multi_explanation": "El manejo de la pancreatitis leve se basa en hidratación agresiva (Ringer lactato, 250-500 mL/h) y analgesia adecuada. La dieta oral precoz (dentro de 24-48h si tolera) está respaldada por evidencia reciente y reduce la estadía. Los antibióticos profilácticos y la nutrición parenteral NO están indicados en formas leves. La CPRE solo si hay colangitis o ictericia obstructiva.",
                "options": [
                    {"id": "a", "text": "Hidratación IV agresiva con Ringer lactato 250-500 mL/h las primeras 12-24h", "correct": True,  "explanation": "Correcto. La hidratación agresiva precoz es el pilar del tratamiento de pancreatitis aguda."},
                    {"id": "b", "text": "Antibióticos profilácticos IV para prevenir infección de la necrosis",         "correct": False, "explanation": "Incorrecto. Los antibióticos profilácticos no tienen indicación en pancreatitis aguda (ninguna guía los recomienda)."},
                    {"id": "c", "text": "Reinicio de dieta oral en 24-48h si el paciente tolera",                        "correct": True,  "explanation": "Correcto. La dieta oral precoz en pancreatitis leve reduce la estadía hospitalaria."},
                    {"id": "d", "text": "Nutrición parenteral total desde el primer día para que el páncreas descanse",  "correct": False, "explanation": "Incorrecto. La NPT no mejora el pronóstico en pancreatitis leve y añade riesgos propios."},
                    {"id": "e", "text": "Analgesia adecuada (ketorolaco, metamizol o morfina si necesario)",              "correct": True,  "explanation": "Correcto. El control del dolor es un pilar del tratamiento — la analgesia no retrasa el diagnóstico."}
                ]
            },
            {
                "id": "q8", "type": "order",
                "hint": "En la hemorragia digestiva alta: primero estabilizar al paciente, luego estratificar, luego actuar según el riesgo.",
                "text": "Ordena el manejo correcto de la hemorragia digestiva alta en urgencias:",
                "correct_order": ["a", "b", "c", "d", "e"],
                "explanation": "En HDA: primero la resucitación hemodinámica (sin estabilidad no se puede endoscopiar con seguridad), luego estratificación del riesgo con Glasgow-Blatchford, luego IBP IV para preparar la mucosa, luego endoscopia dentro de las 24h (o 12h en alto riesgo), y la cirugía solo si fallan dos intentos endoscópicos. La endoscopia precoz reduce la mortalidad significativamente.",
                "items": [
                    {"id": "a", "text": "2 vías periféricas + expansión con cristaloides si inestable (TA <100 o FC >100)"},
                    {"id": "b", "text": "Score Glasgow-Blatchford para estratificación del riesgo"},
                    {"id": "c", "text": "IBP en infusión continua IV (omeprazol 80mg bolo + 8mg/h)"},
                    {"id": "d", "text": "Endoscopia digestiva alta dentro de 12-24h según el riesgo"},
                    {"id": "e", "text": "Hemostasia endoscópica combinada si úlcera de alto riesgo (Forrest I-IIa)"}
                ]
            }
        ]
    },
    {
        "id": "errores-frecuentes-urgencias",
        "title": "Errores Frecuentes en Urgencias",
        "system": "Mixto",
        "difficulty": "Avanzado",
        "description": "Los errores que más ocurren en la guardia. ¿Los reconoces antes de cometerlos?",
        "question_count": 7,
        "questions": [
            {
                "id": "q1", "type": "common_error",
                "text": "Paciente con sepsis de foco urinario confirmado. ¿Cuál es el error que más aumenta la mortalidad?",
                "options": [
                    {"id": "a", "text": "No tomar hemocultivos antes del antibiótico", "correct": False,
                     "explanation": "No tomar hemocultivos es un error (pierde información microbiológica), pero no aumenta tanto la mortalidad inmediata como el retraso en el antibiótico."},
                    {"id": "b", "text": "Retrasar el antibiótico más de 1 hora desde el diagnóstico", "correct": True,
                     "explanation": "Cada hora de retraso en el antibiótico en sepsis aumenta la mortalidad un 7%. El estudio de Kumar (2006) mostró que la mortalidad aumenta de forma lineal con cada hora de retraso. El antibiótico es lo más urgente."},
                    {"id": "c", "text": "Dar solo 15 mL/kg de cristaloides en lugar de 30 mL/kg", "correct": False,
                     "explanation": "La fluidoterapia subóptima es un error, pero el retraso del antibiótico tiene impacto más demostrado en la mortalidad."},
                    {"id": "d", "text": "No calcular el score SOFA al ingreso", "correct": False,
                     "explanation": "El SOFA es útil para diagnóstico y pronóstico pero no calcular no cambia directamente la mortalidad. El antibiótico sí."}
                ]
            },
            {
                "id": "q2", "type": "common_error",
                "text": "Paciente de 70 años con 'confusión aguda' y fiebre. El familiar dice 'es la demencia que avanzó'. ¿Cuál es el error?",
                "options": [
                    {"id": "a", "text": "No solicitar TC cerebral de urgencia en el primer paciente que se ve confuso", "correct": False,
                     "explanation": "La TC tiene indicaciones específicas. No es obligatoria en todo paciente confuso mayor."},
                    {"id": "b", "text": "Aceptar la explicación del familiar sin buscar causa aguda tratable", "correct": True,
                     "explanation": "Error clásico y potencialmente mortal. La 'demencia' no empeora en horas. La confusión aguda en un anciano es siempre una urgencia médica hasta que se demuestre lo contrario. Causas: infección, IAM, ACV, hipoglucemia, hipotiroidismo, fármacos, etc."},
                    {"id": "c", "text": "No llamar al geriatra desde urgencias", "correct": False,
                     "explanation": "La consulta geriátrica es útil pero no es la primera acción ante confusión aguda en urgencias."},
                    {"id": "d", "text": "Dar sedación para manejar la agitación sin diagnóstico", "correct": False,
                     "explanation": "Sedar sin diagnóstico es peligroso (puede enmascarar el deterioro), pero aceptar la confusión como 'demencia que avanzó' sin buscar causa tratable es el error conceptual más frecuente."}
                ]
            },
            {
                "id": "q3", "type": "next_step",
                "text": "Anafilaxia con urticaria generalizada y estridor laríngeo. TA 82/50. ¿Qué das primero?",
                "options": [
                    {"id": "a", "text": "Difenhidramina IV — es una reacción alérgica", "correct": False,
                     "explanation": "Error potencialmente fatal. Los antihistamínicos no tratan el shock anafiláctico ni el angioedema laríngeo. Tardan 30-60 min en hacer efecto. La vía aérea puede cerrarse mientras buscas el antihistamínico."},
                    {"id": "b", "text": "Adrenalina 0.3-0.5mg IM en muslo anterolateral", "correct": True,
                     "explanation": "La adrenalina IM es el único tratamiento que puede revertir el shock anafiláctico y el angioedema en minutos. No hay contraindicaciones absolutas en anafilaxia. Todo lo demás (antihistamínicos, corticoides, fluidos) viene después."},
                    {"id": "c", "text": "Corticoides IV — frenan la respuesta inmune", "correct": False,
                     "explanation": "Los corticoides tardan 4-6 horas en hacer efecto. No tratan el shock ni el angioedema agudo. Son adyuvantes para prevenir la fase tardía, no tratamiento principal."},
                    {"id": "d", "text": "O2 de alto flujo y acceso venoso primero, luego adrenalina", "correct": False,
                     "explanation": "El O2 y el acceso venoso son importantes pero no deben retrasar la adrenalina IM. La adrenalina va PRIMERO porque puede administrarse IM sin vía venosa y salva la vida en minutos."}
                ]
            },
            {
                "id": "q4", "type": "common_error",
                "text": "¿Cuál es el error más frecuente al dar el alta a un paciente post-crisis asmática severa?",
                "options": [
                    {"id": "a", "text": "No dar inhalador de rescate (salbutamol) para llevar a casa", "correct": False,
                     "explanation": "No dar inhalador de rescate es un error, pero no es el que más causa reingreso precoz."},
                    {"id": "b", "text": "No prescribir ciclo de corticoide oral (prednisona 40mg × 5 días)", "correct": True,
                     "explanation": "El error más frecuente. Sin corticoide oral, la fase tardía inflamatoria (4-12h después) causa recaída en el 30% de los pacientes. El corticoide oral previene la fase tardía — es obligatorio al alta en crisis severa."},
                    {"id": "c", "text": "Dar el alta cuando el PEF es >50% del predicho", "correct": False,
                     "explanation": "El criterio de alta es PEF >60% con buena respuesta clínica. Dar el alta con <60% puede ser prematuro, pero el error del corticoide oral es más frecuente y con más impacto."},
                    {"id": "d", "text": "No hacer espirometría antes del alta", "correct": False,
                     "explanation": "La espirometría no es necesaria en urgencias para dar el alta en una crisis asmática. Se realiza de forma ambulatoria."}
                ]
            },
            {
                "id": "q5", "type": "next_step",
                "text": "K+ = 6.8 mEq/L con ondas T picudas en ECG. Paciente con IRA oligúrica. ¿Cuál es la secuencia correcta?",
                "options": [
                    {"id": "a", "text": "Diálisis urgente — la única forma de eliminar el K+ en IRA", "correct": False,
                     "explanation": "La diálisis es el tratamiento definitivo pero tarda en prepararse. Mientras tanto, el corazón está en riesgo. Siempre comenzar con la estabilización de membrana (calcio) antes de esperar la diálisis."},
                    {"id": "b", "text": "Gluconato calcio IV → insulina+dextrosa → bicarbonato → diálisis", "correct": True,
                     "explanation": "La secuencia correcta: 1) Calcio (estabiliza membrana, inmediato), 2) Insulina+dextrosa (mueve K+ intracelular en 15-30 min), 3) Bicarbonato (si hay acidosis), 4) Diálisis (eliminación definitiva en IRA). Cada paso tiene un mecanismo y tiempo de acción diferente."},
                    {"id": "c", "text": "Kayexalato + furosemida IV primero", "correct": False,
                     "explanation": "Kayexalato y furosemida son útiles para eliminar K+ pero actúan en horas. Con cambios ECG activos, la estabilización de membrana con calcio es inmediatamente prioritaria."},
                    {"id": "d", "text": "Salbutamol nebulizado — mueve K+ al intracelular", "correct": False,
                     "explanation": "El salbutamol nebulizado sí puede bajar el K+ 0.5-1 mEq/L como tratamiento adyuvante, pero no es la primera acción con cambios ECG. El calcio IV es primero."}
                ]
            },
            {
                "id": "q6", "type": "common_error",
                "text": "Hombre de 65 años fumador con hematuria macroscópica indolora. El médico le dice 'es una cistitis, tome antibiótico'. ¿Cuál es el error?",
                "options": [
                    {"id": "a", "text": "No prescribir el antibiótico adecuado para cistitis", "correct": False,
                     "explanation": "El problema no es qué antibiótico dar — el problema es que el diagnóstico puede ser erróneo. La hematuria indolora en un hombre mayor fumador no es cistitis hasta demostrar lo contrario."},
                    {"id": "b", "text": "No derivar para cistoscopia a pesar del perfil de alto riesgo de carcinoma vesical", "correct": True,
                     "explanation": "Error diagnóstico con consecuencias graves. Hematuria macroscópica indolora + hombre + >40 años + fumador = carcinoma urotelial hasta descartar. Requiere cistoscopia + uro-TC. El 15% de estas hematurias tienen tumor urológico."},
                    {"id": "c", "text": "No solicitar urocultivo antes del antibiótico", "correct": False,
                     "explanation": "El urocultivo es buena práctica pero el error mayor es no investigar el carcinoma vesical."},
                    {"id": "d", "text": "No solicitar ecografía renal", "correct": False,
                     "explanation": "La ecografía es parte del estudio pero no reemplaza la cistoscopia para descartar carcinoma vesical."}
                ]
            },
            {
                "id": "q7", "type": "complication",
                "text": "¿Cuál es la complicación más temida de la terapia con heparina?",
                "options": [
                    {"id": "a", "text": "Hemorragia mayor", "correct": False,
                     "explanation": "La hemorragia es la complicación más frecuente y la que más preocupa clínicamente, pero la HIT es la más 'temida' por su paradoja: anticoagulante que causa trombosis."},
                    {"id": "b", "text": "Trombocitopenia Inducida por Heparina (HIT tipo II)", "correct": True,
                     "explanation": "La HIT tipo II es la complicación más temida por su paradoja: el anticoagulante causa trombosis. Los anticuerpos anti-factor 4 plaquetario activan las plaquetas → trombosis arterial y venosa severa. Mortalidad del 20-30% si no se reconoce. Se presenta a los 5-14 días, con caída de plaquetas >50%."},
                    {"id": "c", "text": "Hiperpotasemia por inhibición de la aldosterona", "correct": False,
                     "explanation": "La heparina puede causar hipoaldosteronismo e hiperpotasemia, pero es rara y raramente grave comparada con la HIT."},
                    {"id": "d", "text": "Osteoporosis por uso prolongado", "correct": False,
                     "explanation": "La osteoporosis ocurre con uso prolongado (>3 meses) de heparina no fraccionada. No es la complicación más temida en el contexto agudo."}
                ]
            },
            {
                "id": "q8", "type": "multi",
                "hint": "La anafilaxia tiene un tratamiento de primera línea claro y luego adyuvantes. Los adyuvantes nunca van primero.",
                "text": "En el manejo de la anafilaxia grave con angioedema y shock, ¿cuáles de estas acciones son CORRECTAS? (Selecciona TODAS las que apliquen)",
                "multi_explanation": "En anafilaxia: adrenalina IM es el único tratamiento que salva vidas en los primeros minutos — va SIEMPRE primero. Luego fluidos IV para el shock distributivo. Los antihistamínicos y corticoides son adyuvantes para prevenir la fase tardía pero nunca reemplazan a la adrenalina. La observación de 6-8h es obligatoria por el riesgo de reacción bifásica (5-20%). El alta siempre incluye autoinyector de adrenalina.",
                "options": [
                    {"id": "a", "text": "Adrenalina 0.5mg IM en muslo anterolateral — primera acción siempre",                 "correct": True,  "explanation": "Correcto. Sin adrenalina, la anafilaxia puede ser mortal en minutos."},
                    {"id": "b", "text": "Difenhidramina IV primero — para frenar la histamina",                                   "correct": False, "explanation": "Incorrecto. Los antihistamínicos no revierten el shock ni el angioedema. Van después de la adrenalina."},
                    {"id": "c", "text": "SF IV 500-1000 mL para el shock distributivo",                                          "correct": True,  "explanation": "Correcto. Los fluidos compensan la vasodilatación masiva del shock anafiláctico."},
                    {"id": "d", "text": "Corticoides IV (metilprednisolona) para prevenir la reacción bifásica",                  "correct": True,  "explanation": "Correcto. Los corticoides previenen (aunque no eliminan) la reacción bifásica tardía. Van después de la adrenalina."},
                    {"id": "e", "text": "Observación mínima de 6-8 horas antes del alta",                                        "correct": True,  "explanation": "Correcto. La reacción bifásica ocurre en 5-20% de los casos, típicamente 1-8h después."},
                    {"id": "f", "text": "Alta sin más tratamiento si mejoró completamente a los 30 minutos",                     "correct": False, "explanation": "Incorrecto. La mejoría rápida no descarta reacción bifásica. El alta prematura puede ser fatal."}
                ]
            },
            {
                "id": "q9", "type": "order",
                "hint": "Primero lo que determina si hay hemorragia cerebral, luego verificar elegibilidad, luego tratar.",
                "text": "Ordena el manejo correcto del ACV isquémico agudo desde el ingreso a urgencias:",
                "correct_order": ["a", "b", "c", "d", "e"],
                "explanation": "El manejo del ACV agudo sigue esta cadena: 1) TC sin contraste para descartar hemorragia (si hay hemorragia, el tPA está contraindicado), 2) Calcular NIHSS y verificar contraindicaciones para trombolisis, 3) Controlar TA si >185/110 (requisito para tPA), 4) Administrar alteplase dentro del tiempo de ventana, 5) Monitoreo en Unidad de Stroke con TC de control a las 24h. El tiempo puerta-aguja <60 minutos es el estándar de calidad.",
                "items": [
                    {"id": "a", "text": "TC cerebral sin contraste urgente (descartar hemorragia)"},
                    {"id": "b", "text": "NIHSS + verificar contraindicaciones para trombolisis"},
                    {"id": "c", "text": "Controlar TA si >185/110 mmHg con labetalol IV"},
                    {"id": "d", "text": "Administrar alteplase IV 0.9 mg/kg dentro de la ventana de 4.5h"},
                    {"id": "e", "text": "Monitoreo en Unidad de Stroke + TC control a las 24h"}
                ]
            }
        ]
    }
]
