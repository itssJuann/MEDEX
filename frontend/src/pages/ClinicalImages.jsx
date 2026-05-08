import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { getProgress } from '../utils/progress'
import TourGuide from '../components/TourGuide'

const TOUR_KEY = 'medex_images_tour_done'

const DIFFICULTIES = ["Básico", "Intermedio", "Avanzado"]
const MODALITIES   = ["RxTx", "ECG", "TC", "RM", "Histopatología"]

const DIFFICULTY_STYLES = {
  "Básico":     "bg-green-50 text-green-700 border border-green-200",
  "Intermedio": "bg-yellow-50 text-yellow-700 border border-yellow-200",
  "Avanzado":   "bg-red-50 text-red-700 border border-red-200",
}

const MODALITY_ICON = {
  "RxTx": "🫁", "ECG": "💓", "TC": "🧠", "RM": "🔬", "Histopatología": "🔭"
}
const MODALITY_EN = {
  "RxTx": "X-Ray", "ECG": "ECG", "TC": "CT Scan", "RM": "MRI", "Histopatología": "Histopathology"
}

export default function ClinicalImages() {
  const { t, lang } = useLang()
  const [rawCases, setRawCases]     = useState([])
  const [cases, setCases]           = useState([])
  const [search, setSearch]         = useState("")
  const [modality, setModality]     = useState(null)
  const [difficulty, setDifficulty] = useState(null)
  const [showTour, setShowTour]     = useState(false)

  const lbl = (es, en) => lang === 'en' ? en : es

  useEffect(() => {
    if (!localStorage.getItem(TOUR_KEY)) { setShowTour(true); localStorage.setItem(TOUR_KEY, '1') }
  }, [])

  const SLIDES = [
    {
      icon: '🩻',
      title: lbl('Imágenes Clínicas', 'Clinical Images'),
      desc: lbl('Practica la interpretación de radiografías, ECGs, TACs, RMN e histopatología con casos reales guiados.', 'Practice interpreting X-rays, ECGs, CT scans, MRIs and histopathology with guided real cases.'),
      visual: (
        <div className="flex gap-2 flex-wrap justify-center w-full">
          {[['🫁','RxTx'],['💓','ECG'],['🧠','TC'],['🔬','RM'],['🔭','Histopatología']].map(([icon,label],i)=>(
            <div key={i} className="flex flex-col items-center bg-white border border-gray-200 rounded-xl px-3 py-2 text-xs text-gray-600 gap-1">
              <span className="text-xl">{icon}</span>{label}
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '🔍',
      title: lbl('Analiza la imagen sistemáticamente', 'Analyze the image systematically'),
      desc: lbl('Se te presenta la imagen clínica y debes identificar los hallazgos principales antes de responder.', 'You are presented with the clinical image and must identify the main findings before answering.'),
      visual: (
        <div className="w-full bg-gray-900 rounded-xl p-4 flex flex-col gap-2">
          <div className="bg-gray-700 rounded-lg h-16 flex items-center justify-center text-gray-400 text-xs">[ Imagen clínica ]</div>
          <div className="flex gap-2">
            {['Cardiomegalia','Derrame pleural','Normal'].map((f,i)=>(
              <span key={i} className={`text-xs px-2 py-1 rounded-full border ${i===0?'border-purple-400 bg-purple-900 text-purple-200':'border-gray-600 bg-gray-800 text-gray-400'}`}>{f}</span>
            ))}
          </div>
        </div>
      ),
    },
    {
      icon: '🎯',
      title: lbl('Responde preguntas dirigidas', 'Answer guided questions'),
      desc: lbl('Las preguntas te guían para identificar hallazgos específicos: "¿Qué estructura está agrandada?", "¿Qué patrón observas?"', 'Questions guide you to identify specific findings: "What structure is enlarged?", "What pattern do you see?"'),
      visual: (
        <div className="w-full flex flex-col gap-2">
          <div className="text-xs font-semibold text-gray-600 bg-white border border-gray-200 rounded-xl px-3 py-2">¿Cuál es el hallazgo principal en esta radiografía de tórax?</div>
          {['Consolidación en lóbulo inferior derecho','Neumotórax izquierdo','Derrame pleural bilateral'].map((opt,i)=>(
            <div key={i} className={`text-xs px-3 py-2 rounded-lg border ${i===0?'border-purple-400 bg-purple-50 text-purple-800':'border-gray-200 bg-gray-50 text-gray-500'}`}>
              {i===0&&'✓ '}{opt}
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '💡',
      title: lbl('Aprende a interpretar', 'Learn to interpret'),
      desc: lbl('El feedback explica los hallazgos clave, cómo reconocerlos y qué diagnósticos implican.', 'Feedback explains the key findings, how to recognize them and what diagnoses they imply.'),
      visual: (
        <div className="w-full bg-purple-50 border border-purple-200 rounded-xl p-4">
          <div className="text-xs font-bold text-purple-700 mb-1">💡 Interpretación</div>
          <div className="text-xs text-purple-800 leading-relaxed">La opacidad homogénea con broncograma aéreo en el LID es clásica de consolidación neumónica. El signo de Fleischner no está presente, descartando atelectasia.</div>
        </div>
      ),
    },
  ]

  useEffect(() => {
    fetch(`${API}/clinical-images`)
      .then(r => r.json()).then(setRawCases).catch(() => setRawCases([]))
  }, [])

  useEffect(() => {
    if (!rawCases.length) return
    if (lang === 'es') { setCases(rawCases); return }
    let cancelled = false
    Promise.all(rawCases.map(async c => ({
      ...c,
      title:        await translateText(c.title, lang),
      presentation: await translateText(c.presentation, lang),
    }))).then(translated => { if (!cancelled) setCases(translated) })
    return () => { cancelled = true }
  }, [rawCases, lang])

  const availableModalities = [...new Set(cases.map(c => c.modality))]

  const filtered = cases.filter(c => {
    const matchSearch     = c.title.toLowerCase().includes(search.toLowerCase())
    const matchModality   = !modality || c.modality === modality
    const matchDifficulty = !difficulty || c.difficulty === difficulty
    return matchSearch && matchModality && matchDifficulty
  })

  const hasFilter = modality || difficulty || search

  return (
    <div className="min-h-screen bg-gray-50">
      {showTour && <TourGuide slides={SLIDES} onClose={() => setShowTour(false)} />}
      {/* Hero */}
      <div className="bg-gradient-to-br from-[#5b21b6] to-[#7c3aed] text-white py-14 px-8 text-center relative">
        <button onClick={() => setShowTour(true)} title={lbl('Cómo funciona','How it works')}
          className="absolute top-4 right-4 w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 text-white text-sm font-bold transition flex items-center justify-center">?</button>
        <div className="text-purple-200 text-sm font-semibold uppercase tracking-widest mb-2">
          {lang === 'en' ? 'Visual interpretation' : 'Interpretación visual'}
        </div>
        <h1 className="text-4xl font-bold mb-3">
          {lang === 'en' ? 'Clinical Images & Studies' : 'Imágenes Clínicas y Estudios'}
        </h1>
        <p className="text-purple-100 text-base max-w-xl mx-auto mb-6">
          {lang === 'en'
            ? 'Interpret X-rays, ECGs, CT scans and more. Identify findings and answer guided questions.'
            : 'Interpreta radiografías, ECGs, TCs y más. Identifica hallazgos y responde preguntas guiadas.'}
        </p>
        <input
          className="w-full max-w-xl px-5 py-3 rounded-full text-gray-800 text-sm outline-none shadow"
          placeholder={lang === 'en' ? 'Search case...' : 'Buscar caso...'}
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>

      {/* Filtros */}
      <div className="px-8 pt-5 pb-2 space-y-3 max-w-5xl mx-auto">
        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-20 shrink-0">
            {lang === 'en' ? 'Modality' : 'Modalidad'}
          </span>
          <button onClick={() => setModality(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!modality ? "bg-purple-700 text-white border-purple-700" : "bg-white text-gray-600 border-gray-300 hover:border-purple-600"}`}>
            {lang === 'en' ? 'All' : 'Todas'}
          </button>
          {availableModalities.map(m => (
            <button key={m} onClick={() => setModality(m)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${modality === m ? "bg-purple-700 text-white border-purple-700" : "bg-white text-gray-600 border-gray-300 hover:border-purple-600"}`}>
              {MODALITY_ICON[m]} {lang === 'en' ? (MODALITY_EN[m] ?? m) : m}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-20 shrink-0">
            {t.filterLevel}
          </span>
          <button onClick={() => setDifficulty(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!difficulty ? "bg-purple-700 text-white border-purple-700" : "bg-white text-gray-600 border-gray-300 hover:border-purple-600"}`}>
            {lang === 'en' ? 'All' : 'Todos'}
          </button>
          {DIFFICULTIES.map(d => (
            <button key={d} onClick={() => setDifficulty(d)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${difficulty === d
                  ? d === "Básico" ? "bg-green-600 text-white border-green-600"
                  : d === "Intermedio" ? "bg-yellow-500 text-white border-yellow-500"
                  : "bg-red-600 text-white border-red-600"
                  : "bg-white text-gray-600 border-gray-300 hover:border-purple-600"}`}>
              {t.difficulties?.[d] ?? d}
            </button>
          ))}
        </div>
      </div>

      {/* Contador */}
      <div className="px-8 py-3 text-xs text-gray-400 max-w-5xl mx-auto">
        {filtered.length} {lang === 'en'
          ? (filtered.length === 1 ? 'case' : hasFilter ? 'cases found' : 'cases available')
          : (filtered.length === 1 ? 'caso' : hasFilter ? 'casos encontrados' : 'casos disponibles')}
      </div>

      {/* Grid */}
      <div className="px-8 pb-16 max-w-5xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.length === 0 ? (
          <p className="text-gray-400 col-span-3 text-center py-16">
            {lang === 'en' ? 'No cases found.' : 'No se encontraron casos.'}
          </p>
        ) : (
          filtered.map(c => {
            const prog  = getProgress('image', c.id)
            const BADGE = { success: { label: t.completed, cls: 'bg-green-100 text-green-700 border-green-200' }, warning: { label: t.withErrors, cls: 'bg-yellow-100 text-yellow-700 border-yellow-200' }, failure: { label: t.failed, cls: 'bg-red-100 text-red-700 border-red-200' } }
            const badge = prog ? BADGE[prog.best_result] : null
            return (
              <Link key={c.id} to={`/clinical-image/${c.id}`}
                className="bg-white rounded-2xl shadow hover:shadow-md transition p-6 border border-gray-100 group">
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold text-purple-600 uppercase tracking-wide flex items-center gap-1">
                    {MODALITY_ICON[c.modality]} {lang === 'en' ? (MODALITY_EN[c.modality] ?? c.modality) : c.modality}
                  </span>
                  <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${DIFFICULTY_STYLES[c.difficulty] ?? ''}`}>
                    {t.difficulties?.[c.difficulty] ?? c.difficulty}
                  </span>
                </div>
                <h2 className="text-lg font-bold text-gray-800 group-hover:text-purple-700 transition mb-2">{c.title}</h2>
                <p className="text-sm text-gray-500 line-clamp-3">{c.presentation}</p>
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-xs text-purple-600 font-medium">
                    {prog ? `${t.retry} (${prog.attempts} ${prog.attempts === 1 ? t.attempt : t.attempts})` : (lang === 'en' ? 'Start interpretation →' : 'Iniciar interpretación →')}
                  </span>
                  {badge
                    ? <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${badge.cls}`}>{badge.label}</span>
                    : <span className="text-xs text-gray-400">{c.question_count} {lang === 'en' ? 'questions' : 'preguntas'}</span>}
                </div>
              </Link>
            )
          })
        )}
      </div>
    </div>
  )
}
