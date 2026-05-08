import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import TourGuide from '../components/TourGuide'

const TOUR_KEY = 'medex_anatomy_tour_done'

// ─── SVG Body with clickable organs ───────────────────────────────────────────
function BodySVG({ activeZone, hoveredZone, onClickZone, onHoverZone, organs }) {
  const colorFor = (id) => {
    const organ = organs.find(o => o.svg_zone === id)
    if (!organ) return '#d1d5db'
    if (activeZone === id) return organ.color
    if (hoveredZone === id) return organ.color + 'bb'
    return '#e2e8f0'
  }

  const zone = (id) => ({
    fill: colorFor(id),
    stroke: activeZone === id ? '#1e293b' : hoveredZone === id ? '#475569' : '#94a3b8',
    strokeWidth: activeZone === id ? 1.8 : 1,
    onClick: () => onClickZone(id),
    onMouseEnter: () => onHoverZone(id),
    onMouseLeave: () => onHoverZone(null),
    style: { cursor: 'pointer', transition: 'fill 0.15s' },
  })

  // Detail lines (fissures, lobulations, etc.) visible on hover/active
  const det = (id) => ({
    fill: 'none',
    stroke: (activeZone === id || hoveredZone === id) ? 'rgba(255,255,255,0.5)' : 'rgba(148,163,184,0.18)',
    strokeWidth: 0.9,
    style: { pointerEvents: 'none' },
  })

  const np = { style: { pointerEvents: 'none' } }

  return (
    <svg viewBox="0 0 240 530" xmlns="http://www.w3.org/2000/svg"
      className="w-full max-w-[200px] mx-auto select-none">

      {/* ══ BODY SILHOUETTE (background, non-interactive) ══ */}

      {/* Left arm */}
      <path d="M72 100 Q55 132 49 190 Q45 222 52 254 Q58 264 67 260 Q76 256 75 224 Q74 184 78 142 Z"
        fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Right arm */}
      <path d="M168 100 Q185 132 191 190 Q195 222 188 254 Q182 264 173 260 Q164 256 165 224 Q166 184 162 142 Z"
        fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Left hand */}
      <ellipse cx="59" cy="268" rx="9" ry="12" fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Right hand */}
      <ellipse cx="181" cy="268" rx="9" ry="12" fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Chest */}
      <path d="M72 96 Q62 122 60 172 L180 172 Q178 122 168 96 Q150 87 120 86 Q90 87 72 96 Z"
        fill="#faf4ec" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Abdomen */}
      <path d="M60 172 Q56 208 58 250 L182 250 Q184 208 180 172 Z"
        fill="#faf4ec" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Pelvis */}
      <path d="M58 250 Q52 278 57 304 Q66 322 88 326 L152 326 Q174 322 183 304 Q188 278 182 250 Z"
        fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Neck */}
      <rect x="112" y="78" width="16" height="18" rx="2" fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Upper legs */}
      <path d="M72 326 Q64 364 66 408 Q68 438 83 440 Q97 440 99 406 Q102 368 97 326 Z"
        fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      <path d="M168 326 Q176 364 174 408 Q172 438 157 440 Q143 440 141 406 Q138 368 143 326 Z"
        fill="#f1d9c0" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Lower legs */}
      <path d="M66 408 Q62 448 64 476 Q66 496 80 498 Q94 498 96 476 Q98 456 99 408 Z"
        fill="#e8cfb5" stroke="#d4b896" strokeWidth="1" {...np}/>
      <path d="M174 408 Q178 448 176 476 Q174 496 160 498 Q146 498 144 476 Q142 456 141 408 Z"
        fill="#e8cfb5" stroke="#d4b896" strokeWidth="1" {...np}/>
      {/* Feet */}
      <ellipse cx="80" cy="504" rx="17" ry="7" fill="#e8cfb5" stroke="#d4b896" strokeWidth="1" {...np}/>
      <ellipse cx="160" cy="504" rx="17" ry="7" fill="#e8cfb5" stroke="#d4b896" strokeWidth="1" {...np}/>

      {/* ══ HEAD / BRAIN ══ */}
      <ellipse cx="120" cy="41" rx="31" ry="35" {...zone('head')}/>
      {/* Neck portion of brain zone */}
      <rect x="112" y="75" width="16" height="21" rx="2" {...zone('head')} stroke="none"/>
      {/* Hemisphere fissure */}
      <path d="M 120 8 L 120 70" {...det('head')}/>
      {/* Face */}
      <ellipse cx="110" cy="36" rx="5.5" ry="5" fill="white" opacity="0.45" {...np}/>
      <ellipse cx="130" cy="36" rx="5.5" ry="5" fill="white" opacity="0.45" {...np}/>
      <circle cx="110" cy="37" r="2.5" fill="#3d2e22" opacity="0.6" {...np}/>
      <circle cx="130" cy="37" r="2.5" fill="#3d2e22" opacity="0.6" {...np}/>
      <circle cx="120" cy="46" r="2" fill="#c8a090" opacity="0.45" {...np}/>
      <path d="M 114 54 Q 120 59 126 54" stroke="#b09080" strokeWidth="1.2" fill="none" {...np}/>
      <path d="M 106 26 Q 110 23 114 26" stroke="#6b4c3b" strokeWidth="1.1" fill="none" {...np}/>
      <path d="M 126 26 Q 130 23 134 26" stroke="#6b4c3b" strokeWidth="1.1" fill="none" {...np}/>

      {/* ══ LEFT LUNG (patient's left = SVG left) ══ */}
      {/* Apex narrow at top, base wide at bottom, cardiac notch on medial/right border */}
      <path d="
        M 70 100
        C 60 108, 57 136, 60 162
        C 62 180, 68 198, 80 208
        C 92 214, 108 210, 114 198
        C 118 190, 116 178, 112 168
        C 108 158, 105 147, 109 137
        C 112 126, 112 110, 103 102
        C 94 96, 80 96, 70 100 Z
      " {...zone('lungs')}/>
      {/* Oblique fissure */}
      <path d="M 62 154 Q 84 162, 108 154" {...det('lungs')}/>

      {/* ══ RIGHT LUNG (patient's right = SVG right) ══ */}
      {/* Three lobes marked with horizontal + oblique fissures */}
      <path d="
        M 170 100
        C 180 108, 183 136, 180 162
        C 178 180, 172 198, 160 208
        C 148 214, 132 210, 126 198
        C 122 190, 124 178, 127 166
        C 129 154, 128 138, 128 124
        C 128 112, 136 100, 148 98
        C 158 96, 164 98, 170 100 Z
      " {...zone('lungs')}/>
      {/* Horizontal fissure */}
      <path d="M 178 138 Q 156 144, 128 138" {...det('lungs')}/>
      {/* Oblique fissure */}
      <path d="M 178 164 Q 156 170, 128 162" {...det('lungs')}/>

      {/* ══ HEART ══ */}
      {/* Left atrium bulge */}
      <ellipse cx="100" cy="114" rx="13" ry="11" {...zone('heart')}/>
      {/* Right atrium bulge */}
      <ellipse cx="116" cy="114" rx="12" ry="10" {...zone('heart')}/>
      {/* Ventricular body tapering to apex (lower-left) */}
      <path d="
        M 87 118
        C 79 126, 77 140, 81 154
        C 84 164, 93 174, 102 180
        C 107 183, 115 179, 121 171
        C 127 163, 129 150, 127 136
        C 125 124, 118 112, 110 110 Z
      " {...zone('heart')}/>
      {/* Anterior interventricular groove */}
      <path d="M 100 174 Q 110 150, 112 116" {...det('heart')}/>
      {/* Coronary sulcus */}
      <path d="M 85 130 Q 104 122, 124 130" {...det('heart')}/>

      {/* ══ AORTA ══ */}
      {/* Ascending + arch + descending */}
      <path d="
        M 118 100
        C 118 91, 123 85, 130 88
        C 136 91, 135 98, 129 102
        L 124 102 L 124 288 L 118 288 Z
      " {...zone('aorta')}/>

      {/* ══ STOMACH (non-interactive, visual background) ══ */}
      {/* J-shaped: fundus top-left, body curves down, antrum curves right */}
      <path d="
        M 88 180
        C 80 176, 70 180, 68 195
        C 66 209, 70 223, 81 232
        C 88 238, 100 240, 110 236
        C 118 232, 122 222, 118 212
        C 116 204, 108 196, 104 188
        C 100 182, 94 178, 88 180 Z
      " fill="#fde8c8" stroke="#e8c896" strokeWidth="1" {...np}/>
      {/* Rugae folds */}
      <path d="M 72 202 Q 92 197, 114 204" stroke="#e8c896" strokeWidth="0.7" fill="none" {...np}/>
      <path d="M 72 212 Q 94 207, 116 214" stroke="#e8c896" strokeWidth="0.7" fill="none" {...np}/>

      {/* ══ LIVER (large dome, right upper abdomen) ══ */}
      <path d="
        M 120 182
        C 130 177, 150 177, 166 183
        C 178 188, 184 200, 181 214
        C 178 226, 168 236, 152 238
        C 138 240, 124 236, 117 226
        C 112 218, 113 204, 117 194
        C 118 187, 120 184, 120 182 Z
      " {...zone('liver')}/>
      {/* Falciform ligament */}
      <path d="M 120 182 L 124 234" {...det('liver')}/>
      {/* Right/left lobe division */}
      <path d="M 148 178 Q 150 208, 146 236" {...det('liver')}/>

      {/* ══ PANCREAS (horizontal gland, partially visible below stomach) ══ */}
      {/* Head on right (in duodenal loop), tail extends left */}
      <path d="
        M 102 224
        C 116 219, 138 218, 156 222
        C 164 225, 168 230, 162 234
        C 150 237, 128 237, 108 234
        C 100 232, 98 228, 102 224 Z
      " {...zone('pancreas')}/>
      {/* Pancreatic duct line */}
      <path d="M 104 229 Q 130 226, 162 229" {...det('pancreas')}/>

      {/* ══ RIGHT KIDNEY (bean-shaped, patient's right = SVG right) ══ */}
      {/* Lateral border convex outward, medial border concave (hilum) */}
      <path d="
        M 158 220
        C 170 218, 176 228, 176 240
        C 176 252, 168 262, 158 264
        C 152 264, 147 260, 145 252
        C 143 244, 143 234, 147 226
        C 150 220, 154 220, 158 220 Z
      " {...zone('kidneys')}/>
      {/* Renal hilum & pelvis */}
      <path d="M 146 240 Q 152 244, 146 248" {...det('kidneys')}/>
      <path d="M 148 236 Q 156 240, 148 244" {...det('kidneys')}/>

      {/* ══ LEFT KIDNEY (bean-shaped, patient's left = SVG left) ══ */}
      <path d="
        M 82 220
        C 70 218, 64 228, 64 240
        C 64 252, 72 262, 82 264
        C 88 264, 93 260, 95 252
        C 97 244, 97 234, 93 226
        C 90 220, 86 220, 82 220 Z
      " {...zone('kidneys')}/>
      {/* Renal hilum & pelvis */}
      <path d="M 94 240 Q 88 244, 94 248" {...det('kidneys')}/>
      <path d="M 92 236 Q 84 240, 92 244" {...det('kidneys')}/>

      {/* ══ INTESTINES (lower abdomen) ══ */}
      {/* Colon frame — ascending (right), transverse (top), descending (left), sigmoid/rectum (bottom) */}
      <path d="
        M 68 254 L 68 316
        Q 72 324, 84 324 L 156 324
        Q 168 324, 172 316 L 172 254
        Q 166 246, 154 246 L 86 246
        Q 70 246, 68 254 Z
      " {...zone('intestine')}/>
      {/* Small bowel loops (visual detail, non-interactive) */}
      <ellipse cx="112" cy="274" rx="24" ry="17" fill="white" opacity="0.18" {...np}/>
      <ellipse cx="126" cy="285" rx="20" ry="14" fill="white" opacity="0.14" {...np}/>
      <ellipse cx="108" cy="262" rx="18" ry="12" fill="white" opacity="0.14" {...np}/>
      {/* Haustra (colon sacculations) */}
      <path d="M 68 268 L 172 268" {...det('intestine')}/>
      <path d="M 68 284 L 172 284" {...det('intestine')}/>
      <path d="M 68 300 L 172 300" {...det('intestine')}/>
      <path d="M 68 316 L 172 316" {...det('intestine')}/>
      {/* Ileocecal corner */}
      <path d="M 68 254 Q 86 246, 86 254" {...det('intestine')}/>
      <path d="M 172 254 Q 154 246, 154 254" {...det('intestine')}/>

      {/* ══ HOVER LABEL ══ */}
      {hoveredZone && (
        <text x="120" y="522" textAnchor="middle" fill="#1e293b" fontSize="9.5" fontFamily="sans-serif" fontWeight="700" {...np}>
          {organs.find(o => o.svg_zone === hoveredZone)?.name ?? ''}
        </text>
      )}
    </svg>
  )
}

