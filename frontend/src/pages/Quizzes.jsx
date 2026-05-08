import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { getProgress } from '../utils/progress'
import { translateText } from '../utils/translate'
import TourGuide from '../components/TourGuide'

const TOUR_KEY = 'medex_quizzes_tour_done'

const DIFFICULTY_STYLES = {
  'Básico':     'bg-green-50 text-green-700 border border-green-200',
  'Intermedio': 'bg-yellow-50 text-yellow-700 border border-yellow-200',
  'Avanzado':   'bg-red-50 text-red-700 border border-red-200',
}

const SYSTEM_COLORS = {
  'Cardiovascular': '#ef4444', 'Respiratorio': '#3b82f6',
  'Neurológico': '#6366f1',    'Digestivo': '#f59e0b',
  'Endocrino': '#10b981',      'Mixto': '#8b5cf6',
}

export default function Quizzes() {
  const { t, lang } = useLang()
  const [rawQuizzes, setRawQuizzes] = useState([])
  const [quizzes, setQuizzes]       = useState([])
  const [filter, setFilter]         = useState(null)
  const [showTour, setShowTour]     = useState(false)

  const lbl = (es, en) => lang === 'en' ? en : es

  useEffect(() => {
    if (!localStorage.getItem(TOUR_KEY)) { setShowTour(true); localStorage.setItem(TOUR_KEY, '1') }
  }, [])

  const SLIDES = [
    {
      icon: '📝',
      title: lbl('Micro-Quizzes', 'Micro-Quizzes'),
      desc: lbl('Tests cortos con preguntas del tipo "siguiente paso" y "error más frecuente". Feedback explicativo en cada respuesta.', 'Short tests with "next step" and "most common error" questions. Explanatory feedback on every answer.'),
      visual: (
        <div className="flex flex-col gap-2 w-full">
          {[['➜','Siguiente paso','text-blue-700 bg-blue-50 border-blue-200'],['⚠','Error frecuente','text-red-700 bg-red-50 border-red-200'],['✦','Conducta correcta','text-green-700 bg-green-50 border-green-200']].map(([icon,label,cls],i) => (
            <div key={i} className={`flex items-center gap-2 px-3 py-2 rounded-xl border text-xs font-semibold ${cls}`}>
              <span>{icon}</span>{label}
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '☑',
      title: lbl('Selecciona TODAS las correctas', 'Select ALL that apply'),
      desc: lbl('Las preguntas "multi" tienen varias respuestas correctas. Debes marcar todas para puntuar.', '"Multi" questions have several correct answers. You must mark all of them to score.'),
      visual: (
        <div className="flex flex-col gap-2 w-full">
          {[['AAS 100 mg/día', true],['Betabloqueante', true],['Antibiótico profiláctico', false],['Estatina alta intensidad', true]].map(([text, correct], i) => (
            <div key={i} className={`flex items-center gap-2 px-3 py-2 rounded-xl border text-xs ${correct ? 'bg-purple-50 border-purple-300 text-purple-800' : 'bg-gray-50 border-gray-200 text-gray-400'}`}>
              <div className={`w-4 h-4 rounded border-2 flex items-center justify-center shrink-0 ${correct ? 'bg-purple-500 border-purple-500' : 'border-gray-300'}`}>
                {correct && <span className="text-white text-xs">✓</span>}
              </div>
              {text}
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '⟳',
      title: lbl('Ordena los pasos', 'Put the steps in order'),
      desc: lbl('Las preguntas "orden" te piden colocar pasos clínicos en la secuencia correcta. Haz clic para numerarlos.', '"Order" questions ask you to place clinical steps in the correct sequence. Click to number them.'),
      visual: (
        <div className="flex flex-col gap-2 w-full">
          {[['Hemocultivos x2',1],['Antibiótico IV',2],['Cristaloides 30mL/kg',3]].map(([text, pos], i) => (
            <div key={i} className="flex items-center gap-2 px-3 py-2 bg-teal-50 border border-teal-300 rounded-xl text-xs text-teal-800">
              <div className="w-7 h-7 rounded-full bg-teal-500 text-white flex items-center justify-center text-sm font-bold shrink-0">{pos}</div>
              {text}
            </div>
          ))}
        </div>
      ),
    },
    {
      icon: '🔥',
      title: lbl('Racha y progreso', 'Streak and progress'),
      desc: lbl('Acumula rachas de respuestas correctas. Tu progreso queda guardado y puedes repetir cualquier quiz.', 'Build streaks of correct answers. Your progress is saved and you can replay any quiz.'),
      visual: (
        <div className="flex flex-col items-center gap-3 w-full">
          <div className="flex items-center gap-2 bg-orange-50 border border-orange-200 text-orange-700 px-4 py-2 rounded-full text-sm font-bold">🔥 5 en racha</div>
          <div className="w-full bg-gray-200 rounded-full h-2"><div className="h-2 bg-indigo-600 rounded-full" style={{width:'75%'}} /></div>
          <div className="text-xs text-gray-500">6 / 8 correctas — 75%</div>
        </div>
      ),
    },
  ]

  useEffect(() => {
    fetch(`${API}/quizzes`)
      .then(r => r.json()).then(setRawQuizzes).catch(() => {})
  }, [])

  useEffect(() => {
    if (!rawQuizzes.length) return
    if (lang === 'es') { setQuizzes(rawQuizzes); return }
    let cancelled = false
    Promise.all(rawQuizzes.map(async q => ({
      ...q,
      title:       await translateText(q.title, lang),
      description: await translateText(q.description, lang),
    }))).then(translated => { if (!cancelled) setQuizzes(translated) })
    return () => { cancelled = true }
  }, [rawQuizzes, lang])

  const systems = [...new Set(quizzes.map(q => q.system))]
  const filtered = filter ? quizzes.filter(q => q.system === filter) : quizzes

  return (
    <div className="min-h-screen bg-gray-50">
      {showTour && <TourGuide slides={SLIDES} onClose={() => setShowTour(false)} />}
      {/* Hero */}
      <div className="bg-gradient-to-br from-[#1e1b4b] to-[#312e81] text-white py-14 px-8 text-center relative">
        <button onClick={() => setShowTour(true)} title={lbl('Cómo funciona','How it works')}
          className="absolute top-4 right-4 w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 text-white text-sm font-bold transition flex items-center justify-center">?</button>
        <div className="text-indigo-300 text-sm font-semibold uppercase tracking-widest mb-2">
          {lbl('Evaluación activa', 'Active assessment')}
        </div>
        <h1 className="text-4xl font-bold mb-3">
          {lbl('Micro-Quizzes', 'Micro-Quizzes')}
        </h1>
        <p className="text-indigo-200 text-base max-w-xl mx-auto">
          {lbl(
            'Preguntas tipo "¿Cuál es el siguiente paso?" y "¿Cuál es el error más frecuente?" con feedback explicativo.',
            'Questions like "What\'s the next step?" and "What\'s the most common error?" with explanatory feedback.'
          )}
        </p>
      </div>

      {/* Filters */}
      <div className="px-8 pt-5 pb-2 max-w-5xl mx-auto">
        <div className="flex gap-3 flex-wrap">
          <button onClick={() => setFilter(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!filter ? 'bg-indigo-700 text-white border-indigo-700' : 'bg-white text-gray-600 border-gray-300 hover:border-indigo-500'}`}>
            {lbl('Todos', 'All')}
          </button>
          {systems.map(s => (
            <button key={s} onClick={() => setFilter(s)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${filter === s ? 'text-white border-transparent' : 'bg-white text-gray-600 border-gray-300 hover:border-indigo-500'}`}
              style={filter === s ? { backgroundColor: SYSTEM_COLORS[s] ?? '#6366f1', borderColor: SYSTEM_COLORS[s] } : {}}>
              {t.systems?.[s] ?? s}
            </button>
          ))}
        </div>
      </div>

      <div className="px-8 py-3 text-xs text-gray-400 max-w-5xl mx-auto">
        {filtered.length} {lbl('packs disponibles', 'packs available')}
      </div>

      {/* Grid */}
      <div className="px-8 pb-16 max-w-5xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.map(q => {
          const prog  = getProgress('quiz', q.id)
          const BADGE = { success: { label: lbl('Completado', 'Completed'), cls: 'bg-green-100 text-green-700 border-green-200' }, warning: { label: lbl('Con errores', 'With errors'), cls: 'bg-yellow-100 text-yellow-700 border-yellow-200' }, failure: { label: lbl('Fallido', 'Failed'), cls: 'bg-red-100 text-red-700 border-red-200' } }
          const badge = prog ? BADGE[prog.best_result] : null
          return (
          <Link key={q.id} to={`/quiz/${q.id}`}
            className="bg-white rounded-2xl shadow hover:shadow-md transition p-6 border border-gray-100 group">
            <div className="h-1 w-12 rounded-full mb-4" style={{ backgroundColor: SYSTEM_COLORS[q.system] ?? '#6366f1' }}/>
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-semibold uppercase tracking-wide" style={{ color: SYSTEM_COLORS[q.system] ?? '#6366f1' }}>
                {t.systems?.[q.system] ?? q.system}
              </span>
              <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${DIFFICULTY_STYLES[q.difficulty] ?? ''}`}>
                {t.difficulties?.[q.difficulty] ?? q.difficulty}
              </span>
            </div>
            <h2 className="text-lg font-bold text-gray-800 group-hover:text-indigo-700 transition mb-2">{q.title}</h2>
            <p className="text-sm text-gray-500 line-clamp-2 mb-4">{q.description}</p>
            <div className="flex items-center justify-between">
              <span className="text-xs text-indigo-600 font-medium">
                {prog ? `${lbl('Reintentar', 'Retry')} (${prog.attempts} ${prog.attempts === 1 ? lbl('intento', 'attempt') : lbl('intentos', 'attempts')})` : lbl('Iniciar quiz →', 'Start quiz →')}
              </span>
              {badge
                ? <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${badge.cls}`}>{badge.label}</span>
                : <span className="text-xs text-gray-400">{q.question_count} {lbl('preguntas', 'questions')}</span>}
            </div>
          </Link>
          )
        })}
      </div>
    </div>
  )
}
