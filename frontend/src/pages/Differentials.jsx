import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { getProgress } from '../utils/progress'
import TourGuide from '../components/TourGuide'

const TOUR_KEY = 'medex_differentials_tour_done'

const SYSTEMS      = ["Cardiovascular", "Respiratorio", "Digestivo", "Neurológico", "Endocrino", "Infeccioso", "Renal"]
const DIFFICULTIES = ["Básico", "Intermedio", "Avanzado"]

const DIFFICULTY_STYLES = {
  "Básico":     "bg-green-50 text-green-700 border border-green-200",
  "Intermedio": "bg-yellow-50 text-yellow-700 border border-yellow-200",
  "Avanzado":   "bg-red-50 text-red-700 border border-red-200",
}

export default function Differentials() {
  const { t, lang } = useLang()
  const [rawCases, setRawCases]     = useState([])
  const [cases, setCases]           = useState([])
  const [search, setSearch]         = useState("")
  const [system, setSystem]         = useState(null)
  const [difficulty, setDifficulty] = useState(null)
  const [showTour, setShowTour]     = useState(false)

  const lbl = (es, en) => lang === 'en' ? en : es

  useEffect(() => {
    if (!localStorage.getItem(TOUR_KEY)) { setShowTour(true); localStorage.setItem(TOUR_KEY, '1') }
  }, [])

  const SLIDES = [
    {
      icon: '🔬',
      title: lbl('Diagnóstico Diferencial', 'Differential Diagnosis'),
      desc: lbl('Se te presenta un cuadro clínico y debes identificar los diagnósticos posibles, ordenados por probabilidad.', 'You are presented with a clinical picture and must identify possible diagnoses, ordered by probability.'),
      visual: (
        <div className="flex flex-col gap-2 w-full">
          <div className="text-xs font-semibold text-gray-500 mb-1">Disnea + dolor pleurítico + hemoptisis...</div>
          {[['TEP','Alta probabilidad','bg-red-50 border-red-300 text-red-700'],['Neumonía','Media probabilidad','bg-yellow-50 border-yellow-300 text-yellow-700'],['Pleuritis','Baja probabilidad','bg-green-50 border-green-200 text-green-700']].map(([dx,prob,cls],i)=>(
            <div key={i} className={`flex items-center justify-between px-3 py-2 rounded-xl border text-xs font-medium ${cls}`}>
              <span>{dx}</span><span className="opacity-70">{prob}</span>
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '📋',
      title: lbl('Analiza los datos clínicos', 'Analyze clinical data'),
      desc: lbl('Cada caso te muestra síntomas, signos y resultados de laboratorio. Usa toda la información para razonar.', 'Each case shows symptoms, signs and lab results. Use all the information to reason through it.'),
      visual: (
        <div className="flex flex-col gap-2 w-full text-xs">
          {[['Síntomas','Disnea brusca, hemoptisis, dolor pleurítico'],['Antecedentes','Cirugía hace 10 días, inmovilización'],['Labs','D-dímero 3.400, SatO2 88%']].map(([label,val],i)=>(
            <div key={i} className="flex gap-2 items-start bg-white border border-gray-200 rounded-xl px-3 py-2">
              <span className="font-semibold text-gray-500 shrink-0 w-20">{label}</span>
              <span className="text-gray-700">{val}</span>
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '🎯',
      title: lbl('Elige el diagnóstico más probable', 'Choose the most likely diagnosis'),
      desc: lbl('Selecciona el diagnóstico correcto y recibe feedback explicando por qué cada opción es más o menos probable.', 'Select the correct diagnosis and get feedback explaining why each option is more or less likely.'),
      visual: (
        <div className="flex flex-col gap-2 w-full">
          {[['Tromboembolismo Pulmonar',true],['Neumonía atípica',false],['Crisis de asma',false]].map(([dx,correct],i)=>(
            <div key={i} className={`px-3 py-2 rounded-xl border text-xs font-medium ${correct ? 'border-green-400 bg-green-50 text-green-800' : 'border-gray-200 bg-gray-50 text-gray-500'}`}>
              {correct && '✓ '}{dx}
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '💡',
      title: lbl('Aprende el razonamiento', 'Learn the reasoning'),
      desc: lbl('El feedback explica qué hallazgos apuntan a cada diagnóstico y cuáles permiten descartarlos.', 'Feedback explains which findings point to each diagnosis and which allow you to rule them out.'),
      visual: (
        <div className="w-full bg-blue-50 border border-blue-200 rounded-xl p-4">
          <div className="text-xs font-bold text-blue-700 mb-1">💡 Razonamiento clínico</div>
          <div className="text-xs text-blue-800 leading-relaxed">Cirugía reciente + inmovilización + D-dímero elevado + taquicardia + hipoxemia = Wells alto → TEP hasta confirmar con TCAP.</div>
        </div>
      ),
    },
  ]

  useEffect(() => {
    fetch(`${API}/differentials`)
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

  const filtered = cases.filter(c => {
    const matchSearch     = c.title.toLowerCase().includes(search.toLowerCase())
    const matchSystem     = !system || c.system === system
    const matchDifficulty = !difficulty || c.difficulty === difficulty
    return matchSearch && matchSystem && matchDifficulty
  })

  const hasFilter = system || difficulty || search

  return (
    <div className="min-h-screen bg-gray-50">
      {showTour && <TourGuide slides={SLIDES} onClose={() => setShowTour(false)} />}
      <div className="bg-primary text-white py-14 px-8 text-center relative">
        <button onClick={() => setShowTour(true)} title={lbl('Cómo funciona','How it works')}
          className="absolute top-4 right-4 w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 text-white text-sm font-bold transition flex items-center justify-center">?</button>
        <div className="text-accent text-sm font-semibold uppercase tracking-widest mb-2">{t.interactiveMode}</div>
        <h1 className="text-4xl font-bold mb-3">{t.differentialsTitle}</h1>
        <p className="text-blue-200 text-base max-w-xl mx-auto mb-6">{t.differentialsSubtitle}</p>
        <input
          className="w-full max-w-xl px-5 py-3 rounded-full text-gray-800 text-sm outline-none shadow"
          placeholder={t.searchDiff}
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>

      <div className="px-8 pt-5 pb-2 space-y-3 max-w-5xl mx-auto">
        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-16 shrink-0">{t.filterSystem}</span>
          <button onClick={() => setSystem(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!system ? "bg-primary text-white border-primary" : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}>
            {t.allDiff}
          </button>
          {SYSTEMS.map(s => (
            <button key={s} onClick={() => setSystem(s)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${system === s ? "bg-primary text-white border-primary" : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}>
              {t.systems?.[s] ?? s}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-16 shrink-0">{t.filterLevel}</span>
          <button onClick={() => setDifficulty(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!difficulty ? "bg-primary text-white border-primary" : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}>
            {t.allDiff}
          </button>
          {DIFFICULTIES.map(d => (
            <button key={d} onClick={() => setDifficulty(d)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${difficulty === d
                  ? d === "Básico" ? "bg-green-600 text-white border-green-600"
                  : d === "Intermedio" ? "bg-yellow-500 text-white border-yellow-500"
                  : "bg-red-600 text-white border-red-600"
                  : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}>
              {t.difficulties?.[d] ?? d}
            </button>
          ))}
        </div>
      </div>

      <div className="px-8 py-3 text-xs text-gray-400 max-w-5xl mx-auto">
        {filtered.length} {filtered.length === 1 ? t.case : (hasFilter ? t.casesFound : t.casesTotal)}
      </div>

      <div className="px-8 pb-16 max-w-5xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.length === 0 ? (
          <p className="text-gray-400 col-span-3 text-center py-16">{t.noResultsDiff}</p>
        ) : (
          filtered.map(c => {
            const prog  = getProgress('differential', c.id)
            const BADGE = { success: { label: t.completed, cls: 'bg-green-100 text-green-700 border-green-200' }, warning: { label: t.withErrors, cls: 'bg-yellow-100 text-yellow-700 border-yellow-200' }, failure: { label: t.failed, cls: 'bg-red-100 text-red-700 border-red-200' } }
            const badge = prog ? BADGE[prog.best_result] : null
            return (
              <Link key={c.id} to={`/differential/${c.id}`}
                className="bg-white rounded-2xl shadow hover:shadow-md transition p-6 border border-gray-100 group">
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold text-accent uppercase tracking-wide">{t.systems?.[c.system] ?? c.system}</span>
                  <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${DIFFICULTY_STYLES[c.difficulty] ?? ''}`}>
                    {t.difficulties?.[c.difficulty] ?? c.difficulty}
                  </span>
                </div>
                <h2 className="text-lg font-bold text-gray-800 group-hover:text-primary transition mb-2">{c.title}</h2>
                <p className="text-sm text-gray-500 line-clamp-3">{c.presentation}</p>
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-xs text-primary font-medium">
                    {prog ? `${t.retry} (${prog.attempts} ${prog.attempts === 1 ? t.attempt : t.attempts})` : t.startDiagnosis}
                  </span>
                  {badge
                    ? <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${badge.cls}`}>{badge.label}</span>
                    : <span className="text-xs text-gray-400">{c.diagnosis_count} {t.hypotheses}</span>}
                </div>
              </Link>
            )
          })
        )}
      </div>
    </div>
  )
}
