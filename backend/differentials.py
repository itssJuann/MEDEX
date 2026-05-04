DIFFERENTIALS = [
    {
        "id": "dolor-toracico-agudo",
        "title": "Dolor Torácico Agudo",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "presentation": "Paciente masculino de 58 años, hipertenso, diabético y fumador de 30 paquetes/año. Consulta por dolor retroesternal opresivo de inicio brusco hace 90 minutos, irradiado al brazo izquierdo y mandíbula, acompañado de diaforesis profusa y náuseas. TA 150/95 mmHg, FC 98 lpm, FR 18 rpm, SatO2 96%.",
        "diagnoses": [
            {
                "id": "iamcest",
                "name": "IAM con elevación del ST (IAMCEST)",
                "correct": True,
                "initial_hint": "Dolor opresivo irradiado con factores de riesgo cardiovascular múltiples."
            },
            {
                "id": "iamsest",
                "name": "IAMSEST / Angina Inestable",
                "correct": False,
                "initial_hint": "Síntomas muy similares al IAMCEST. Solo el ECG y la troponina los diferencian."
            },
            {
                "id": "tep",
                "name": "Tromboembolismo Pulmonar",
                "correct": False,
                "initial_hint": "Puede producir dolor pleurítico y disnea. Menos típico sin hipoxemia ni taquicardia."
            },
            {
                "id": "pericarditis",
                "name": "Pericarditis Aguda",
                "correct": False,
                "initial_hint": "Produce dolor torácico que mejora al inclinarse hacia adelante. Menos opresivo."
            },
            {
                "id": "diseccion",
                "name": "Disección Aórtica",
                "correct": False,
                "initial_hint": "Dolor desgarrante, irradiado a la espalda, de inicio brusco. Sin factores de riesgo específicos aquí."
            },
            {
                "id": "erge",
                "name": "ERGE / Espasmo Esofágico",
                "correct": False,
                "initial_hint": "Puede simular dolor coronario. Generalmente sin diaforesis ni irradiación al brazo."
            }
        ],
        "clues": [
            {
                "id": "c1",
                "text": "ECG de 12 derivaciones: elevación del segmento ST de 3mm en derivaciones V1-V4. Imagen en espejo (descenso ST) en derivaciones inferiores.",
                "question": "Con este ECG, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "tep": "El TEP raramente produce elevación del ST localizada. Típicamente muestra taquicardia sinusal o patrón S1Q3T3, no elevación de ST anterior.",
                    "pericarditis": "La pericarditis produce elevación del ST cóncava ('en silla de montar') y difusa en múltiples territorios, no la elevación convexa y localizada en V1-V4 que vemos aquí.",
                    "diseccion": "La disección aórtica no produce elevación del ST típica (salvo que comprometa el ostium coronario). El dolor de la disección es desgarrante y de máxima intensidad al inicio.",
                    "erge": "El ERGE y el espasmo esofágico no producen cambios en el ECG. Un ECG normal descarta el origen esofágico como causa de este cuadro."
                },
                "cannot_eliminate": {
                    "iamcest": "La elevación del ST en V1-V4 confirma isquemia transmural anterior — es el hallazgo cardinal del IAMCEST.",
                    "iamsest": "Aún no puedes eliminarlo solo con el ECG. Aunque el ST elevado apunta a IAMCEST, necesitas la troponina para confirmar necrosis."
                }
            },
            {
                "id": "c2",
                "text": "Troponina I seriada: basal 0.8 ng/mL → a las 3h: 4.2 ng/mL (VN <0.04). Curva ascendente confirmada. Ecocardiograma urgente: hipocinesia severa de pared anterior y apex.",
                "question": "Con la troponina y el ecocardiograma, ¿qué diagnóstico puedes eliminar ahora?",
                "eliminates": {
                    "iamsest": "El IAMSEST/Angina Inestable se define por ausencia de elevación del ST Y troponina normal o levemente elevada. Con troponina en 4.2 ng/mL en ascenso + elevación del ST + hipocinesia anterior: es IAMCEST sin dudas."
                },
                "cannot_eliminate": {
                    "iamcest": "Todo confirma el IAMCEST: elevación del ST localizada, troponina muy elevada en curva ascendente e hipocinesia ecocardiográfica del territorio de la DA."
                }
            }
        ],
        "resolution": "IAMCEST anterior extenso por oclusión de la arteria descendente anterior (DA) proximal. La tríada diagnóstica es: dolor típico + elevación del ST en territorio coronario + troponina elevada en curva ascendente. La hipocinesia ecocardiográfica confirma la zona de necrosis.",
        "pearl": "Perla clínica: El tiempo es músculo. Cada 30 minutos de retraso en la reperfusión aumenta la mortalidad a 30 días en un 7.5%. El diagnóstico diferencial no debe retrasar el activar el protocolo de código IAM."
    },
    {
        "id": "disnea-aguda-hipoxemia",
        "title": "Disnea Aguda con Hipoxemia",
        "system": "Respiratorio",
        "difficulty": "Intermedio",
        "presentation": "Paciente femenina de 45 años sin antecedentes relevantes. Consulta por disnea de inicio brusco hace 3 horas, mientras estaba sentada en su escritorio. Refiere dolor pleurítico en hemitórax derecho y una hemoptisis leve. No fiebre. TA 108/70 mmHg, FC 118 lpm, FR 24 rpm, SatO2 88% con aire ambiente. Sin historia de tabaquismo. Toma anticonceptivos orales desde hace 2 años.",
        "diagnoses": [
            {
                "id": "tep",
                "name": "Tromboembolismo Pulmonar",
                "correct": True,
                "initial_hint": "Disnea brusca + dolor pleurítico + hemoptisis + taquicardia + hipoxemia en mujer con ACO."
            },
            {
                "id": "neumo",
                "name": "Neumotórax Espontáneo",
                "correct": False,
                "initial_hint": "Disnea brusca + dolor pleurítico unilateral. Típico en adultos jóvenes delgados."
            },
            {
                "id": "nac",
                "name": "Neumonía Adquirida en la Comunidad",
                "correct": False,
                "initial_hint": "Dolor pleurítico + hipoxemia. Pero la fiebre está ausente y el inicio fue muy brusco."
            },
            {
                "id": "icc",
                "name": "Insuficiencia Cardíaca Aguda",
                "correct": False,
                "initial_hint": "Produce disnea e hipoxemia. Generalmente con crepitantes, edema y ortopnea."
            },
            {
                "id": "crisis_asma",
                "name": "Crisis Asmática",
                "correct": False,
                "initial_hint": "Disnea aguda con hipoxemia. Sin antecedentes de asma ni sibilancias descritas."
            }
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Auscultación: murmullo vesicular normal bilateral, sin sibilancias ni crepitantes. Sin ingurgitación yugular. Sin edema en miembros inferiores. RxTx: sin infiltrados, sin cardiomegalia, sin derrame. Índice de Wells calculado: 7.5 puntos (probabilidad ALTA).",
                "question": "Con la auscultación normal y la radiografía sin infiltrados, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "nac": "La NAC produce consolidación en la RxTx y en la auscultación (crepitantes, matidez, pectoriloquia áfona). Una radiografía normal prácticamente la descarta como causa de hipoxemia severa.",
                    "icc": "La ICC con hipoxemia produce crepitantes bilaterales, ingurgitación yugular, cardiomegalia en RxTx y edema periférico — ninguno de los cuales está presente aquí.",
                    "crisis_asma": "La crisis asmática produce sibilancias bilaterales en la auscultación, que están ausentes. Además no hay antecedentes de asma."
                },
                "cannot_eliminate": {
                    "tep": "El TEP produce RxTx normal o inespecífica en el 40% de los casos. La auscultación es normal en el TEP sin infarto pulmonar.",
                    "neumo": "El neumotórax puede producir disminución del murmullo, pero en neumotórax pequeños la auscultación puede ser normal."
                }
            },
            {
                "id": "c2",
                "text": "TC angiografía pulmonar: defectos de relleno en arterias lobares derechas e izquierda inferior, confirmando trombos. Sin neumotórax. Doppler venoso: trombosis venosa profunda en vena poplítea derecha.",
                "question": "Con la TCAP, ¿qué diagnóstico puedes eliminar definitivamente?",
                "eliminates": {
                    "neumo": "La TCAP es una TC de tórax de alta resolución — el neumotórax habría sido visible como hipertransparencia sin trama vascular. Su ausencia lo descarta definitivamente."
                },
                "cannot_eliminate": {
                    "tep": "La TCAP confirma el TEP: defectos de relleno = trombos en las arterias pulmonares. Diagnóstico confirmado."
                }
            }
        ],
        "resolution": "Tromboembolismo Pulmonar bilateral submasivo. La combinación de disnea brusca + dolor pleurítico + hemoptisis + taquicardia + hipoxemia + ACO en mujer configura una probabilidad pretest muy alta (Wells 7.5). La TCAP confirmó el diagnóstico. TVP poplítea derecha como fuente embólica.",
        "pearl": "Perla clínica: Los anticonceptivos orales aumentan el riesgo de TEP 3-5 veces. En toda mujer joven con disnea brusca sin causa aparente, interrogar siempre sobre ACO, embarazo e inmovilización reciente."
    },
    {
        "id": "cefalea-thunderclap",
        "title": "Cefalea de Inicio Brusco",
        "system": "Neurológico",
        "difficulty": "Avanzado",
        "presentation": "Paciente femenina de 42 años sin antecedentes relevantes. Refiere que mientras realizaba actividad física moderada presentó una cefalea 'como un martillazo en la cabeza' de instauración en segundos, la peor de su vida (10/10). Actualmente persiste como cefalea 7/10. No fiebre. No rigidez de nuca. No déficit neurológico focal. TA 138/82, FC 88, Glasgow 15.",
        "diagnoses": [
            {
                "id": "hsa",
                "name": "Hemorragia Subaracnoidea (HSA)",
                "correct": True,
                "initial_hint": "Cefalea en trueno de máxima intensidad instantánea durante esfuerzo — patrón clásico de HSA."
            },
            {
                "id": "migrana",
                "name": "Migraña Severa",
                "correct": False,
                "initial_hint": "Causa más frecuente de cefalea severa. Pero raramente llega a su máxima intensidad en segundos."
            },
            {
                "id": "meningitis",
                "name": "Meningitis Bacteriana",
                "correct": False,
                "initial_hint": "Cefalea intensa + fiebre + rigidez de nuca. Aquí no hay fiebre ni meningismo."
            },
            {
                "id": "hta_maligna",
                "name": "HTA Maligna / Crisis Hipertensiva",
                "correct": False,
                "initial_hint": "Puede producir cefalea severa. La TA aquí es 138/82, no sugiere crisis hipertensiva."
            },
            {
                "id": "tvc",
                "name": "Trombosis Venosa Cerebral",
                "correct": False,
                "initial_hint": "Cefalea progresiva con signos focales o convulsiones. Raramente en trueno."
            }
        ],
        "clues": [
            {
                "id": "c1",
                "text": "TC de cráneo sin contraste: sin hemorragia evidente, sin efecto de masa, ventrículos de tamaño normal. La TC fue realizada 4 horas después del inicio de los síntomas.",
                "question": "La TC es normal. ¿Qué diagnósticos puedes eliminar con este resultado?",
                "eliminates": {
                    "hta_maligna": "La HTA maligna con encefalopatía produce leucoencefalopatía posterior visible en imagen (PRES). Una TC normal prácticamente la descarta como causa de esta cefalea.",
                    "tvc": "La TVC típicamente muestra el signo de la cuerda (trombo en seno venoso) o infarto venoso hemorrágico. Una TC normal hace la TVC muy poco probable como causa de cefalea en trueno aguda."
                },
                "cannot_eliminate": {
                    "hsa": "IMPORTANTE: La TC normal NO descarta la HSA. La sensibilidad de la TC disminuye con el tiempo: 98% en las primeras 12h, pero cae al 85-90% entre 12-24h. Siempre se necesita punción lumbar ante sospecha de HSA con TC normal.",
                    "migrana": "La migraña no produce hallazgos en la TC — una TC normal no puede confirmar ni descartar migraña.",
                    "meningitis": "La meningitis bacteriana precoz puede tener TC normal. La ausencia de fiebre y rigidez de nuca reduce su probabilidad, pero no la descarta con la TC."
                }
            },
            {
                "id": "c2",
                "text": "Punción lumbar realizada: LCR con xantocromía (coloración amarillenta) visible a ojo desnudo. Eritrocitos: 12.000/mm³ en los 4 tubos (no disminuyen entre tubo 1 y 4 — descarta punción traumática). Proteínas levemente elevadas.",
                "question": "Con la xantocromía en el LCR, ¿qué diagnósticos puedes eliminar definitivamente?",
                "eliminates": {
                    "migrana": "La migraña produce LCR absolutamente normal. La xantocromía confirma sangre en el espacio subaracnoideo — esto es incompatible con migraña.",
                    "meningitis": "La meningitis bacteriana produce LCR turbio con PMN elevados, glucosa baja y proteínas muy elevadas. El LCR xantocrómico con eritrocitos sin pleocitosis linfocítica descarta meningitis bacteriana."
                },
                "cannot_eliminate": {
                    "hsa": "La xantocromía + eritrocitos uniformes en los 4 tubos confirma la HSA. El LCR xantocrómico indica sangre degradada en el espacio subaracnoideo — hallazgo patognomónico de HSA cuando la TC es negativa."
                }
            }
        ],
        "resolution": "Hemorragia Subaracnoidea (HSA) secundaria a rotura de aneurisma. La cefalea en trueno (thunderclap headache) con inicio en segundos durante esfuerzo es el síntoma cardinal. La TC normal no la descarta — siempre requiere PL. La xantocromía confirma el diagnóstico. Requirió angioTC que identificó aneurisma en la comunicante posterior izquierda.",
        "pearl": "Perla clínica: 'La peor cefalea de mi vida de inicio en segundos' = HSA hasta demostrar lo contrario. El 12% de las HSA tienen TC normal en las primeras horas. La PL es obligatoria si la sospecha clínica es alta y la TC es negativa. El 30% de los pacientes con HSA tienen un 'episodio centinela' ignorado días antes."
    },
    {
        "id": "dolor-abdominal-fid",
        "title": "Dolor Abdominal en Fosa Ilíaca Derecha",
        "system": "Digestivo",
        "difficulty": "Básico",
        "presentation": "Paciente masculino de 24 años, sin antecedentes. Consulta por 24 horas de dolor abdominal que comenzó periumbilical y migró a la fosa ilíaca derecha. Fiebre 38.3°C, náuseas y anorexia. Examen: punto de McBurney doloroso, signo de Blumberg positivo, Rovsing positivo. Leucocitos 14.800 con 87% neutrófilos. Sin síntomas urinarios. Sin diarrea.",
        "diagnoses": [
            {
                "id": "apendicitis",
                "name": "Apendicitis Aguda",
                "correct": True,
                "initial_hint": "Migración del dolor periumbilical a FID + fiebre + leucocitosis + signos peritoneales."
            },
            {
                "id": "colico_renal",
                "name": "Cólico Renal Derecho",
                "correct": False,
                "initial_hint": "Dolor en flanco/FID. Pero típicamente cólico, sin fiebre alta ni signo de Blumberg."
            },
            {
                "id": "adenitis",
                "name": "Adenitis Mesentérica",
                "correct": False,
                "initial_hint": "Causa frecuente de dolor en FID en jóvenes, difícil de distinguir de apendicitis sin imagen."
            },
            {
                "id": "hernia",
                "name": "Hernia Inguinal Complicada",
                "correct": False,
                "initial_hint": "Puede producir dolor en FID. Sin masa inguinal palpable mencionada."
            },
            {
                "id": "ileitis",
                "name": "Ileítis Terminal (Crohn)",
                "correct": False,
                "initial_hint": "Inflamación del íleon terminal que puede simular apendicitis. Sin historia previa de diarrea crónica."
            }
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Ecografía abdominal: apéndice visible, diámetro 10mm, no compresible, con líquido periapendicular libre. Uroanálisis: completamente normal, sin leucocituria ni hematuria.",
                "question": "Con la ecografía y el uroanálisis, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "colico_renal": "El cólico renal produce hematuria microscópica en el 90% de los casos. Un uroanálisis completamente normal prácticamente descarta el cólico renal como causa del cuadro.",
                    "hernia": "La ecografía abdominal habría identificado una hernia inguinal complicada con contenido intestinal. Su ausencia en la imagen la descarta."
                },
                "cannot_eliminate": {
                    "apendicitis": "El apéndice de 10mm no compresible con líquido periapendicular es diagnóstico de apendicitis aguda en la ecografía (VPP >95%).",
                    "adenitis": "La adenitis mesentérica puede coexistir con apendicitis y la ecografía no siempre la diferencia claramente.",
                    "ileitis": "La ileítis terminal puede producir hallazgos similares en la ecografía. Se diferencia por la historia clínica y la TC."
                }
            },
            {
                "id": "c2",
                "text": "Score de Alvarado calculado: 9/10 puntos (migración del dolor 1 + anorexia 1 + náuseas 1 + dolor en FID 2 + rebote 1 + fiebre 1 + leucocitosis 2). El score de 9 tiene valor predictivo positivo >95% para apendicitis.",
                "question": "Con el score de Alvarado de 9/10, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "adenitis": "La adenitis mesentérica típicamente produce un score de Alvarado bajo (3-5). Un score de 9 con ecografía positiva tiene una probabilidad post-test de apendicitis >97%. La adenitis no justifica este cuadro.",
                    "ileitis": "La ileítis de Crohn en debut agudo raramente produce todos los criterios de Alvarado simultáneamente con este puntaje. Además el joven no tiene historia de episodios previos de diarrea crónica o aftas."
                },
                "cannot_eliminate": {
                    "apendicitis": "Score de Alvarado 9 + ecografía positiva + clínica típica = diagnóstico de apendicitis confirmado. Indicación quirúrgica."
                }
            }
        ],
        "resolution": "Apendicitis aguda no complicada. La combinación de score de Alvarado 9/10 + ecografía con apéndice de 10mm no compresible + líquido periapendicular = indicación quirúrgica directa sin necesidad de TC. Apendicectomía laparoscópica realizada. Hallazgo: apendicitis flegmonosa sin perforación.",
        "pearl": "Perla clínica: El score de Alvarado combina clínica y laboratorio con alta precisión diagnóstica. Score 0-4: baja probabilidad (manejo ambulatorio). Score 5-6: probabilidad intermedia (observación + imagen). Score 7-10: alta probabilidad (cirugía directa o con imagen confirmatoria)."
    },
    {
        "id": "fiebre-confusion-adulto-mayor",
        "title": "Fiebre y Confusión en Adulto Mayor",
        "system": "Infeccioso",
        "difficulty": "Avanzado",
        "presentation": "Paciente masculino de 78 años con antecedentes de HTA, DM2 y demencia leve (vive con su familia). Lo traen por fiebre de 38.9°C y confusión aguda desde esta mañana. La familia refiere que estaba bien ayer. Actualmente agitado, no colabora. FC 112, TA 100/65, FR 22, SatO2 92%. Sin rigidez de nuca. Sin focalidad neurológica nueva evidente. Orina turbia con mal olor.",
        "diagnoses": [
            {
                "id": "sepsis_urinaria",
                "name": "Sepsis de Origen Urinario",
                "correct": True,
                "initial_hint": "Fiebre + hipotensión + taquicardia + confusión + orina turbia en adulto mayor = SEPSIS hasta demostrar lo contrario."
            },
            {
                "id": "meningitis",
                "name": "Meningitis Bacteriana",
                "correct": False,
                "initial_hint": "Fiebre + confusión. Pero la rigidez de nuca está ausente y puede ser difícil de evaluar en demencia."
            },
            {
                "id": "encefalopatia_metabolica",
                "name": "Encefalopatía Metabólica",
                "correct": False,
                "initial_hint": "Confusión aguda en diabético — pensar en hipoglucemia, hiperglucemia, hiponatremia."
            },
            {
                "id": "ictus",
                "name": "Ictus / ACV",
                "correct": False,
                "initial_hint": "Confusión aguda de inicio brusco. Sin focalidad neurológica nueva descripta claramente."
            },
            {
                "id": "nac",
                "name": "Neumonía / Sepsis Respiratoria",
                "correct": False,
                "initial_hint": "Causa frecuente de sepsis en adultos mayores. SatO2 92% puede indicar compromiso pulmonar."
            }
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Glucemia capilar: 138 mg/dL (normal). Sodio: 136 mEq/L. Potasio: 3.8 mEq/L. TC de cráneo sin contraste: sin hemorragia, sin infarto agudo visible, atrofia cortical crónica compatible con demencia. Lactato: 3.8 mmol/L (hiperlactatemia).",
                "question": "Con la glucemia, electrolitos y TC normales, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "encefalopatia_metabolica": "La encefalopatía metabólica más frecuente en diabéticos es la hipoglucemia (glucemia normal la descarta) y la hiponatremia (sodio 136 es normal). Sin alteraciones metabólicas identificadas, este diagnóstico es poco probable como causa principal.",
                    "ictus": "El ACV isquémico agudo puede tener TC normal en las primeras horas, pero la confusión difusa sin focalidad neurológica clara y el contexto febril hacen la sepsis mucho más probable. El lactato elevado apunta a hipoperfusión sistémica, no a un evento focal."
                },
                "cannot_eliminate": {
                    "sepsis_urinaria": "El lactato de 3.8 mmol/L confirma hipoperfusión tisular — criterio de shock séptico. La orina turbia + fiebre + hipotensión + taquicardia apuntan fuertemente a foco urinario.",
                    "meningitis": "La TC normal no descarta meningitis. Sin rigidez de nuca clara (difícil en demencia) y con fiebre, debe considerarse PL.",
                    "nac": "La SatO2 92% puede reflejar neumonía — se necesita RxTx."
                }
            },
            {
                "id": "c2",
                "text": "Uroanálisis: 50+ leucocitos/campo, bacterias +++, nitritos positivos. Hemocultivos x2 tomados. RxTx: sin infiltrados, sin derrame pleural. Sedimento urinario con cilindros leucocitarios. Urocultivo pendiente.",
                "question": "Con el uroanálisis y la radiografía, ¿qué diagnósticos puedes eliminar ahora?",
                "eliminates": {
                    "nac": "La radiografía de tórax sin infiltrados ni derrame descarta la neumonía como causa del cuadro de sepsis. La SatO2 92% en este caso se explica mejor por la hipoperfusión sistémica de la sepsis.",
                    "meningitis": "El uroanálisis con piuria masiva, nitritos y cilindros leucocitarios identifica el foco infeccioso urinario. Con una fuente infecciosa clara que justifica el cuadro completo, la meningitis pasa a ser muy poco probable — aunque puede realizarse PL si hay duda clínica."
                },
                "cannot_eliminate": {
                    "sepsis_urinaria": "Uroanálisis compatible con infección urinaria alta (pielonefritis/urosepsis) + hipotensión + taquicardia + lactato elevado + confusión = SEPSIS DE ORIGEN URINARIO confirmada. Iniciar bundle de 1 hora."
                }
            }
        ],
        "resolution": "Urosepsis (sepsis de origen urinario) con criterios de shock séptico. En adultos mayores la confusión aguda es frecuentemente el síntoma de presentación de infecciones graves — equivale a la fiebre en jóvenes. El urocultivo reportó E. coli >100.000 UFC sensible a cefalosporinas. Respuesta a ceftriaxona IV + resucitación con fluidos en las primeras 6 horas.",
        "pearl": "Perla clínica: En adultos mayores con demencia, la confusión aguda o el 'cambio del estado de base' es la presentación más frecuente de infección grave, IAM, TEP y otras emergencias. No asumir que es 'la demencia que avanzó' sin descartar causa aguda tratable."
    },
    {
        "id": "dolor-hipocondrio-derecho",
        "title": "Dolor en Hipocondrio Derecho",
        "system": "Digestivo",
        "difficulty": "Básico",
        "presentation": "Paciente femenina de 38 años, obesa, con antecedente de colelitiasis conocida. Consulta por dolor intenso en hipocondrio derecho de 8 horas de evolución, irradiado a escápula derecha, con náuseas y vómitos. Temperatura 38.6°C, TA 125/80, FC 96 lpm. Dolor a la palpación profunda en HCD con defensa muscular leve.",
        "diagnoses": [
            {"id": "colecistitis", "name": "Colecistitis Aguda", "correct": True, "initial_hint": "Dolor en HCD + fiebre + náuseas + colelitiasis conocida. Murphy positivo clásico."},
            {"id": "colico", "name": "Cólico Biliar Simple", "correct": False, "initial_hint": "Dolor en HCD irradiado a escápula. Pero el cólico biliar no produce fiebre ni leucocitosis."},
            {"id": "hepatitis", "name": "Hepatitis Aguda", "correct": False, "initial_hint": "Causa dolor en HCD. Generalmente con ictericia, transaminasas muy elevadas y sin fiebre tan alta."},
            {"id": "ulcera", "name": "Úlcera Péptica Perforada", "correct": False, "initial_hint": "Dolor abdominal agudo. Pero típicamente epigástrico, con abdomen en tabla y neumoperitoneo."},
            {"id": "neumonia_basal", "name": "Neumonía Basal Derecha", "correct": False, "initial_hint": "Puede referir dolor en HCD. Sin síntomas respiratorios y con antecedente de colelitiasis, es menos probable."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Signo de Murphy positivo. Leucocitos 15.400 con 89% neutrófilos. Bilirrubina total 1.8 mg/dL (levemente elevada). PCR 98 mg/L. Transaminasas normales.",
                "question": "Con fiebre, leucocitosis y Murphy positivo, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "colico": "El cólico biliar simple NO produce fiebre ni leucocitosis. La inflamación de la pared vesicular (colecistitis) es lo que causa estos signos sistémicos. Sin fiebre = cólico; con fiebre = colecistitis.",
                    "hepatitis": "La hepatitis aguda produce transaminasas muy elevadas (>10 veces el valor normal) y rara vez produce signo de Murphy positivo. Las transaminasas normales prácticamente la descartan.",
                    "ulcera": "La úlcera perforada produce abdomen en tabla (rigidez intensa), neumoperitoneo en RxTx y transaminasas/bilirrubina normales. El Murphy positivo localizado en HCD no es característico."
                },
                "cannot_eliminate": {
                    "colecistitis": "Murphy positivo + fiebre + leucocitosis + colelitiasis conocida = colecistitis aguda hasta demostrar lo contrario.",
                    "neumonia_basal": "La neumonía basal puede producir fiebre y leucocitosis. Se necesita una RxTx para descartarla."
                }
            },
            {
                "id": "c2",
                "text": "Ecografía abdominal: vesícula biliar distendida, pared engrosada 6mm (VN <4mm), cálculo enclavado en cuello de 1.8cm, líquido pericolecístico libre. Sin dilatación del colédoco. RxTx: sin infiltrados pulmonares.",
                "question": "Con la ecografía y la radiografía, ¿qué diagnóstico puedes eliminar?",
                "eliminates": {
                    "neumonia_basal": "La RxTx sin infiltrados descarta la neumonía basal derecha como causa del dolor en HCD."
                },
                "cannot_eliminate": {
                    "colecistitis": "Pared vesicular >4mm + cálculo enclavado + líquido pericolecístico = colecistitis aguda confirmada ecográficamente. Criterios de Tokio Grado I-II. Indicación quirúrgica."
                }
            }
        ],
        "resolution": "Colecistitis aguda litiásica grado I (Tokio). La tríada clásica es: dolor en HCD + fiebre + Murphy positivo, sobre una paciente con colelitiasis conocida. La ecografía confirma con alta especificidad. Tratamiento: colecistectomía laparoscópica precoz (<72h) + antibióticos.",
        "pearl": "Perla clínica: Las '5 F' del riesgo de colelitiasis: Female, Fat, Forty, Fertile, Fair (mujer, obesa, 40 años, multípara, piel clara). La colecistitis aguda es la complicación más frecuente de la colelitiasis — ocurre cuando un cálculo se encalla en el cuello vesicular o el cístico."
    },
    {
        "id": "sincope",
        "title": "Síncope — Pérdida Brusca de Conciencia",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "presentation": "Paciente femenina de 28 años sin antecedentes cardíacos. Pérdida de conciencia brusca de 30 segundos mientras estaba de pie en una fila larga bajo el sol. Referida por testigos como caída suave, sin movimientos tónicos clónicos, sin mordedura de lengua. Recuperación completa en 1 minuto, con náuseas residuales. Antes del episodio: mareo, visión borrosa y sensación de calor.",
        "diagnoses": [
            {"id": "vasovagal", "name": "Síncope Vasovagal (Neurocardiogénico)", "correct": True, "initial_hint": "Pródromos clásicos + desencadenante ortostático + recuperación rápida y completa."},
            {"id": "arritmia", "name": "Síncope Cardiogénico por Arritmia", "correct": False, "initial_hint": "El síncope arrítmico es brusco, sin pródromos, y puede ocurrir en cualquier posición."},
            {"id": "ortostatica", "name": "Hipotensión Ortostática", "correct": False, "initial_hint": "Síncope al ponerse de pie por caída de la TA sistólica >20mmHg. Frecuente en deshidratados."},
            {"id": "epilepsia", "name": "Crisis Epiléptica con Pérdida de Conciencia", "correct": False, "initial_hint": "La epilepsia produce movimientos tónico-clónicos, mordedura de lengua y confusión post-ictal."},
            {"id": "hipoglucemia", "name": "Hipoglucemia", "correct": False, "initial_hint": "Pérdida de conciencia por glucemia baja. Sin diabetes ni ayuno prolongado mencionado."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "No hubo movimientos tónico-clónicos ni mordedura de lengua según testigos. La recuperación fue completa en menos de 2 minutos sin confusión post-ictal. ECG: ritmo sinusal, QT normal, sin bloqueos ni preexcitación. Glucemia capilar al llegar a urgencias: 94 mg/dL.",
                "question": "Con el ECG normal, glucemia normal y ausencia de signos post-ictales, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "epilepsia": "La crisis epiléptica generalizada produce: movimientos tónico-clónicos, mordedura de lengua, pérdida de orina y confusión post-ictal prolongada (5-30 min). Nada de esto está presente.",
                    "hipoglucemia": "La glucemia de 94 mg/dL es completamente normal. La hipoglucemia produce síntomas más prolongados y no se recupera espontáneamente sin glucosa exógena.",
                    "arritmia": "El ECG normal descarta las principales causas de síncope arrítmico: QT largo, Wolff-Parkinson-White, Brugada y bloqueo AV de alto grado."
                },
                "cannot_eliminate": {
                    "vasovagal": "Pródromos típicos (mareo, visión borrosa, calor) + desencadenante ortostático + recuperación rápida = síncope vasovagal clásico.",
                    "ortostatica": "La hipotensión ortostática también ocurre en bipedestación prolongada. Se diferencia midiendo la TA en decúbito y de pie."
                }
            },
            {
                "id": "c2",
                "text": "TA en decúbito: 118/76 mmHg. TA a los 3 minutos de bipedestación: 114/74 mmHg (sin caída ortostática). Frecuencia cardíaca en decúbito: 68 lpm. De pie: 72 lpm. Test de mesa basculante (tilt test) positivo: reproduce el síncope con bradicardia y vasodilatación.",
                "question": "Con la TA ortostática normal y el tilt test positivo, ¿qué diagnóstico puedes eliminar?",
                "eliminates": {
                    "ortostatica": "La hipotensión ortostática se define como caída de TA sistólica ≥20mmHg o diastólica ≥10mmHg a los 3 minutos de bipedestación. Aquí la TA es estable — no hay hipotensión ortostática."
                },
                "cannot_eliminate": {
                    "vasovagal": "El tilt test positivo (reproduce síncope con bradicardia refleja y vasodilatación) confirma el mecanismo neurocardiogénico. Es el diagnóstico definitivo."
                }
            }
        ],
        "resolution": "Síncope vasovagal (neurocardiogénico). Es la causa más frecuente de síncope (50% de los casos). El mecanismo es un reflejo vagal exagerado ante desencadenantes (ortostatismo, dolor, emoción) que produce bradicardia y vasodilatación simultáneas. Tratamiento: medidas posturales, hidratación y educación.",
        "pearl": "Perla clínica: La regla ROSE predice síncope de alto riesgo: BNP elevado, bradicardia <50 en ECG, anemia, dolor torácico, ECG anormal. Si ninguno presente en joven con síncope típico → síncope vasovagal, no requiere hospitalización ni estudio cardíaco extenso."
    },
    {
        "id": "hematuria-macroscopica",
        "title": "Hematuria Macroscópica",
        "system": "Renal",
        "difficulty": "Intermedio",
        "presentation": "Paciente masculino de 65 años, fumador de 40 paquetes/año, sin antecedentes urológicos. Consulta por orina 'color rojo' desde ayer, sin dolor, sin fiebre, sin síntomas urinarios irritativos (no disuria, no polaquiuria). Orina de toda la micción es de color rojo uniforme. No ha tenido traumatismo. TA 138/85, afebril.",
        "diagnoses": [
            {"id": "ca_vesical", "name": "Carcinoma Vesical", "correct": True, "initial_hint": "Hematuria indolora en hombre mayor fumador es carcinoma vesical hasta demostrar lo contrario."},
            {"id": "litiasis", "name": "Litiasis Urinaria", "correct": False, "initial_hint": "Causa frecuente de hematuria. Generalmente con cólico renal intenso e irradiación inguinal."},
            {"id": "cistitis", "name": "Cistitis Bacteriana Hemorrágica", "correct": False, "initial_hint": "Puede producir hematuria macroscópica. Pero casi siempre con disuria, polaquiuria y urgencia miccional."},
            {"id": "ca_renal", "name": "Carcinoma de Células Renales", "correct": False, "initial_hint": "Puede producir hematuria indolora. La tríada clásica: hematuria + masa renal + dolor lumbar."},
            {"id": "glomerulonefritis", "name": "Glomerulonefritis Aguda", "correct": False, "initial_hint": "Hematuria + proteinuria + HTA + edema. Más frecuente en jóvenes post-infección estreptocócica."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Uroanálisis: hematíes >50/campo, sin leucocitos, sin nitritos, sin cilindros, proteínas negativas. Hematuria total (toda la micción igual de roja — no inicial ni terminal). Creatinina normal. Eco renal: sin litiasis visible, riñones de tamaño normal sin masa.",
                "question": "Con el uroanálisis sin infección, sin proteínas y la ecografía sin litiasis ni masa renal, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "litiasis": "La ecografía sin litiasis visible, junto con la ausencia de cólico renal, prácticamente descarta la litiasis como causa. Los cálculos >5mm son visibles en la ecografía.",
                    "cistitis": "La cistitis bacteriana produce leucocituria y nitritos positivos en el uroanálisis, y clínicamente cursa con disuria y polaquiuria — todos ausentes aquí.",
                    "glomerulonefritis": "La GN aguda produce hematuria con cilindros eritrocitarios, proteinuria significativa e hipertensión. Sin proteinuria, sin cilindros y función renal normal, la GN es muy poco probable.",
                    "ca_renal": "La ecografía sin masa renal visible hace el carcinoma renal poco probable como causa principal. El CCR produce una masa parenquimatosa visible en imagen."
                },
                "cannot_eliminate": {
                    "ca_vesical": "Hematuria macroscópica indolora, total, en hombre de 65 años fumador sin otra causa identificada = carcinoma vesical hasta demostrar lo contrario. La vejiga no se evalúa bien con ecografía — se necesita cistoscopia."
                }
            },
            {
                "id": "c2",
                "text": "Cistoscopia: lesión papilar de 2.5cm en pared posterior vesical, de aspecto vascularizado. Biopsia: carcinoma urotelial papilar de alto grado, sin invasión muscular (Ta G3).",
                "question": "Con la cistoscopia y biopsia, ¿qué queda confirmado?",
                "eliminates": {},
                "cannot_eliminate": {
                    "ca_vesical": "La cistoscopia con biopsia es el gold standard para el diagnóstico de carcinoma vesical. Carcinoma urotelial Ta G3 — alto riesgo de recurrencia y progresión. Tratamiento: RTU-V + BCG intravesical."
                }
            }
        ],
        "resolution": "Carcinoma vesical urotelial de alto grado no músculo-invasivo (Ta G3). La hematuria macroscópica indolora en hombre mayor fumador requiere cistoscopia mandatoria. El tabaquismo es el principal factor de riesgo (aumenta el riesgo 4 veces). La cistoscopia es el único método que descarta o confirma el carcinoma vesical.",
        "pearl": "Perla clínica: Toda hematuria macroscópica en mayor de 40 años requiere estudio urológico completo (cistoscopia + uro-TC) independientemente de si hay otra 'causa explicable'. El 15% de los pacientes con hematuria macroscópica tienen un tumor urológico. La hematuria nunca es 'benigna por descarte' sin imagen."
    },
    {
        "id": "artritis-monoarticular-aguda",
        "title": "Artritis Monoarticular Aguda",
        "system": "Infeccioso",
        "difficulty": "Intermedio",
        "presentation": "Paciente masculino de 52 años con HTA en tratamiento con hidroclorotiazida. Despertó a las 3am con dolor intensísimo en la primera articulación metatarsofalángica (MTF) del pie derecho (dedo gordo), con eritema, calor y edema que imposibilita apoyar el pie. No fiebre. Refiere haber consumido mariscos y alcohol la noche anterior. Uricemia: 9.8 mg/dL.",
        "diagnoses": [
            {"id": "gota", "name": "Artritis Gotosa Aguda", "correct": True, "initial_hint": "1° MTF + hiperuricemia + desencadenante dietético + diurético tiazídico = gota hasta demostrar lo contrario."},
            {"id": "septica", "name": "Artritis Séptica", "correct": False, "initial_hint": "Artritis aguda monoarticular con gran inflamación local. La artritis séptica es una emergencia — siempre descartar."},
            {"id": "pseudogota", "name": "Pseudogota (PPCD)", "correct": False, "initial_hint": "Depósito de cristales de pirofosfato cálcico. Más frecuente en rodilla y muñeca, raramente en 1° MTF."},
            {"id": "reactiva", "name": "Artritis Reactiva", "correct": False, "initial_hint": "Artritis post-infecciosa (urinaria, GI). Sin antecedente de infección reciente descrito."},
            {"id": "trauma", "name": "Hemartros / Artritis Traumática", "correct": False, "initial_hint": "Artritis por trauma. Sin antecedente de golpe o lesión en el pie."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Temperatura axilar 36.8°C (afebril). GB: 9.200 (normal). PCR: 42 mg/L (levemente elevada). El dolor comenzó durante la noche sin trauma previo. La articulación MTF está clásicamente inflamada ('podagra'). Hidroclorotiazida es un diurético que aumenta la uricemia.",
                "question": "Con afebrilidad, leucocitos normales y contexto clínico típico, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "septica": "La artritis séptica casi siempre produce fiebre y leucocitosis marcada. Un paciente afebril con GB normal tiene baja probabilidad de artritis séptica, aunque idealmente se debe realizar artrocentesis para confirmarlo.",
                    "trauma": "El inicio nocturno espontáneo sin antecedente de trauma descarta el hemartros traumático. La artritis traumática requiere un mecanismo lesional claro.",
                    "reactiva": "La artritis reactiva ocurre 1-4 semanas después de una infección urogenital o gastrointestinal y típicamente afecta rodillas, tobillos o articulaciones grandes — no la 1° MTF como presentación inicial."
                },
                "cannot_eliminate": {
                    "gota": "Podagra (artritis del primer dedo) + hiperuricemia + tiazida + desencadenante alimentario = gota con probabilidad >90% antes de la artrocentesis.",
                    "pseudogota": "Aunque la pseudogota rara vez afecta la MTF, sin artrocentesis no puede excluirse completamente."
                }
            },
            {
                "id": "c2",
                "text": "Artrocentesis de la 1° MTF: líquido amarillo turbio, 18.000 leucocitos/mm³ (predominio PMN). Microscopía con luz polarizada: cristales en forma de aguja con birrefringencia negativa (color amarillo cuando paralelos al eje del compensador). Gram y cultivo: negativos.",
                "question": "Con los cristales de urato y el cultivo negativo, ¿qué diagnóstico puedes confirmar y cuál eliminar?",
                "eliminates": {
                    "pseudogota": "Los cristales de pseudogota (PPCD) son romboidales con birrefringencia positiva (azul cuando paralelos). Los cristales aquí son en aguja con birrefringencia negativa — son cristales de urato monosódico, no PPCD."
                },
                "cannot_eliminate": {
                    "gota": "Cristales de urato monosódico en forma de aguja con birrefringencia negativa + cultivo negativo = diagnóstico definitivo de gota aguda. El gold standard es la identificación de cristales en el líquido sinovial."
                }
            }
        ],
        "resolution": "Artritis gotosa aguda (podagra). La hidroclorotiazida reduce la excreción renal de urato, siendo un precipitante frecuente. El alcohol y los mariscos aumentan la producción de urato. Tratamiento de la crisis: colchicina o AINEs. A largo plazo: alopurinol para reducir uricemia <6 mg/dL y cambiar el diurético tiazídico.",
        "pearl": "Perla clínica: La artrocentesis es OBLIGATORIA ante cualquier artritis monoarticular aguda para descartar artritis séptica (emergencia con destrucción articular en horas). La artritis séptica puede coexistir con la gota ('gota infectada'). Nunca diagnosticar gota sin artrocentesis en la primera crisis."
    },
    {
        "id": "ictericia-obstructiva",
        "title": "Ictericia de Aparición Progresiva",
        "system": "Digestivo",
        "difficulty": "Avanzado",
        "presentation": "Paciente masculino de 70 años, no alcohólico, sin antecedentes hepáticos. Consulta por ictericia progresiva de 6 semanas de evolución, prurito generalizado, coluria (orina oscura) y acolia (heces pálidas). Pérdida de 8 kg en 2 meses sin causa aparente. Dolor sordo en epigastrio/HCD. Sin fiebre. Sin historia de litiasis. Bilirrubina total 12 mg/dL, directa 10 mg/dL. Fosfatasa alcalina 520 UI/L (VN <120).",
        "diagnoses": [
            {"id": "ca_pancreas", "name": "Adenocarcinoma de Páncreas", "correct": True, "initial_hint": "Ictericia obstructiva indolora + pérdida de peso en mayor de 60 años = páncreas hasta demostrar lo contrario."},
            {"id": "coledocolitiasis", "name": "Coledocolitiasis", "correct": False, "initial_hint": "Causa más frecuente de ictericia obstructiva. Generalmente con historia de colelitiasis y dolor cólico previo."},
            {"id": "colangiocarcinoma", "name": "Colangiocarcinoma", "correct": False, "initial_hint": "Tumor de la vía biliar. Puede producir ictericia obstructiva similar al cáncer de páncreas."},
            {"id": "hepatitis", "name": "Hepatitis Aguda Grave", "correct": False, "initial_hint": "La hepatitis produce ictericia por daño hepatocelular, no obstructiva. Transaminasas muy elevadas."},
            {"id": "cirrosis", "name": "Cirrosis con Ictericia", "correct": False, "initial_hint": "La cirrosis puede producir ictericia, pero de tipo hepatocelular, con estigmas de hepatopatía crónica."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Transaminasas (GOT/GPT): levemente elevadas (2-3 veces el valor normal). Ecografía abdominal: vía biliar intrahepática dilatada, colédoco de 18mm (VN <8mm), vesícula distendida sin cálculos visibles. Signo de Courvoisier positivo (vesícula palpable e indolora).",
                "question": "Con la bilirrubina predominantemente directa, FA muy elevada, colédoco dilatado sin cálculos y signo de Courvoisier, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "hepatitis": "La hepatitis aguda produce patrón hepatocelular: transaminasas >10 veces lo normal con FA levemente elevada. Aquí el patrón es claramente colestásico (FA muy elevada, transaminasas levemente elevadas). La hepatitis no produce dilatación de la vía biliar.",
                    "cirrosis": "La cirrosis produce ictericia hepatocelular sin dilatación de la vía biliar. El signo de Courvoisier (vesícula distendida e indolora) es incompatible con cirrosis y apunta a obstrucción distal de la vía biliar.",
                    "coledocolitiasis": "El signo de Courvoisier (vesícula grande e indolora) + historia sin colelitiasis + pérdida de peso apuntan a una obstrucción tumoral. La ley de Courvoisier establece que la vesícula distendida e indolora con ictericia obstructiva indica causa tumoral, no litiásica (los cálculos producen vesícula fibrótica y contraída)."
                },
                "cannot_eliminate": {
                    "ca_pancreas": "Ictericia obstructiva progresiva + pérdida de peso + signo de Courvoisier en hombre mayor = cáncer de páncreas cabeza hasta demostrar lo contrario.",
                    "colangiocarcinoma": "El colangiocarcinoma también puede producir ictericia obstructiva con colédoco dilatado. Se diferencia por la localización de la obstrucción en imagen."
                }
            },
            {
                "id": "c2",
                "text": "TC de abdomen con contraste: masa hipodensa de 3.2cm en cabeza del páncreas con dilatación del conducto de Wirsung (signo del doble conducto — dilatación simultánea de colédoco y Wirsung). Adenopatías peripancreáticas. CA 19-9: 1.840 U/mL (VN <37).",
                "question": "Con la masa pancreática, el signo del doble conducto y el CA 19-9 muy elevado, ¿qué diagnóstico puedes eliminar?",
                "eliminates": {
                    "colangiocarcinoma": "El colangiocarcinoma obstruye la vía biliar pero NO dilata el conducto de Wirsung. El signo del doble conducto (colédoco + Wirsung dilatados simultáneamente) es prácticamente patognomónico de adenocarcinoma de cabeza de páncreas."
                },
                "cannot_eliminate": {
                    "ca_pancreas": "Masa en cabeza de páncreas + signo del doble conducto + CA 19-9 muy elevado + clínica compatible = adenocarcinoma de páncreas confirmado. Estadificación completa y evaluación de resecabilidad."
                }
            }
        ],
        "resolution": "Adenocarcinoma de cabeza de páncreas estadio III (con adenopatías). La ictericia obstructiva indolora + pérdida de peso en mayor de 60 años es la presentación clásica. El signo del doble conducto en TC es prácticamente diagnóstico. Pronóstico grave: sobrevida a 5 años <10%. Solo el 20% son resecables al diagnóstico.",
        "pearl": "Perla clínica: Ley de Courvoisier: vesícula palpable + indolora + ictericia obstructiva = causa tumoral (NO litiásica). Los cálculos producen colecistitis crónica con vesícula fibrótica contraída. El signo de Courvoisier positivo debe urgir la búsqueda de neoplasia pancreática o biliar."
    },
    {
        "id": "edema-miembros-inferiores",
        "title": "Edema Bilateral de Miembros Inferiores",
        "system": "Cardiovascular",
        "difficulty": "Básico",
        "presentation": "Paciente masculino de 55 años con antecedente de consumo excesivo de alcohol durante años. Consulta por aumento progresivo del volumen abdominal y edema en ambos miembros inferiores desde hace 3 semanas. Refiere ictericia leve, cansancio extremo y pérdida de apetito. En el examen: ascitis evidente, circulación colateral abdominal, eritema palmar, telangiectasias en tronco, escleras ictéricas. TA 100/65, FC 88.",
        "diagnoses": [
            {"id": "cirrosis", "name": "Cirrosis Hepática Descompensada", "correct": True, "initial_hint": "Alcohol crónico + ascitis + circulación colateral + estigmas de hepatopatía = cirrosis descompensada."},
            {"id": "icc", "name": "Insuficiencia Cardíaca Congestiva", "correct": False, "initial_hint": "Causa frecuente de edema bilateral y ascitis. Produce ortopnea, crepitantes y cardiomegalia."},
            {"id": "nefrotico", "name": "Síndrome Nefrótico", "correct": False, "initial_hint": "Edema masivo por hipoalbuminemia + proteinuria >3.5g/día. Más facial y generalizado."},
            {"id": "venosa", "name": "Insuficiencia Venosa Crónica", "correct": False, "initial_hint": "Edema bilateral de MMII. Sin ascitis, sin estigmas sistémicos."},
            {"id": "linfedema", "name": "Linfedema Bilateral", "correct": False, "initial_hint": "Edema de MMII por obstrucción linfática. Sin fóvea, sin ascitis, sin estigmas sistémicos."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Sin ortopnea ni disnea de esfuerzo. Auscultación cardiopulmonar: sin crepitantes, sin tercer ruido. RxTx: sin cardiomegalia, sin redistribución vascular. Uroanálisis: sin proteinuria. Albúmina sérica: 2.2 g/dL. Bilirrubina total: 3.8 mg/dL. Transaminasas: 2-3 veces el valor normal.",
                "question": "Con la ausencia de síntomas cardíacos, RxTx normal y uroanálisis sin proteinuria, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "icc": "La ICC produce ortopnea, disnea de esfuerzo, crepitantes bibasales, tercer ruido y cardiomegalia en RxTx. Ninguno de estos signos está presente. La ausencia de todos los criterios de Framingham prácticamente descarta la ICC.",
                    "nefrotico": "El síndrome nefrótico produce proteinuria masiva (>3.5g/día) como criterio diagnóstico cardinal. Un uroanálisis sin proteinuria lo descarta definitivamente.",
                    "venosa": "La insuficiencia venosa crónica produce edema de MMII pero NO produce ascitis, ni hipoalbuminemia, ni ictericia, ni los estigmas sistémicos presentes.",
                    "linfedema": "El linfedema es un edema no con fóvea (duro) que afecta partes distales. No produce ascitis ni los signos sistémicos de hepatopatía."
                },
                "cannot_eliminate": {
                    "cirrosis": "Alcohol crónico + ascitis + circulación colateral + eritema palmar + telangiectasias + ictericia + hipoalbuminemia = cirrosis descompensada. El cuadro es altamente específico."
                }
            },
            {
                "id": "c2",
                "text": "Ecografía abdominal: hígado nodular de bordes irregulares con aumento de la ecogenicidad (patrón cirrótico), esplenomegalia (bazo 16cm), ascitis moderada. Doppler portal: flujo hepatopetal conservado. Child-Pugh B (7 puntos). MELD score: 14.",
                "question": "Con la ecografía que confirma el patrón cirrótico, ¿qué queda confirmado?",
                "eliminates": {},
                "cannot_eliminate": {
                    "cirrosis": "Hígado nodular + esplenomegalia + ascitis + estigmas clínicos + alcohol crónico = cirrosis hepática descompensada confirmada. Child-Pugh B indica disfunción hepática moderada. Iniciar tratamiento de la descompensación (diuréticos, restricción sódica, profilaxis de PBE)."
                }
            }
        ],
        "resolution": "Cirrosis hepática alcohólica descompensada (Child-Pugh B). La descompensación se manifiesta como ascitis, encefalopatía, hemorragia variceal o ictericia. Los estigmas de hepatopatía crónica (eritema palmar, telangiectasias, circulación colateral, ginecomastia) son claves diagnósticas. Abstinencia alcohólica es la única medida que modifica la historia natural.",
        "pearl": "Perla clínica: Los estigmas de hepatopatía crónica permiten el diagnóstico clínico: arañas vasculares (>5 son significativas), eritema palmar, leuconiquia, acropaquias, ginecomastia, atrofia testicular, circulación colateral abdominal (caput medusae). Su presencia obliga a buscar cirrosis."
    },
    {
        "id": "palpitaciones-agudas",
        "title": "Palpitaciones de Inicio Brusco",
        "system": "Cardiovascular",
        "difficulty": "Intermedio",
        "presentation": "Paciente femenina de 32 años sin antecedentes cardíacos. Consulta por palpitaciones de inicio brusco hace 40 minutos, que describe como 'el corazón muy rápido y regular'. Leve mareo pero no síncope. Sin dolor torácico. TA 118/76 mmHg, FC 178 lpm, SatO2 98%. El propio paciente refiere que ha tenido episodios similares desde joven que ceden solos o con maniobras de Valsalva.",
        "diagnoses": [
            {"id": "tsv", "name": "Taquicardia Supraventricular Paroxística (AVNRT)", "correct": True, "initial_hint": "FC regular de 178 en mujer joven + inicio y fin brusco + cede con Valsalva = TSV clásica."},
            {"id": "fa", "name": "Fibrilación Auricular", "correct": False, "initial_hint": "Taquiarritmia frecuente. Irregularmente irregular — si el pulso es regular, la FA es menos probable."},
            {"id": "flutter", "name": "Flutter Auricular", "correct": False, "initial_hint": "Ritmo regular a 150 lpm clásicamente (relación 2:1). Posible pero menos típico en jóvenes."},
            {"id": "tv", "name": "Taquicardia Ventricular", "correct": False, "initial_hint": "Taquicardia de QRS ancho. Emergencia que produce síncope e hipotensión. Más en cardiopatía estructural."},
            {"id": "sinusal", "name": "Taquicardia Sinusal Reactiva", "correct": False, "initial_hint": "FC elevada por fiebre, anemia, ansiedad o hipertiroidismo. Raramente llega a 178 lpm en reposo."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "ECG durante el episodio: taquicardia de QRS estrecho (<120ms), regular a 178 lpm. No se identifican ondas P claramente (o están inmediatamente después del QRS — P retrógrada). Maniobra de Valsalva realizada: terminó el episodio abruptamente. ECG post-cardioversión: ritmo sinusal a 72 lpm, sin preexcitación, sin QT largo.",
                "question": "Con el QRS estrecho, la regularidad y la respuesta al Valsalva, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "tv": "La taquicardia ventricular produce QRS ANCHO (>120ms) y es una emergencia con compromiso hemodinámico. Un QRS estrecho con paciente estable prácticamente descarta la TV.",
                    "fa": "La FA es irregularmente irregular. Un ritmo estrictamente regular a 178 lpm descarta la fibrilación auricular.",
                    "sinusal": "La taquicardia sinusal raramente supera los 150 lpm en reposo, es gradual (no de inicio brusco) y no termina abruptamente con Valsalva. La terminación brusca con maniobra vagal es característica de TSV por reentrada."
                },
                "cannot_eliminate": {
                    "tsv": "QRS estrecho + regular + inicio/fin bruscos + termina con Valsalva + P retrógrada = AVNRT (reentrada nodal) con alta probabilidad.",
                    "flutter": "El flutter puede terminar con maniobras vagales aunque es menos frecuente. Sin ver las ondas F en serrucho claramente, no puede descartarse completamente."
                }
            },
            {
                "id": "c2",
                "text": "ECG post-episodio revisado con atención: sin ondas F en serrucho en derivaciones inferiores (II, III, aVF) ni en V1. Estudio electrofisiológico (EEF): inducción reproducible de taquicardia con S1S2 con salto y eco auricular. Diagnóstico definitivo: AVNRT típica (slow-fast).",
                "question": "Con la ausencia de ondas F y el EEF, ¿qué diagnóstico puedes eliminar definitivamente?",
                "eliminates": {
                    "flutter": "El flutter auricular produce ondas F en serrucho claramente visibles en II, III, aVF y V1. Su ausencia y el EEF con inducción de AVNRT lo descartan definitivamente."
                },
                "cannot_eliminate": {
                    "tsv": "EEF confirma AVNRT típica (slow-fast): la reentrada usa la vía lenta para conducir anterógradamente y la rápida retrógrada. Tratamiento definitivo: ablación por radiofrecuencia del nodo lento (tasa de éxito >95%)."
                }
            }
        ],
        "resolution": "Taquicardia supraventricular paroxística por reentrada nodal (AVNRT típica). Es la TSV más frecuente en mujeres jóvenes. Los episodios recurrentes desde la juventud y la respuesta a Valsalva son claves diagnósticas. La ablación por radiofrecuencia es curativa en >95% de los casos.",
        "pearl": "Perla clínica: Algoritmo de taquicardias de QRS estrecho: regular → TSV o flutter 2:1 → maniobra vagal o adenosina: si termina = TSV por reentrada; si no termina pero aparecen ondas F = flutter. Irregular → FA. La adenosina (6-12mg IV rápido) termina la TSV por reentrada nodal y es diagnóstica y terapéutica."
    },
    {
        "id": "hemoptisis",
        "title": "Hemoptisis en Paciente Fumador",
        "system": "Respiratorio",
        "difficulty": "Avanzado",
        "presentation": "Paciente masculino de 58 años, fumador de 45 paquetes/año. Consulta por hemoptisis (expectoración con sangre roja) de 3 semanas de evolución, moderada (menos de 100mL/día), asociada a tos productiva crónica y pérdida de 6kg en 2 meses. Sin fiebre. Sin disnea de reposo. SatO2 95%. Auscultación: murmullo vesicular disminuido en vértice derecho.",
        "diagnoses": [
            {"id": "ca_bronco", "name": "Carcinoma Broncogénico", "correct": True, "initial_hint": "Fumador intenso + hemoptisis + pérdida de peso = carcinoma broncogénico hasta descartar."},
            {"id": "tbc", "name": "Tuberculosis Pulmonar", "correct": False, "initial_hint": "Causa clásica de hemoptisis con afección en vértices y síntomas constitucionales."},
            {"id": "bronquiectasias", "name": "Bronquiectasias", "correct": False, "initial_hint": "Producen hemoptisis recurrente con expectoración crónica abundante y purulenta."},
            {"id": "absceso", "name": "Absceso Pulmonar", "correct": False, "initial_hint": "Produce hemoptisis con fiebre, expectoración purulenta fétida y imagen cavitada."},
            {"id": "bronquitis", "name": "Bronquitis Aguda", "correct": False, "initial_hint": "Hemoptisis leve por inflamación bronquial aguda. Sin pérdida de peso ni síntomas de 3 semanas."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Temperatura 36.9°C (afebril). GB: 9.800 (normal). RxTx: masa hiliar derecha de 3cm con atelectasia del lóbulo superior derecho. Sin cavitación. Sin infiltrados de aspecto tuberculoso. Baciloscopias de esputo x3: negativas.",
                "question": "Con la masa hiliar en RxTx y las baciloscopias negativas, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "tbc": "Las baciloscopias de esputo negativas x3 reducen significativamente la probabilidad de TBC pulmonar activa bacilífera. Además, la imagen de masa hiliar compacta sin cavitación no es el patrón típico de TBC (que produce infiltrados en vértices con cavitación).",
                    "absceso": "El absceso pulmonar produce imagen cavitada con nivel hidroaéreo, fiebre alta y expectoración fétida — ninguna presente aquí.",
                    "bronquiectasias": "Las bronquiectasias se presentan como imagen en 'rail de tranvía' o quística en la RxTx, no como masa hiliar. La hemoptisis de bronquiectasias es recurrente con expectoración purulenta crónica abundante.",
                    "bronquitis": "La bronquitis aguda no produce masa hiliar, no dura 3 semanas y no causa pérdida de 6kg. Una hemoptisis de 3 semanas con masa en imagen nunca es bronquitis."
                },
                "cannot_eliminate": {
                    "ca_bronco": "Masa hiliar derecha + atelectasia (obstrucción endobronquial por tumor) + fumador + pérdida de peso = carcinoma broncogénico con altísima probabilidad. Requiere TC y broncoscopia urgentes."
                }
            },
            {
                "id": "c2",
                "text": "TC de tórax con contraste: masa espiculada de 3.8cm en hilio derecho con adenopatías mediastínicas (4R y 7) de hasta 2.5cm. Sin metástasis a distancia visibles. Broncoscopia: masa endobronquial obstruyendo bronquio lobar superior derecho. Biopsia: carcinoma de células no pequeñas (adenocarcinoma), EGFR mutado.",
                "question": "Con la biopsia que confirma carcinoma, ¿qué confirmas y qué queda definitivamente descartado?",
                "eliminates": {
                    "tbc": "La biopsia con resultado de adenocarcinoma descarta definitivamente la TBC como causa de la masa y los síntomas."
                },
                "cannot_eliminate": {
                    "ca_bronco": "Adenocarcinoma de pulmón EGFR mutado, estadio IIIA (T2N2M0). La mutación EGFR permite tratamiento con inhibidores de tirosina quinasa (osimertinib). La estadificación completa determinará si es candidato a resección o tratamiento sistémico."
                }
            }
        ],
        "resolution": "Carcinoma broncogénico (adenocarcinoma EGFR+) estadio IIIA. Toda hemoptisis en fumador >40 años requiere TC y broncoscopia — el 20% tienen neoplasia subyacente. La presencia de masa hiliar en RxTx hace mandatoria la investigación urgente. La mutación EGFR es un factor pronóstico favorable y permite terapia dirigida.",
        "pearl": "Perla clínica: Hemoptisis en fumador >40 años = TC de tórax obligatorio. Una RxTx normal NO descarta carcinoma broncogénico (25% son invisibles en RxTx). Las causas más frecuentes de hemoptisis son: bronquitis aguda (más frecuente pero benigna), bronquiectasias, TBC y carcinoma broncogénico — este último es el más importante a descartar."
    },
    {
        "id": "dolor-lumbar-agudo",
        "title": "Dolor Lumbar Agudo Intenso",
        "system": "Renal",
        "difficulty": "Intermedio",
        "presentation": "Paciente masculino de 45 años, sin antecedentes relevantes. Consulta por dolor lumbar derecho de inicio brusco hace 2 horas, intensidad 9/10, tipo cólico con irradiación a la fosa ilíaca derecha y región inguinal. Náuseas y vómitos. Agitado, no puede quedarse quieto. Afebril. TA 145/90 (por dolor), FC 102, SatO2 99%. Sin déficit neurológico. Orina: marrón.",
        "diagnoses": [
            {"id": "litiasis", "name": "Litiasis Renal (Cólico Nefrítico)", "correct": True, "initial_hint": "Cólico lumbar irradiado a ingle + agitación + orina oscura en hombre de 45 años = litiasis hasta demostrar lo contrario."},
            {"id": "pielonefritis", "name": "Pielonefritis Aguda", "correct": False, "initial_hint": "Dolor lumbar + fiebre + síntomas urinarios. Aquí no hay fiebre y el dolor es tipo cólico."},
            {"id": "musculo", "name": "Lumbalgia Muscular / Contractura", "correct": False, "initial_hint": "Causa más frecuente de dolor lumbar. Pero la lumbalgia mecánica no irradia a la ingle ni produce hematuria."},
            {"id": "aneurisma", "name": "Aneurisma Aórtico Abdominal Roto", "correct": False, "initial_hint": "Dolor lumbar súbito en mayor de 60 años. Emergencia vascular con hipotensión y masa pulsátil."},
            {"id": "apendice", "name": "Apendicitis Aguda Retrocecal", "correct": False, "initial_hint": "El apéndice retrocecal puede producir dolor en flanco/fosa ilíaca derecha similar al cólico renal."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "Temperatura 36.7°C (afebril). Uroanálisis: hematíes 50+/campo, sin leucocitos, sin nitritos. Puño-percusión renal derecha: muy dolorosa. El paciente no puede estar quieto (a diferencia de la peritonitis, donde el paciente está inmóvil). Abdomen: sin defensa ni rebote. Sin masa palpable.",
                "question": "Con hematuria sin leucocituria, afebrilidad y sin signos peritoneales, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "pielonefritis": "La pielonefritis produce fiebre (generalmente >38°C), leucocituria y bacteriuria en el uroanálisis. La ausencia de todos estos elementos prácticamente la descarta.",
                    "musculo": "La contractura muscular NO produce hematuria. La hematuria con cólico lumbar que irradia a la ingle es el sello de la litiasis urinaria.",
                    "aneurisma": "El aneurisma roto produce hipotensión, palidez, masa pulsátil abdominal y paciente inmóvil por el dolor peritoneal. Aquí la TA es normal (elevada por el dolor), sin masa y el paciente está agitado pero sin signos de shock.",
                    "apendice": "La apendicitis produce dolor peritoneal con defensa y rebote, fiebre y leucocitosis. El paciente con apendicitis está quieto (el movimiento empeora el dolor peritoneal). Aquí sin signos peritoneales y con hematuria."
                },
                "cannot_eliminate": {
                    "litiasis": "Cólico lumbar irradiado a ingle + hematuria + puño-percusión positiva + paciente agitado que no puede quedarse quieto = cólico nefrítico hasta confirmación por imagen."
                }
            },
            {
                "id": "c2",
                "text": "TC de abdomen sin contraste (uro-TC): cálculo de 6mm en uréter proximal derecho con dilatación de la pelvis renal ipsilateral (hidronefrosis grado II). Sin hidronefrosis izquierda. Sin otros hallazgos.",
                "question": "Con el cálculo visible en la uro-TC, ¿qué queda confirmado?",
                "eliminates": {},
                "cannot_eliminate": {
                    "litiasis": "Cálculo ureteral de 6mm con hidronefrosis = cólico nefrítico confirmado. Los cálculos <5mm suelen expulsarse espontáneamente. Los de 6-9mm tienen 50% de probabilidad de expulsión espontánea. Con 6mm: manejo expectante con alfa-bloqueantes (tamsulosina) + analgesia, o litotricia si no progresa en 4 semanas."
                }
            }
        ],
        "resolution": "Cólico nefrítico por litiasis ureteral derecha de 6mm. La tríada clásica es: dolor lumbar cólico irradiado a la ingle + hematuria + agitación (el paciente NO puede estar quieto). La uro-TC sin contraste es el gold standard diagnóstico (sensibilidad >95%). Tratamiento: analgesia (AINE + opioides) + tamsulosina (alfa-bloqueante que facilita la expulsión).",
        "pearl": "Perla clínica: El paciente con cólico renal es incapaz de quedarse quieto (el dolor no mejora con ninguna posición). El paciente con peritonitis está completamente inmóvil (el movimiento empeora el dolor). Este simple signo diferencia la patología urológica de la quirúrgica abdominal."
    },
    {
        "id": "perdida-peso-hipertiroidismo",
        "title": "Pérdida de Peso Inexplicada",
        "system": "Endocrino",
        "difficulty": "Intermedio",
        "presentation": "Paciente femenina de 35 años sin antecedentes relevantes. Consulta por pérdida de 9kg en 3 meses a pesar de apetito conservado (come bien pero sigue adelgazando). Refiere nerviosismo, insomnio, sensación de calor y palpitaciones frecuentes. Menstruación irregular desde hace 2 meses. Examen: FC 108 lpm, temblor fino en manos, piel caliente y húmeda, bocio difuso palpable de grado II, exoftalmos bilateral leve.",
        "diagnoses": [
            {"id": "hipertiro", "name": "Hipertiroidismo (Enfermedad de Graves)", "correct": True, "initial_hint": "Pérdida de peso con apetito conservado + taquicardia + temblor + bocio + exoftalmos = hipertiroidismo."},
            {"id": "diabetes", "name": "Diabetes Mellitus tipo 1", "correct": False, "initial_hint": "Pérdida de peso + polidipsia/poliuria. Sin mencionar síntomas urinarios. Sin hiperglucemia descrita."},
            {"id": "neoplasia", "name": "Neoplasia Maligna Oculta", "correct": False, "initial_hint": "Pérdida de peso constitucional en adulto joven. Pero con apetito conservado y síntomas adrenérgicos."},
            {"id": "tbc", "name": "Tuberculosis", "correct": False, "initial_hint": "Pérdida de peso + sudoración. Sin tos, sin fiebre, sin exposición conocida."},
            {"id": "ansiedad", "name": "Trastorno de Ansiedad", "correct": False, "initial_hint": "Nerviosismo + palpitaciones + insomnio. Pero no produce pérdida de peso con hiperfagia ni bocio ni exoftalmos."}
        ],
        "clues": [
            {
                "id": "c1",
                "text": "TSH: <0.01 mUI/L (suprimida, VN 0.4-4.0). T4 libre: 4.8 ng/dL (elevada, VN 0.8-1.8). T3 total: 380 ng/dL (elevada). Glucemia: 89 mg/dL (normal). Hemograma normal. RxTx: sin infiltrados.",
                "question": "Con la TSH suprimida y T4/T3 elevadas, ¿qué diagnósticos puedes eliminar?",
                "eliminates": {
                    "diabetes": "La glucemia de 89 mg/dL es completamente normal, descartando diabetes mellitus como causa de la pérdida de peso.",
                    "neoplasia": "La pérdida de peso por neoplasia oculta no produce supresión de TSH ni elevación de T4/T3. Además, la pérdida de peso neoplásica típicamente cursa con anorexia, no con hiperfagia.",
                    "tbc": "La TBC no produce alteraciones en el eje tiroideo. La RxTx normal y el hemograma sin leucocitosis hacen la TBC muy poco probable.",
                    "ansiedad": "El trastorno de ansiedad no produce TSH suprimida ni T4/T3 elevadas. La presencia de hipertiroidismo bioquímico confirma una causa orgánica."
                },
                "cannot_eliminate": {
                    "hipertiro": "TSH suprimida + T4/T3 elevadas + síntomas adrenérgicos (taquicardia, temblor, sudoración) + bocio + exoftalmos = hipertiroidismo confirmado, probablemente enfermedad de Graves."
                }
            },
            {
                "id": "c2",
                "text": "Anticuerpos anti-receptor de TSH (TRAb): 28 UI/L (muy elevados, VN <1.8). Gammagrafía tiroidea: bocio difuso hipercaptante. Ecografía tiroidea: glándula aumentada de tamaño con vascularización marcada (patrón 'infierno tiroideo').",
                "question": "Con los TRAb muy elevados y la gammagrafía hipercaptante, ¿qué confirmas?",
                "eliminates": {},
                "cannot_eliminate": {
                    "hipertiro": "TRAb muy elevados + bocio difuso hipercaptante en gammagrafía = Enfermedad de Graves confirmada. Los TRAb son anticuerpos que estimulan el receptor de TSH, causando hiperfunción tiroidea autoinmune. El exoftalmos (oftalmopatía de Graves) es patognomónico. Tratamiento: metimazol o propiltiouracilo + betabloqueante para los síntomas adrenérgicos."
                }
            }
        ],
        "resolution": "Enfermedad de Graves (hipertiroidismo autoinmune). La tríada clásica es: hipertiroidismo + bocio difuso + oftalmopatía (exoftalmos). Los TRAb son el marcador diagnóstico específico. La pérdida de peso con apetito conservado ('come pero adelgaza') es el sello del hipertiroidismo. Tratamiento: antitiroideos (metimazol), radioyodo o tiroidectomía.",
        "pearl": "Perla clínica: Causas de pérdida de peso con apetito conservado (hiperfagia): hipertiroidismo, diabetes mellitus descontrolada, malabsorción (enfermedad celíaca, insuficiencia pancreática exocrina), parasitosis. Si hay anorexia: neoplasia, TBC, depresión, ICC avanzada. El apetito orienta el diagnóstico diferencial."
    }
]
