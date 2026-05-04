ORGANS = [
    {
        "id": "cerebro",
        "name": "Cerebro",
        "system": "Neurológico",
        "color": "#6366f1",
        "svg_zone": "head",
        "anatomy": "El cerebro pesa ~1400g y contiene 86 mil millones de neuronas. Recibe el 15-20% del gasto cardíaco (750 mL/min). La barrera hematoencefálica protege el SNC de toxinas y patógenos. La interrupción del flujo sanguíneo cerebral por más de 4-6 minutos produce daño neuronal irreversible.",
        "pathologies": [
            {
                "id_case": "acv-isquemico",
                "name": "ACV Isquémico",
                "anatomy_context": "La oclusión de una arteria cerebral (ACM, ACA, ACP o sus ramas) genera una zona de infarto central (necrosis irreversible) rodeada de una penumbra isquémica (tejido disfuncional pero recuperable). La penumbra es el objetivo terapéutico: si se reperfunde a tiempo, se salva.",
                "clinical": "Déficit neurológico focal de instauración brusca: hemiparesia/hemiplejía contralateral, afasia (hemisferio dominante), hemianopsia, ataxia o vértigo (territorio posterior). El NIHSS cuantifica la gravedad (0-42).",
                "complications": [
                    "Transformación hemorrágica — sangrado dentro del infarto (más frecuente post-trombolisis)",
                    "Edema cerebral maligno — en infartos extensos de ACM, pico a las 48-72h",
                    "Herniación uncal — compresión del III par y tronco del encéfalo",
                    "Epilepsia post-ACV — en el 5-10% de los casos, especialmente en infartos corticales"
                ]
            },
            {
                "id_case": "meningitis-bacteriana",
                "name": "Meningitis Bacteriana",
                "anatomy_context": "La infección bacteriana de las meninges (piamadre y aracnoides) produce inflamación del espacio subaracnoideo. El exudado purulento obstruye el flujo de LCR, produce vasculitis e inflamación cerebral difusa. N. meningitidis (jóvenes) y S. pneumoniae (adultos y mayores) son los gérmenes más frecuentes.",
                "clinical": "Tríada clásica: fiebre + cefalea intensa + rigidez de nuca. Signos de Kernig (dolor al extender la rodilla con cadera flexionada) y Brudzinski (flexión refleja de rodillas al flexionar el cuello). En meningococcemia: petequias y púrpura fulminante.",
                "complications": [
                    "Ventriculitis y empiema subdural",
                    "Hidrocefalia — obstrucción al flujo de LCR por exudado",
                    "Infarto cerebral — vasculitis séptica de arterias cerebrales",
                    "Sordera neurosensorial — daño del VIII par (más frecuente en meningitis neumocócica)"
                ]
            },
            {
                "id_case": "status-epileptico",
                "name": "Status Epiléptico",
                "anatomy_context": "La actividad epiléptica sostenida produce excitotoxicidad neuronal por acumulación de glutamato y entrada masiva de Ca²⁺ intracelular. Las neuronas hipocampales son especialmente vulnerables. Después de 30 minutos de status, el daño neuronal es progresivo e irreversible.",
                "clinical": "Convulsiones tónico-clónicas generalizadas que duran más de 5 minutos o dos crisis sin recuperación de conciencia entre ellas. Puede presentarse como status no convulsivo (confusión persistente, diagnóstico solo por EEG).",
                "complications": [
                    "Daño neuronal hipóxico — hipoxemia y acidosis durante las convulsiones",
                    "Rabdomiólisis — necrosis muscular por contracciones sostenidas",
                    "Aspiración — por pérdida del reflejo de deglución",
                    "Edema pulmonar neurogénico — liberación masiva de catecolaminas"
                ]
            }
        ]
    },
    {
        "id": "corazon",
        "name": "Corazón",
        "system": "Cardiovascular",
        "color": "#ef4444",
        "svg_zone": "heart",
        "anatomy": "El corazón pesa ~280g y tiene 4 cámaras. El gasto cardíaco en reposo es 5 L/min (puede subir a 25 L/min en ejercicio). Las arterias coronarias (DA, Cx, CD) irrigan el miocardio durante la diástole. El nodo SA genera el impulso a 60-100 lpm; el nodo AV retrasa la conducción 120-200 ms.",
        "pathologies": [
            {
                "id_case": "infarto-agudo-miocardio",
                "name": "IAM con elevación del ST",
                "anatomy_context": "La oclusión completa de una arteria coronaria por rotura de placa aterosclerótica + trombosis produce necrosis transmural. La zona de necrosis (sin función) está rodeada de zona de lesión (ST elevado) y zona de isquemia (ondas T invertidas). Cada minuto sin reperfusión = necrosis de ~1g de miocardio.",
                "clinical": "Dolor retroesternal opresivo irradiado a brazo izquierdo, mandíbula o espalda. Diaforesis, náuseas. ECG: elevación del ST ≥1mm en ≥2 derivaciones contiguas. Troponina en ascenso.",
                "complications": [
                    "Shock cardiogénico — necrosis >40% del ventrículo izquierdo",
                    "Arritmias ventriculares — FV es la causa más frecuente de muerte prehospitalaria",
                    "Rotura miocárdica — rara pero catastrófica (días 3-7 post-IAM)",
                    "Insuficiencia mitral aguda — rotura del músculo papilar",
                    "Aneurisma ventricular — área de necrosis que no contrae"
                ]
            },
            {
                "id_case": "insuficiencia-cardiaca-aguda",
                "name": "Insuficiencia Cardíaca Aguda",
                "anatomy_context": "La disfunción sistólica (FE reducida) o diastólica (FE preservada) eleva la presión de llenado. La congestión pulmonar ocurre cuando la presión capilar pulmonar supera 18-22 mmHg (edema intersticial) y 28 mmHg (edema alveolar). El ventrículo derecho se afecta secundariamente por la hipertensión pulmonar.",
                "clinical": "Disnea progresiva, ortopnea, disnea paroxística nocturna. SatO2 baja, crepitantes bibasales, edema periférico. Clasificación Killip: I (sin signos), II (crepitantes), III (edema pulmonar), IV (shock cardiogénico).",
                "complications": [
                    "Edema agudo de pulmón — emergencia hipóxica",
                    "Shock cardiogénico — IC con hipoperfusión sistémica",
                    "Derrame pleural — trasudado bilateral por hipertensión venosa pulmonar",
                    "Arritmias — FA es desencadenante y consecuencia de la IC"
                ]
            },
            {
                "id_case": "fibrilacion-auricular",
                "name": "Fibrilación Auricular",
                "anatomy_context": "Múltiples circuitos de reentrada en el miocardio auricular producen activación eléctrica caótica a 350-600 lpm. Las venas pulmonares son el foco gatillador más frecuente (objetivo de la ablación). La orejuela izquierda es el sitio donde se forman los trombos (90% de los casos) por la estasis en FA.",
                "clinical": "Palpitaciones, disnea, mareo. Pulso irregularmente irregular. ECG: sin ondas P, línea basal irregular (ondas f), intervalos RR irregulares. FC ventricular variable (60-180 lpm según conducción AV).",
                "complications": [
                    "ACV tromboembólico — trombo en orejuela izquierda que emboliza al cerebro",
                    "Miocardiopatía taquicardiogénica — IC reversible por FC persistentemente alta",
                    "Síncope — por pausa post-conversión o respuesta ventricular baja",
                    "Tromboembolia sistémica — embolias a extremidades, mesenterio, riñones"
                ]
            }
        ]
    },
    {
        "id": "pulmones",
        "name": "Pulmones",
        "system": "Respiratorio",
        "color": "#3b82f6",
        "svg_zone": "lungs",
        "anatomy": "Los pulmones tienen una superficie alveolar de 70-100 m². El pulmón derecho tiene 3 lóbulos; el izquierdo 2. La membrana alvéolo-capilar mide 0.2-0.5 μm de grosor. La CRF (capacidad residual funcional) es ~2.5L. La PaO2 normal es 75-100 mmHg; la PaCO2 normal 35-45 mmHg.",
        "pathologies": [
            {
                "id_case": "neumonia-adquirida-comunidad",
                "name": "Neumonía Adquirida en la Comunidad",
                "anatomy_context": "Los microorganismos alcanzan el alvéolo por microaspiración de secreciones orofaríngeas, inhalación o vía hematógena. La respuesta inflamatoria llena los alvéolos de exudado (consolidación alveolar). El shunt intrapulmonar (alvéolos perfundidos pero no ventilados) explica la hipoxemia.",
                "clinical": "Fiebre, tos productiva, dolor pleurítico, disnea. Crepitantes y matidez en el área afectada. RxTx: consolidación lobar con broncograma aéreo. CURB-65 estratifica la gravedad.",
                "complications": [
                    "Derrame pleural paraneumónico — en el 40% de las neumonías bacterianas",
                    "Empiema pleural — derrame infectado que requiere drenaje",
                    "Absceso pulmonar — necrosis del parénquima con cavitación",
                    "SDRA — en neumonías graves bilaterales (mortalidad 40-60%)"
                ]
            },
            {
                "id_case": "tromboembolia-pulmonar",
                "name": "Tromboembolismo Pulmonar",
                "anatomy_context": "Los trombos (80-90% de origen venoso profundo de MMII) migran por la circulación venosa, atraviesan el corazón derecho y obstruyen arterias pulmonares. La obstrucción aumenta la postcarga del VD, que se dilata y desplaza el septum hacia el VI (fenómeno de interdependencia ventricular).",
                "clinical": "Disnea brusca, dolor pleurítico, hemoptisis. Taquicardia, hipoxemia. Wells score estratifica la probabilidad pretest. TCAP es el gold standard diagnóstico.",
                "complications": [
                    "Shock obstructivo — en TEP masivo con obstrucción >50%",
                    "Cor pulmonale agudo — dilatación y fallo del VD",
                    "Infarto pulmonar — necrosis del parénquima en arterias distales",
                    "Hipertensión pulmonar tromboembólica crónica — si no se anticoagula adecuadamente"
                ]
            },
            {
                "id_case": "crisis-asmatica",
                "name": "Crisis Asmática",
                "anatomy_context": "La inflamación crónica de la vía aérea produce hiperreactividad bronquial. En la crisis: broncoespasmo + edema de la mucosa + hipersecreción de moco → obstrucción al flujo espiratorio. La hiperinsuflación dinámica (air trapping) aumenta el trabajo respiratorio y puede progresar a paro.",
                "clinical": "Disnea, sibilancias bilaterales, tos. FR elevada, uso de músculos accesorios. Peak flow <60% del predicho en crisis moderada, <40% en grave. Silencio auscultatorio = crisis casi fatal.",
                "complications": [
                    "Paro respiratorio — la causa de muerte más frecuente en asma",
                    "Neumotórax — por hiperinsuflación y rotura de bullas",
                    "Neumomediastino — escape de aire por ruptura alveolar",
                    "Miocardiopatía por estrés — en crisis muy graves con hipoxia severa"
                ]
            }
        ]
    },
    {
        "id": "higado",
        "name": "Hígado",
        "system": "Digestivo",
        "color": "#f59e0b",
        "svg_zone": "liver",
        "anatomy": "El hígado pesa ~1500g y tiene irrigación dual: arteria hepática (25%) + vena porta (75%). Realiza más de 500 funciones: síntesis de factores de coagulación, albumina, gluconeogénesis, metabolismo de fármacos y bilirrubina. La capacidad regenerativa es extraordinaria (hasta el 75% de resección con regeneración completa).",
        "pathologies": [
            {
                "id_case": "hemorragia-digestiva-alta",
                "name": "Várices Esofágicas / Hipertensión Portal",
                "anatomy_context": "La cirrosis produce fibrosis hepática que obstruye el flujo portal → hipertensión portal (>12 mmHg). Las colaterales porto-sistémicas se desarrollan: varices esofágicas (más peligrosas), varices gástricas, hemorroides y caput medusae. Las varices esofágicas sangran cuando la presión portal supera 12 mmHg.",
                "clinical": "Hematemesis (sangre roja o en 'posos de café') con estigmas de hepatopatía crónica (ictericia, ascitis, eritema palmar). Examen: estigmas de hepatopatía, esplenomegalia.",
                "complications": [
                    "Peritonitis bacteriana espontánea — infección del líquido ascítico",
                    "Encefalopatía hepática — acumulación de amoniaco y otras toxinas",
                    "Síndrome hepatorrenal — vasoconstricción renal funcional en cirrosis avanzada",
                    "Síndrome hepatopulmonar — shunt intrapulmonar en cirrosis"
                ]
            }
        ]
    },
    {
        "id": "pancreas",
        "name": "Páncreas",
        "system": "Digestivo",
        "color": "#f97316",
        "svg_zone": "pancreas",
        "anatomy": "El páncreas pesa ~75g. La cabeza está en el asa duodenal; el cuerpo y cola cruzan hacia el bazo. Función exocrina: produce 1.5-2L de jugo pancreático/día (lipasa, amilasa, proteasas). Función endocrina: islotes de Langerhans (células β=insulina, α=glucagón, δ=somatostatina). El conducto de Wirsung desemboca junto al colédoco en la ampolla de Vater.",
        "pathologies": [
            {
                "id_case": "pancreatitis-aguda",
                "name": "Pancreatitis Aguda",
                "anatomy_context": "La activación prematura del tripsinógeno dentro del acino pancreático desencadena autodigestión del parénquima. Las causas más frecuentes son colelitiasis (obstrucción de la ampolla de Vater) y alcohol (efecto tóxico directo). La necrosis puede ser estéril o infectarse (peor pronóstico).",
                "clinical": "Dolor epigástrico en 'faja' irradiado a la espalda, náuseas, vómitos. Lipasa >3 veces lo normal es diagnóstico. BISAP y Ranson estratifican la gravedad. TC con contraste: grado de necrosis (Balthazar).",
                "complications": [
                    "Necrosis pancreática infectada — principal causa de mortalidad tardía",
                    "Pseudoquiste pancreático — colección de jugo pancreático encapsulada",
                    "SDRA — en pancreatitis severa (mediadores inflamatorios sistémicos)",
                    "Falla multiorgánica — en pancreatitis grave (mortalidad 30-50%)"
                ]
            },
            {
                "id_case": "cetoacidosis-diabetica",
                "name": "Cetoacidosis Diabética",
                "anatomy_context": "El déficit absoluto de insulina (DM tipo 1) o relativo (DM tipo 2 con estrés) activa la lipólisis y la cetogénesis hepática. Los ácidos grasos libres se convierten en cuerpos cetónicos (acetoacetato, β-hidroxibutirato) que acidifican el plasma. La hiperglucemia produce diuresis osmótica → deshidratación severa.",
                "clinical": "Poliuria, polidipsia, náuseas, vómitos, dolor abdominal. Respiración de Kussmaul (profunda y rápida). Aliento cetónico. Glucemia >250, pH <7.30, HCO3 <15, cetonas positivas.",
                "complications": [
                    "Edema cerebral — más frecuente en niños, especialmente con corrección rápida",
                    "Hipopotasemia — por el tratamiento con insulina sin reposición de K+",
                    "Hipoglucemia iatrogénica — por exceso de insulina sin transición adecuada",
                    "Trombosis venosa — por hiperviscosidad sanguínea en la deshidratación"
                ]
            }
        ]
    },
    {
        "id": "rinon",
        "name": "Riñones",
        "system": "Renal",
        "color": "#06b6d4",
        "svg_zone": "kidneys",
        "anatomy": "Cada riñón pesa ~150g y contiene ~1 millón de nefronas. La TFG normal es >90 mL/min/1.73m². Filtran 180L de plasma/día produciendo 1.5-2L de orina. Producen eritropoyetina (estimula la hematopoyesis), renina (regula la TA) y calcitriol (vitamina D activa). La corteza (nefronas) es más sensible a la isquemia que la médula.",
        "pathologies": [
            {
                "id_case": "insuficiencia-renal-aguda",
                "name": "Insuficiencia Renal Aguda",
                "anatomy_context": "La IRA prerrenal (más frecuente, 55-60%) se produce por hipoperfusión sin daño del parénquima — reversible con fluidos. La IRA intrínseca (NTA = necrosis tubular aguda) ocurre cuando la isquemia o los nefrotóxicos dañan directamente los túbulos proximales. La IRA posrenal es por obstrucción del flujo urinario.",
                "clinical": "Oliguria (<0.5 mL/kg/h) o anuria. Creatinina en ascenso. Retención de K+ y ácidos → hiperpotasemia y acidosis metabólica. FENa <1% en prerrenal; >2% en intrínseca.",
                "complications": [
                    "Hiperpotasemia grave — K+ >6.5 con riesgo de FV",
                    "Edema pulmonar — por sobrecarga hídrica en oliguria",
                    "Pericarditis urémica — en IRA prolongada sin diálisis",
                    "Progresión a ERC — especialmente en episodios repetidos"
                ]
            }
        ]
    },
    {
        "id": "aorta-vasos",
        "name": "Aorta y Vasos",
        "system": "Cardiovascular",
        "color": "#dc2626",
        "svg_zone": "aorta",
        "anatomy": "La aorta mide ~3 cm de diámetro. Asciende desde el VI, forma el cayado (origen de carótidas y subclavias), desciende por el tórax y se bifurca en L4 en las ilíacas. La pared aórtica tiene 3 capas: íntima, media (elástica) y adventicia. La disección ocurre cuando la sangre penetra entre la íntima y la media.",
        "pathologies": [
            {
                "id_case": "shock-septico",
                "name": "Shock Distributivo / Séptico",
                "anatomy_context": "En el shock séptico, la respuesta inflamatoria sistémica produce vasodilatación masiva por óxido nítrico → caída de la resistencia vascular periférica. A pesar del alto gasto cardíaco (shock 'caliente'), la hipoperfusión tisular persiste por maldistribución del flujo y disfunción mitocondrial.",
                "clinical": "Fiebre o hipotermia, taquicardia, taquipnea. Hipotensión refractaria a fluidos. Lactato >4 mmol/L. Extremidades calientes (shock distributivo) en fase inicial. Fallo multiorgánico en estadios avanzados.",
                "complications": [
                    "SDRA — lesión pulmonar aguda por mediadores inflamatorios",
                    "IRA — hipoperfusión renal y nefrotoxicidad de antibióticos",
                    "CID — consumo de factores de coagulación",
                    "Insuficiencia suprarrenal relativa — en shock prolongado"
                ]
            }
        ]
    },
    {
        "id": "intestino",
        "name": "Intestino y Colon",
        "system": "Digestivo",
        "color": "#84cc16",
        "svg_zone": "intestine",
        "anatomy": "El intestino delgado mide 6-7m con superficie de absorción de 250 m² (por vellosidades y microvellosidades). El colon mide 1.5m y absorbe agua y electrolitos. El apéndice vermiforme nace en el ciego a la confluencia de las tenias. La válvula ileocecal separa el intestino delgado del colon.",
        "pathologies": [
            {
                "id_case": "apendicitis-aguda",
                "name": "Apendicitis Aguda",
                "anatomy_context": "La obstrucción del lumen apendicular (por fecalito, hiperplasia linfoide o parásitos) eleva la presión intraluminal → isquemia de la pared → invasión bacteriana → gangrena → perforación. La localización retrocecal del apéndice (65%) puede producir presentaciones atípicas con dolor lumbar.",
                "clinical": "Migración del dolor periumbilical a FID (punto de McBurney). Fiebre, náuseas, anorexia. Blumberg y Rovsing positivos. Score de Alvarado estratifica el riesgo. Ecografía: apéndice >6mm no compresible.",
                "complications": [
                    "Perforación con peritonitis localizada — absceso periapendicular",
                    "Peritonitis difusa — contaminación de toda la cavidad abdominal",
                    "Pileflebitis — tromboflebitis séptica de la vena porta",
                    "Obstrucción intestinal por adherencias — complicación tardía postquirúrgica"
                ]
            }
        ]
    }
]
