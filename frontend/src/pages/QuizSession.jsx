import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { saveProgress as persistProgress } from '../utils/progress'
import { translateText } from '../utils/translate'

const TYPE_LABELS = {
  next_step:    { es: '¿Cuál es el siguiente paso?', en: "What's the next step?",    icon: '➜', color: 'text-blue-600  bg-blue-50  border-blue-200'  },
  common_error: { es: '¿Cuál es el error más frecuente?', en: "What's the most common error?", icon: '⚠', color: 'text-red-600   bg-red-50   border-red-200'   },
  diagnosis:    { es: '¿Cuál es la conducta correcta?', en: "What's the correct approach?",   icon: '✦', color: 'text-green-600 bg-green-50 border-green-200' },
  complication: { es: '¿Cuál es la complicación más temida?', en: "What's the most feared complication?", icon: '💢', color: 'text-orange-600 bg-orange-50 border-orange-200' },
}

export default function QuizSession() {
  const { id } = useParams()
  const { lang } = useLang()
  const lbl = (es, en) => lang === 'en' ? en : es

  const [rawData, setRawData]   = useState(null)
  const [data, setData]         = useState(null)
  const [index, setIndex]       = useState(0)
  const [selected, setSelected] = useState(null)
  const [results, setResults]   = useState([])   // {correct, selectedId}
  const [streak, setStreak]     = useState(0)
  const [maxStreak, setMaxStreak] = useState(0)
  const [done, setDone]         = useState(false)

  useEffect(() => {
    fetch(`${API}/quizzes/${id}`)
      .then(r => r.json()).then(setRawData)
  }, [id])

  // Translate questions, option text and explanations
  useEffect(() => {
    if (!rawData) return
    if (lang === 'es') { setData(rawData); return }
    let cancelled = false
    const translateQuiz = async () => {
      const questions = await Promise.all(rawData.questions.map(async q => ({
        ...q,
        text: await translateText(q.text, lang),
        options: await Promise.all(q.options.map(async opt => ({
          ...opt,
          text:        await translateText(opt.text, lang),
          explanation: await translateText(opt.explanation, lang),
        }))),
      })))
      if (!cancelled) setData({ ...rawData, questions })
    }
    translateQuiz()
    return () => { cancelled = true }
  }, [rawData, lang])

  if (!data) return <div className="p-10 text-center text-gray-400">{lbl('Cargando...', 'Loading...')}</div>

  const questions  = data.questions
  const current    = questions[index]
  const typeMeta   = TYPE_LABELS[current?.type] ?? TYPE_LABELS.next_step
  const score      = results.filter(r => r.correct).length
  const pct        = Math.round((score / questions.length) * 100)

  const handleSelect = (opt) => {
    if (selected) return
    setSelected(opt.id)
    const correct = opt.correct
    setResults(r => [...r, { correct, selectedId: opt.id }])
    if (correct) {
      const ns = streak + 1
      setStreak(ns)
      setMaxStreak(m => Math.max(m, ns))
    } else {
      setStreak(0)
    }
  }

  const saveProgress = (result) => { persistProgress('quiz', id, result) }

  const next = () => {
    if (index + 1 >= questions.length) {
      const finalScore = results.filter(r => r.correct).length + (selectedOpt && questions[index].options.find(o=>o.id===selectedOpt)?.correct ? 0 : 0)
      const pct = Math.round((results.filter(r => r.correct).length / questions.length) * 100)
      saveProgress(pct >= 80 ? 'success' : pct >= 50 ? 'warning' : 'failure')
      setDone(true)
    } else {
      setIndex(i => i + 1); setSelected(null)
    }
  }

  const restart = () => {
    setIndex(0); setSelected(null)
    setResults([]); setStreak(0); setMaxStreak(0); setDone(false)
  }

  if (done) {
    const grade = pct >= 80 ? 'success' : pct >= 50 ? 'warning' : 'failure'
    const gradeStyle = {
      success: { bg: 'from-green-500 to-emerald-600',  msg: lbl('¡Excelente!', 'Excellent!'),  sub: lbl('Dominas este tema.', 'You master this topic.') },
      warning: { bg: 'from-yellow-400 to-orange-500',  msg: lbl('Bien hecho', 'Well done'),     sub: lbl('Repasa los errores para afianzar.', 'Review mistakes to consolidate.') },
      failure: { bg: 'from-red-500 to-rose-600',       msg: lbl('Sigue practicando', 'Keep practicing'), sub: lbl('Revisa los casos clínicos de este sistema.', 'Review the clinical cases for this system.') },
    }[grade]

    return (
      <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center px-4 py-10">
        <div className={`w-full max-w-md rounded-3xl bg-gradient-to-br ${gradeStyle.bg} text-white p-8 mb-6 text-center shadow-xl`}>
          <div className="text-6xl font-bold mb-2">{pct}%</div>
          <div className="text-2xl font-bold mb-1">{gradeStyle.msg}</div>
          <div className="text-white/80 text-sm">{gradeStyle.sub}</div>
          <div className="mt-6 flex justify-center gap-8 text-sm">
            <div><div className="text-2xl font-bold">{score}/{questions.length}</div><div className="text-white/70">{lbl('Correctas', 'Correct')}</div></div>
            <div><div className="text-2xl font-bold">{maxStreak}</div><div className="text-white/70">{lbl('Racha máx.', 'Max streak')}</div></div>
          </div>
        </div>

        {/* Question review */}
        <div className="w-full max-w-md bg-white rounded-2xl border border-gray-100 shadow p-5 mb-5">
          <div className="text-xs font-semibold text-gray-400 uppercase mb-3">{lbl('Resumen de respuestas', 'Answer summary')}</div>
          <div className="flex flex-col gap-2">
            {questions.map((q, i) => {
              const r = results[i]
              const chosen = q.options.find(o => o.id === r?.selectedId)
              const correct = q.options.find(o => o.correct)
              return (
                <div key={q.id} className={`rounded-xl p-3 border text-xs ${r?.correct ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`}>
                  <div className="font-semibold text-gray-700 mb-1 line-clamp-2">{i + 1}. {q.text}</div>
                  {!r?.correct && (
                    <>
                      <div className="text-red-600">✕ {chosen?.text}</div>
                      <div className="text-green-700">✓ {correct?.text}</div>
                    </>
                  )}
                  {r?.correct && <div className="text-green-700">✓ {correct?.text}</div>}
                </div>
              )
            })}
          </div>
        </div>

        <div className="flex gap-3 w-full max-w-md flex-wrap">
          <button onClick={restart}
            className="flex-1 bg-indigo-700 text-white py-3 rounded-2xl font-medium text-sm hover:bg-indigo-800 transition">
            {lbl('Repetir quiz', 'Repeat quiz')}
          </button>
          <Link to="/quizzes"
            className="flex-1 border border-indigo-700 text-indigo-700 py-3 rounded-2xl font-medium text-sm hover:bg-indigo-50 transition text-center">
            {lbl('Otros quizzes', 'Other quizzes')}
          </Link>
          <Link to="/"
            className="w-full border border-gray-300 text-gray-600 py-3 rounded-2xl font-medium text-sm hover:bg-gray-50 transition text-center">
            {lbl('Ir al inicio', 'Go to home')}
          </Link>
        </div>
      </div>
    )
  }

  const selectedOpt = current.options.find(o => o.id === selected)
  const correctOpt  = current.options.find(o => o.correct)

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-8 max-w-2xl mx-auto">

      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <Link to="/quizzes" className="text-xs text-indigo-600 hover:underline">
          ← {lbl('Quizzes', 'Quizzes')}
        </Link>
        <div className="flex items-center gap-4 text-sm">
          {/* Streak */}
          {streak > 1 && (
            <div className="flex items-center gap-1 bg-orange-50 border border-orange-200 text-orange-600 px-3 py-1 rounded-full text-xs font-bold">
              🔥 {streak} {lbl('en racha', 'streak')}
            </div>
          )}
          {/* Score */}
          <div className="text-xs text-gray-500">
            {score}/{index} {lbl('correctas', 'correct')}
          </div>
        </div>
      </div>

      {/* Progress bar */}
      <div className="w-full bg-gray-100 rounded-full h-2 mb-6 overflow-hidden">
        <div className="h-2 rounded-full bg-indigo-600 transition-all"
          style={{ width: `${((index) / questions.length) * 100}%` }}/>
      </div>
      <div className="text-xs text-gray-400 mb-6 text-right">
        {index + 1} / {questions.length}
      </div>

      {/* Question card */}
      <div className="bg-white rounded-2xl shadow border border-gray-100 p-6">

        {/* Type badge */}
        <div className={`inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-full border mb-4 ${typeMeta.color}`}>
          <span>{typeMeta.icon}</span>
          <span>{lang === 'en' ? typeMeta.en : typeMeta.es}</span>
        </div>

        {/* Question text */}
        <p className="text-gray-800 font-semibold text-base leading-snug mb-5">{current.text}</p>

        {/* Options */}
        <div className="flex flex-col gap-3">
          {current.options.map(opt => {
            const isSelected = selected === opt.id
            const showResult = !!selected

            let cls = 'text-left px-4 py-3.5 rounded-xl border text-sm transition '
            if (!showResult) {
              cls += 'border-gray-200 bg-gray-50 hover:border-indigo-400 hover:bg-indigo-50 cursor-pointer'
            } else if (opt.correct) {
              cls += 'border-green-400 bg-green-50 text-green-800'
            } else if (isSelected && !opt.correct) {
              cls += 'border-red-400 bg-red-50 text-red-800'
            } else {
              cls += 'border-gray-100 bg-gray-50 text-gray-400 opacity-60'
            }

            return (
              <button key={opt.id} onClick={() => handleSelect(opt)}
                disabled={!!selected} className={cls}>
                <span className="font-semibold text-gray-400 mr-2">{opt.id.toUpperCase()}.</span>
                {opt.text}
                {showResult && opt.correct && <span className="ml-2 text-green-600">✓</span>}
                {showResult && isSelected && !opt.correct && <span className="ml-2 text-red-500">✕</span>}
              </button>
            )
          })}
        </div>

        {/* Feedback */}
        {selected && selectedOpt && (
          <div className={`mt-5 rounded-xl border p-4 text-sm leading-relaxed ${
            selectedOpt.correct
              ? 'bg-green-50 border-green-200 text-green-900'
              : 'bg-red-50 border-red-200 text-red-900'
          }`}>
            <div className="font-semibold mb-1">
              {selectedOpt.correct ? '✓ ' : '✕ '}
              {selectedOpt.correct ? lbl('Correcto', 'Correct') : lbl('Incorrecto', 'Incorrect')}
              {!selectedOpt.correct && ` — ${lbl('La correcta es', 'Correct answer is')} ${correctOpt?.id?.toUpperCase()}`}
            </div>
            <p>{selectedOpt.explanation}</p>
          </div>
        )}

        {/* Next button */}
        {selected && (
          <button onClick={next}
            className="mt-5 w-full bg-indigo-700 text-white py-3 rounded-xl text-sm font-medium hover:bg-indigo-800 transition">
            {index + 1 < questions.length
              ? lbl('Siguiente pregunta →', 'Next question →')
              : lbl('Ver resultados →', 'See results →')}
          </button>
        )}
      </div>
    </div>
  )
}