// ─── Main component ────────────────────────────────────────────────────────────
const TABS = ['anatomy', 'clinical', 'complications']

export default function AnatomyMap() {
  const { lang } = useLang()

  const [organs, setOrgans]               = useState([])
  const [activeZone, setActiveZone]       = useState(null)
  const [hoveredZone, setHoveredZone]     = useState(null)
  const [organData, setOrganData]         = useState(null)
  const [selectedPath, setSelectedPath]   = useState(null)
  const [tab, setTab]                     = useState('anatomy')
  const [loading, setLoading]             = useState(false)
  const [showTour, setShowTour]           = useState(false)

  const lbl = (es, en) => lang === 'en' ? en : es

  useEffect(() => {
    if (!localStorage.getItem(TOUR_KEY)) { setShowTour(true); localStorage.setItem(TOUR_KEY, '1') }
  }, [])

  const SLIDES = [
    {
      icon: '🫀',
      title: lbl('Mapa Anatómico Interactivo', 'Interactive Anatomy Map'),
      desc: lbl('Un cuerpo humano interactivo. Haz clic en cualquier órgano para explorar su anatomía, patologías y complicaciones.', 'An interactive human body. Click any organ to explore its anatomy, pathologies and complications.'),
      visual: (
        <div className="flex flex-col items-center gap-3 w-full">
          <div className="flex gap-3 text-2xl">{'🫀🫁🧠🫘'.split('').map((e,i)=><span key={i}>{e}</span>)}</div>
          <div className="text-xs text-gray-500 text-center">Haz clic en cualquier órgano del mapa</div>
          <div className="flex gap-2 flex-wrap justify-center">
            {['Corazón','Pulmones','Hígado','Riñones'].map((o,i)=>(
              <span key={i} className="text-xs bg-gray-800 text-white px-3 py-1 rounded-full">{o}</span>
            ))}
          </div>
        </div>
      ),
    },
    {
      icon: '👆',
      title: lbl('Selecciona un órgano', 'Select an organ'),
      desc: lbl('Al hacer clic aparecen las patologías asociadas a ese órgano. Elige una para estudiarla en detalle.', 'Clicking shows the pathologies associated with that organ. Choose one to study it in detail.'),
      visual: (
        <div className="w-full bg-white border border-gray-200 rounded-xl p-4">
          <div className="text-xs font-bold text-gray-700 mb-3">🫀 Corazón — Patologías</div>
          <div className="flex flex-col gap-2">
            {['Infarto Agudo de Miocardio','Insuficiencia Cardíaca','Pericarditis'].map((p,i)=>(
              <div key={i} className={`text-xs px-3 py-2 rounded-lg border ${i===0?'border-blue-400 bg-blue-50 text-blue-800 font-semibold':'border-gray-200 bg-gray-50 text-gray-600'}`}>{p}</div>
            ))}
          </div>
        </div>
      ),
    },
    {
      icon: '📚',
      title: lbl('Tres pestañas de contenido', 'Three content tabs'),
      desc: lbl('Cada patología tiene anatomía detallada, presentación clínica y complicaciones frecuentes.', 'Each pathology has detailed anatomy, clinical presentation and common complications.'),
      visual: (
        <div className="w-full">
          <div className="flex gap-1 mb-3">
            {[['Anatomía','bg-gray-800 text-white'],['Clínica','bg-white border border-gray-300 text-gray-600'],['Complicaciones','bg-white border border-gray-300 text-gray-600']].map(([label,cls],i)=>(
              <span key={i} className={`text-xs px-3 py-1.5 rounded-full font-medium ${cls}`}>{label}</span>
            ))}
          </div>
          <div className="bg-gray-50 border border-gray-200 rounded-xl p-3 text-xs text-gray-700 leading-relaxed">
            Oclusión de la arteria coronaria → isquemia → necrosis miocárdica. Zona de infarto determinada por la arteria afectada.
          </div>
        </div>
      ),
    },
  ]

  // Load organ list on mount
  useEffect(() => {
    fetch(`${API}/anatomy`).then(r => r.json()).then(setOrgans).catch(() => {})
  }, [])

  // Load organ detail when zone selected
  useEffect(() => {
    if (!activeZone) return
    setLoading(true)
    setOrganData(null)
    setSelectedPath(null)
    const organId = organs.find(o => o.svg_zone === activeZone)?.id
    if (!organId) { setLoading(false); return }

    fetch(`${API}/anatomy/${organId}`)
      .then(r => r.json())
      .then(async data => {
        if (lang === 'en') {
          data = {
            ...data,
            name:    await translateText(data.name, lang),
            anatomy: await translateText(data.anatomy, lang),
            pathologies: await Promise.all(data.pathologies.map(async p => ({
              ...p,
              name:             await translateText(p.name, lang),
              anatomy_context:  await translateText(p.anatomy_context, lang),
              clinical:         await translateText(p.clinical, lang),
              complications:    await Promise.all(p.complications.map(c => translateText(c, lang))),
            }))),
          }
        }
        setOrganData(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [activeZone, organs, lang])

  const handleClickZone = (zone) => {
    setActiveZone(zone)
    setSelectedPath(null)
    setTab('anatomy')
  }

  const handleSelectPath = (p) => {
    setSelectedPath(p)
    setTab('anatomy')
  }

  const activeOrganMeta = organs.find(o => o.svg_zone === activeZone)

  return (
    <div className="min-h-screen bg-gray-50">
      {showTour && <TourGuide slides={SLIDES} onClose={() => setShowTour(false)} />}
      {/* Hero */}
      <div className="bg-gradient-to-br from-gray-800 to-gray-900 text-white py-10 px-8 text-center relative">
        <button onClick={() => setShowTour(true)} title={lbl('Cómo funciona','How it works')}
          className="absolute top-4 right-4 w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 text-white text-sm font-bold transition flex items-center justify-center">?</button>
        <div className="text-gray-400 text-sm font-semibold uppercase tracking-widest mb-2">
          {lbl('Anatomía interactiva', 'Interactive anatomy')}
        </div>
        <h1 className="text-4xl font-bold mb-2">{lbl('Mapa Anatómico', 'Anatomical Map')}</h1>
        <p className="text-gray-400 text-sm max-w-md mx-auto">
          {lbl(
            'Haz clic en un órgano → ve sus patologías → selecciona una para ver anatomía, clínica y complicaciones.',
            'Click an organ → see its pathologies → select one to view anatomy, clinical features and complications.'
          )}
        </p>
      </div>

      <div className="max-w-6xl mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-12 gap-8">

        {/* ── Column 1: Body SVG ── */}
        <div className="lg:col-span-3 flex flex-col items-center gap-4">
          <BodySVG
            organs={organs}
            activeZone={activeZone}
            hoveredZone={hoveredZone}
            onClickZone={handleClickZone}
            onHoverZone={setHoveredZone}
          />
          <p className="text-xs text-gray-400 text-center">
            {lbl('Haz clic en un órgano', 'Click on an organ')}
          </p>
        </div>

        {/* ── Column 2: Organ / Pathology list ── */}
        <div className="lg:col-span-3">
          {!activeZone && (
            <div className="flex flex-col items-center justify-center h-64 text-center text-gray-400 gap-3">
              <div className="text-4xl">👈</div>
              <p className="text-sm">{lbl('Selecciona un órgano del cuerpo', 'Select an organ from the body')}</p>
            </div>
          )}

          {loading && (
            <div className="flex flex-col items-center justify-center h-64 gap-3 text-gray-400">
              <div className="w-7 h-7 border-2 border-gray-800 border-t-transparent rounded-full animate-spin"/>
            </div>
          )}

          {organData && !loading && (
            <div>
              {/* Organ header */}
              <div className="flex items-center gap-2 mb-4">
                <span className="w-3 h-3 rounded-full" style={{ backgroundColor: activeOrganMeta?.color }}/>
                <h2 className="font-bold text-gray-800 text-lg">{organData.name}</h2>
              </div>
              <p className="text-xs text-gray-500 leading-relaxed mb-5">{organData.anatomy}</p>

              <div className="text-xs font-semibold text-gray-400 uppercase mb-3">
                {lbl('Patologías asociadas', 'Associated pathologies')}
              </div>
              <div className="flex flex-col gap-2">
                {organData.pathologies.map(p => (
                  <button key={p.id_case}
                    onClick={() => handleSelectPath(p)}
                    className={`text-left px-4 py-3 rounded-xl border text-sm transition ${
                      selectedPath?.id_case === p.id_case
                        ? 'border-gray-800 bg-gray-800 text-white'
                        : 'border-gray-200 bg-white hover:border-gray-400 text-gray-700'
                    }`}>
                    <div className="font-semibold">{p.name}</div>
                    {p.summary && (
                      <div className={`text-xs mt-0.5 line-clamp-2 ${selectedPath?.id_case === p.id_case ? 'text-gray-300' : 'text-gray-500'}`}>
                        {p.summary}
                      </div>
                    )}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* ── Column 3: Pathology detail ── */}
        <div className="lg:col-span-6">
          {!selectedPath && (
            <div className="flex flex-col items-center justify-center h-64 text-center text-gray-400 gap-3">
              <div className="text-4xl">☝️</div>
              <p className="text-sm">{lbl('Selecciona una patología', 'Select a pathology')}</p>
            </div>
          )}

          {selectedPath && (
            <div className="bg-white rounded-2xl border border-gray-100 shadow p-6">
              {/* Pathology header */}
              <div className="flex items-start justify-between mb-5">
                <div>
                  <h3 className="text-xl font-bold text-gray-800">{selectedPath.name}</h3>
                  <span className="text-xs text-gray-400">{selectedPath.difficulty}</span>
                </div>
                <Link to={`/pathology/${selectedPath.id_case}`}
                  className="shrink-0 ml-3 text-xs bg-primary text-white px-4 py-2 rounded-full hover:bg-blue-900 transition whitespace-nowrap">
                  {lbl('Ver caso clínico →', 'View clinical case →')}
                </Link>
              </div>

              {/* Tabs */}
              <div className="flex gap-1 bg-gray-100 p-1 rounded-xl mb-5">
                {[
                  { key: 'anatomy',         label: lbl('Anatomía', 'Anatomy') },
                  { key: 'clinical',        label: lbl('Clínica', 'Clinical') },
                  { key: 'complications',   label: lbl('Complicaciones', 'Complications') },
                ].map(t => (
                  <button key={t.key} onClick={() => setTab(t.key)}
                    className={`flex-1 py-1.5 rounded-lg text-xs font-medium transition ${
                      tab === t.key ? 'bg-white text-gray-800 shadow-sm' : 'text-gray-500 hover:text-gray-700'
                    }`}>
                    {t.label}
                  </button>
                ))}
              </div>

              {/* Tab content */}
              {tab === 'anatomy' && (
                <div>
                  <div className="text-xs font-semibold text-gray-400 uppercase mb-2">
                    {lbl('Contexto anatómico', 'Anatomical context')}
                  </div>
                  <p className="text-sm text-gray-700 leading-relaxed">{selectedPath.anatomy_context}</p>
                </div>
              )}

              {tab === 'clinical' && (
                <div>
                  <div className="text-xs font-semibold text-gray-400 uppercase mb-2">
                    {lbl('Presentación clínica', 'Clinical presentation')}
                  </div>
                  <p className="text-sm text-gray-700 leading-relaxed">{selectedPath.clinical}</p>
                </div>
              )}

              {tab === 'complications' && (
                <div>
                  <div className="text-xs font-semibold text-gray-400 uppercase mb-2">
                    {lbl('Complicaciones', 'Complications')}
                  </div>
                  <ul className="flex flex-col gap-3">
                    {selectedPath.complications.map((c, i) => (
                      <li key={i} className="flex gap-3 text-sm text-gray-700 bg-red-50 border border-red-100 rounded-xl px-4 py-3">
                        <span className="text-red-400 shrink-0 mt-0.5">▸</span>
                        <span>{c}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
