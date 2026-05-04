PATHOLOGIES = [
    {
        "id": "infarto-agudo-miocardio",
        "name": "Infarto Agudo de Miocardio",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "summary": "Necrosis del tejido miocárdico por oclusión de una arteria coronaria. Emergencia médica que requiere diagnóstico y tratamiento inmediato.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 58 años llega a urgencias con dolor retroesternal opresivo de 2 horas de evolución, irradiado al brazo izquierdo y mandíbula. Diaforesis profusa y náuseas. TA 150/90 mmHg, FC 95 lpm. ¿Cuál es tu primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Solicitar ECG de 12 derivaciones de inmediato",
                            "correct": True,
                            "feedback": "Correcto. El ECG es la herramienta diagnóstica más rápida e importante ante sospecha de IAM. Debe realizarse en menos de 10 minutos desde el ingreso.",
                            "next": "n2_ecg"
                        },
                        {
                            "id": "b",
                            "text": "Administrar analgésico y observar evolución",
                            "correct": False,
                            "feedback": "Incorrecto. No se debe retrasar el diagnóstico. El tiempo es músculo — cada minuto sin reperfusión aumenta la necrosis miocárdica.",
                            "next": "n2_deterioro"
                        },
                        {
                            "id": "c",
                            "text": "Solicitar radiografía de tórax",
                            "correct": False,
                            "feedback": "Incorrecto. La RxTx puede ser parte del estudio pero el ECG es absolutamente prioritario. Has perdido tiempo valioso.",
                            "next": "n2_rxtx"
                        }
                    ]
                },

                # --- PATH A: ECG correcto ---
                "n2_ecg": {
                    "description": "El ECG muestra elevación del segmento ST mayor a 2mm en derivaciones V1-V4. Troponinas pendientes. IAMCEST confirmado. Han pasado 8 minutos desde el ingreso. ¿Cuál es el tratamiento de reperfusión de elección?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Angioplastia primaria (ICPP) — el laboratorio de hemodinamia está disponible en 40 minutos",
                            "correct": True,
                            "feedback": "Correcto. La ICPP es de elección cuando puede realizarse en menos de 120 minutos desde el primer contacto médico. 40 minutos es óptimo.",
                            "next": "n3_posticpp"
                        },
                        {
                            "id": "b",
                            "text": "Trombolisis con alteplase — es más rápido que esperar la hemodinamia",
                            "correct": False,
                            "feedback": "Incorrecto como primera elección cuando la ICPP es accesible en tiempo. La trombolisis tiene mayor riesgo de hemorragia y menor tasa de reperfusión completa.",
                            "next": "n3_trombo"
                        },
                        {
                            "id": "c",
                            "text": "Iniciar heparina IV y antiagregantes, observar 24 horas",
                            "correct": False,
                            "feedback": "Incorrecto. La anticoagulación sola no reperfunde la arteria ocluida. El retraso aumentará significativamente la extensión de la necrosis.",
                            "next": "end_sin_reperfusion"
                        }
                    ]
                },
                "n3_posticpp": {
                    "description": "La ICPP fue exitosa. Se implantó stent en DA proximal. El paciente está estable, FC 78 lpm, TA 120/75 mmHg. ¿Cuál es el esquema de tratamiento médico correcto al alta?",
                    "options": [
                        {
                            "id": "a",
                            "text": "AAS + clopidogrel + betabloqueante + IECA + estatina de alta intensidad",
                            "correct": True,
                            "feedback": "Perfecto. Este es el pilar del tratamiento post-IAM: doble antiagregación (previene reoclusión del stent), betabloqueante (reduce mortalidad), IECA (remodelado ventricular) y estatina (estabilización de placa).",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "AAS + antibióticos de amplio espectro 7 días + estatina",
                            "correct": False,
                            "feedback": "Incorrecto. Los antibióticos no tienen indicación rutinaria en el IAM. Además falta la doble antiagregación, el betabloqueante y el IECA.",
                            "next": "end_antibiotico"
                        },
                        {
                            "id": "c",
                            "text": "Solo AAS indefinida + control en 1 mes",
                            "correct": False,
                            "feedback": "Insuficiente. La monoterapia antiagregante no protege el stent del riesgo de trombosis en los primeros 12 meses. Faltan betabloqueante, IECA y estatina.",
                            "next": "end_incompleto"
                        }
                    ]
                },
                "n3_trombo": {
                    "description": "Se administró alteplase. A los 45 minutos el paciente presenta deterioro del nivel de consciencia y hemiparesia izquierda de instalación brusca. La TC de urgencia confirma hemorragia intracraneal. ¿Cuál es tu conducta?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Suspender trombolítico, revertir con PFC + vitamina K, neurocirugía urgente",
                            "correct": True,
                            "feedback": "Correcto. La hemorragia intracraneal es la complicación más temida de la trombolisis (1-2%). El manejo es suspensión inmediata, reversión de la anticoagulación y evaluación neuroquirúrgica.",
                            "next": "end_trombo_complicado"
                        },
                        {
                            "id": "b",
                            "text": "Continuar el trombolítico y agregar manitol para el edema",
                            "correct": False,
                            "feedback": "Incorrecto. Continuar el trombolítico ante una hemorragia intracraneal activa es una conducta mortal. Se debe suspender de inmediato.",
                            "next": "end_hemorragia"
                        }
                    ]
                },

                # --- PATH B: Analgesico (deterioro) ---
                "n2_deterioro": {
                    "description": "Han pasado 35 minutos. El paciente presenta hipotensión (TA 80/50 mmHg), FC 120 lpm, diaforesis intensa y disnea en aumento. Shock cardiogénico incipiente. ¿Qué haces ahora?",
                    "options": [
                        {
                            "id": "a",
                            "text": "ECG urgente + activar protocolo de código IAM",
                            "correct": True,
                            "feedback": "Tardío pero correcto. El ECG confirma IAMCEST. El retraso de 35 minutos ya comprometió tejido miocárdico adicional. Aun así, la reperfusión sigue siendo prioritaria.",
                            "next": "n2_ecg"
                        },
                        {
                            "id": "b",
                            "text": "Administrar otro analgésico y solicitar laboratorio completo",
                            "correct": False,
                            "feedback": "Fatal. El paciente está en shock cardiogénico. Seguir sin diagnóstico ni reperfusión resultará en paro cardíaco inminente.",
                            "next": "end_muerte"
                        }
                    ]
                },

                # --- PATH C: RxTx (tiempo perdido) ---
                "n2_rxtx": {
                    "description": "La radiografía de tórax muestra silueta cardíaca normal, sin signos de falla cardíaca. Han pasado 15 minutos. El técnico te recuerda que aún no se hizo el ECG. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Solicitar ECG de inmediato",
                            "correct": True,
                            "feedback": "Correcto, aunque con 15 minutos de retraso. El ECG muestra IAMCEST. Aún estás dentro de la ventana para ICPP, pero el tiempo perdido es músculo perdido.",
                            "next": "n2_ecg"
                        },
                        {
                            "id": "b",
                            "text": "Solicitar TC de tórax para descartar disección aórtica",
                            "correct": False,
                            "feedback": "Incorrecto. Aunque la disección aórtica es un diagnóstico diferencial, la presentación clínica es más consistente con IAM. La TC agrega un retraso crítico.",
                            "next": "end_muy_tarde"
                        }
                    ]
                },

                # --- TERMINALES ---
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Excelente manejo. Diagnóstico precoz con ECG, reperfusión óptima con ICPP en menos de 60 minutos y tratamiento médico completo al alta. El paciente fue dado de alta al 5to día con fracción de eyección conservada del 55%.",
                    "pearl": "Perla clínica: El tiempo puerta-balón menor a 90 minutos es el indicador de calidad más importante en el IAMCEST. Cada 30 minutos de retraso en la reperfusión aumenta la mortalidad a 30 días en un 7.5%."
                },
                "end_antibiotico": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La reperfusión fue exitosa, pero el esquema al alta incluye antibióticos sin indicación y omite betabloqueante e IECA. El paciente tendrá mayor riesgo de remodelado ventricular adverso y reinfarto en el seguimiento.",
                    "pearl": "Perla clínica: Los pilares del tratamiento post-IAM son DAAT + betabloqueante + IECA/ARA-II + estatina de alta intensidad. Los antibióticos no tienen rol en el IAM no complicado."
                },
                "end_incompleto": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La ICPP fue exitosa pero el tratamiento médico es insuficiente. Sin doble antiagregación, el riesgo de trombosis del stent en los primeros 12 meses es significativo. Sin betabloqueante e IECA, el remodelado ventricular progresará.",
                    "pearl": "Perla clínica: La doble antiagregación (AAS + inhibidor P2Y12) debe mantenerse mínimo 12 meses post-stent en IAMCEST, independientemente del riesgo de sangrado en la mayoría de pacientes."
                },
                "end_sin_reperfusion": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente evolucionó sin reperfusión. A las 6 horas presentó shock cardiogénico severo con fracción de eyección del 20%. La zona de necrosis se extendió al ventrículo derecho. Requirió soporte con balón de contrapulsación intraaórtica.",
                    "pearl": "Perla clínica: Sin reperfusión, la necrosis miocárdica avanza a razón de 1 g de tejido por minuto. 'Time is muscle' no es una metáfora — es la fisiopatología del IAM."
                },
                "end_trombo_complicado": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El manejo de la hemorragia intracraneal fue correcto y el paciente sobrevivió con secuela neurológica leve. Sin embargo, el evento podría haberse evitado eligiendo ICPP como primera opción cuando estaba disponible en tiempo.",
                    "pearl": "Perla clínica: Las contraindicaciones de la trombolisis son extensas (ACV previo, cirugía reciente, HTA severa no controlada). La ICPP las evita todas cuando es accesible en tiempo."
                },
                "end_hemorragia": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente falleció por hemorragia intracraneal masiva. Continuar el trombolítico ante una hemorragia activa es una de las causas de muerte más evitables en urgencias.",
                    "pearl": "Perla clínica: Ante cualquier deterioro neurológico durante trombolisis, el protocolo es: STOP inmediato + TC de cráneo urgente + reversión. Sin excepciones."
                },
                "end_muerte": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente presentó fibrilación ventricular y paro cardíaco. El retraso diagnóstico y terapéutico comprometió una masa miocárdica crítica. A pesar de la reanimación, no se logró recuperación de la función cardíaca.",
                    "pearl": "Perla clínica: La FV es la causa más frecuente de muerte en la fase prehospitalaria del IAM. El acceso rápido al desfibrilador y el diagnóstico precoz son los únicos modificadores pronósticos reales."
                },
                "end_muy_tarde": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El tiempo puerta-balón superó los 180 minutos. El área de necrosis abarcó toda la pared anterior. El ecocardiograma a las 24h mostró fracción de eyección del 28% con aneurisma apical. Alta mortalidad a mediano plazo.",
                    "pearl": "Perla clínica: Cada 10 minutos de retraso en la reperfusión equivale a aproximadamente 1 año de vida perdido. La TC no está indicada como primer estudio en sospecha de IAM."
                }
            }
        }
    },
    {
        "id": "neumonia-adquirida-comunidad",
        "name": "Neumonía Adquirida en la Comunidad",
        "system": "Respiratorio",
        "difficulty": "Básico",
        "summary": "Infección del parénquima pulmonar adquirida fuera del ambiente hospitalario. Causa frecuente de morbimortalidad a nivel mundial.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente femenina de 45 años, previamente sana, con 5 días de fiebre (39°C), tos productiva con expectoración amarillenta, dolor pleurítico derecho y disnea leve. FR 22 rpm, FC 98 lpm, TA 118/76 mmHg, SatO2 94%, Glasgow 15. ¿Cuál es el estudio inicial de elección?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Radiografía de tórax PA y lateral",
                            "correct": True,
                            "feedback": "Correcto. La RxTx confirma el diagnóstico, delimita la extensión del compromiso y excluye complicaciones como derrame o absceso. Es el estándar inicial en NAC.",
                            "next": "n2_rxtx_confirmado"
                        },
                        {
                            "id": "b",
                            "text": "TC de tórax con contraste de inmediato",
                            "correct": False,
                            "feedback": "Innecesario como primer estudio. La TC tiene mayor sensibilidad pero no es costo-efectiva como estudio inicial en NAC sin complicaciones. Además irradia más y retrasa el diagnóstico.",
                            "next": "n2_tc"
                        },
                        {
                            "id": "c",
                            "text": "Broncoscopia diagnóstica urgente",
                            "correct": False,
                            "feedback": "Incorrecto. La broncoscopia no es un procedimiento diagnóstico inicial en NAC. Se reserva para casos graves, inmunocomprometidos o sin respuesta antibiótica.",
                            "next": "end_broncoscopia_mal"
                        }
                    ]
                },

                # --- PATH A: RxTx correcto ---
                "n2_rxtx_confirmado": {
                    "description": "La RxTx PA y lateral muestra consolidación lobar en el lóbulo inferior derecho con broncograma aéreo, sin derrame pleural. Aplicas el score CURB-65: Confusión 0, Urea normal 0, FR 22 rpm 1, TA normal 0, Edad <65 años 0. Total: 1 punto. ¿Cuál es el manejo más apropiado?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Tratamiento ambulatorio con amoxicilina 1g cada 8h por 7 días",
                            "correct": True,
                            "feedback": "Correcto. CURB-65 de 0-1 indica manejo ambulatorio con bajo riesgo de mortalidad (<1%). Amoxicilina es el antibiótico de primera línea en NAC leve sin comorbilidades según guías IDSA/ATS.",
                            "next": "n3_ambulatorio"
                        },
                        {
                            "id": "b",
                            "text": "Hospitalización y ceftriaxona IV 2g/día",
                            "correct": False,
                            "feedback": "Incorrecto. La hospitalización se indica con CURB-65 ≥ 2. Este caso puntaje 1 puede manejarse ambulatoriamente. La hospitalización innecesaria expone a infecciones nosocomiales y aumenta costos.",
                            "next": "end_hospitalizacion_innecesaria"
                        },
                        {
                            "id": "c",
                            "text": "Ingreso a UCI y soporte ventilatorio",
                            "correct": False,
                            "feedback": "Marcadamente excesivo. La UCI se reserva para NAC grave con criterios mayores (shock séptico, necesidad de VMI). Este caso tiene CURB-65 de 1 y SatO2 del 94% con aire ambiente.",
                            "next": "end_uci_innecesario"
                        }
                    ]
                },
                "n3_ambulatorio": {
                    "description": "La paciente inicia amoxicilina ambulatoria. A los 3 días llama porque persiste la fiebre (38.2°C) pero refiere que la tos está mejorando levemente y el dolor pleurítico disminuyó. SatO2 por oxímetro domiciliario: 96%. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Tranquilizar: la respuesta clínica puede tardar 48-72h, citar en 5 días si no mejora",
                            "correct": True,
                            "feedback": "Correcto. La respuesta a antibióticos en NAC puede tardar 3-5 días. La mejoría clínica parcial (menos tos y dolor) con SatO2 adecuada son signos favorables. No se indica cambio de antibiótico aún.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Cambiar antibiótico a levofloxacino por falla de tratamiento",
                            "correct": False,
                            "feedback": "Prematuro. La falla de tratamiento se define después de 72h sin mejoría o con deterioro clínico. Cambiar antes genera resistencia y no hay datos de atípicos que justifiquen la fluoroquinolona.",
                            "next": "end_cambio_antibiotico_precoz"
                        },
                        {
                            "id": "c",
                            "text": "Hospitalizar para antibióticos IV por persistencia de fiebre",
                            "correct": False,
                            "feedback": "Incorrecto. La fiebre puede persistir hasta 3-5 días sin indicar falla de tratamiento. La SatO2 de 96% y la mejoría clínica parcial son tranquilizadores.",
                            "next": "end_hospitalizacion_precoz"
                        }
                    ]
                },

                # --- PATH B: TC (innecesario) ---
                "n2_tc": {
                    "description": "La TC muestra consolidación en lóbulo inferior derecho con broncograma aéreo, sin absceso ni empiema. Costo: 8 veces mayor que RxTx, dosis de radiación 400 veces mayor. La consolidación es compatible con NAC. Aplicas CURB-65: 1 punto. ¿Cuál es el manejo?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Tratamiento ambulatorio con amoxicilina — el diagnóstico es claro",
                            "correct": True,
                            "feedback": "Correcto, aunque el diagnóstico podía haberse confirmado con RxTx a menor costo y radiación. CURB-65 de 1 indica manejo ambulatorio con amoxicilina.",
                            "next": "n3_ambulatorio"
                        },
                        {
                            "id": "b",
                            "text": "Hospitalizar porque la TC mostró una lesión 'importante'",
                            "correct": False,
                            "feedback": "Incorrecto. La decisión de hospitalizar se basa en scores clínicos (CURB-65, PSI), no en la apariencia radiológica aislada. CURB-65 de 1 es ambulatorio.",
                            "next": "end_hospitalizacion_innecesaria"
                        }
                    ]
                },

                # --- TERMINALES ---
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Excelente manejo. Diagnóstico con la herramienta correcta, estratificación con CURB-65, tratamiento ambulatorio apropiado y seguimiento adecuado. La paciente completó 7 días de amoxicilina y fue dada de alta sin complicaciones.",
                    "pearl": "Perla clínica: En NAC leve (CURB-65 0-1) el tratamiento ambulatorio reduce la mortalidad respecto a la hospitalización por infecciones nosocomiales. La amoxicilina cubre el 90% de los Streptococcus pneumoniae en NAC no complicada."
                },
                "end_cambio_antibiotico_precoz": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El cambio prematuro generó presión antibiótica innecesaria. La paciente mejoró con levofloxacino, pero seleccionó flora resistente para futuras infecciones. Además, las quinolonas respiratorias no son primera línea en NAC leve sin comorbilidades.",
                    "pearl": "Perla clínica: La falla de tratamiento en NAC se evalúa a las 72h. Los criterios son: ausencia de mejoría clínica O deterioro (hipoxemia progresiva, inestabilidad hemodinámica). La fiebre aislada no es criterio de falla."
                },
                "end_hospitalizacion_precoz": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La hospitalización fue innecesaria. Durante la estadía, la paciente adquirió Clostridium difficile por los antibióticos IV, complicando su recuperación. La SatO2 de 96% y la mejoría clínica parcial no justificaban el ingreso.",
                    "pearl": "Perla clínica: La hospitalización innecesaria en NAC aumenta el riesgo de infecciones nosocomiales, trombosis venosa profunda y costos del sistema. El CURB-65 existe precisamente para evitar esta práctica."
                },
                "end_hospitalizacion_innecesaria": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La hospitalización no estaba indicada. La paciente mejoró con antibióticos IV, pero estuvo expuesta innecesariamente a infecciones nosocomiales y costos. El CURB-65 de 1 es manejo ambulatorio.",
                    "pearl": "Perla clínica: CURB-65 — Confusión, Urea >7 mmol/L, FR ≥30, TA sistólica <90 o diastólica ≤60, Edad ≥65. Puntaje 0-1: ambulatorio. Puntaje 2: considerar hospitalización. Puntaje ≥3: hospitalización, evaluar UCI."
                },
                "end_uci_innecesario": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El ingreso a UCI ocupó un recurso crítico innecesariamente. La paciente desarrolló infección por Pseudomonas resistente a los antibióticos de amplio espectro empíricos. El manejo excesivo fue más dañino que la enfermedad.",
                    "pearl": "Perla clínica: Los criterios mayores de NAC grave para UCI son: shock séptico requiriendo vasopresores O insuficiencia respiratoria requiriendo ventilación mecánica. Este caso no cumple ninguno."
                },
                "end_broncoscopia_mal": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La broncoscopia causó broncoespasmo severo en una paciente con SatO2 de 94%. Debió suspenderse. Se retrasó el diagnóstico 4 horas y el tratamiento antibiótico fue demorado. El diagnóstico hubiera sido inmediato con una radiografía.",
                    "pearl": "Perla clínica: La broncoscopia tiene indicaciones precisas en NAC: inmunocompromiso severo, neumonía necrotizante, sospecha de malignidad, falta de respuesta antibiótica. No es herramienta diagnóstica de primer nivel."
                }
            }
        }
    },
    {
        "id": "acv-isquemico",
        "name": "ACV Isquémico",
        "system": "Neurológico",
        "difficulty": "Intermedio",
        "summary": "Infarto cerebral por oclusión arterial que requiere diagnóstico y reperfusión urgente dentro de una ventana terapéutica estrecha.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 67 años con hemiparesia derecha de instalación brusca hace 1 hora, afasia de expresión y desviación de la comisura labial. TA 175/100 mmHg, Glasgow 14. Su familiar refiere que estaba perfectamente bien hace 90 minutos. ¿Cuál es tu primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "TC de cráneo sin contraste urgente",
                            "correct": True,
                            "feedback": "Correcto. La TC sin contraste es el estudio de imagen inicial en todo ACV sospechado. Permite descartar hemorragia (contraindicación para trombolisis) en menos de 25 minutos.",
                            "next": "n2_tc"
                        },
                        {
                            "id": "b",
                            "text": "RMN cerebral con difusión — mayor sensibilidad para isquemia",
                            "correct": False,
                            "feedback": "Incorrecto como primer paso. La RMN es más sensible pero tarda más en realizarse. En ACV agudo, el tiempo es cerebro — cada minuto se pierden 1.9 millones de neuronas.",
                            "next": "n2_rmn_lento"
                        },
                        {
                            "id": "c",
                            "text": "Punción lumbar para descartar meningitis",
                            "correct": False,
                            "feedback": "Incorrecto. La presentación es focal y de instalación brusca, clásica de ACV. La PL está contraindicada sin TC previo y no es el estudio inicial en este contexto.",
                            "next": "end_pl_mal"
                        }
                    ]
                },
                "n2_tc": {
                    "description": "La TC sin contraste no muestra hemorragia. Signo de la arteria cerebral media hiperdensa leve. NIHSS calculado: 12 puntos. Han transcurrido 110 minutos desde el inicio de síntomas. El paciente está dentro de la ventana de 4.5 horas. ¿Cuál es el tratamiento de reperfusión?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Trombolisis IV con alteplase 0.9 mg/kg",
                            "correct": True,
                            "feedback": "Correcto. Dentro de las 4.5h del inicio, con TC sin hemorragia y sin contraindicaciones, la trombolisis IV reduce la discapacidad a 90 días significativamente (NNT=8).",
                            "next": "n3_trombo"
                        },
                        {
                            "id": "b",
                            "text": "Aspirina 300mg y hospitalización en sala general",
                            "correct": False,
                            "feedback": "Insuficiente. La aspirina no es sustituto de la reperfusión cuando el paciente está dentro de ventana. Cada hora sin reperfusión equivale a 3.6 años de envejecimiento cerebral.",
                            "next": "end_aspirina"
                        },
                        {
                            "id": "c",
                            "text": "Anticoagulación con heparina IV",
                            "correct": False,
                            "feedback": "Incorrecto. La heparina no tiene indicación en ACV isquémico agudo para reperfusión. Aumenta el riesgo de transformación hemorrágica sin mejorar el pronóstico.",
                            "next": "end_heparina_acv"
                        }
                    ]
                },
                "n2_rmn_lento": {
                    "description": "La RMN tardó 55 minutos. Confirma infarto en territorio de ACM izquierda. Han pasado 145 minutos desde el inicio. Aún dentro de ventana. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Trombolisis IV alteplase — aún dentro de las 4.5h",
                            "correct": True,
                            "feedback": "Correcto, aunque el retraso de 55 minutos ya comprometió tejido adicional. La trombolisis sigue siendo beneficiosa dentro de la ventana, pero el pronóstico es peor que con diagnóstico precoz.",
                            "next": "n3_trombo"
                        },
                        {
                            "id": "b",
                            "text": "Manejo conservador — ya pasó demasiado tiempo",
                            "correct": False,
                            "feedback": "Incorrecto. 145 minutos sigue siendo dentro de la ventana de 270 minutos (4.5h). El beneficio de la trombolisis, aunque menor, sigue superando el riesgo.",
                            "next": "end_conservador"
                        }
                    ]
                },
                "n3_trombo": {
                    "description": "Se inicia alteplase. A los 30 minutos el paciente mejora: NIHSS pasa de 12 a 5, recupera algo de movimiento en brazo derecho y mejora la comprensión. TA 168/95 mmHg. ¿Cuál es el siguiente paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Monitoreo en Unidad de Stroke, TA objetivo <180/105 durante las primeras 24h, nueva TC en 24h",
                            "correct": True,
                            "feedback": "Correcto. Tras trombolisis se debe mantener TA <180/105 (no bajar demasiado — riesgo de hipoperfusión), monitoreo neurológico estricto y TC de control para evaluar transformación hemorrágica.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Agregar anticoagulación con heparina para evitar reoclusión",
                            "correct": False,
                            "feedback": "Incorrecto y peligroso. La anticoagulación está contraindicada las primeras 24h post-trombolisis por riesgo de hemorragia cerebral. La antiagregación también se difiere.",
                            "next": "end_anticoag_post_tpa"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Excelente manejo. Diagnóstico precoz con TC, trombolisis dentro de ventana y cuidados post-reperfusión correctos. El paciente fue dado de alta a los 5 días con NIHSS de 2, recuperación casi completa del lenguaje y fuerza 4/5 en brazo derecho. Inicia rehabilitación ambulatoria.",
                    "pearl": "Perla clínica: El tiempo puerta-aguja (door-to-needle) debe ser menor a 60 minutos. Por cada 15 minutos de reducción en el tiempo de trombolisis, se salvan 4 semanas de vida saludable ajustada por discapacidad."
                },
                "end_aspirina": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente no recibió reperfusión. A las 24h persiste hemiplejía derecha y afasia severa. NIHSS de 14. Requirió internación en rehabilitación por 3 meses con recuperación parcial.",
                    "pearl": "Perla clínica: La aspirina en ACV isquémico agudo reduce el riesgo de recurrencia precoz pero NO es un tratamiento de reperfusión. No reemplaza la trombolisis cuando el paciente está dentro de ventana y sin contraindicaciones."
                },
                "end_heparina_acv": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente desarrolló transformación hemorrágica del infarto a las 12 horas, probablemente facilitada por la anticoagulación. Deterioro neurológico grave con NIHSS de 20. Traslado a UCI neurológica.",
                    "pearl": "Perla clínica: La anticoagulación con heparina en ACV isquémico agudo no está recomendada por guías internacionales. El riesgo de transformación hemorrágica supera el beneficio teórico de prevenir extensión del trombo."
                },
                "end_anticoag_post_tpa": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El paciente desarrolló hemorragia cerebral sintomática post-trombolisis (3% de los casos), agravada por la anticoagulación precoz. Requirió reversión con crioprecipitado. Secuela moderada.",
                    "pearl": "Perla clínica: Las primeras 24h post-tPA son la ventana de mayor riesgo hemorrágico. Se deben evitar: anticoagulantes, antiagregantes, procedimientos invasivos y bajadas bruscas de tensión arterial."
                },
                "end_conservador": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente no recibió reperfusión pudiendo haberla recibido. A los 3 meses presenta hemiplejía derecha persistente y afasia mixta severa. Dependiente para actividades básicas.",
                    "pearl": "Perla clínica: La ventana de trombolisis es de 4.5 horas desde el inicio CLARO de síntomas. Si no se sabe la hora exacta de inicio (ej: se despertó con el ACV), la ventana se calcula desde la última vez que se lo vio normal."
                },
                "end_pl_mal": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La punción lumbar demoró el diagnóstico 2 horas. Fue normal. El paciente llegó fuera de ventana terapéutica. No pudo recibir trombolisis. Secuela neurológica grave permanente.",
                    "pearl": "Perla clínica: En ACV agudo con déficit focal brusco, la TC sin contraste es el primer estudio SIEMPRE. La PL tiene su rol cuando se sospecha hemorragia subaracnoidea con TC normal, no en ACV isquémico."
                }
            }
        }
    },
    {
        "id": "apendicitis-aguda",
        "name": "Apendicitis Aguda",
        "system": "Digestivo",
        "difficulty": "Básico",
        "summary": "Inflamación del apéndice vermiforme, causa más frecuente de abdomen agudo quirúrgico. El diagnóstico clínico y la cirugía oportuna son clave para evitar la perforación.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 22 años, previamente sano, con 18 horas de dolor abdominal que inició en región periumbilical y migró a fosa ilíaca derecha (FID). Fiebre 38.4°C, náuseas, anorexia. Examen: dolor en punto de McBurney, signo de Blumberg (+), Rovsing (+). GB 14.500 con 85% neutrófilos. ¿Cuál es tu enfoque diagnóstico?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Score de Alvarado + ecografía abdominal",
                            "correct": True,
                            "feedback": "Correcto. El score de Alvarado estratifica el riesgo (este paciente puntúa 8/10 = alto riesgo). La ecografía confirma el diagnóstico con alta especificidad y sin radiación ionizante.",
                            "next": "n2_alvarado"
                        },
                        {
                            "id": "b",
                            "text": "TC de abdomen y pelvis con contraste de inmediato",
                            "correct": False,
                            "feedback": "No es el primer paso en un adulto joven con clínica típica. La TC es válida pero implica radiación. En jóvenes se prefiere ecografía primero. La TC se reserva para casos dudosos o ecografía no diagnóstica.",
                            "next": "n2_tc"
                        },
                        {
                            "id": "c",
                            "text": "Analgesia, antiemético y alta con AINE por 48h",
                            "correct": False,
                            "feedback": "Peligroso. Dar el alta sin descartar apendicitis en un cuadro típico expone al paciente a perforación. Los AINEs pueden enmascarar síntomas y retrasar el diagnóstico definitivo.",
                            "next": "end_alta_mal"
                        }
                    ]
                },
                "n2_alvarado": {
                    "description": "Score de Alvarado: 8/10 (alto riesgo). Ecografía: apéndice de 9mm, no compresible, con líquido periapendicular. Diagnóstico confirmado. ¿Cuál es el manejo?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Cirugía urgente — apendicectomía laparoscópica",
                            "correct": True,
                            "feedback": "Correcto. Con diagnóstico confirmado y Alvarado alto, la cirugía urgente es el estándar. La laparoscopia tiene menor tasa de complicaciones y recuperación más rápida que la laparotomía.",
                            "next": "n3_cirugia"
                        },
                        {
                            "id": "b",
                            "text": "Antibióticos IV y observación 24-48h — manejo no quirúrgico",
                            "correct": False,
                            "feedback": "El manejo antibiótico es una opción estudiada en apendicitis no complicada leve, pero con ecografía confirmando inflamación y Alvarado de 8, la cirugía sigue siendo el estándar por menor tasa de fracaso y recurrencia.",
                            "next": "n3_antibioticos"
                        }
                    ]
                },
                "n2_tc": {
                    "description": "La TC confirma apendicitis aguda no complicada, sin perforación ni absceso. Tardó 50 minutos adicionales. Alvarado calculado: 8/10. ¿Cuál es el manejo?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Cirugía urgente — el diagnóstico es claro",
                            "correct": True,
                            "feedback": "Correcto. Con diagnóstico confirmado por TC, la cirugía urgente es el siguiente paso. El retraso de 50 minutos por la TC era evitable con ecografía en este caso típico.",
                            "next": "n3_cirugia"
                        },
                        {
                            "id": "b",
                            "text": "Solicitar cirujano de guardia mañana — no es de madrugada urgente",
                            "correct": False,
                            "feedback": "Incorrecto. La apendicitis es una urgencia quirúrgica. Cada hora de demora aumenta el riesgo de perforación un 5%. La cirugía nocturna tiene resultados equivalentes a la diurna.",
                            "next": "end_demora_cirugia"
                        }
                    ]
                },
                "n3_cirugia": {
                    "description": "Apendicectomía laparoscópica completada. Hallazgo intraoperatorio: apendicitis gangrenosa sin perforación. Cultivo de líquido peritoneal enviado. El paciente está estable en recuperación. ¿Cuál es el manejo postoperatorio?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Antibióticos IV por 24h (cefazolina) y alta precoz si evolución favorable",
                            "correct": True,
                            "feedback": "Correcto para apendicitis gangrenosa sin perforación. 24h de antibióticos postoperatorios es suficiente. La alta a las 24-48h es segura si el paciente tolera la vía oral y no hay fiebre.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "No antibióticos postoperatorios — la cirugía fue el tratamiento",
                            "correct": False,
                            "feedback": "Incorrecto en apendicitis gangrenosa. La contaminación intraabdominal requiere cobertura antibiótica postoperatoria. Sin antibióticos aumenta el riesgo de absceso de herida e infección de sitio quirúrgico.",
                            "next": "end_sin_antibio"
                        },
                        {
                            "id": "c",
                            "text": "Antibióticos IV por 7 días y hospitalización prolongada",
                            "correct": False,
                            "feedback": "Excesivo para una apendicitis gangrenosa sin perforación. Los cursos prolongados de antibióticos no ofrecen beneficio adicional y aumentan el riesgo de infección por Clostridioides difficile.",
                            "next": "end_antibio_exceso"
                        }
                    ]
                },
                "n3_antibioticos": {
                    "description": "Se inicia ceftriaxona + metronidazol IV. A las 20 horas el paciente evoluciona con fiebre en aumento (39.5°C), abdomen rígido y dolor generalizado. TA 90/60 mmHg. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Cirugía de urgencia — perforación con peritonitis",
                            "correct": True,
                            "feedback": "Correcto. El fracaso del manejo no quirúrgico con signos de peritonitis y shock séptico requiere laparotomía exploradora urgente. El manejo antibiótico falló.",
                            "next": "end_cirugia_tardio"
                        },
                        {
                            "id": "b",
                            "text": "Cambiar antibiótico y ampliar cobertura",
                            "correct": False,
                            "feedback": "Incorrecto. Los signos de abdomen agudo con shock séptico son indicación quirúrgica. Los antibióticos no pueden tratar una peritonitis establecida sin control del foco.",
                            "next": "end_peritonitis"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Excelente manejo. Diagnóstico eficiente, cirugía oportuna antes de la perforación y manejo postoperatorio correcto. El paciente fue dado de alta a las 36 horas, tolerando dieta oral, sin complicaciones. Control ambulatorio a los 7 días.",
                    "pearl": "Perla clínica: La apendicitis gangrenosa sin perforación tiene una tasa de complicaciones infecciosas postoperatorias del 5-10%. 24h de antibióticos la reduce a <2%. En apendicitis perforada, se extiende a 4-5 días."
                },
                "end_sin_antibio": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El paciente desarrolló absceso de herida quirúrgica y colección intraabdominal a los 5 días. Requirió drenaje percutáneo y antibióticos por 2 semanas. Hospitalización prolongada evitable.",
                    "pearl": "Perla clínica: En apendicitis complicada (gangrenosa, perforada, con absceso), los antibióticos postoperatorios son mandatorios. La decisión de duración se basa en los hallazgos intraoperatorios y la respuesta clínica."
                },
                "end_antibio_exceso": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El paciente evolucionó bien quirúrgicamente pero desarrolló diarrea por Clostridioides difficile al 6to día de antibióticos. La hospitalización prolongada innecesaria generó una complicación iatrogénica.",
                    "pearl": "Perla clínica: El uso prolongado e innecesario de antibióticos de amplio espectro es la principal causa de infección por C. difficile hospitalaria. La duración debe ser la mínima efectiva según la evidencia."
                },
                "end_alta_mal": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente regresó a urgencias 36 horas después en shock séptico por perforación apendicular con peritonitis fecal difusa. Requirió laparotomía, lavado peritoneal y antibióticos por 10 días. UCI postoperatoria.",
                    "pearl": "Perla clínica: La tríada de McBurney + migración del dolor + fiebre en adulto joven tiene un valor predictivo positivo del 90% para apendicitis. No debe darse el alta sin descartar el diagnóstico."
                },
                "end_demora_cirugia": {
                    "terminal": True,
                    "result": "failure",
                    "description": "A las 6 horas el paciente presentó perforación con peritonitis localizada. La cirugía electiva matutina se convirtió en una urgencia mayor con mayor morbilidad, hospitalización de 7 días y antibióticos prolongados.",
                    "pearl": "Perla clínica: El riesgo de perforación en apendicitis no tratada aumenta significativamente después de las 36-72 horas de síntomas. La cirugía dentro de las primeras 24h del diagnóstico tiene la menor tasa de complicaciones."
                },
                "end_cirugia_tardio": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La cirugía controló el foco. Peritonitis secundaria por perforación apendicular. Hospitalización de 8 días con antibióticos IV. El manejo no quirúrgico inicial falló como ocurre en el 20-30% de los casos seleccionados.",
                    "pearl": "Perla clínica: El manejo no quirúrgico de la apendicitis tiene una tasa de fracaso del 20-30% a 5 años, con mayor riesgo en pacientes con Alvarado alto o con apendicolito en imagen. La cirugía sigue siendo el estándar."
                },
                "end_peritonitis": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente progresó a sepsis severa. El cambio de antibiótico sin control quirúrgico del foco no tuvo efecto. Ingresó a UCI con falla multiorgánica incipiente. La peritonitis por perforación no se resuelve con antibióticos solos.",
                    "pearl": "Perla clínica: Control del foco + antibióticos es la fórmula en infecciones abdominales. Los antibióticos solos no pueden resolver una infección con foco anatómico activo (apéndice perforado, colecistitis gangrenosa, etc.)."
                }
            }
        }
    },
    {
        "id": "cetoacidosis-diabetica",
        "name": "Cetoacidosis Diabética",
        "system": "Endocrino",
        "difficulty": "Intermedio",
        "summary": "Complicación aguda de la diabetes caracterizada por hiperglucemia, cetonemia y acidosis metabólica. Requiere manejo sistemático con hidratación, insulina y corrección electrolítica.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente femenina de 28 años con DM tipo 1 de 8 años de evolución. Consulta por vómitos desde hace 24h, dolor abdominal difuso, respiración profunda y rápida (FR 28 rpm), aliento cetónico. Glucemia capilar: 450 mg/dL. Está confusa. ¿Cuál es tu primer paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "GSA, electrolitos, cetonemia/cetonuria, hemograma y función renal",
                            "correct": True,
                            "feedback": "Correcto. Antes de cualquier tratamiento en CAD es imperativo conocer el pH, bicarbonato, potasio sérico, creatinina y cetonas. El K+ es crítico — puede estar falsamente normal o elevado aunque el K+ corporal total esté depletado.",
                            "next": "n2_labs"
                        },
                        {
                            "id": "b",
                            "text": "Iniciar insulina rápida IV de inmediato — la glucemia es muy alta",
                            "correct": False,
                            "feedback": "Peligroso sin conocer el potasio. Si el K+ sérico es <3.5 mEq/L y se administra insulina, el K+ puede caer a niveles letales produciendo arritmia. La insulina SIEMPRE se difiere hasta corregir la hipocalemia.",
                            "next": "n2_insulina_precoz"
                        },
                        {
                            "id": "c",
                            "text": "Suero fisiológico IV y antiemético — posiblemente es solo una gastroenteritis",
                            "correct": False,
                            "feedback": "Incorrecto. La glucemia de 450, el aliento cetónico, la respiración de Kussmaul y la confusión son banderas rojas de CAD. Tratarla como gastroenteritis retrasa el manejo adecuado.",
                            "next": "end_suero_solo"
                        }
                    ]
                },
                "n2_labs": {
                    "description": "Resultados: pH 7.18, HCO3 8 mEq/L, K+ 3.1 mEq/L, Glucosa 452 mg/dL, Cr 1.4 mg/dL, cetonas (++++). Gap aniónico: 26. CAD severa confirmada. ¿Cuál es el orden correcto de manejo?",
                    "options": [
                        {
                            "id": "a",
                            "text": "1° Hidratación IV con SF — 2° Reposición de K+ — 3° Insulina en infusión continua",
                            "correct": True,
                            "feedback": "Correcto. Este es el orden mandatorio en CAD: primero hidratar para restaurar volumen intravascular, luego corregir K+ hasta >3.5 mEq/L, y solo entonces iniciar insulina. La insulina sin K+ corregido puede ser fatal.",
                            "next": "n3_manejo"
                        },
                        {
                            "id": "b",
                            "text": "Bicarbonato IV para corregir el pH rápidamente",
                            "correct": False,
                            "feedback": "Incorrecto. El bicarbonato no está indicado en CAD excepto en pH <6.9 con compromiso hemodinámico. Puede causar hipokalemia paradójica, acidosis paradójica del LCR y edema cerebral.",
                            "next": "end_bicarbonato"
                        },
                        {
                            "id": "c",
                            "text": "Insulina IV primero para bajar la glucemia rápido, luego el resto",
                            "correct": False,
                            "feedback": "Peligroso. Con K+ de 3.1, la insulina agravará la hipokalemia. La insulina mueve K+ al intracelular y puede provocar arritmias letales con K+ <2.5. Primero hidratación y reposición de potasio.",
                            "next": "end_insulina_sin_k"
                        }
                    ]
                },
                "n2_insulina_precoz": {
                    "description": "Se inició insulina sin medir electrolitos. A los 40 minutos el ECG muestra ondas T aplanadas y aparecen extrasístoles ventriculares. K+ urgente: 2.3 mEq/L. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Suspender insulina + cloruro de potasio IV urgente + monitoreo ECG continuo",
                            "correct": True,
                            "feedback": "Correcto. Debes detener la insulina inmediatamente y reponer K+ agresivamente. El K+ <2.5 con cambios ECG es una emergencia que puede progresar a fibrilación ventricular.",
                            "next": "end_recovery_k"
                        },
                        {
                            "id": "b",
                            "text": "Continuar insulina y agregar K+ oral",
                            "correct": False,
                            "feedback": "Incorrecto. El K+ oral no es suficiente en hipokalemia severa aguda con cambios ECG. Continuar la insulina mientras el K+ cae es potencialmente mortal.",
                            "next": "end_arritmia"
                        }
                    ]
                },
                "n3_manejo": {
                    "description": "A las 4 horas: hidratación 2L SF administrados, K+ repuesto a 3.8 mEq/L, insulina en infusión 0.1 U/kg/h. Glucemia actual: 248 mg/dL. pH: 7.29. La glucemia bajó más rápido que la cetonemia. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Agregar dextrosa al 5% al suero y mantener la insulina — el objetivo es resolver la cetosis, no solo la glucemia",
                            "correct": True,
                            "feedback": "Correcto. Cuando la glucemia llega a 250 mg/dL se agrega dextrosa para poder mantener la insulina corriendo (que resuelve la cetoacidosis). La CAD se resuelve cuando el pH >7.30 y HCO3 >15, no cuando la glucemia es normal.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Suspender la insulina — la glucemia ya bajó a rango aceptable",
                            "correct": False,
                            "feedback": "Error frecuente. La insulina resuelve la cetoacidosis, no solo la hiperglucemia. Si se suspende con cetonas aún positivas, la CAD recidiva. El criterio de resolución es pH y bicarbonato, no la glucemia.",
                            "next": "end_recaida"
                        },
                        {
                            "id": "c",
                            "text": "Aumentar la dosis de insulina para bajar la glucemia más rápido",
                            "correct": False,
                            "feedback": "Incorrecto. Descender la glucemia muy rápido (>100 mg/dL/h) aumenta el riesgo de edema cerebral, especialmente en jóvenes. El descenso objetivo es 50-75 mg/dL por hora.",
                            "next": "end_hipoglucemia"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Excelente manejo. Diagnóstico con laboratorio completo, secuencia correcta (hidratación → K+ → insulina), y transición a dextrosa al llegar a 250 mg/dL. A las 12h: pH 7.36, HCO3 18, cetonas (-). Paciente alerta. Transición a insulina subcutánea e inicio de educación en ajuste de dosis.",
                    "pearl": "Perla clínica: La CAD se resuelve cuando: pH >7.30, HCO3 >15 mEq/L y cetonas negativas — no cuando la glucemia es normal. Suspender insulina prematuramente es la causa más frecuente de recidiva intrahospitalaria."
                },
                "end_recaida": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La suspensión prematura de insulina causó rebote de la cetoacidosis. A las 3h la glucemia subió a 380 y el pH cayó a 7.22. Se debió reiniciar el protocolo desde el principio. El tiempo total de resolución se duplicó.",
                    "pearl": "Perla clínica: Al suspender insulina IV, se debe traslapar con insulina subcutánea: administrar insulina SC 1-2h ANTES de suspender el goteo para evitar la brecha de cobertura que lleva a recidiva."
                },
                "end_bicarbonato": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El bicarbonato agravó la hipokalemia (K+ cayó a 2.7) y produjo alcalosis de rebote a las 6 horas. La resolución de la CAD fue más lenta y complicada que con el protocolo estándar.",
                    "pearl": "Perla clínica: El bicarbonato en CAD solo está indicado con pH <6.9 y compromiso hemodinámico grave. En cualquier otro caso, la insulina y la hidratación resuelven la acidosis de manera fisiológica y segura."
                },
                "end_insulina_sin_k": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El K+ cayó a 2.1 mEq/L produciendo fibrilación ventricular. El equipo de reanimación logró revertirla, pero la paciente quedó con daño anóxico leve. Complicación 100% prevenible con la medición de electrolitos previo al tratamiento.",
                    "pearl": "Perla clínica: Nunca iniciar insulina en CAD con K+ <3.5 mEq/L. La insulina promueve la entrada de K+ a la célula — si ya está bajo, la caída adicional puede ser fatal. Esta es la regla más importante del protocolo CAD."
                },
                "end_suero_solo": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Tratada como gastroenteritis, la paciente fue internada en sala general sin monitoreo. A las 6h presentó paro cardiorrespiratorio por hipokalemia severa no detectada (K+ 2.0). La CAD avanzada no diagnosticada fue la causa.",
                    "pearl": "Perla clínica: El aliento cetónico + respiración de Kussmaul (profunda, rápida) + hiperglucemia en DM1 = CAD hasta demostrar lo contrario. La tríada es prácticamente patognomónica y requiere manejo inmediato."
                },
                "end_recovery_k": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La suspensión de insulina y reposición de K+ revirtió la hipokalemia. Después de 2 horas con K+ de 3.8, se reinició el protocolo correctamente. Resolución de la CAD a las 14h (4h más de lo esperado). Complicación evitable.",
                    "pearl": "Perla clínica: Si se comete el error de iniciar insulina con K+ bajo y aparecen arritmias: STOP insulina + K+ IV agresivo (10-20 mEq/h con monitoreo ECG continuo) + no reiniciar insulina hasta K+ >3.5."
                },
                "end_arritmia": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La fibrilación ventricular no fue revertida a tiempo. La paciente falleció. La continuación de insulina con K+ de 2.3 y cambios ECG activos fue una conducta mortal ante una emergencia electrolítica clara.",
                    "pearl": "Perla clínica: Los cambios ECG de hipokalemia progresan: ondas T aplanadas → ondas U prominentes → prolongación QT → torsades de pointes → FV. Cada paso es una señal de alarma que exige acción inmediata."
                },
                "end_hipoglucemia": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El descenso rápido de glucemia (<50 mg/dL/h) causó hipoglucemia severa (38 mg/dL) y edema cerebral leve. La paciente requirió dextrosa hipertónica y presentó cefalea intensa. Resolución de la CAD retrasada.",
                    "pearl": "Perla clínica: El objetivo en CAD es descender la glucemia 50-75 mg/dL por hora. Más rápido que eso aumenta el riesgo de edema cerebral (especialmente en niños y adultos jóvenes) e hipoglucemia."
                }
            }
        }
    },
    {
        "id": "tromboembolia-pulmonar",
        "name": "Tromboembolismo Pulmonar",
        "system": "Respiratorio",
        "difficulty": "Avanzado",
        "summary": "Obstrucción de la circulación arterial pulmonar por trombos, generalmente de origen venoso profundo. Espectro clínico amplio: desde formas leves hasta shock obstructivo fatal.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente femenina de 55 años, 12 días postoperatorio de artroplastia de cadera. Consulta por disnea brusca de inicio hace 2 horas, dolor pleurítico en hemitórax derecho y hemoptisis leve. FC 118 lpm, FR 24 rpm, TA 108/70 mmHg, SatO2 88% con aire ambiente. ¿Cuál es tu primer paso diagnóstico?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Calcular score de Wells para TEP y actuar según resultado",
                            "correct": True,
                            "feedback": "Correcto. El score de Wells estratifica la probabilidad pre-test y guía si se puede usar dímero D o ir directamente a TC angiografía. Con cirugía ortopédica reciente + taquicardia + síntomas, el Wells será alto.",
                            "next": "n2_wells"
                        },
                        {
                            "id": "b",
                            "text": "Dímero D — si es negativo descarta el TEP",
                            "correct": False,
                            "feedback": "Incorrecto en este contexto. El dímero D es útil solo cuando la probabilidad pre-test es BAJA. En alta probabilidad (cirugía reciente, taquicardia, hipoxemia), el dímero siempre será positivo y no aporta información diagnóstica.",
                            "next": "n2_dimero_mal"
                        },
                        {
                            "id": "c",
                            "text": "Radiografía de tórax urgente",
                            "correct": False,
                            "feedback": "La RxTx generalmente es normal o inespecífica en TEP (signo de Hampton, Westermark son raros). No descarta ni confirma. No debe ser el primer paso cuando hay alta sospecha clínica.",
                            "next": "n2_rxtx"
                        }
                    ]
                },
                "n2_wells": {
                    "description": "Score de Wells: Cirugía reciente +1.5 / FC >100 +1.5 / Síntomas de TVP +3 / Diagnóstico alternativo menos probable +3. Total: 9 puntos = Probabilidad ALTA. ¿Cuál es el siguiente paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "TC angiografía pulmonar (TCAP) directamente — Wells alto, dímero no necesario",
                            "correct": True,
                            "feedback": "Correcto. Con Wells >6 (probabilidad alta), se va directamente a TCAP sin pasar por dímero D. El dímero no sirve para descartar cuando la probabilidad es alta. La TCAP es el gold standard diagnóstico.",
                            "next": "n3_tcap"
                        },
                        {
                            "id": "b",
                            "text": "Dímero D primero para confirmar que se justifica la TCAP",
                            "correct": False,
                            "feedback": "Error de algoritmo. Con Wells alto, el dímero D estará elevado por el contexto postquirúrgico independientemente del TEP — no tiene valor predictivo. Ir directo a TCAP.",
                            "next": "end_dimero_innecesario"
                        }
                    ]
                },
                "n2_dimero_mal": {
                    "description": "El dímero D resultó 4.800 ng/mL (muy elevado, VN <500). Esto era predecible en una paciente postquirúrgica. No cambia la probabilidad. ¿Qué haces ahora?",
                    "options": [
                        {
                            "id": "a",
                            "text": "TCAP urgente — el dímero elevado en alta probabilidad exige imagen confirmatoria",
                            "correct": True,
                            "feedback": "Correcto, aunque el tiempo de diagnóstico aumentó innecesariamente. El dímero no debía pedirse aquí. Ahora sí corresponde la TCAP.",
                            "next": "n3_tcap"
                        },
                        {
                            "id": "b",
                            "text": "Con dímero tan alto, iniciar anticoagulación sin más estudios",
                            "correct": False,
                            "feedback": "Incorrecto. La anticoagulación sin diagnóstico confirmado expone a riesgos sin beneficio demostrado. El dímero elevado no confirma TEP — siempre se requiere imagen en alta probabilidad.",
                            "next": "end_anticoag_sin_dx"
                        }
                    ]
                },
                "n2_rxtx": {
                    "description": "La RxTx muestra atelectasia laminar en base derecha y elevación del hemidiafragma ipsilateral — hallazgos inespecíficos. No se puede concluir TEP. La paciente persiste con SatO2 88% y FC 122. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Wells + TCAP urgente — la RxTx no descartó nada",
                            "correct": True,
                            "feedback": "Correcto, aunque se perdió tiempo. La RxTx normal o inespecífica en TEP es lo esperado. Ahora el algoritmo correcto: Wells alto → TCAP directo.",
                            "next": "n3_tcap"
                        },
                        {
                            "id": "b",
                            "text": "La RxTx no muestra neumonía, probablemente es broncoespasmo — salbutamol y observar",
                            "correct": False,
                            "feedback": "Error diagnóstico grave. El TEP con hemoptisis, taquicardia e hipoxemia en postoperatorio no puede descartarse con RxTx normal. El diagnóstico diferencial no justifica el alta sin imagen vascular.",
                            "next": "end_broncoespasmo_mal"
                        }
                    ]
                },
                "n3_tcap": {
                    "description": "La TCAP confirma TEP bilateral con trombos en arterias lobares derechas e izquierda inferior. Disfunción ventricular derecha leve (VD/VI 0.9). Paciente hemodinámicamente estable: TA 105/68 mmHg, FC 115 lpm. ¿Cuál es el tratamiento?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Anticoagulación: HBPM o NACO (rivaroxabán/apixabán) — TEP sin shock",
                            "correct": True,
                            "feedback": "Correcto. TEP con estabilidad hemodinámica (sin shock ni hipotensión sostenida) se trata con anticoagulación. Los NACOs son de elección en TEP no oncológico sin contraindicaciones, con evidencia no inferior a HBPM/AVK.",
                            "next": "n4_anticoag"
                        },
                        {
                            "id": "b",
                            "text": "Trombolisis sistémica con alteplase — TEP bilateral extenso",
                            "correct": False,
                            "feedback": "Incorrecto. La trombolisis sistémica está indicada en TEP masivo con shock o paro. Con TA 105 y sin shock, el riesgo hemorrágico de la trombolisis (HIC 2-3%) supera el beneficio. Es TEP submasivo.",
                            "next": "end_trombolisis_exceso"
                        },
                        {
                            "id": "c",
                            "text": "Filtro de vena cava inferior como primera medida",
                            "correct": False,
                            "feedback": "Incorrecto como primera línea. El filtro de VCI no trata el TEP existente, solo previene nuevos émbolos. Se reserva para contraindicación absoluta de anticoagulación o trombosis recurrente bajo anticoagulación.",
                            "next": "end_filtro_mal"
                        }
                    ]
                },
                "n4_anticoag": {
                    "description": "Se inicia apixabán (10mg cada 12h por 7 días, luego 5mg cada 12h). A las 24h la paciente mejora: FC 92 lpm, SatO2 95%. Se planifica el alta. ¿Cuánto tiempo debe anticoagularse y qué seguimiento harás?",
                    "options": [
                        {
                            "id": "a",
                            "text": "3-6 meses de anticoagulación + doppler venoso + evaluar factores de riesgo persistentes",
                            "correct": True,
                            "feedback": "Correcto. TEP provocado por cirugía: 3 meses es suficiente si se removió el factor de riesgo. Se debe investigar trombofilia, malignidad oculta y valorar riesgo-beneficio de extensión del tratamiento.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Suspender anticoagulación al mes — ya mejoró clínicamente",
                            "correct": False,
                            "feedback": "Incorrecto. La recurrencia de TEP es del 40-50% si se suspende prematuramente. El mínimo para TEP con factor de riesgo transitorio es 3 meses. La mejoría clínica no indica resolución del trombo.",
                            "next": "end_recidiva"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Manejo ejemplar. Wells → TCAP → anticoagulación correcta → seguimiento apropiado. La paciente completó 3 meses de apixabán. Angiotomografía de control sin trombos residuales. Doppler venoso sin TVP residual. Estratificación de riesgo trombótico para futuros procedimientos realizada.",
                    "pearl": "Perla clínica: TEP provocado (cirugía, inmovilización, estrógenos) → 3 meses de anticoagulación. TEP no provocado → mínimo 3 meses, evaluar extensión indefinida según riesgo-beneficio. TEP con cáncer activo → HBPM o NACO oncológico indefinido."
                },
                "end_recidiva": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La paciente reingresó a los 6 semanas con TEP masivo bilateral y shock obstructivo. Requirió trombolisis de urgencia y UCI. La suspensión prematura de anticoagulación fue la causa directa de la recurrencia.",
                    "pearl": "Perla clínica: La tasa de recurrencia de TEP sin anticoagulación completa es del 40% en el primer año. El riesgo es máximo en los primeros 3-6 meses. Nunca suspender antes del tiempo mínimo recomendado."
                },
                "end_trombolisis_exceso": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La trombolisis causó hemorragia en el sitio quirúrgico (cadera) que requirió reintervención. La paciente resolvió el TEP pero con una complicación hemorrágica mayor evitable. La estabilidad hemodinámica contraindicaba la trombolisis.",
                    "pearl": "Perla clínica: Indicaciones de trombolisis en TEP: shock cardiogénico (TA <90 sostenida) O paro cardíaco. En TEP submasivo (disfunción VD sin shock), la trombolisis no reduce mortalidad pero sí aumenta sangrado — no está recomendada de rutina."
                },
                "end_filtro_mal": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El filtro de VCI no trató el TEP existente. La paciente siguió deteriorándose. Se debió agregar anticoagulación igual. El filtro generó un cuerpo extraño innecesario con riesgo de trombosis del filtro a largo plazo.",
                    "pearl": "Perla clínica: El filtro de VCI NO es tratamiento del TEP. Su única indicación es prevenir nuevos émbolos cuando la anticoagulación está contraindicada (cirugía inminente, hemorragia activa, trombocitopenia severa)."
                },
                "end_dimero_innecesario": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El tiempo perdido con el dímero permitió que el TEP progresara. La paciente presentó deterioro hemodinámico mientras esperaba resultados. La TCAP tardó 90 minutos adicionales. El diagnóstico correcto fue tardío.",
                    "pearl": "Perla clínica: Algoritmo TEP — Wells BAJO + dímero negativo = descartado. Wells MODERADO + dímero negativo = descartado. Wells ALTO = TCAP directo, el dímero no modifica la conducta."
                },
                "end_anticoag_sin_dx": {
                    "terminal": True,
                    "result": "warning",
                    "description": "Se anticoaguló sin diagnóstico confirmado. Resultó ser TEP (correcto clínicamente), pero la decisión fue metodológicamente incorrecta. En otro paciente con dímero elevado por otra causa, hubiera anticoagulado innecesariamente.",
                    "pearl": "Perla clínica: La probabilidad clínica alta no autoriza a omitir el estudio confirmatorio salvo en contextos muy específicos (shock + sospecha de TEP masivo sin tiempo para imagen). En paciente estable, siempre confirmar con TCAP."
                },
                "end_broncoespasmo_mal": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La paciente fue dada de alta con diagnóstico de broncoespasmo. Regresó 8 horas después en paro cardiorrespiratorio por TEP masivo. El error de no considerar el TEP en una paciente de alto riesgo fue fatal.",
                    "pearl": "Perla clínica: Todo paciente postquirúrgico con disnea brusca + taquicardia + hipoxemia = TEP hasta demostrar lo contrario. La RxTx normal NO descarta TEP. El 40% de los TEP tienen RxTx absolutamente normal."
                }
            }
        }
    },
    {
        "id": "shock-septico",
        "name": "Shock Séptico",
        "system": "Infeccioso",
        "difficulty": "Avanzado",
        "summary": "Disfunción orgánica potencialmente fatal causada por una respuesta desregulada del huésped a la infección, con hipotensión persistente a pesar de resucitación con fluidos.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 72 años con DM2 e HTA. Traído por familiares por confusión aguda, fiebre de 39.8°C y escalofríos desde hace 6 horas. Antecedente de disuria los últimos 3 días. TA 82/50 mmHg, FC 124 lpm, FR 26 rpm, SatO2 93%, temperatura 39.5°C. Glasgow 13. ¿Cuál es tu primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Hemocultivos x2 + urocultivo + lactato sérico + antibióticos en la primera hora",
                            "correct": True,
                            "feedback": "Correcto. El bundle de la primera hora en sepsis incluye: medir lactato, hemocultivos ANTES del antibiótico, y administrar antibiótico de amplio espectro dentro de la hora. Cada hora de demora aumenta la mortalidad un 7%.",
                            "next": "n2_cultivos"
                        },
                        {
                            "id": "b",
                            "text": "Esperar resultado del urocultivo para elegir el antibiótico correcto",
                            "correct": False,
                            "feedback": "Fatal error. En shock séptico, los cultivos toman 24-72h. Esperar es inaceptable — el antibiótico empírico de amplio espectro debe iniciarse dentro de la primera hora. Los cultivos se toman ANTES del antibiótico, no se espera su resultado.",
                            "next": "n2_espera"
                        },
                        {
                            "id": "c",
                            "text": "Corticoides IV para controlar la respuesta inflamatoria",
                            "correct": False,
                            "feedback": "Incorrecto como primera acción. Los corticoides (hidrocortisona) se reservan para shock refractario a vasopresores. Antes se necesita antibiótico, cultivos, lactato y resucitación con fluidos.",
                            "next": "end_cortico_precoz"
                        }
                    ]
                },
                "n2_cultivos": {
                    "description": "Hemocultivos tomados, urocultivo enviado, lactato: 4.8 mmol/L (hiperlactatemia severa). Piperacilina-tazobactam iniciada. TA persiste 80/48 mmHg. ¿Cuál es el siguiente paso en resucitación?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Bolo de SF 30 mL/kg IV rápido + norepinefrina si no responde a fluidos",
                            "correct": True,
                            "feedback": "Correcto. La guía Surviving Sepsis recomienda 30 mL/kg de cristaloide en las primeras 3h. Si no se logra TA media >65 mmHg, iniciar norepinefrina (vasopresor de primera línea en sepsis).",
                            "next": "n3_reanimacion"
                        },
                        {
                            "id": "b",
                            "text": "Furosemida IV — el paciente puede hacer edema pulmonar con tantos líquidos",
                            "correct": False,
                            "feedback": "Incorrecto. En shock distributivo séptico con hipotensión e hipoperfusión, el diurético está contraindicado. La prioridad es restaurar la precarga. El edema pulmonar es una complicación tardía, no la preocupación inmediata.",
                            "next": "end_diuretico_shock"
                        },
                        {
                            "id": "c",
                            "text": "Transfusión de sangre — lactato alto implica anemia severa",
                            "correct": False,
                            "feedback": "Incorrecto. El lactato elevado en sepsis refleja hipoperfusión tisular, no necesariamente anemia. La transfusión se indica con Hb <7 g/dL en sepsis estabilizada, no como primera medida de resucitación.",
                            "next": "end_transfusion_mal"
                        }
                    ]
                },
                "n2_espera": {
                    "description": "Han pasado 3 horas esperando el urocultivo. El paciente se deteriora: TA 70/40 mmHg, Glasgow 10, anuria. Lactato ahora 7.2 mmol/L. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Antibiótico de amplio espectro AHORA + resucitación agresiva",
                            "correct": True,
                            "feedback": "Correcto pero tardío. Tres horas de demora en sepsis equivalen a una mortalidad significativamente mayor. El antibiótico debía haberse dado en la primera hora. Ahora el daño orgánico ya está establecido.",
                            "next": "n3_reanimacion_tardio"
                        },
                        {
                            "id": "b",
                            "text": "Esperar aún — el cultivo debe estar por llegar",
                            "correct": False,
                            "feedback": "Inaceptable. Con TA 70, Glasgow 10 y lactato 7.2, el paciente está en shock séptico descompensado con falla multiorgánica inminente. Cada minuto sin antibiótico aumenta la mortalidad.",
                            "next": "end_muerte_sepsis"
                        }
                    ]
                },
                "n3_reanimacion": {
                    "description": "Post-bolo 2L SF: TA 94/62 mmHg, FC 108, diuresis 30 mL/h. Lactato de control a las 2h: 2.9 mmol/L (mejoró). El urocultivo reporta E. coli sensible a quinolonas y cefalosporinas. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Continuar pip-tazo, ingresar a UCI, control de foco (ecografía renal), repetir lactato",
                            "correct": True,
                            "feedback": "Correcto. La mejora del lactato (clearance >10% en 2h) es un buen signo. Se debe continuar el antibiótico, buscar el foco (posible absceso perinéfrico), y monitorizar en UCI. El antibiótico se ajustará según antibiograma en 24-48h.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Retirar norepinefrina — la TA mejoró con fluidos",
                            "correct": False,
                            "feedback": "Prematuro si se había iniciado. Pero más importante: no se debe retirar el vasopresor hasta confirmar estabilidad hemodinámica sostenida y clearance de lactato adecuado. La mejora inicial puede ser transitoria.",
                            "next": "end_recaida_sepsis"
                        }
                    ]
                },
                "n3_reanimacion_tardio": {
                    "description": "Se inicia antibiótico con 3h de retraso. Post-resucitación: TA 88/55 mmHg con norepinefrina a dosis altas. Oliguria. Creatinina 3.2 mg/dL (basal 0.9). Lactato 5.1 mmol/L. ¿Qué agregas?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Hidrocortisona IV 200 mg/día — shock refractario a vasopresores",
                            "correct": True,
                            "feedback": "Correcto. La hidrocortisona está indicada en shock séptico refractario (norepinefrina >0.25 mcg/kg/min). Mejora la vasoplejia y puede reducir la duración del shock, aunque no reduce mortalidad claramente.",
                            "next": "end_tardio_complicado"
                        },
                        {
                            "id": "b",
                            "text": "Más fluidos — el lactato sigue alto",
                            "correct": False,
                            "feedback": "Incorrecto. Con norepinefrina a dosis altas y oliguria, agregar más fluidos puede causar sobrecarga e impactar negativamente en la mortalidad. La fluidoterapia liberal en sepsis establecida se asocia a peor pronóstico.",
                            "next": "end_fluidos_exceso"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Bundle de 1 hora cumplido: cultivos + lactato + antibiótico + fluidos. Respuesta hemodinámica adecuada. El cultivo confirmó E. coli sensible. A las 48h se rotó a ceftriaxona IV según antibiograma. Alta de UCI al 5to día, sin secuelas orgánicas.",
                    "pearl": "Perla clínica: El bundle de la primera hora en sepsis (Surviving Sepsis Campaign): 1) Lactato sérico, 2) Hemocultivos antes del antibiótico, 3) Antibiótico de amplio espectro, 4) 30 mL/kg de cristaloide si hipotensión o lactato >4. Cada hora de demora aumenta mortalidad 7%."
                },
                "end_recaida_sepsis": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El retiro prematuro del vasopresor causó hipotensión de rebote. Se debió reiniciar norepinefrina. El paciente tuvo una estadía en UCI más prolongada pero finalmente se recuperó. El retiro de vasopresores requiere destete gradual con monitoreo estrecho.",
                    "pearl": "Perla clínica: El destete de vasopresores en sepsis se hace cuando: TA media >65 mmHg estable, lactato normalizado, diuresis >0.5 mL/kg/h y signos de perfusión adecuada. Nunca retiro brusco."
                },
                "end_tardio_complicado": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El shock fue controlado con hidrocortisona y soporte intensivo. Sin embargo, el retraso de 3h en el antibiótico causó falla renal aguda que requirió diálisis transitoria. Alta de UCI al día 12 con función renal recuperada parcialmente.",
                    "pearl": "Perla clínica: La falla renal aguda ocurre en el 40-50% de los shocks sépticos. La principal medida preventiva es el antibiótico precoz y la resucitación hemodinámica temprana. El retraso en ambas medidas duplica el riesgo de lesión renal permanente."
                },
                "end_cortico_precoz": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Sin antibiótico ni resucitación, los corticoides solos no pudieron revertir el shock. El paciente progresó a falla multiorgánica. La inmunosupresión relativa de los corticoides puede agravar la sepsis no tratada con antibióticos.",
                    "pearl": "Perla clínica: Los corticoides en sepsis son adyuvantes, no tratamiento principal. La secuencia correcta es: antibiótico + fluidos + vasopresores. Los corticoides se agregan SOLO si el shock es refractario a vasopresores a dosis adecuadas."
                },
                "end_diuretico_shock": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El furosemida empeoró la hipoperfusión renal y cerebral. El paciente presentó anuria y deterioro del sensorio. La reducción de la precarga con shock distributivo activo causó colapso hemodinámico.",
                    "pearl": "Perla clínica: Shock distributivo + diuréticos = combinación mortal. El edema en sepsis es por aumento de permeabilidad capilar, no por sobrecarga hídrica. Los diuréticos se usan en la fase de desescalada, nunca en la fase aguda de shock."
                },
                "end_transfusion_mal": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La Hb era 10.2 g/dL — la transfusión no estaba indicada y no mejoró la hipoperfusión. Se perdió tiempo valioso sin iniciar resucitación con cristaloides ni vasopresores. El lactato siguió subiendo.",
                    "pearl": "Perla clínica: En sepsis, el umbral transfusional es Hb <7 g/dL (o <8-9 en cardiopatía isquémica). El lactato elevado no es indicación de transfusión — es indicación de resucitación con fluidos y vasopresores."
                },
                "end_muerte_sepsis": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente presentó paro cardiorrespiratorio por shock séptico refractario. El retraso de 5 horas en el antibiótico fue el factor determinante. La mortalidad del shock séptico con antibiótico tardío supera el 50%.",
                    "pearl": "Perla clínica: La sepsis no es una emergencia diagnóstica — es una emergencia terapéutica. No hay que esperar un diagnóstico confirmado para iniciar el antibiótico. La sospecha clínica + disfunción orgánica = actuar."
                },
                "end_fluidos_exceso": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La sobrecarga de fluidos causó edema pulmonar agudo. El paciente requirió ventilación mecánica invasiva. Balance positivo acumulado de 8L en 24h se asocia a mortalidad significativamente mayor en UCI.",
                    "pearl": "Perla clínica: La fluidoterapia en sepsis tiene dos fases: Resucitación (primeras 3-6h, 30 mL/kg) y Desescalada (balance cero o negativo posterior). Más fluidos después de la resucitación inicial es perjudicial."
                }
            }
        }
    },
    {
        "id": "insuficiencia-cardiaca-aguda",
        "name": "Insuficiencia Cardíaca Aguda Descompensada",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "summary": "Aparición rápida de síntomas y signos de IC que requiere evaluación urgente y tratamiento inmediato. Causa más frecuente de hospitalización en mayores de 65 años.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 70 años con IC crónica con FE reducida (FE 30%) en tratamiento habitual con enalapril, carvedilol y furosemida oral. Consulta por disnea progresiva en las últimas 48h, ortopnea, disnea paroxística nocturna. Examen: SatO2 88%, TA 158/96 mmHg, FC 102 lpm, crepitantes bibasales, edema de miembros inferiores 3+. ¿Cuál es el manejo inicial?",
                    "options": [
                        {
                            "id": "a",
                            "text": "O2 + furosemida IV 40-80mg + monitoreo hemodinámico",
                            "correct": True,
                            "feedback": "Correcto. En ICAD con congestión pulmonar: O2 para corregir hipoxemia, furosemida IV (el doble de la dosis oral habitual) para aliviar la congestión, y monitoreo continuo. La TA elevada favorece el uso de nitratos si no hay respuesta.",
                            "next": "n2_diuretico"
                        },
                        {
                            "id": "b",
                            "text": "Cristaloides IV 500 mL — puede estar deshidratado por el diurético",
                            "correct": False,
                            "feedback": "Incorrecto. La clínica es de sobrecarga hídrica (crepitantes, edema 3+, SatO2 88%). Los fluidos IV en este contexto empeorarán el edema pulmonar y la hipoxemia. El paciente necesita diuresis, no fluidos.",
                            "next": "end_liquidos_ic"
                        },
                        {
                            "id": "c",
                            "text": "Solo O2 y observar evolución durante 4 horas",
                            "correct": False,
                            "feedback": "Insuficiente. El O2 corrige parcialmente la hipoxemia pero no trata la causa (congestión). Sin diurético, el paciente seguirá acumulando fluidos y puede requerir ventilación mecánica.",
                            "next": "end_solo_o2"
                        }
                    ]
                },
                "n2_diuretico": {
                    "description": "A las 2h post-furosemida IV: diuresis 900 mL, SatO2 94%, persiste disnea al mínimo esfuerzo, crepitantes en 1/3 inferior bilateral. TA 152/88 mmHg. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Segunda dosis de furosemida IV + agregar nitratos sublinguales por la TA elevada",
                            "correct": True,
                            "feedback": "Correcto. La respuesta parcial al diurético indica que se necesita más. Los nitratos reducen la precarga y poscarga, y son especialmente útiles en ICAD hipertensiva (TA >140). Combinados con diurético, mejoran la congestión más rápido.",
                            "next": "n3_respuesta"
                        },
                        {
                            "id": "b",
                            "text": "Alta con doble dosis de furosemida oral — mejoró la SatO2",
                            "correct": False,
                            "feedback": "Prematuro. SatO2 94% con crepitantes persistentes y disnea de reposo no es criterio de alta. El paciente sigue con congestión significativa. El alta precoz en ICAD se asocia a rehospitalización a los 30 días.",
                            "next": "end_alta_precoz_ic"
                        },
                        {
                            "id": "c",
                            "text": "Intubar y ventilar mecánicamente — SatO2 insuficiente",
                            "correct": False,
                            "feedback": "Excesivo. SatO2 94% con O2 y paciente alerta no es criterio de VMI. La VMI tiene mortalidad significativa en IC. El siguiente paso es optimizar el tratamiento médico; si hay falla, usar VNI antes de la intubación.",
                            "next": "end_vmi_prematuro"
                        }
                    ]
                },
                "n3_respuesta": {
                    "description": "A las 6h: diuresis total 2.2L, SatO2 97% con cánula nasal 2L/min, disnea leve en reposo, crepitantes mínimos. TA 135/82 mmHg, FC 88 lpm. Troponina levemente elevada (daño miocárdico por estrés). ¿Cuál es el plan?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Hospitalización, transición a furosemida oral, optimizar IECA y betabloqueante, ecocardiograma",
                            "correct": True,
                            "feedback": "Correcto. La mejoría clínica es buena señal pero el paciente aún no está listo para el alta. Se necesita estabilización con medicación oral, identificar el factor desencadenante (abandono de tratamiento, arritmia, infección) y optimizar la terapia modificadora.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Alta inmediata — ya está compensado",
                            "correct": False,
                            "feedback": "Prematuro. El paciente estuvo en edema pulmonar hace 6 horas. Necesita al menos 24-48h de observación para confirmar estabilidad, identificar el desencadenante y ajustar la medicación oral antes del alta segura.",
                            "next": "end_alta_precoz2_ic"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Manejo correcto: diurético IV + nitratos en ICAD hipertensiva + hospitalización + optimización del tratamiento. El factor desencadenante fue abandono de furosemida por 5 días. Alta al 3er día con educación sobre adherencia, peso diario y signos de alarma. Control cardiológico en 1 semana.",
                    "pearl": "Perla clínica: El 50% de las descompensaciones de IC tienen un factor desencadenante identificable: transgresión dietética (sal), abandono de medicación, infección, arritmia (FA), isquemia o fármacos (AINEs, calcioantagonistas no dihidropiridínicos)."
                },
                "end_liquidos_ic": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Los cristaloides IV agravaron el edema pulmonar. SatO2 cayó a 82%, requirió VNI y luego intubación. Estadía en UCI de 5 días. El error de confundir sobrecarga hídrica con deshidratación fue crítico.",
                    "pearl": "Perla clínica: En IC descompensada, el perfil hemodinámico más común es 'húmedo y caliente' (congestión + perfusión preservada). Los fluidos están indicados solo en el perfil 'seco y frío' (bajo gasto + ausencia de congestión), que es mucho menos frecuente."
                },
                "end_solo_o2": {
                    "terminal": True,
                    "result": "warning",
                    "description": "Sin diurético, la congestión progresó. A las 4h SatO2 85%, requirió VNI. El O2 sin tratamiento de la causa subyacente solo retrasa el deterioro inevitable. El diurético IV debía haberse iniciado desde el primer momento.",
                    "pearl": "Perla clínica: En ICAD con congestión pulmonar, el diurético IV es el tratamiento central. La furosemida IV tiene efecto vasodilatador venoso inmediato (antes del efecto diurético), aliviando la precarga en minutos."
                },
                "end_alta_precoz_ic": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente reingresó a las 48h en edema agudo de pulmón. Las rehospitalizaciones a 30 días en IC son un indicador de calidad. La TA >150 y los crepitantes persistentes al alta son predictores de reingreso.",
                    "pearl": "Perla clínica: Criterios de alta segura en ICAD: SatO2 >94% con aire ambiente, PA estable, diuresis adecuada con medicación oral, sin signos de congestión, paciente capaz de monitorear su peso y con seguimiento asegurado en 7 días."
                },
                "end_alta_precoz2_ic": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El alta precoz resultó en reingreso a las 72h. Sin identificar el desencadenante (abandono de furosemida) ni ajustar el tratamiento, el paciente repitió el cuadro. Tasa de rehospitalización a 30 días del 25% en IC descompensada.",
                    "pearl": "Perla clínica: Antes del alta en IC: identificar y tratar el desencadenante, optimizar medicación modificadora (IECA/sacubitrilo-valsartán + betabloqueante + espironolactona + dapagliflozina), educar en dieta y monitoreo de peso diario."
                },
                "end_vmi_prematuro": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La intubación fue innecesaria en este contexto. El paciente desarrolló neumonía asociada al ventilador. La VMI en IC tiene mortalidad inherente. La VNI (CPAP/BiPAP) es el puente correcto cuando el tratamiento médico es insuficiente y antes de la intubación.",
                    "pearl": "Perla clínica: Escalada ventilatoria en ICAD: 1° O2 por cánula/mascarilla, 2° VNI (CPAP reduce precarga y mejora oxigenación en edema pulmonar), 3° VMI solo si VNI falla o hay apnea/deterioro de conciencia."
                }
            }
        }
    },
    {
        "id": "hemorragia-digestiva-alta",
        "name": "Hemorragia Digestiva Alta",
        "system": "Digestivo",
        "difficulty": "Intermedio",
        "summary": "Sangrado proximal al ángulo de Treitz. Las causas más frecuentes son la úlcera péptica y las várices esofágicas. La estabilización hemodinámica precede siempre a la endoscopia.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 45 años, consumidor de AINEs por lumbalgia crónica. Consulta por 2 episodios de hematemesis con coágulos en las últimas 4 horas y deposiciones melénicas. TA 88/55 mmHg, FC 122 lpm, FR 20 rpm, palidez marcada, Hb 7.1 g/dL. ¿Cuál es tu primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Dos vías periféricas calibre 18 + expansión con cristaloides + score de Glasgow-Blatchford",
                            "correct": True,
                            "feedback": "Correcto. El paciente está en shock hipovolémico (TA 88, FC 122). La prioridad es el acceso vascular y la resucitación. El score de Glasgow-Blatchford estratifica el riesgo y guía la urgencia de la endoscopia.",
                            "next": "n2_estabilizacion"
                        },
                        {
                            "id": "b",
                            "text": "Endoscopia digestiva alta urgente de inmediato",
                            "correct": False,
                            "feedback": "Incorrecto con paciente inestable. La endoscopia en un paciente con TA 88 y FC 122 es peligrosa: riesgo de broncoaspiración y deterioro hemodinámico durante el procedimiento. Primero estabilizar, luego endoscopiar.",
                            "next": "end_endoscopia_inestable"
                        },
                        {
                            "id": "c",
                            "text": "IBP en infusión continua IV y observar",
                            "correct": False,
                            "feedback": "Insuficiente. Los IBP son parte del tratamiento pero no resuelven el shock hipovolémico. Sin acceso vascular y expansión, el paciente puede entrar en paro por hipoperfusión.",
                            "next": "end_solo_ibp"
                        }
                    ]
                },
                "n2_estabilizacion": {
                    "description": "Post-expansión 1.5L SF: TA 104/68 mmHg, FC 98 lpm. Glasgow-Blatchford: 12 (alto riesgo). IBP en infusión continua iniciado. Hb 7.1 g/dL. El paciente está más estable. ¿Cuál es el siguiente paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Endoscopia digestiva alta dentro de las primeras 24h (idealmente antes de 12h en alto riesgo)",
                            "correct": True,
                            "feedback": "Correcto. Con paciente estabilizado y Glasgow-Blatchford alto, la endoscopia debe realizarse dentro de las 24h (idealmente <12h en alto riesgo). Permite diagnóstico y hemostasia simultánea.",
                            "next": "n3_endoscopia"
                        },
                        {
                            "id": "b",
                            "text": "Transfundir hasta Hb >10 g/dL antes de la endoscopia",
                            "correct": False,
                            "feedback": "Incorrecto. En HDA, el objetivo transfusional es Hb >7-8 g/dL (no >10). La transfusión liberal en HDA por varices aumenta la mortalidad. Transfundir restrictivamente y no demorar la endoscopia por esperar una Hb arbitraria.",
                            "next": "end_transfusion_liberal"
                        }
                    ]
                },
                "n3_endoscopia": {
                    "description": "La endoscopia muestra úlcera duodenal de 1.5cm con sangrado activo en chorro (Forrest Ia). No hay varices. ¿Cuál es la conducta endoscópica?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Hemostasia combinada: inyección de adrenalina + clip hemostático o coagulación térmica",
                            "correct": True,
                            "feedback": "Correcto. La hemostasia combinada (adrenalina + método mecánico o térmico) es superior a la monoterapia para Forrest Ia. La adrenalina sola tiene alta tasa de resangrado. El clip o la coagulación aseguran hemostasia definitiva.",
                            "next": "n4_post_endoscopia"
                        },
                        {
                            "id": "b",
                            "text": "Solo inyección de adrenalina perilesional",
                            "correct": False,
                            "feedback": "Insuficiente para Forrest Ia. La adrenalina en monoterapia tiene tasa de resangrado del 15-20%. Las guías recomiendan siempre combinar con clip o método térmico en sangrado activo.",
                            "next": "end_adrenalina_sola"
                        },
                        {
                            "id": "c",
                            "text": "Cirugía directa — la úlcera es grande",
                            "correct": False,
                            "feedback": "Incorrecto. La cirugía se reserva para falla de la hemostasia endoscópica (después del segundo intento) o inestabilidad hemodinámica que no responde a resucitación. La endoscopia tiene éxito primario en >90% de los casos.",
                            "next": "end_cirugia_precoz_hda"
                        }
                    ]
                },
                "n4_post_endoscopia": {
                    "description": "Hemostasia endoscópica exitosa. Sin sangrado activo al finalizar. ¿Cuál es el manejo post-endoscópico?",
                    "options": [
                        {
                            "id": "a",
                            "text": "IBP IV en infusión continua 72h + suspender AINEs + H. pylori en muestra de biopsia",
                            "correct": True,
                            "feedback": "Correcto. Post-hemostasia en úlcera de alto riesgo: IBP IV 72h reduce resangrado (NNT=13). Suspender AINEs es mandatorio. La biopsia para H. pylori identifica la causa tratable más importante de úlcera péptica.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Alta al día siguiente con IBP oral — la hemostasia fue exitosa",
                            "correct": False,
                            "feedback": "Prematuro para Forrest Ia. El resangrado ocurre en las primeras 72h en el 20% de úlceras de alto riesgo. Las guías recomiendan IBP IV continuo las primeras 72h y observación hospitalaria mínimo 3 días.",
                            "next": "end_alta_precoz_hda"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Manejo ejemplar: estabilización hemodinámica → endoscopia oportuna → hemostasia combinada → IBP IV 72h → biopsia para H. pylori (positivo, erradicado con triple terapia). Sin resangrado. Alta al 4to día con IBP oral 8 semanas y suspensión definitiva de AINEs.",
                    "pearl": "Perla clínica: El H. pylori se encuentra en el 70-90% de las úlceras duodenales. Su erradicación reduce la recurrencia del 70% al 5% a 1 año. Siempre biopsiar antro y cuerpo en endoscopia por HDA, y tratar si es positivo."
                },
                "end_endoscopia_inestable": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente broncoaspiró durante la sedación para endoscopia. Requirió intubación de urgencia y UCI. La endoscopia en paciente hemodinámicamente inestable tiene mortalidad procedimental significativa.",
                    "pearl": "Perla clínica: Criterios de estabilidad pre-endoscopia en HDA: TA sistólica >100 mmHg, FC <100 lpm, SatO2 adecuada y paciente cooperador. Si no se cumplen, primero resucitar. La endoscopia de urgencia (<6h) solo se considera en sangrado masivo con inestabilidad refractaria a resucitación."
                },
                "end_solo_ibp": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Sin acceso vascular ni expansión, el paciente entró en shock descompensado. La Hb cayó a 5.2 g/dL. Requirió reanimación agresiva y transfusión masiva. Los IBP no tratan el shock hipovolémico.",
                    "pearl": "Perla clínica: En HDA con inestabilidad hemodinámica: la reanimación es la prioridad absoluta. Los IBP son complemento, no tratamiento del shock. La mortalidad de la HDA es del 3-14% y depende principalmente de la velocidad de estabilización."
                },
                "end_transfusion_liberal": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La transfusión hasta Hb 10 retrasó la endoscopia 4h. El paciente presentó resangrado mientras esperaba, requiriendo endoscopia de urgencia en condiciones subóptimas. La transfusión liberal también aumenta el riesgo en sangrado variceal.",
                    "pearl": "Perla clínica: Estrategia transfusional restrictiva en HDA: Hb umbral 7 g/dL (8 en cardiopatía isquémica). Los estudios muestran mejor sobrevida con estrategia restrictiva vs liberal en HDA, especialmente en sangrado variceal por cirrosis."
                },
                "end_adrenalina_sola": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El paciente presentó resangrado a las 36h. Requirió segunda endoscopia de rescate con clip. La hemostasia combinada desde el inicio hubiera reducido este riesgo significativamente.",
                    "pearl": "Perla clínica: Forrest Ia (sangrado activo en chorro) y Ib (sangrado en babeo) requieren hemostasia combinada. Forrest IIa (vaso visible sin sangrado) también. Solo Forrest IIb (coágulo adherido) puede manejarse con solo IBP IV sin hemostasia endoscópica."
                },
                "end_cirugia_precoz_hda": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La cirugía fue exitosa pero con mayor morbilidad que la endoscopia. El riesgo de dehiscencia, infección y íleo prolongado es significativamente mayor que con hemostasia endoscópica. La cirugía es el rescate, no el primer paso.",
                    "pearl": "Perla clínica: Indicaciones de cirugía en HDA: falla de dos intentos de hemostasia endoscópica, inestabilidad hemodinámica refractaria o resangrado masivo. La embolización angiográfica es una alternativa intermedia entre endoscopia y cirugía."
                },
                "end_alta_precoz_hda": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El resangrado ocurrió a las 48h fuera del hospital. El paciente llegó en shock hemorrágico. Para úlcera Forrest Ia, las guías recomiendan mínimo 72h de observación e IBP IV. El alta precoz fue un error de protocolo.",
                    "pearl": "Perla clínica: Criterios de alta segura en HDA: ausencia de resangrado, tolerancia oral, Hb estable, Forrest IIc o III en la endoscopia. Para Forrest Ia/Ib/IIa, mínimo 72h hospitalizado con IBP IV en infusión continua (80 mg bolo + 8 mg/h)."
                }
            }
        }
    },
    {
        "id": "meningitis-bacteriana",
        "name": "Meningitis Bacteriana",
        "system": "Neurológico",
        "difficulty": "Avanzado",
        "summary": "Infección bacteriana de las meninges con alta mortalidad y morbilidad neurológica. El diagnóstico y tratamiento antibiótico precoz son determinantes del pronóstico.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 20 años universitario. Lo traen sus compañeros por fiebre de 40°C de inicio brusco hace 8 horas, cefalea intensa ('la peor de su vida'), rigidez de nuca, fotofobia y petequias en tronco y extremidades. Glasgow 13. FC 118, TA 105/68. ¿Cuál es tu primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Antibiótico IV de inmediato + dexametasona, luego TC y punción lumbar",
                            "correct": True,
                            "feedback": "Correcto. En meningitis bacteriana con presentación fulminante (petequias, deterioro neurológico, sepsis), el antibiótico NO puede esperar imagen ni PL. Cada hora de demora aumenta la mortalidad en un 10%. TC y PL se hacen después del antibiótico.",
                            "next": "n2_antibiotico_primero"
                        },
                        {
                            "id": "b",
                            "text": "TC de cráneo primero para descartar hipertensión endocraneana antes de la PL",
                            "correct": False,
                            "feedback": "Error crítico de tiempo. La TC tarda 30-90 minutos. En meningitis bacteriana fulminante, ese retraso puede ser mortal. La TC es necesaria antes de la PL, pero el antibiótico no puede esperar a la TC — se inicia antes.",
                            "next": "n2_tc_primero"
                        },
                        {
                            "id": "c",
                            "text": "Punción lumbar de inmediato para diagnóstico definitivo",
                            "correct": False,
                            "feedback": "Peligroso sin TC previa en este paciente. El deterioro neurológico (Glasgow 13) puede indicar HTE — la PL sin TC puede causar herniación cerebral. Además, las petequias sugieren meningococo: el antibiótico no puede esperar.",
                            "next": "end_pl_sin_tc"
                        }
                    ]
                },
                "n2_antibiotico_primero": {
                    "description": "Ceftriaxona 2g IV + dexametasona 0.15 mg/kg IV iniciados. TC: normal, sin signos de HTE. PL realizada: LCR turbio, presión de apertura elevada, PMN 3800/mm³, glucosa 18 mg/dL, proteínas 420 mg/dL, Gram: diplococos gram negativos. Compatible con N. meningitidis. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Continuar ceftriaxona 7 días + dexametasona 4 días + notificación epidemiológica + profilaxis a contactos",
                            "correct": True,
                            "feedback": "Correcto. N. meningitidis es sensible a ceftriaxona (7 días). La dexametasona reduce complicaciones neurológicas (sordera, secuelas) cuando se inicia con o antes del antibiótico. La notificación y profilaxis con rifampicina/ciprofloxacino a contactos cercanos es obligatoria.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Cambiar a amoxicilina oral a los 3 días si el paciente mejora clínicamente",
                            "correct": False,
                            "feedback": "Incorrecto. La meningitis bacteriana requiere antibiótico IV durante todo el tratamiento (7-14 días según germen). El cambio precoz a vía oral no alcanza concentraciones adecuadas en LCR y tiene alta tasa de fracaso.",
                            "next": "end_cambio_oral_precoz"
                        }
                    ]
                },
                "n2_tc_primero": {
                    "description": "La TC tardó 75 minutos. Normal. Durante ese tiempo el paciente deterioró: Glasgow 9, nueva petequias en coalescencia (púrpura fulminante). TA 88/52 mmHg. ¿Qué haces ahora?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Antibiótico IV INMEDIATO + resucitación + ingreso UCI — omitir PL por inestabilidad",
                            "correct": True,
                            "feedback": "Correcto aunque tardío. Con shock séptico y deterioro neurológico severo, la PL ya no es segura ni cambiará el manejo. El antibiótico empírico cubre los gérmenes más probables. El diagnóstico microbiológico puede obtenerse de hemocultivos.",
                            "next": "end_tardio_meningitis"
                        },
                        {
                            "id": "b",
                            "text": "Hacer la PL ahora que la TC fue normal",
                            "correct": False,
                            "feedback": "Con shock séptico, Glasgow 9 y coagulopatía por púrpura fulminante, la PL está contraindicada. El antibiótico lleva 75 minutos de retraso. Cada minuto adicional empeora el pronóstico.",
                            "next": "end_muerte_meningitis"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Antibiótico precoz (antes de TC y PL), dexametasona, diagnóstico por PL y manejo completo con profilaxis de contactos. El paciente fue dado de alta al día 10 sin secuelas neurológicas. La velocidad de acción fue el factor determinante.",
                    "pearl": "Perla clínica: Tríada de Kernig + Brudzinski + fiebre tiene especificidad del 95% para meningitis. Pero su ausencia no descarta. En meningitis bacteriana: antibiótico en los primeros 30-60 minutos desde el ingreso, sin importar si la PL o TC están pendientes."
                },
                "end_tardio_meningitis": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El antibiótico llegó 75 minutos tarde. El paciente sobrevivió pero con sordera neurosensorial bilateral y secuela cognitiva leve. La dexametasona iniciada con el antibiótico (aunque tardía) redujo algo la inflamación. Las petequias en coalescencia son un marcador de mal pronóstico.",
                    "pearl": "Perla clínica: La meningococcemia con púrpura fulminante tiene mortalidad del 20-40% incluso con tratamiento óptimo. La velocidad de inicio del antibiótico es el único factor modificable. Cada 1h de retraso = 10% más de mortalidad."
                },
                "end_cambio_oral_precoz": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El cambio a amoxicilina oral causó recaída de la meningitis al 5to día. Los niveles de antibiótico en LCR con vía oral son insuficientes. Requirió reinicio de ceftriaxona IV y 14 días adicionales de tratamiento. Secuela auditiva.",
                    "pearl": "Perla clínica: Los antibióticos para meningitis deben penetrar la barrera hematoencefálica. Ceftriaxona y penicilina IV alcanzan concentraciones bactericidas en LCR. Los antibióticos orales, incluso en dosis altas, son insuficientes para tratar meningitis bacteriana establecida."
                },
                "end_pl_sin_tc": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La PL causó herniación uncal. El paciente presentó deterioro brusco a Glasgow 6 con midriasis arreactiva derecha durante el procedimiento. Requirió intubación y manitol urgente. La regla es TC antes de PL cuando hay signos neurológicos focales o deterioro de conciencia.",
                    "pearl": "Perla clínica: Contraindicaciones de PL sin TC previa: Glasgow <13, déficit neurológico focal, convulsiones recientes, papiledema, inmunocompromiso. En estos casos: antibiótico → TC → PL (si TC normal). En meningitis típica sin estos factores, la PL puede hacerse sin TC previa."
                },
                "end_muerte_meningitis": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente falleció por shock séptico refractario con coagulación intravascular diseminada. 75 minutos sin antibiótico + púrpura fulminante + shock = pronóstico fatal. La meningococcemia fulminante puede matar en horas.",
                    "pearl": "Perla clínica: Meningococcemia + púrpura fulminante = emergencia máxima. Si hay sospecha en sala de espera: antibiótico IM/IV ANTES de que el médico lo evalúe formalmente. La velocidad supera cualquier protocolo diagnóstico."
                }
            }
        }
    },
    {
        "id": "pancreatitis-aguda",
        "name": "Pancreatitis Aguda",
        "system": "Digestivo",
        "difficulty": "Intermedio",
        "summary": "Inflamación aguda del páncreas con espectro clínico desde formas leves autolimitadas hasta necrosis infectada con falla multiorgánica. La hidratación precoz es el pilar del tratamiento.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente femenina de 38 años con antecedente de colelitiasis conocida (nunca operada). Consulta por dolor epigástrico intenso irradiado 'en faja' hacia el dorso, de 6 horas de evolución, acompañado de vómitos repetidos. No fiebre. Lipasa sérica: 1.840 UI/L (VN <60). Amilasa: 920 UI/L. ¿Cuál es tu manejo inicial?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Hidratación IV agresiva + analgesia + score BISAP + NPO inicial",
                            "correct": True,
                            "feedback": "Correcto. Los pilares iniciales en pancreatitis aguda son: hidratación agresiva con cristaloides (Ringer lactato es preferido sobre SF), analgesia adecuada, estratificación de severidad (BISAP, APACHE-II) y NPO transitorio.",
                            "next": "n2_severidad"
                        },
                        {
                            "id": "b",
                            "text": "CPRE urgente — probablemente es colelitiasis obstruyendo el colédoco",
                            "correct": False,
                            "feedback": "Incorrecto. La CPRE urgente se indica solo si hay colangitis aguda o ictericia obstructiva progresiva (cálculo en colédoco con obstrucción biliar). Una pancreatitis aguda por colelitiasis sin colangitis no requiere CPRE urgente.",
                            "next": "end_cpre_precoz"
                        },
                        {
                            "id": "c",
                            "text": "Antiespasmódico IM y alta con dieta blanda — el dolor ya cedió parcialmente",
                            "correct": False,
                            "feedback": "Peligroso. Lipasa >3 veces el límite normal con clínica típica confirma pancreatitis aguda. El alta sin estratificación de severidad puede exponer a complicaciones graves (necrosis, sepsis) que se desarrollan en las primeras 48-72h.",
                            "next": "end_alta_pancreatitis"
                        }
                    ]
                },
                "n2_severidad": {
                    "description": "BISAP: 1 punto (solo BUN levemente elevado). TAC abdominal con contraste: edema pancreático difuso, sin necrosis, sin colecciones. Criterios de Balthazar B. Pancreatitis aguda LEVE. Leucocitos 13.000. Sin fiebre. ¿Cuál es el manejo?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Hidratación IV 250 mL/h + analgesia + reinicio de dieta oral precoz (líquidos claros) cuando tolere",
                            "correct": True,
                            "feedback": "Correcto. En pancreatitis leve, la evidencia actual favorece el reinicio precoz de la dieta oral (dentro de las primeras 24-48h si tolera), lo que reduce la estadía hospitalaria. La nutrición parenteral total no está indicada en formas leves.",
                            "next": "n3_dieta"
                        },
                        {
                            "id": "b",
                            "text": "Nutrición parenteral total desde el inicio — el páncreas debe reposar completamente",
                            "correct": False,
                            "feedback": "Incorrecto y desactualizado. La NPT no reduce las complicaciones en pancreatitis leve y tiene sus propios riesgos (infección del catéter, hiperglucemia). El reposo pancreático no mejora el pronóstico en formas leves.",
                            "next": "end_npt_innecesaria"
                        },
                        {
                            "id": "c",
                            "text": "Antibióticos profilácticos para prevenir infección de la necrosis",
                            "correct": False,
                            "feedback": "Incorrecto. Los antibióticos profilácticos en pancreatitis aguda no están recomendados por ninguna guía actual (AGA, ACG, IAP). No reducen la infección de la necrosis ni la mortalidad. Solo se indican ante infección documentada.",
                            "next": "end_antibio_profilactico"
                        }
                    ]
                },
                "n3_dieta": {
                    "description": "A las 30 horas la paciente tolera líquidos claros sin aumento del dolor. Lipasa en descenso (680 UI/L). Sin fiebre. Dolor 2/10. ¿Cuál es el plan?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Progresar dieta a semiblanda + planificar colecistectomía laparoscópica en esta hospitalización o próximos 30 días",
                            "correct": True,
                            "feedback": "Correcto. La tolerancia oral es criterio de mejoría. La colecistectomía debe realizarse durante la misma hospitalización o dentro de las 4 semanas en pancreatitis leve por litiasis — previene recurrencia (riesgo del 25-30% sin cirugía).",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "NPO por 7 días más 'para asegurarse' que el páncreas descanse",
                            "correct": False,
                            "feedback": "Incorrecto. El ayuno prolongado innecesario deteriora el estado nutricional, favorece la atrofia de la mucosa intestinal, aumenta el riesgo de translocación bacteriana y prolonga la hospitalización sin beneficio.",
                            "next": "end_npo_prolongado"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Manejo óptimo: hidratación agresiva precoz, analgesia, dieta oral precoz al tolerar y planificación de colecistectomía. Alta al 3er día. Colecistectomía laparoscópica electiva a las 3 semanas sin complicaciones. Sin recurrencia de pancreatitis.",
                    "pearl": "Perla clínica: El 80% de las pancreatitis agudas son leves y autolimitadas. Los 2 pilares del tratamiento son la hidratación agresiva precoz (Ringer lactato 250-500 mL/h las primeras 12-24h) y la analgesia. La colecistectomía en la misma hospitalización reduce la recurrencia del 25% al 1%."
                },
                "end_cpre_precoz": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La CPRE sin obstrucción biliar documentada causó pancreatitis post-CPRE (complicación en el 3-5% de los procedimientos). La paciente tuvo dos pancreatitis simultáneas. La CPRE debe reservarse para colangitis o ictericia obstructiva confirmada.",
                    "pearl": "Perla clínica: Indicaciones de CPRE urgente (<24h) en pancreatitis aguda biliar: colangitis aguda (fiebre + ictericia + dolor = tríada de Charcot) o ictericia obstructiva persistente con evidencia de cálculo en colédoco. Sin estos criterios, la CPRE no está indicada."
                },
                "end_alta_pancreatitis": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La paciente regresó a las 36h con pancreatitis necrotizante infectada (BISAP 3) y falla orgánica. La severidad de la pancreatitis puede no ser evidente en las primeras horas — la estratificación y la observación hospitalaria son obligatorias.",
                    "pearl": "Perla clínica: El pico de severidad de la pancreatitis aguda ocurre en las primeras 48-72h. Una presentación inicial leve puede evolucionar a necrosis extensa. Todo paciente con pancreatitis confirmada debe hospitalizarse para monitoreo mínimo 24-48h."
                },
                "end_npt_innecesaria": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La NPT fue innecesaria e introdujo riesgos adicionales: el catéter venoso central se infectó al 4to día (Candida). La estadía se prolongó 6 días más. La evidencia actual favorece la nutrición enteral precoz incluso en pancreatitis moderada-grave.",
                    "pearl": "Perla clínica: Nutrición en pancreatitis aguda: Leve → dieta oral precoz. Moderada-grave → nutrición enteral (sonda nasoyeyunal) si no tolera oral. Severa con íleo → nutrición parenteral como último recurso. La vía enteral preserva la barrera intestinal y reduce infección."
                },
                "end_antibio_profilactico": {
                    "terminal": True,
                    "result": "warning",
                    "description": "Los antibióticos profilácticos no previnieron complicaciones (no hay necrosis en este caso) y seleccionaron flora resistente. Al 5to día la paciente desarrolló diarrea por C. difficile. Antibióticos sin indicación = iatrogenia.",
                    "pearl": "Perla clínica: Los antibióticos en pancreatitis aguda se indican SOLO ante: necrosis infectada documentada (punción-aspiración con Gram positivo o cultivo positivo), colangitis concomitante o infección extrapancreática. La necrosis estéril NO es indicación de antibiótico."
                },
                "end_npo_prolongado": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El ayuno de 7 días causó desnutrición, atrofia de la mucosa intestinal y translocación bacteriana. La paciente desarrolló fiebre al 6to día (infección del tracto biliar). La hospitalización duró 12 días en lugar de 3-4. El ayuno prolongado en pancreatitis leve no tiene ningún beneficio demostrado.",
                    "pearl": "Perla clínica: El concepto de 'reposo pancreático' como tratamiento de la pancreatitis está superado. Los estudios muestran que el reinicio oral precoz (cuando tolera, con dolor controlado) acelera la recuperación y reduce las complicaciones infecciosas."
                }
            }
        }
    },
    {
        "id": "crisis-asmatica",
        "name": "Crisis Asmática Severa",
        "system": "Respiratorio",
        "difficulty": "Básico",
        "summary": "Exacerbación aguda de asma bronquial con obstrucción severa al flujo aéreo. El reconocimiento de la gravedad y el tratamiento escalonado precoz determinan el pronóstico.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 24 años asmático conocido desde la infancia. Consulta por disnea que progresó en las últimas 2 horas luego de exposición a polvo. No puede completar frases completas, usa músculos accesorios (esternocleidomastoideo), FR 32 rpm, FC 118 lpm, SatO2 88% con aire ambiente, sibilancias bilaterales intensas. Peak Flow: 30% del valor predicho. ¿Cuál es el tratamiento inicial?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Salbutamol nebulizado + ipratropio nebulizado + metilprednisolona IV + O2 para SatO2 >94%",
                            "correct": True,
                            "feedback": "Correcto. El tratamiento de la crisis severa incluye: broncodilatador de acción corta (SABA) nebulizado, bromuro de ipratropio (aumenta la broncodilatación un 25% adicional), corticoide sistémico (efecto en 2-4h) y O2 titulado para SatO2 94-98%.",
                            "next": "n2_tratamiento"
                        },
                        {
                            "id": "b",
                            "text": "Salbutamol inhalador MDI 2 puffs y observar 30 minutos",
                            "correct": False,
                            "feedback": "Insuficiente para crisis severa. El MDI con 2 puffs es para crisis leve. Con Peak Flow 30%, uso de músculos accesorios y SatO2 88%, se necesita nebulización continua, ipratropio y corticoide IV urgente.",
                            "next": "end_mdi_solo"
                        },
                        {
                            "id": "c",
                            "text": "Adrenalina IV de inmediato — crisis severa requiere adrenalina",
                            "correct": False,
                            "feedback": "Incorrecto. La adrenalina IV no es primera línea en crisis asmática. Se reserva para anafilaxia con broncoespasmo o asma casi fatal con paro inminente. El salbutamol nebulizado + ipratropio es más seguro y eficaz.",
                            "next": "end_adrenalina_asma"
                        }
                    ]
                },
                "n2_tratamiento": {
                    "description": "A los 20 minutos post-primera nebulización: SatO2 93%, FR 26, el paciente puede hablar en frases cortas (antes solo palabras), sibilancias persisten pero menos intensas. Peak Flow no medible aún. ¿Cuál es el siguiente paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Repetir nebulizaciones de salbutamol + ipratropio cada 20 minutos (hasta 3 ciclos) y reevaluar a los 60 minutos",
                            "correct": True,
                            "feedback": "Correcto. En crisis severa se hacen nebulizaciones cada 20 minutos durante la primera hora (3 ciclos). La mejoría parcial a los 20 minutos es una buena señal pero insuficiente para dar el alta — el pico del corticoide aún no llegó.",
                            "next": "n3_evaluacion"
                        },
                        {
                            "id": "b",
                            "text": "Alta con inhalador — mejoró claramente en 20 minutos",
                            "correct": False,
                            "feedback": "Peligroso. La mejoría a los 20 minutos es del broncodilatador, pero el corticoide aún no actuó. La crisis severa puede revertir en las horas siguientes. El alta precoz en crisis severa tiene mortalidad documentada.",
                            "next": "end_alta_precoz_asma"
                        }
                    ]
                },
                "n3_evaluacion": {
                    "description": "A los 60 minutos (3 nebulizaciones completas): SatO2 96%, FR 18, habla normalmente, sin uso de músculos accesorios, sibilancias leves solo en espiratorio, Peak Flow 65% del predicho. ¿Cuál es el plan?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Observación 1-4h más, alta con corticoide oral 5-7 días + salbutamol de rescate + control con neumología",
                            "correct": True,
                            "feedback": "Correcto. Peak Flow >60% con buena respuesta clínica permite el alta. El corticoide oral (prednisona 40-50mg/día por 5-7 días) previene la fase tardía. Es mandatorio el seguimiento neumológico para optimizar el tratamiento controlador.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Hospitalizar por al menos 48h — fue una crisis severa",
                            "correct": False,
                            "feedback": "Innecesario con esta respuesta. Si el Peak Flow es >60%, la SatO2 >94% en aire ambiente y el paciente está clínicamente bien después de observación, el alta es segura con corticoide oral y seguimiento estrecho.",
                            "next": "end_hospitalizacion_excesiva"
                        },
                        {
                            "id": "c",
                            "text": "Alta sin corticoide oral — ya recibió metilprednisolona IV en urgencias",
                            "correct": False,
                            "feedback": "Incorrecto. La metilprednisolona IV tiene vida media corta. Sin corticoide oral de continuación, el 30% de los pacientes presentará recaída en las 48-72h por la fase tardía inflamatoria. El ciclo oral de 5-7 días es mandatorio.",
                            "next": "end_sin_cortico_oral"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Manejo correcto: SABA + ipratropio nebulizados en 3 ciclos, corticoide IV, O2, observación y alta con corticoide oral + plan de acción escrito. Control con neumología a los 7 días donde se inicia ICS/LABA controlador. Sin recaídas en 6 meses.",
                    "pearl": "Perla clínica: Toda crisis severa de asma es una oportunidad para revisar el tratamiento controlador. El 60% de los pacientes que consultan a urgencias por asma severa NO usan corticoide inhalado de mantenimiento — la principal causa de crisis evitables."
                },
                "end_mdi_solo": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente no mejoró con 2 puffs de salbutamol. A los 30 minutos presentó silencio auscultatorio bilateral (tórax silente = asma casi fatal). Requirió intubación de urgencia. La subestimación de la severidad fue el error crítico.",
                    "pearl": "Perla clínica: Signos de crisis asmática casi fatal: tórax silente (sin sibilancias por ausencia de flujo aéreo), cianosis, bradicardia, hipotensión, Glasgow alterado. En este escenario: intubación inmediata + ketamina como inductor (broncodilatador)."
                },
                "end_adrenalina_asma": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La adrenalina IV causó taquicardia severa (FC 158) e hipertensión. El paciente mejoró el broncoespasmo pero con efectos adversos cardiovasculares significativos. El salbutamol nebulizado tiene perfil de seguridad muy superior.",
                    "pearl": "Perla clínica: La adrenalina IM (no IV) tiene rol en anafilaxia con broncoespasmo. En crisis asmática pura, el salbutamol nebulizado es más selectivo (beta-2), más seguro y tan eficaz. La adrenalina IV en asma se reserva para paro cardiorrespiratorio."
                },
                "end_alta_precoz_asma": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente fue dado de alta con mejoría parcial. A las 4 horas, la fase tardía inflamatoria causó broncoespasmo severo en su domicilio. Llegó al servicio de emergencias en paro respiratorio. La crisis severa nunca debe recibir el alta con menos de 60 minutos de observación post-nebulización.",
                    "pearl": "Perla clínica: La respuesta bifásica del asma: fase temprana (broncoespasmo, responde a SABA en minutos) y fase tardía (inflamación, 4-12h después). El corticoide sistémico previene la fase tardía — pero necesita 4-6h para actuar. Nunca dar el alta antes de que su efecto sea evaluable."
                },
                "end_hospitalizacion_excesiva": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La hospitalización fue innecesaria. El paciente desarrolló infección nosocomial leve. Con Peak Flow >60% y respuesta clínica completa, el alta con corticoide oral y seguimiento estrecho es el manejo correcto y seguro.",
                    "pearl": "Perla clínica: Criterios de alta en crisis asmática: Peak Flow >60% del predicho, SatO2 >94% en aire ambiente, sin uso de músculos accesorios, capaz de usar correctamente el inhalador, con corticoide oral prescrito y seguimiento confirmado."
                },
                "end_sin_cortico_oral": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Sin corticoide oral de continuación, la inflamación de la vía aérea persistió. El paciente reingresó a las 36h con nueva crisis severa. El 30% de los pacientes con asma que no reciben corticoide oral al alta tienen recaída en 48-72h.",
                    "pearl": "Perla clínica: El ciclo corto de corticoide oral post-crisis es tan importante como el tratamiento en urgencias. Prednisona 40-50mg/día por 5-7 días sin reducción gradual (ciclos cortos no requieren tapering). Junto con esto: revisar técnica inhalatoria y plan de acción escrito."
                }
            }
        }
    },
    {
        "id": "hipoglucemia-severa",
        "name": "Hipoglucemia Severa",
        "system": "Endocrino",
        "difficulty": "Básico",
        "summary": "Descenso crítico de la glucemia que produce disfunción del sistema nervioso central. Emergencia frecuente en diabéticos insulinizados que requiere acción inmediata.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Familiar trae a urgencias a paciente masculino de 65 años con DM2 insulinizado. Lo encontró inconsciente en su domicilio. Glucemia capilar: 28 mg/dL. Glasgow 9. Piel fría y sudorosa. FC 108, TA 135/85. ¿Cuál es tu primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Dextrosa 50% IV en bolo (25-50 mL) de inmediato",
                            "correct": True,
                            "feedback": "Correcto. Con acceso venoso disponible, la dextrosa IV es el tratamiento más rápido y efectivo. 25 mL de dextrosa 50% elevan la glucemia aproximadamente 50 mg/dL en 2-3 minutos. Es la primera línea en hipoglucemia grave con compromiso de conciencia.",
                            "next": "n2_recuperacion"
                        },
                        {
                            "id": "b",
                            "text": "Insulina rápida IV — puede que sea hiperglucémico y el glucómetro falló",
                            "correct": False,
                            "feedback": "Fatal. La glucemia de 28 mg/dL es real y confirmada. Administrar insulina ante hipoglucemia severa causará la muerte por hipoglucemia profunda. Nunca se administra insulina sin glucemia documentada elevada.",
                            "next": "end_insulina_mal"
                        },
                        {
                            "id": "c",
                            "text": "Glucagón 1mg IM — no tenemos acceso venoso aún",
                            "correct": False,
                            "feedback": "Razonable si realmente no hubiera acceso venoso. Pero en urgencias hospitalarias siempre se debe canalizar primero. El glucagón IM tarda 10-15 minutos y no funciona en pacientes desnutridos o alcohólicos (sin glucógeno hepático).",
                            "next": "n2_glucagon"
                        }
                    ]
                },
                "n2_recuperacion": {
                    "description": "Tras 25 mL de dextrosa 50%: glucemia 92 mg/dL, Glasgow 15. El paciente está despierto y orientado. Refiere que 'se olvidó de comer' después de ponerse la insulina de la mañana. ¿Cuál es el siguiente paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Colación con hidratos de carbono complejos + investigar causa + revisar dosis de insulina + observación 2-4h",
                            "correct": True,
                            "feedback": "Correcto. La dextrosa IV es de acción corta. Se necesita colación con HC complejos para mantener la glucemia. Además, hay que investigar el factor precipitante (omisión de comida, dosis excesiva, ejercicio) y ajustar el esquema insulínico.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Alta inmediata — ya está lúcido y la glucemia normalizó",
                            "correct": False,
                            "feedback": "Prematuro. La insulina basal del paciente sigue activa durante horas. Sin colación y sin identificar la causa, la hipoglucemia puede repetirse en el domicilio. La observación mínima de 2-4h es mandatoria.",
                            "next": "end_alta_precoz_hipo"
                        }
                    ]
                },
                "n2_glucagon": {
                    "description": "Se administró glucagón 1mg IM. A los 12 minutos el paciente abre ojos pero está somnoliento (Glasgow 12). Glucemia ahora 55 mg/dL. Se logró canalizar una vía venosa. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Dextrosa 50% IV + colación oral cuando esté alerta",
                            "correct": True,
                            "feedback": "Correcto. El glucagón funcionó parcialmente. Con vía venosa disponible, la dextrosa IV asegura una corrección más rápida y confiable. El glucagón puede repetirse, pero la dextrosa IV es más efectiva.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Segunda dosis de glucagón — el primero no fue suficiente",
                            "correct": False,
                            "feedback": "Innecesario con vía venosa disponible. El glucagón agota el glucógeno hepático; una segunda dosis puede ser ineficaz y causa náuseas intensas. La dextrosa IV es la opción correcta ahora que hay acceso venoso.",
                            "next": "end_glucagon_exceso"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Corrección rápida con dextrosa IV, colación post-tratamiento y revisión del esquema insulínico. Se identificó que la dosis de insulina glargina era excesiva. Se ajustó a la baja y se educó al paciente en reconocimiento de síntomas y manejo domiciliario con glucagón.",
                    "pearl": "Perla clínica: La regla 15-15 en hipoglucemia leve: 15g de HC simples (3 sobres de azúcar, 150mL jugo) → esperar 15 minutos → medir glucemia. En hipoglucemia grave con compromiso de conciencia: dextrosa IV o glucagón IM. Siempre seguir con HC complejos."
                },
                "end_insulina_mal": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La insulina IV profundizó la hipoglucemia. Glucemia cayó a 12 mg/dL. El paciente presentó convulsiones hipoglucémicas y paro cardiorrespiratorio. Daño neurológico anóxico severo. Error absolutamente prevenible.",
                    "pearl": "Perla clínica: Ante cualquier paciente diabético inconsciente, el protocolo es SIEMPRE medir glucemia primero. La hipoglucemia es la causa más frecuente de alteración de conciencia en diabéticos. 'Si está inconsciente y es diabético → medir glucemia antes de cualquier otra acción'."
                },
                "end_alta_precoz_hipo": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El paciente regresó en ambulancia 3h después con glucemia de 22 mg/dL. La insulina glargina (acción de 24h) siguió actuando sin ingesta de alimentos. La hipoglucemia recurrente en domicilio puede ser fatal.",
                    "pearl": "Perla clínica: Hipoglucemias que requieren observación prolongada (4-12h): uso de insulinas de acción prolongada, sulfonilureas (glibenclamida puede causar hipoglucemia de hasta 24h), ingesta de alcohol, insuficiencia renal o hepática asociada."
                },
                "end_glucagon_exceso": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La segunda dosis de glucagón fue ineficaz (glucógeno hepático agotado) y causó vómitos intensos. Con la vía venosa disponible, la dextrosa era la opción correcta. El paciente se recuperó pero con mayor tiempo de corrección.",
                    "pearl": "Perla clínica: El glucagón moviliza el glucógeno hepático para producir glucosa. No funciona en: ayuno prolongado, alcoholismo, desnutrición, enfermedad hepática. En estos pacientes la dextrosa IV es la única opción confiable."
                }
            }
        }
    },
    {
        "id": "insuficiencia-renal-aguda",
        "name": "Insuficiencia Renal Aguda",
        "system": "Renal",
        "difficulty": "Intermedio",
        "summary": "Deterioro brusco de la función renal con acumulación de productos nitrogenados. La clasificación en prerrenal, intrínseca y posrrenal es el primer paso diagnóstico y terapéutico.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 70 años con HTA e IC leve crónica. Consulta por astenia, edema y oliguria (200 mL/día) desde hace 3 días. Laboratorio: Creatinina 4.2 mg/dL (basal 1.0), BUN 68, K+ 5.8 mEq/L. Medicación habitual: enalapril, furosemida e ibuprofeno (tomando por lumbalgia hace 2 semanas). ¿Cuál es tu primer enfoque diagnóstico?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Clasificar causa (prerrenal/intrínseca/posrenal) + orina completa + FENa + ecografía renal",
                            "correct": True,
                            "feedback": "Correcto. El abordaje diagnóstico sistemático de la IRA comienza por clasificar la causa: FENa <1% sugiere prerrenal, >2% sugiere daño intrínseco. La ecografía descarta obstrucción. El ibuprofeno + IECA + diurético es una combinación nefrotóxica clásica.",
                            "next": "n2_clasificacion"
                        },
                        {
                            "id": "b",
                            "text": "Furosemida IV a dosis alta para forzar diuresis",
                            "correct": False,
                            "feedback": "Incorrecto sin saber la causa. Si la IRA es prerrenal (hipovolemia), el diurético empeorará la perfusión renal. Si es posrenal (obstrucción), tampoco ayuda. La causa determina el tratamiento.",
                            "next": "end_diuretico_ira"
                        },
                        {
                            "id": "c",
                            "text": "Diálisis de urgencia — creatinina de 4.2 es muy alta",
                            "correct": False,
                            "feedback": "Prematuro. La creatinina de 4.2 es alta pero no es indicación automática de diálisis. Las indicaciones de diálisis urgente son: hiperpotasemia refractaria, acidosis severa, sobrecarga hídrica refractaria o uremia sintomática. Primero hay que tratar la causa.",
                            "next": "end_dialisis_precoz"
                        }
                    ]
                },
                "n2_clasificacion": {
                    "description": "FENa: 0.4% (prerrenal). FEUrea: 28% (prerrenal). Orina concentrada (osmolaridad 520). Ecografía: riñones normales, sin hidronefrosis. Sedimento urinario sin cilindros. Diagnóstico: IRA prerrenal por triple nefrotoxicidad (IECA + diurético + AINE). K+ 5.8 mEq/L. ¿Cuál es el manejo?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Suspender AINE + suspender diurético + reducir/suspender IECA + hidratación IV cautelosa",
                            "correct": True,
                            "feedback": "Correcto. La tríada IECA + diurético + AINE es causa clásica de IRA prerrenal: los AINE bloquean prostaglandinas vasodilatadoras aferentes, el IECA bloquea angiotensina vasoconstrictora eferente, y el diurético reduce volumen. Retirar la causa es el tratamiento.",
                            "next": "n3_recuperacion"
                        },
                        {
                            "id": "b",
                            "text": "Continuar todos los medicamentos y solo hidratar",
                            "correct": False,
                            "feedback": "Incorrecto. Sin retirar los nefrotóxicos (especialmente el AINE), la hidratación no revertirá la IRA. El ibuprofeno sigue bloqueando la vasodilatación aferente necesaria para la perfusión renal.",
                            "next": "end_medicamentos_activos"
                        }
                    ]
                },
                "n3_recuperacion": {
                    "description": "A las 48h post-suspensión de nefrotóxicos e hidratación: creatinina 2.4 mg/dL (mejorando), diuresis 800 mL/día, K+ 5.2 mEq/L. Buena tendencia. ¿Cuál es el plan?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Continuar monitoreo, interconsulta a nefrología, no reintroducir AINE nunca, reconsidering IECA cuando creatinina estabilice",
                            "correct": True,
                            "feedback": "Correcto. La IRA prerrenal por nefrotóxicos tiene buena recuperación si la causa se retira a tiempo. El IECA puede reintroducirse con cautela cuando la función renal se normalice. Los AINE están contraindicados en este paciente de forma permanente.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Reiniciar ibuprofeno — el dolor lumbar es intenso y la creatinina está mejorando",
                            "correct": False,
                            "feedback": "Contraindicado. Reiniciar el AINE causante de la IRA, incluso con función renal en recuperación, puede precipitar una nueva injuria renal potencialmente irreversible. El manejo del dolor debe ser con paracetamol.",
                            "next": "end_recaida_ira"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Diagnóstico correcto (IRA prerrenal por triple nefrotoxicidad), retiro oportuno de la causa y recuperación completa. Creatinina a los 7 días: 1.1 mg/dL. El paciente fue educado sobre la contraindicación permanente de AINEs y la importancia del monitoreo renal con IECA.",
                    "pearl": "Perla clínica: La combinación IECA/ARA-II + diurético + AINE se denomina 'triple whammy' — triplica el riesgo de IRA. Es especialmente peligrosa en pacientes mayores con IC, HTA o diabetes. El paracetamol es el analgésico de elección en insuficiencia renal."
                },
                "end_diuretico_ira": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El furosemide IV agravó la depleción de volumen en una IRA prerrenal. La creatinina subió a 6.8 mg/dL y el K+ llegó a 6.5 mEq/L con cambios ECG. Requirió diálisis de urgencia que hubiera podido evitarse.",
                    "pearl": "Perla clínica: Los diuréticos en IRA solo están indicados en sobrecarga hídrica documentada. En IRA prerrenal (FENa <1%), el diurético empeora la hipoperfusión renal. La 'prueba de fluidos' con cristaloides es el primer paso en IRA prerrenal."
                },
                "end_dialisis_precoz": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La diálisis no estaba indicada aún. Se instaló un catéter de hemodiálisis con riesgo de infección y trombosis. Al retirar los nefrotóxicos, la función renal se recuperó sin diálisis. Se generó un procedimiento invasivo innecesario.",
                    "pearl": "Perla clínica: Indicaciones de diálisis urgente (AEIOU): A=Acidosis metabólica severa refractaria, E=Electrolitos (K+ >6.5 con cambios ECG), I=Intoxicaciones dializables, O=Sobrecarga hídrica refractaria, U=Uremia sintomática (pericarditis, encefalopatía)."
                },
                "end_medicamentos_activos": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Sin retirar los nefrotóxicos, la IRA progresó a creatinina 7.1 mg/dL con oliguria y K+ 6.8 mEq/L con cambios ECG. Requirió diálisis de urgencia y hospitalización en UCI. La causa era 100% reversible si se hubiera actuado correctamente.",
                    "pearl": "Perla clínica: La IRA prerrenal por fármacos es la causa más tratable de IRA. La recuperación es completa si se retiran los nefrotóxicos en las primeras 24-48h. Después de 48-72h de isquemia renal sostenida, puede evolucionar a NTA (necrosis tubular aguda) que ya no es totalmente reversible."
                },
                "end_recaida_ira": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La reintroducción del ibuprofeno causó recaída de la IRA, esta vez más severa (creatinina 5.8, oliguria, K+ 6.2). La injuria repetida aumenta el riesgo de ERC permanente. Los AINEs quedan contraindicados de por vida en este paciente.",
                    "pearl": "Perla clínica: Cada episodio de IRA aumenta el riesgo de enfermedad renal crónica (ERC) en un 10-40%. Los pacientes con IRA deben evitar nefrotóxicos de forma permanente y tener seguimiento nefrológico para monitorizar la función renal a largo plazo."
                }
            }
        }
    },
    {
        "id": "fibrilacion-auricular",
        "name": "Fibrilación Auricular con Respuesta Ventricular Rápida",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "summary": "Arritmia supraventricular más frecuente. La estrategia terapéutica depende de la estabilidad hemodinámica, el tiempo de inicio y el riesgo tromboembólico.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente femenina de 58 años, sin cardiopatía estructural conocida. Consulta por palpitaciones, disnea leve y mareo desde hace 'unas horas' (no puede precisar el tiempo exacto). TA 138/85 mmHg, FC 148 lpm irregular, SatO2 96%. ECG: fibrilación auricular sin onda P, intervalo RR irregular, FC ventricular 148. ¿Cuál es tu enfoque inicial?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Control de frecuencia cardíaca + determinar tiempo de inicio + anticoagulación",
                            "correct": True,
                            "feedback": "Correcto. En FA con inicio incierto (>12h o desconocido), la cardioversión sin anticoagulación previa tiene riesgo de embolismo del 5-7% por trombos en la orejuela izquierda. Primero: controlar la FC, anticoagular y luego planificar la cardioversión en forma segura.",
                            "next": "n2_control_fc"
                        },
                        {
                            "id": "b",
                            "text": "Cardioversión eléctrica de inmediato — la FC es muy alta",
                            "correct": False,
                            "feedback": "Incorrecto con inicio desconocido. Si la FA lleva más de 48h, puede haber un trombo en la orejuela izquierda. La cardioversión podría desalojar ese trombo y causar un ACV. Solo se cardiovierte de urgencia si hay inestabilidad hemodinámica.",
                            "next": "end_cardioversion_sin_anticoag"
                        },
                        {
                            "id": "c",
                            "text": "Adenosina IV — para terminar la taquicardia",
                            "correct": False,
                            "feedback": "Incorrecto. La adenosina no tiene efecto en la FA — es útil para TSV por reentrada (AVNRT, AVRT). En FA bloquea momentáneamente el nodo AV pero la arritmia auricular continúa. Solo muestra el ritmo subyacente brevemente.",
                            "next": "end_adenosina_mal"
                        }
                    ]
                },
                "n2_control_fc": {
                    "description": "Se inicia metoprolol IV 5mg lento. FC a los 15 min: 98 lpm irregular. Paciente refiere mejoría de los síntomas. Se confirma que los síntomas comenzaron hace al menos 24 horas (FA de inicio >48h no descartable). ¿Cuál es el plan de cardioversión?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Anticoagular + ecocardiograma transesofágico (ETE) para descartar trombo → cardioversión si ETE negativo",
                            "correct": True,
                            "feedback": "Correcto. El ETE tiene sensibilidad >95% para detectar trombos en la orejuela. Si es negativo, puede cardiovertirse de forma segura con anticoagulación iniciada. Alternativa: anticoagular 3-4 semanas antes de la cardioversión sin ETE.",
                            "next": "n3_cardioversion"
                        },
                        {
                            "id": "b",
                            "text": "Cardioversión inmediata con solo heparina IV iniciada hace 2 horas",
                            "correct": False,
                            "feedback": "Insuficiente. La heparina de corta duración no protege contra trombos ya formados en la orejuela. Se necesita ETE para descartar trombo O anticoagulación de 3-4 semanas antes de la cardioversión.",
                            "next": "end_cardioversion_precoz_fa"
                        }
                    ]
                },
                "n3_cardioversion": {
                    "description": "ETE: sin trombo en orejuela izquierda. Se realiza cardioversión eléctrica sincronizada (200J bifásico). Resultado: ritmo sinusal a 72 lpm. ¿Cuánto tiempo se mantiene la anticoagulación post-cardioversión?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Mínimo 4 semanas post-cardioversión + calcular CHA2DS2-VASc para decidir anticoagulación indefinida",
                            "correct": True,
                            "feedback": "Correcto. Post-cardioversión existe riesgo de 'aturdimiento auricular' (la orejuela recupera su contractilidad en 2-4 semanas). Se debe anticoagular mínimo 4 semanas independientemente del CHA2DS2-VASc. Luego evaluar riesgo para decisión de anticoagulación crónica.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Suspender anticoagulación inmediatamente — ya está en ritmo sinusal",
                            "correct": False,
                            "feedback": "Error grave. El ritmo sinusal no significa que la orejuela izquierda ya controla adecuadamente. El 'aturdimiento auricular' post-cardioversión dura semanas. Suspender la anticoagulación antes de las 4 semanas triplica el riesgo de ACV.",
                            "next": "end_sin_anticoag_post_fa"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Manejo correcto: control de FC → anticoagulación → ETE → cardioversión segura → 4 semanas de anticoagulación post-CV. CHA2DS2-VASc: 2 puntos (mujer + edad 58). Se indica anticoagulación crónica con apixabán. Control con cardiología para evaluar antiarrítmico de mantenimiento.",
                    "pearl": "Perla clínica: CHA2DS2-VASc: Insuficiencia cardíaca(1) + HTA(1) + Edad ≥75(2) + Diabetes(1) + ACV previo(2) + Vasculopatía(1) + Edad 65-74(1) + Sexo femenino(1). Anticoagular si ≥2 en hombres o ≥3 en mujeres. La FA es responsable del 15-20% de todos los ACV."
                },
                "end_cardioversion_sin_anticoag": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La cardioversión desalojó un trombo de la orejuela izquierda. La paciente presentó ACV embólico masivo en los 30 minutos siguientes. Hemiplejía derecha y afasia severa permanentes. La cardioversión sin anticoagulación adecuada fue la causa directa.",
                    "pearl": "Perla clínica: Regla de los 48h en FA: si el inicio es <48h documentado, la cardioversión puede hacerse con anticoagulación simultánea sin ETE previo. Si el inicio es >48h o incierto: ETE para descartar trombo O 3-4 semanas de anticoagulación antes. Sin excepciones."
                },
                "end_adenosina_mal": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La adenosina produjo un breve bloqueo AV que 'desnudó' la FA subyacente pero no terminó la arritmia. La FC rebotó a 155 lpm. Se perdió tiempo valioso. El diagnóstico de FA con adenosina no tiene ningún valor terapéutico.",
                    "pearl": "Perla clínica: Diferenciación en taquicardias de complejo estrecho: FA = irregularmente irregular, sin onda P. Flutter = regularmente regular, ondas F en serrucho. TSV = regular, P retrógrada. La adenosina solo trata TSV por reentrada y ayuda a desenmascarar flutter/FA transitoriamente."
                },
                "end_cardioversion_precoz_fa": {
                    "terminal": True,
                    "result": "warning",
                    "description": "Afortunadamente no había trombo (como confirmó el ETE realizado post-ACV menor que presentó la paciente). El ACV transitorio (AIT) fue la señal de alarma. La heparina de 2 horas no previene embolias de trombos ya formados.",
                    "pearl": "Perla clínica: La anticoagulación pre-cardioversión NO disuelve trombos existentes — solo previene la formación de nuevos. Por eso se necesitan 3-4 semanas (tiempo para que el trombo existente se organice y adhiera a la pared) o ETE que confirme ausencia de trombo."
                },
                "end_sin_anticoag_post_fa": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La paciente presentó ACV embólico a los 10 días post-cardioversión por aturdimiento auricular. La orejuela izquierda no recuperó su función contráctil adecuada hasta las 3-4 semanas, generando un trombo que embolizó al cerebro.",
                    "pearl": "Perla clínica: El 'aturdimiento auricular' (stunning) post-cardioversión es un fenómeno fisiológico donde la orejuela izquierda recupera su función mecánica gradualmente en 2-4 semanas. Durante este período existe alto riesgo de tromboembolismo incluso en ritmo sinusal."
                }
            }
        }
    },
    {
        "id": "anafilaxia",
        "name": "Anafilaxia",
        "system": "Infeccioso",
        "difficulty": "Básico",
        "summary": "Reacción alérgica sistémica severa y potencialmente fatal. La adrenalina intramuscular inmediata es el tratamiento de primera línea y no debe retrasarse por ningún otro fármaco.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente femenina de 28 años. Cinco minutos después de recibir penicilina benzatínica IM por faringoamigdalitis estreptocócica, presenta urticaria generalizada, angioedema facial, estridor laríngeo, sibilancias y TA 74/48 mmHg, FC 128 lpm. Refiere dificultad para respirar. ¿Cuál es tu primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Adrenalina 0.3-0.5mg IM en el muslo anterolateral de inmediato",
                            "correct": True,
                            "feedback": "Correcto. La adrenalina IM es el único tratamiento que puede revertir el shock anafiláctico y el angioedema laríngeo. No hay contraindicaciones en anafilaxia. El muslo anterolateral permite absorción más rápida que el deltoides. No retrasar por ningún otro fármaco.",
                            "next": "n2_post_adrenalina"
                        },
                        {
                            "id": "b",
                            "text": "Difenhidramina IV + dexametasona IV — es una reacción alérgica",
                            "correct": False,
                            "feedback": "Error potencialmente fatal. Los antihistamínicos y corticoides no tratan el shock ni el angioedema laríngeo activo. Son adyuvantes que se usan DESPUÉS de la adrenalina. El tiempo que toma buscar estos fármacos puede ser el tiempo en que la vía aérea se cierra.",
                            "next": "end_antihistaminico"
                        },
                        {
                            "id": "c",
                            "text": "Corticoides IV primero para frenar la respuesta inmune",
                            "correct": False,
                            "feedback": "Incorrecto. Los corticoides tardan 4-6 horas en hacer efecto. No tratan el broncoespasmo ni el shock anafiláctico de forma aguda. Son adyuvantes para prevenir reacciones bifásicas, no el tratamiento primario.",
                            "next": "end_corticoide_primero"
                        }
                    ]
                },
                "n2_post_adrenalina": {
                    "description": "A los 5 minutos post-adrenalina IM: TA 95/62 mmHg, FC 108 lpm, estridor mejoró, urticaria persiste. Signos vitales mejorando pero paciente aún sintomática. ¿Cuál es el siguiente paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Repetir adrenalina si no hay respuesta completa + SF IV 500-1000 mL + difenhidramina + corticoide + observación 4-8h",
                            "correct": True,
                            "feedback": "Correcto. La adrenalina puede repetirse cada 5-15 minutos si la respuesta es incompleta. Los fluidos IV tratan el shock distributivo. Los antihistamínicos y corticoides previenen reacciones bifásicas. La observación de 4-8h es mandatoria por riesgo de reacción bifásica.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Alta porque ya mejoró con la adrenalina",
                            "correct": False,
                            "feedback": "Peligroso. La reacción bifásica ocurre en el 20% de las anafilaxias: el paciente mejora y luego recae 1-8 horas después sin nueva exposición al alérgeno. Toda anafilaxia requiere observación mínima de 4-8h en urgencias.",
                            "next": "end_alta_precoz_anafi"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Adrenalina IM inmediata, fluidos IV, antihistamínicos y corticoides. Observación 6h sin reacción bifásica. Alta con autoinyector de adrenalina (EpiPen), pulsera de alergia a penicilina, antihistamínico oral 3 días, prednisona 5 días y derivación a alergología. Contraindicación permanente de betalactámicos documentada.",
                    "pearl": "Perla clínica: Toda persona con anafilaxia debe irse de alta con: 1) Autoinyector de adrenalina y entrenamiento en su uso, 2) Plan de acción escrito, 3) Identificación del alérgeno, 4) Derivación a alergología, 5) Corticoide oral 5 días para prevenir fase tardía."
                },
                "end_antihistaminico": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Mientras se preparaba la difenhidramina, el angioedema progresó a cierre completo de la vía aérea. La paciente requirió cricotirotomía de urgencia. La adrenalina administrada después del evento ya no pudo revertir el angioedema establecido. Secuela: disfonía permanente.",
                    "pearl": "Perla clínica: La adrenalina en anafilaxia no puede esperar. Cada minuto de retraso aumenta el riesgo de muerte. Los antihistamínicos tardan 30-60 minutos en hacer efecto y no revierten el broncoespasmo ni el shock. Son adyuvantes post-adrenalina, nunca sustitutos."
                },
                "end_corticoide_primero": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El shock anafiláctico progresó durante los 4-6 minutos que tardó la dexametasona en prepararse e infundirse. Paro cardiorrespiratorio por shock obstructivo-distributivo combinado. Los corticoides tienen efecto diferido de horas y no tratan la anafilaxia aguda.",
                    "pearl": "Perla clínica: Orden de prioridad en anafilaxia: 1° Adrenalina IM, 2° Posición (decúbito con piernas elevadas si hay hipotensión), 3° O2 de alto flujo, 4° Fluidos IV, 5° Antihistamínicos, 6° Corticoides. Solo el primer paso salva la vida en los primeros minutos."
                },
                "end_alta_precoz_anafi": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La paciente presentó reacción bifásica a las 4 horas en su domicilio. Llegó en paro cardiorrespiratorio. La reacción bifásica ocurre cuando los mediadores de mastocitos y basófilos tienen una segunda ola de liberación sin nueva exposición al alérgeno.",
                    "pearl": "Perla clínica: Reacción bifásica en anafilaxia: ocurre en 1-20% de los casos, típicamente 1-8h después de la resolución aparente. Factores de riesgo: anafilaxia grave inicial, idiopática, retraso en la adrenalina. El corticoide sistémico reduce (pero no elimina) este riesgo."
                }
            }
        }
    },
    {
        "id": "status-epileptico",
        "name": "Status Epiléptico",
        "system": "Neurológico",
        "difficulty": "Avanzado",
        "summary": "Actividad epiléptica continua por más de 5 minutos o convulsiones repetidas sin recuperación de la conciencia. Emergencia neurológica con mortalidad del 10-20% si no se trata a tiempo.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Traen a urgencias a paciente masculino de 35 años epiléptico conocido, convulsionando de forma generalizada tónico-clónica desde hace 8 minutos (testigos lo confirmaron). Esposa dice que tomó su levetiracetam esta mañana. Sin fiebre. Glucemia capilar: 98 mg/dL. SatO2 89%. FC 118. ¿Cuál es la primera acción?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Lorazepam IV 4mg (o diazepam IV 10mg) + O2 de alto flujo",
                            "correct": True,
                            "feedback": "Correcto. Las benzodiazepinas son la primera línea del status epiléptico. A los 5 minutos sin tratamiento, las convulsiones tienen alta probabilidad de no ceder espontáneamente. El O2 corrige la hipoxemia por hipoventilación durante las convulsiones.",
                            "next": "n2_benzo"
                        },
                        {
                            "id": "b",
                            "text": "Esperar 5 minutos más — puede ser una crisis prolongada que ceda sola",
                            "correct": False,
                            "feedback": "Incorrecto. El umbral de tratamiento del status epiléptico es 5 minutos. Este paciente ya lleva 8 minutos. Cada minuto de retraso aumenta el daño neuronal por excitotoxicidad y hace que las convulsiones sean más refractarias al tratamiento.",
                            "next": "end_espera_status"
                        },
                        {
                            "id": "c",
                            "text": "Fenitoína IV primero — es el antiepiléplico de carga estándar",
                            "correct": False,
                            "feedback": "Incorrecto como primera línea. La fenitoína tarda 20-30 minutos en cargarse y no tiene efecto inmediato en las convulsiones activas. Las benzodiazepinas son más rápidas y efectivas en la fase aguda. La fenitoína es segunda línea.",
                            "next": "end_fenitoina_primero"
                        }
                    ]
                },
                "n2_benzo": {
                    "description": "Lorazepam 4mg IV administrado. Han pasado 5 minutos más (total 13 min de status). Las convulsiones no cedieron completamente — hay actividad motora sutil en extremidades. ¿Cuál es el siguiente paso?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Segunda línea: levetiracetam IV 60 mg/kg o valproato IV 40 mg/kg o fenitoína 20 mg/kg",
                            "correct": True,
                            "feedback": "Correcto. Ante falla de la benzodiazepina, se pasa a la segunda línea (minuto 10-20 del protocolo). Los tres fármacos tienen eficacia similar. La elección depende de contraindicaciones: valproato evitar en embarazo/hepatopatía, fenitoína evitar en arritmias.",
                            "next": "n3_segunda_linea"
                        },
                        {
                            "id": "b",
                            "text": "Segunda dosis de lorazepam 4mg más",
                            "correct": False,
                            "feedback": "Subóptimo. Una segunda dosis de benzo puede darse si la primera dosis fue insuficiente, pero con convulsiones persistentes a los 13 minutos ya debe pasarse a segunda línea. Las benzodiacepinas repetidas aumentan el riesgo de depresión respiratoria sin beneficio adicional.",
                            "next": "n3_benzo_repetida"
                        }
                    ]
                },
                "n3_segunda_linea": {
                    "description": "Levetiracetam 3g IV en 15 minutos. Las convulsiones cesan a los 8 minutos de iniciada la infusión. Fase post-ictal: paciente somnoliento pero responde a estímulos. Glasgow 11. ¿Cuál es el plan?",
                    "options": [
                        {
                            "id": "a",
                            "text": "TC de cráneo + EEG + investigar causa + monitoreo neurológico + continuar antiepiléplico",
                            "correct": True,
                            "feedback": "Correcto. Todo status epiléptico requiere identificar la causa: no adherencia al tratamiento, cambio de fármaco, trastorno metabólico, lesión estructural nueva, encefalitis. TC para descartar sangrado o masa. EEG para confirmar cese de actividad eléctrica y descartar status no convulsivo.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Alta cuando el paciente despierte — las convulsiones cedieron",
                            "correct": False,
                            "feedback": "Prematuro. El cese clínico de las convulsiones no garantiza el cese eléctrico. El status epiléptico no convulsivo puede persistir sin actividad motora visible. Además, hay que investigar la causa del status y ajustar el tratamiento.",
                            "next": "end_alta_precoz_status"
                        }
                    ]
                },
                "n3_benzo_repetida": {
                    "description": "Segunda dosis de lorazepam 4mg. Las convulsiones persisten, ahora con depresión respiratoria (FR 8 rpm, SatO2 84%). ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Intubación + ventilación mecánica + segunda línea IV (levetiracetam/valproato) + anestesia si status refractario",
                            "correct": True,
                            "feedback": "Correcto. La depresión respiratoria por benzodiacepinas con convulsiones persistentes requiere asegurar la vía aérea mediante intubación. Se continúa el tratamiento del status con segunda línea y si no cede, anestesia general (propofol/midazolam en infusión) para status refractario.",
                            "next": "end_status_refractario"
                        },
                        {
                            "id": "b",
                            "text": "Tercera dosis de lorazepam",
                            "correct": False,
                            "feedback": "Contraindicado. Tres dosis de benzodiacepinas causan depresión respiratoria severa sin beneficio adicional. Con FR 8 y SatO2 84%, la prioridad es la vía aérea. Es el momento de escalar a segunda línea e intubación.",
                            "next": "end_benzo_triple"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Status controlado en 21 minutos con protocolo correcto: BZD → segunda línea. TC normal. EEG sin actividad epiléptica. Causa: nivel subterapéutico de levetiracetam (paciente refiere vómitos ese día). Ajuste de dosis y agregado de valproato. Alta al 3er día sin nuevas crisis.",
                    "pearl": "Perla clínica: Protocolo del status epiléptico por tiempo: 0-5min: BZD (lorazepam/diazepam). 10-20min: Segunda línea (levetiracetam/valproato/fenitoína). 20-40min: Status refractario → anestesia (propofol/midazolam). Cada etapa tiene 10 minutos de margen. El tiempo es neurona."
                },
                "end_espera_status": {
                    "terminal": True,
                    "result": "failure",
                    "description": "Las convulsiones continuaron 22 minutos hasta que se inició el tratamiento. El status prolongado causó excitotoxicidad con daño neuronal significativo. El EEG mostró enlentecimiento difuso. El paciente quedó con deterioro cognitivo y epilepsia refractaria.",
                    "pearl": "Perla clínica: Las convulsiones que duran más de 5 minutos tienen <3% de probabilidad de cesar espontáneamente. Después de 30 minutos de status, el daño neuronal es progresivo e irreversible. El tratamiento no puede esperar confirmación diagnóstica."
                },
                "end_fenitoina_primero": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La fenitoína tardó 25 minutos en cargarse. Las convulsiones continuaron 25 minutos adicionales antes de cesar. El daño neuronal acumulado fue mayor que si se hubiera usado benzodiazepina primero. La fenitoína es segunda línea, no primera.",
                    "pearl": "Perla clínica: La fenitoína tiene varias desventajas en el status agudo: requiere 20 mg/kg en infusión lenta (≤50mg/min por riesgo de arritmia y hipotensión), tarda en alcanzar nivel terapéutico y no tiene efecto inmediato sobre convulsiones activas. Por eso las BZD son siempre la primera línea."
                },
                "end_alta_precoz_status": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente tenía status epiléptico no convulsivo persistente (sin actividad motora visible pero con actividad eléctrica en el EEG). Fue dado de alta y tuvo un accidente de tráfico al intentar manejar, estando en realidad en un estado confusional continuo por el status eléctrico.",
                    "pearl": "Perla clínica: El status epiléptico no convulsivo (SENC) puede presentarse como confusión, agitación o simplemente somnolencia post-ictal prolongada. Sin EEG no puede descartarse. Todo status convulsivo debe confirmarse con EEG antes del alta."
                },
                "end_status_refractario": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El paciente requirió intubación y propofol en infusión para status refractario. Controlado a las 2h. UCI por 4 días. La demora en pasar a segunda línea y la triple dosis de benzodiacepinas prolongaron el status y requirieron el tratamiento más agresivo.",
                    "pearl": "Perla clínica: Status epiléptico refractario (no cede con BZD + segunda línea): anestesia general con propofol o midazolam en infusión continua bajo monitoreo EEG continuo. El objetivo es supresión de brotes en EEG, no solo cese clínico."
                },
                "end_benzo_triple": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La tercera dosis de lorazepam causó apnea completa. Paro respiratorio. La intubación de urgencia fue difícil por el estado convulsivo. Daño anóxico cerebral por hipoxemia prolongada. La triple benzodiacepina sin intubación es una combinación letal.",
                    "pearl": "Perla clínica: Máximo de benzodiacepinas en status: 2 dosis. Si no hay respuesta a la segunda dosis, pasar a segunda línea e intubación si hay depresión respiratoria. Las benzodiacepinas repetidas sin intubación son la causa más prevenible de muerte en status epiléptico tratado."
                }
            }
        }
    },
    {
        "id": "colecistitis-aguda",
        "name": "Colecistitis Aguda",
        "system": "Digestivo",
        "difficulty": "Básico",
        "summary": "Inflamación aguda de la vesícula biliar, casi siempre por colelitiasis. El diagnóstico es clínico-ecográfico y el tratamiento definitivo es quirúrgico.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente femenina de 42 años, obesa, multípara. Consulta por dolor en hipocondrio derecho de 14 horas de evolución, irradiado a escápula derecha, fiebre 38.6°C, náuseas. Examen físico: signo de Murphy positivo, dolor a la palpación profunda en HCD, defensa muscular leve. GB: 15.200 con 88% neutrófilos. ¿Cuál es el manejo inicial?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Criterios de Tokio + ecografía abdominal + hidratación + analgesia + antibióticos",
                            "correct": True,
                            "feedback": "Correcto. Los criterios de Tokio estratifican la severidad de la colecistitis (Grado I, II, III) y guían el timing quirúrgico. La ecografía confirma el diagnóstico (pared >4mm, cálculos, líquido pericolicístico). Los antibióticos cubren gérmenes entéricos gram negativos.",
                            "next": "n2_severidad"
                        },
                        {
                            "id": "b",
                            "text": "Analgesia IM y alta con antibiótico oral — es un cólico biliar complicado",
                            "correct": False,
                            "feedback": "Incorrecto. La fiebre, leucocitosis y Murphy positivo configuran colecistitis aguda, no cólico biliar. El cólico biliar no tiene fiebre ni leucocitosis. La colecistitis requiere hospitalización, antibióticos IV y evaluación quirúrgica.",
                            "next": "end_alta_colecistitis"
                        },
                        {
                            "id": "c",
                            "text": "CPRE urgente — puede haber un cálculo en el colédoco",
                            "correct": False,
                            "feedback": "Incorrecto. La CPRE trata la coledocolitiasis y la colangitis, no la colecistitis aguda. Sin ictericia, sin dilatación del colédoco y sin colangitis, la CPRE no está indicada. El tratamiento de la colecistitis es la colecistectomía.",
                            "next": "end_cpre_colecistitis"
                        }
                    ]
                },
                "n2_severidad": {
                    "description": "Ecografía: vesícula distendida, pared de 6mm, cálculo enclavado en cuello, líquido pericolicístico. Criterios de Tokio Grado I (colecistitis leve, sin disfunción orgánica). Antibióticos iniciados. ¿Cuál es la estrategia quirúrgica?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Colecistectomía laparoscópica dentro de las primeras 72h del inicio de síntomas",
                            "correct": True,
                            "feedback": "Correcto. Las guías de Tokio recomiendan colecistectomía laparoscópica precoz (dentro de las 72h) en colecistitis Grado I y II como paciente operable. La cirugía precoz reduce la morbilidad, la estadía hospitalaria y los costos comparada con la cirugía diferida.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Tratamiento médico 6-8 semanas y cirugía electiva diferida",
                            "correct": False,
                            "feedback": "Estrategia superada. La colecistitis diferida se asocia a mayor riesgo de recurrencia (25-30% en las siguientes semanas), mayor dificultad técnica quirúrgica por fibrosis y mayor tasa de conversión a laparotomía. La cirugía precoz es hoy el estándar.",
                            "next": "end_conservador_colecistitis"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Diagnóstico correcto con criterios de Tokio y ecografía. Colecistectomía laparoscópica a las 28h del ingreso sin complicaciones. Tiempo quirúrgico 45 minutos. Alta al día siguiente de la cirugía. Sin conversión a laparotomía abierta.",
                    "pearl": "Perla clínica: La colecistectomía laparoscópica precoz (<72h del inicio de síntomas) en colecistitis aguda Grado I-II tiene menor tasa de complicaciones que la cirugía diferida. Después de las 72h, la inflamación y fibrosis aumentan el riesgo quirúrgico. La ventana óptima es las primeras 24-48h."
                },
                "end_alta_colecistitis": {
                    "terminal": True,
                    "result": "failure",
                    "description": "La paciente regresó a las 12 horas con perforación de vesícula y peritonitis biliar localizada. La colecistitis aguda no tratada puede progresar a gangrena y perforación en el 10-15% de los casos. Requirió laparotomía de urgencia y lavado peritoneal.",
                    "pearl": "Perla clínica: Distinguir cólico biliar de colecistitis aguda: Cólico biliar = dolor cólico sin fiebre, dura <6h, Murphy negativo, leucocitos normales. Colecistitis = dolor persistente >6h + fiebre + Murphy positivo + leucocitosis. El cólico puede manejarse ambulatoriamente; la colecistitis siempre requiere hospitalización."
                },
                "end_cpre_colecistitis": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La CPRE fue normal (sin cálculo en colédoco). El procedimiento generó una pancreatitis post-CPRE leve. Se perdieron 4 horas en un procedimiento innecesario mientras la colecistitis progresaba. El diagnóstico correcto era colecistitis aguda, no coledocolitiasis.",
                    "pearl": "Perla clínica: Indicadores de coledocolitiasis que justifican CPRE: bilirrubina >4 mg/dL, colédoco dilatado >8mm en ecografía, ictericia obstructiva, colangitis (fiebre + ictericia + dolor = tríada de Charcot). Sin estos criterios, la CPRE no es el siguiente paso."
                },
                "end_conservador_colecistitis": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La paciente tuvo recurrencia de colecistitis a las 3 semanas, esta vez con empiema vesicular (Tokio Grado II). La segunda cirugía fue más difícil técnicamente, requirió conversión a laparotomía y la estadía hospitalaria fue el doble. La cirugía diferida fue la estrategia equivocada.",
                    "pearl": "Perla clínica: El 25-30% de los pacientes con colecistitis tratada médicamente sin cirugía precoz presentan recurrencia o complicación grave (empiema, gangrena, perforación) dentro de las 6 semanas. La colecistectomía precoz es el estándar actual en pacientes con bajo riesgo quirúrgico."
                }
            }
        }
    },
    {
        "id": "iamsest",
        "name": "IAMSEST / Angina Inestable",
        "system": "Cardiovascular",
        "difficulty": "Avanzado",
        "summary": "Síndrome coronario agudo sin elevación del segmento ST. La estratificación de riesgo con score GRACE define el timing de la coronariografía y la intensidad del tratamiento.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 65 años con HTA, DM2 y dislipemia. Consulta por dolor precordial en reposo de 2 horas de evolución, irradiado al brazo izquierdo, sudoración. TA 145/90, FC 88 lpm. ECG: depresión del ST 1.5mm en V4-V6, sin elevación. Troponina I: 0.9 ng/mL (VN <0.04). ¿Cuál es el manejo inicial?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Score GRACE + doble antiagregación (AAS + ticagrelor) + anticoagulación + estrategia invasiva según riesgo",
                            "correct": True,
                            "feedback": "Correcto. El IAMSEST se maneja con: estratificación de riesgo (GRACE), doble antiagregación inmediata y anticoagulación. La estrategia invasiva (coronariografía) se programa según el puntaje GRACE: muy alto riesgo (<2h), alto riesgo (<24h), intermedio (<72h).",
                            "next": "n2_grace"
                        },
                        {
                            "id": "b",
                            "text": "Coronariografía inmediata como en el IAMCEST — la troponina está alta",
                            "correct": False,
                            "feedback": "Incorrecto. El IAMSEST no es la misma urgencia que el IAMCEST. En el IAMSEST la arteria no está completamente ocluida — hay tiempo para estratificar el riesgo. Solo se va de urgencia (<2h) si hay inestabilidad hemodinámica, arritmia maligna o dolor refractario.",
                            "next": "end_cateterismo_innecesario"
                        },
                        {
                            "id": "c",
                            "text": "Anticoagulación oral y alta con seguimiento ambulatorio",
                            "correct": False,
                            "feedback": "Gravemente inadecuado. El IAMSEST con troponina elevada y cambios del ST es una emergencia. La anticoagulación oral no tiene efecto inmediato y el alta sin estratificación de riesgo ni coronariografía puede resultar en IAMCEST o muerte súbita.",
                            "next": "end_alta_iamsest"
                        }
                    ]
                },
                "n2_grace": {
                    "description": "Score GRACE calculado: 158 puntos (alto riesgo — mortalidad hospitalaria estimada >3%). Troponina en ascenso (3.2 ng/mL a las 3h). Dolor controlado. Hemodinámicamente estable. ¿Cuál es el timing de la coronariografía?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Estrategia invasiva precoz: coronariografía dentro de las 24 horas",
                            "correct": True,
                            "feedback": "Correcto. GRACE >140 (alto riesgo) indica estrategia invasiva dentro de las 24h. El estudio TIMACS demostró beneficio de la estrategia precoz (<24h) vs tardía (>36h) en pacientes de alto riesgo: reducción de muerte, IAM y ACV.",
                            "next": "n3_coronariografia"
                        },
                        {
                            "id": "b",
                            "text": "Manejo médico solo — está estable hemodinámicamente",
                            "correct": False,
                            "feedback": "Incorrecto en alto riesgo. La estabilidad hemodinámica en reposo no excluye el beneficio de la coronariografía. Con GRACE >140 y troponina en ascenso, el manejo conservador se asocia a mayor mortalidad a 6 meses comparado con la estrategia invasiva.",
                            "next": "end_solo_medico_iamsest"
                        }
                    ]
                },
                "n3_coronariografia": {
                    "description": "Coronariografía a las 18h del ingreso: estenosis del 75% en DA proximal y 60% en CD media. Función ventricular izquierda conservada (FE 55%). Se realiza ATC con stent farmacoactivo en DA. CD no significativa hemodinámicamente. ¿Cuál es el tratamiento al alta?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Doble antiagregación 12 meses (AAS + ticagrelor) + betabloqueante + IECA + estatina alta intensidad",
                            "correct": True,
                            "feedback": "Correcto. Post-IAMSEST con stent: DAAT por 12 meses mínimo (previene trombosis del stent), betabloqueante (reduce mortalidad), IECA (remodelado ventricular) y estatina de alta intensidad (reduce LDL <70 mg/dL y estabiliza placa).",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Solo AAS indefinida + estatina — el stent fue exitoso",
                            "correct": False,
                            "feedback": "Insuficiente. La monoterapia con AAS no protege el stent de la trombosis en los primeros 12 meses. La DAAT (doble antiagregación) es mandatoria después de ATC con stent para prevenir la trombosis intrastent que tiene una mortalidad del 45%.",
                            "next": "end_monoterapia_iamsest"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Estratificación correcta con GRACE, estrategia invasiva precoz dentro de las 24h y tratamiento médico óptimo al alta. A los 12 meses: sin eventos cardiovasculares mayores, LDL 58 mg/dL, FE estable en 55%. Modificación de factores de riesgo en curso.",
                    "pearl": "Perla clínica: IAMSEST vs IAMCEST: en el IAMCEST la arteria está 100% ocluida → cateterismo inmediato (<90min). En el IAMSEST hay oclusión parcial o subtotal → estratificación con GRACE → cateterismo según riesgo (<2h, <24h o <72h). La diferencia en el ECG: elevación ST (IAMCEST) vs depresión ST o sin cambios (IAMSEST)."
                },
                "end_cateterismo_innecesario": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La coronariografía inmediata no causó daño pero tampoco fue necesaria de urgencia. Con un GRACE >140, el cateterismo en <24h hubiera sido el momento correcto y con mejor preparación del equipo. La urgencia en IAMSEST no es igual que en IAMCEST.",
                    "pearl": "Perla clínica: Indicaciones de coronariografía <2h en IAMSEST (igual que IAMCEST): inestabilidad hemodinámica, shock cardiogénico, arritmia ventricular maligna, dolor isquémico refractario al tratamiento médico. Fuera de estos criterios, la estrategia es programada según GRACE."
                },
                "end_alta_iamsest": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente presentó IAMCEST a las 6 horas del alta por progresión a oclusión total de la DA. Llegó en shock cardiogénico. La lesión culpable que podría haberse tratado electivamente se convirtió en una emergencia con mucho mayor mortalidad.",
                    "pearl": "Perla clínica: El IAMSEST es una emergencia que requiere hospitalización. El 15% de los IAMSEST progresan a IAMCEST si no se tratan. La troponina elevada con cambios del ST es la combinación de mayor riesgo — mortalidad hospitalaria del 5-10% sin tratamiento adecuado."
                },
                "end_solo_medico_iamsest": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente fue manejado médicamente. A las 48h presentó re-infarto con elevación del ST y shock cardiogénico. El manejo conservador en IAMSEST de alto riesgo (GRACE >140) tiene mortalidad significativamente mayor a 6 meses comparado con la estrategia invasiva.",
                    "pearl": "Perla clínica: El meta-análisis FRISC II/TACTICS-TIMI18 demostró: en IAMSEST de alto riesgo, la estrategia invasiva reduce muerte e IAM en un 20% comparado con el manejo conservador. El beneficio es proporcional al riesgo — a mayor GRACE, mayor beneficio de la coronariografía."
                },
                "end_monoterapia_iamsest": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente presentó trombosis del stent a los 3 meses (oclusión súbita del stent por falta de doble antiagregación). IAMCEST masivo con FE post-evento del 30%. La trombosis del stent es una de las complicaciones más catastróficas y prevenibles de la cardiología intervencionista.",
                    "pearl": "Perla clínica: La trombosis del stent farmacoactivo tiene mortalidad del 45%. La DAAT (AAS + inhibidor P2Y12: ticagrelor o clopidogrel) debe mantenerse mínimo 12 meses. Suspensión prematura por cirugía o sangrado: siempre consultar con cardiología antes de suspender."
                }
            }
        }
    },
    {
        "id": "epoc-exacerbado",
        "name": "EPOC Exacerbado Grave",
        "system": "Respiratorio",
        "difficulty": "Intermedio",
        "summary": "Agudización de la EPOC con aumento de disnea, esputo purulento y deterioro del intercambio gaseoso. La VNI es el pilar del tratamiento en la insuficiencia respiratoria hipercápnica.",
        "clinical_case": {
            "start": "n1",
            "nodes": {
                "n1": {
                    "description": "Paciente masculino de 68 años, tabaquista de 50 paquetes/año, EPOC GOLD III en tratamiento con tiotropio + salmeterol/fluticasona. Consulta por empeoramiento de disnea en 3 días, expectoración purulenta aumentada, uso de músculos accesorios. FR 30 rpm, FC 104, TA 138/85, SatO2 84%, temperatura 37.8°C. GSA: pH 7.30, PaCO2 62 mmHg, PaO2 48 mmHg. ¿Cuál es el manejo inicial?",
                    "options": [
                        {
                            "id": "a",
                            "text": "O2 controlado (SatO2 objetivo 88-92%) + SABA + SAMA nebulizados + corticoide sistémico + antibiótico",
                            "correct": True,
                            "feedback": "Correcto. En EPOC con hipercapnia, el O2 de alto flujo puede suprimir el drive hipóxico y agravar la hipercapnia. El objetivo de SatO2 es 88-92%, no 98%. Los broncodilatadores nebulizados, el corticoide (reduce el tiempo de recuperación) y el antibiótico (esputo purulento = infección bacteriana) son los pilares.",
                            "next": "n2_tratamiento"
                        },
                        {
                            "id": "b",
                            "text": "O2 al 100% por máscara de reservorio — la SatO2 de 84% es peligrosa",
                            "correct": False,
                            "feedback": "Peligroso en EPOC hipercápnico. El O2 al 100% suprime el drive hipóxico (que en EPOC severo reemplaza al drive hipercápnico cronicamente) y puede causar apnea con hipercapnia fatal. El objetivo es SatO2 88-92%, no normalizar la saturación.",
                            "next": "end_o2_alto_epoc"
                        },
                        {
                            "id": "c",
                            "text": "Furosemida IV — la disnea puede ser por descompensación cardíaca",
                            "correct": False,
                            "feedback": "Incorrecto. La presentación es consistente con EPOC exacerbado (esputo purulento, tabaquista, hipercapnia). Sin edema periférico ni crepitantes, no hay evidencia de descompensación cardíaca. El furosemide empeorará la deshidratación e hiperviscosidad del moco.",
                            "next": "end_diuretico_epoc"
                        }
                    ]
                },
                "n2_tratamiento": {
                    "description": "A la hora post-tratamiento: broncodilatadores + corticoide + antibiótico iniciados, O2 a 1.5 L/min (SatO2 89%). Control GSA: pH 7.27, PaCO2 68 mmHg (empeoró). El paciente está más agotado, FR 32 rpm, no puede completar frases. ¿Qué haces?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Ventilación No Invasiva (BiPAP) — insuficiencia respiratoria hipercápnica con acidosis",
                            "correct": True,
                            "feedback": "Correcto. La VNI (BiPAP) está fuertemente recomendada en EPOC con insuficiencia respiratoria hipercápnica (pH <7.35, PaCO2 >45). Reduce la mortalidad, evita la intubación en el 50% de los casos y disminuye la estadía en UCI. Es el tratamiento de elección antes de la intubación.",
                            "next": "n3_vni"
                        },
                        {
                            "id": "b",
                            "text": "Intubación orotraqueal inmediata",
                            "correct": False,
                            "feedback": "Prematuro. La VNI debe intentarse primero en EPOC con acidosis respiratoria. La intubación tiene mortalidad propia significativa en EPOC (difícil destete) y debe reservarse para falla de la VNI o contraindicaciones a la misma.",
                            "next": "end_intubacion_precoz_epoc"
                        },
                        {
                            "id": "c",
                            "text": "Continuar igual y repetir GSA en 2 horas",
                            "correct": False,
                            "feedback": "Peligroso. El pH de 7.27 con PaCO2 en ascenso indica que el paciente se está fatigando. Sin escalar el tratamiento, puede presentar paro respiratorio. La VNI debe iniciarse sin más demora.",
                            "next": "end_esperar_epoc"
                        }
                    ]
                },
                "n3_vni": {
                    "description": "BiPAP iniciado (IPAP 14, EPAP 5). A las 4 horas: pH 7.35, PaCO2 55 mmHg, SatO2 91%. El paciente está más confortable y puede dormir con la máscara. ¿Cuál es el plan?",
                    "options": [
                        {
                            "id": "a",
                            "text": "Continuar VNI nocturna + completar antibiótico 5-7 días + corticoide 5 días + fisioterapia respiratoria",
                            "correct": True,
                            "feedback": "Correcto. La respuesta a las 4h es un buen predictor de éxito de la VNI. Se continúa de forma discontinua (con descansos para comidas y movilización). El antibiótico y corticoide se completan. La fisioterapia ayuda a movilizar secreciones.",
                            "next": "end_exito"
                        },
                        {
                            "id": "b",
                            "text": "Retirar la VNI — el pH se normalizó",
                            "correct": False,
                            "feedback": "Prematuro. La normalización del pH a las 4h no significa que el paciente tolere sin VNI. El destete de la VNI se hace progresivamente, primero retirando durante el día y manteniendo de noche, y evaluando la tolerancia con GSA.",
                            "next": "end_retirar_vni_precoz"
                        }
                    ]
                },
                "end_exito": {
                    "terminal": True,
                    "result": "success",
                    "description": "Manejo correcto: O2 controlado, broncodilatadores, corticoide sistémico, antibiótico (amoxicilina-clavulánico) y VNI precoz ante acidosis. Alta al 6to día con O2 domiciliario, VNI nocturna domiciliaria y derivación a rehabilitación pulmonar. Abandono del tabaco reforzado.",
                    "pearl": "Perla clínica: La VNI en EPOC exacerbado grave (pH 7.25-7.35) reduce la mortalidad en un 50%, la necesidad de intubación en un 65% y la estadía hospitalaria en 3 días. Es uno de los tratamientos con mayor nivel de evidencia en medicina intensiva."
                },
                "end_o2_alto_epoc": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El O2 al 100% suprimió el drive hipóxico. El PaCO2 subió a 85 mmHg y el pH bajó a 7.18. El paciente entró en narcosis por CO2 (somnolencia, Glasgow 8) y requirió intubación de urgencia. Complicación clásica y completamente prevenible en EPOC.",
                    "pearl": "Perla clínica: En EPOC con hipercapnia crónica, el riñón compensa reteniendo bicarbonato, por lo que el pH puede ser normal con PaCO2 de 60-70. Estos pacientes toleran la hipercapnia pero son muy sensibles al O2 excesivo. Meta: SatO2 88-92%, no más."
                },
                "end_diuretico_epoc": {
                    "terminal": True,
                    "result": "warning",
                    "description": "El furosemide causó deshidratación con espesamiento del moco bronquial, dificultando aún más la expectoration. La causa de la disnea era el EPOC exacerbado, no la insuficiencia cardíaca. Se perdió tiempo valioso con un tratamiento incorrecto.",
                    "pearl": "Perla clínica: El cor pulmonale (insuficiencia cardíaca derecha por EPOC) puede coexistir con el EPOC exacerbado. Diferenciación: EPOC puro = hipercapnia + sin crepitantes + sin edema bilateral. Cor pulmonale = ingurgitación yugular + edema simétrico + hepatomegalia. La ecografía a pie de cama es invaluable."
                },
                "end_intubacion_precoz_epoc": {
                    "terminal": True,
                    "result": "warning",
                    "description": "La intubación fue exitosa pero generó dependencia prolongada del ventilador. El EPOC severo tiene músculo respiratorio debilitado — el destete tardó 18 días. Con VNI, probablemente hubiera evitado la intubación. Alta de UCI al día 22.",
                    "pearl": "Perla clínica: La intubación en EPOC tiene consecuencias significativas: el destete es difícil (EPOC = hiperinsuflación dinámica + músculo fatigado), tasa de traqueotomía del 30% en exacerbaciones graves, y mortalidad hospitalaria del 25%. La VNI evita estos riesgos cuando está indicada."
                },
                "end_esperar_epoc": {
                    "terminal": True,
                    "result": "failure",
                    "description": "El paciente entró en paro respiratorio 45 minutos después. La intubación de urgencia en paro es significativamente más riesgosa que la intubación planificada. La VNI iniciada a tiempo hubiera evitado este desenlace. El pH 7.27 con tendencia descendente era señal inequívoca de alarma.",
                    "pearl": "Perla clínica: Indicadores de necesidad urgente de VNI en EPOC: pH <7.35 + PaCO2 en ascenso + FR >25 + uso de músculos accesorios + incapacidad de completar frases. Si hay dos o más criterios: VNI inmediata, no observar."
                },
                "end_retirar_vni_precoz": {
                    "terminal": True,
                    "result": "warning",
                    "description": "Sin VNI, el pH volvió a 7.29 y PaCO2 subió a 72 mmHg en 3 horas. Se debió reiniciar la VNI. El destete prematuro es la causa más frecuente de fracaso de la VNI. El paciente tuvo 6 horas adicionales de VNI innecesarias por el retiro precoz.",
                    "pearl": "Perla clínica: Destete de VNI en EPOC: primero retirar durante el día (períodos de 2-4h con O2 solo), manteniendo de noche. Se evalúa tolerancia con GSA. Solo se retira completamente cuando el pH se mantiene >7.35 y PaCO2 estable durante varias horas sin VNI."
                }
            }
        }
    }
]
