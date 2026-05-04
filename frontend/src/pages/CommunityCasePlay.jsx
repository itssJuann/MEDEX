import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { saveProgress } from '../utils/progress'

export default function CommunityCasePlay() {
  const { id } = useParams()
  const { lang } = useLang()
  const lbl = (es, en) => lang === 'en' ? en : es

  const [data, setData]         = useState(null)
  const [index, setIndex]       = useState(0)
  const [selected, setSelected] = useState(null)
  const [results, setResults]   = useState([])
  const [done, setDone]         = useState(false)

  useEffect(() => {
    fetch(`${API}/community-cases/${id}`)
      .then(r => r.ok ? r.json() : null)
      .then(d => setData(d))
      .catch(() => setData(null))
  }, [id])

  if (!data) return (
    <div className="p-10 text-center text-gray-400">
      {lbl('Cargando...', 'Loading...')}
    </div>
  )

  const questions   = data.questions
  const current     = questions[index]
  const selectedOpt = current?.options.find(o => o.id === selected)
  const correctOpt  = current?.options.find(o => o.correct)
  const score       = results.filter(r => r.correct).length
  const pct         = Math.round((score / questions.length) * 100)

  const handleSelect = (opt) => {
    if (selected) return
    setSelected(opt.id)
    setResults(r => [...r, { correct: opt.correct, selectedId: opt.id }])
  }

  const next = () => {
    if (index + 1 >= questions.length) {
      const finalPct = Math.round(((results.filter(r => r.correct).length + (selectedOpt?.correct ? 0 : 0)) / questions.length) * 100)
      const result = finalPct >= 80 ? 'success' : finalPct >= 50 ? 'warning' : 'failure'
      saveProgress('community', id, result)
      setDone(true)
    } else {
      setIndex(i => i + 1)
      setSelected(null)
    }
  }

  const restart = () => {
    setIndex(0); setSelected(null); setResults([]); setDone(false)
  }

  if (done) {
    const grade = pct >= 80 ? 'success' : pct >= 50 ? 'warning' : 'failure'
    const gradeStyle = {
      success: { bg: 'from-green-500 to-emerald-600',  msg: lbl('¡Excelente!','Excellent!'),       sub: lbl('Dominas este caso.','You mastered this case.') },
      warning: { bg: 'from-yellow-400 to-orange-500',  msg: lbl('Bien hecho','Well done'),          sub: lbl('Repasa los errores.','Review your mistakes.') },
      failure: { bg: 'from-red-500 to-rose-600',       msg: lbl('Sigue intentando','Keep trying'), sub: lbl('Vuelve a intentarlo.','Try again.') },
    }[grade]

    return (
      <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center px-4 py-10">
        <div className={`w-full max-w-md rounded-3xl bg-gradient-to-br ${gradeStyle.bg} text-white p-8 mb-6 text-center shadow-xl`}>
          <div className="text-6xl font-bold mb-2">{pct}%</div>
          <div className="text-2xl font-bold mb-1">{gradeStyle.msg}</div>
          <div className="text-white/80 text-sm">{gradeStyle.sub}</div>
          <div className="mt-4 text-sm text-white/70">{score}/{questions.length} {lbl('correctas','correct')}</div>
        </div>

        {/* Diagnosis */}
        <div className="w-full max-w-md bg-white rounded-2xl border border-gray-100 shadow p-5 mb-4">
          <div className="text-xs font-semibold text-gray-400 uppercase mb-2">{lbl('Diagnóstico y resolución','Diagnosis & resolution')}</div>
          <p className="text-sm text-gray-700 leading-relaxed">{data.diagnosis}</p>
          {data.pearl && (
            <div className="mt-3 bg-blue-50 border border-blue-200 rounded-xl p-3">
              <div className="text-xs font-semibold text-blue-600 mb-1">{lbl('Perla clínica','Clinical pearl')}</div>
              <p className="text-xs text-blue-800 leading-relaxed">{data.pearl}</p>
            </div>
          )}
        </div>

        {/* Answer review */}
        <div className="w-full max-w-md bg-white rounded-2xl border border-gray-100 shadow p-5 mb-5">
          <div className="text-xs font-semibold text-gray-400 uppercase mb-3">{lbl('Resumen','Summary')}</div>
          <div className="flex flex-col gap-2">
            {questions.map((q, i) => {
              const r   = results[i]
              const cor = q.options.find(o => o.correct)
              return (
                <div key={q.id} className={`rounded-xl p-3 border text-xs ${r?.correct ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`}>
                  <div className="font-semibold text-gray-700 mb-1 line-clamp-2">{i+1}. {q.text}</div>
                  {!r?.correct && <div className="text-green-700">✓ {cor?.text}</div>}
                  {r?.correct  && <div className="text-green-700">✓ {cor?.text}</div>}
                </div>
              )
            })}
          </div>
        </div>

        <div className="flex gap-3 w-full max-w-md flex-wrap">
          <button onClick={restart}
            className="flex-1 bg-violet-700 text-white py-3 rounded-2xl font-medium text-sm hover:bg-violet-800 transition">
            {lbl('Repetir','Repeat')}
          </button>
          <Link to="/community"
            className="flex-1 border border-violet-700 text-violet-700 py-3 rounded-2xl font-medium text-sm hover:bg-violet-50 transition text-center">
            {lbl('Otros casos','Other cases')}
          </Link>
          <Link to="/"
            className="w-full border border-gray-300 text-gray-600 py-3 rounded-2xl font-medium text-sm hover:bg-gray-50 transition text-center">
            {lbl('Ir al inicio','Go to home')}
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-8 max-w-2xl mx-auto">
      {/* Header */}
      <div className="mb-6">
        <Link to="/community" className="text-xs text-violet-600 hover:underline mb-2 inline-block">
          ← {lbl('Casos comunidad','Community cases')}
        </Link>
        <div className="flex items-center gap-2 mt-1 flex-wrap">
          <span className="text-xs font-semibold text-violet-600 uppercase">{data.system}</span>
          <span className="text-xs text-gray-400">•</span>
          <span className="text-xs text-gray-400">{data.difficulty}</span>
          <span className="text-xs text-gray-400">•</span>
          <span className="text-xs text-gray-400">{lbl('Por','By')} {data.author}</span>
        </div>
        <h1 className="text-xl font-bold text-gray-800 mt-1">{data.title}</h1>
      </div>

      {/* Progress bar */}
      <div className="w-full bg-gray-100 rounded-full h-2 mb-6 overflow-hidden">
        <div className="h-2 rounded-full bg-violet-600 transition-all"
          style={{ width: `${(index / questions.length) * 100}%` }}/>
      </div>
      <div className="text-xs text-gray-400 mb-5 text-right">{index + 1} / {questions.length}</div>

      {/* Clinical presentation (always visible) */}
      <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-5 mb-5">
        <div className="text-xs font-semibold text-gray-400 uppercase mb-2">{lbl('Presentación clínica','Clinical presentation')}</div>
        <p className="text-sm text-gray-700 leading-relaxed whitespace-pre-line">{data.presentation}</p>
      </div>

      {/* Question */}
      <div className="bg-white rounded-2xl shadow border border-gray-100 p-6">
        <div className="text-xs font-semibold text-violet-600 uppercase mb-3">
          {lbl(`Pregunta ${index + 1} de ${questions.length}`, `Question ${index + 1} of ${questions.length}`)}
        </div>
        <p className="text-gray-800 font-semibold text-base leading-snug mb-5">{current.text}</p>

        <div className="flex flex-col gap-3">
          {current.options.map(opt => {
            const isSelected = selected === opt.id
            const showResult = !!selected
            let cls = 'text-left px-4 py-3.5 rounded-xl border text-sm transition '
            if (!showResult)
              cls += 'border-gray-200 bg-gray-50 hover:border-violet-400 hover:bg-violet-50 cursor-pointer'
            else if (opt.correct)
              cls += 'border-green-400 bg-green-50 text-green-800'
            else if (isSelected && !opt.correct)
              cls += 'border-red-400 bg-red-50 text-red-800'
            else
              cls += 'border-gray-100 bg-gray-50 text-gray-400 opacity-60'

            return (
              <button key={opt.id} onClick={() => handleSelect(opt)} disabled={!!selected} className={cls}>
                <span className="font-semibold text-gray-400 mr-2">{opt.id.toUpperCase()}.</span>
                {opt.text}
                {showResult && opt.correct && <span className="ml-2 text-green-600 font-bold">✓</span>}
                {showResult && isSelected && !opt.correct && <span className="ml-2 text-red-500 font-bold">✕</span>}
              </button>
            )
          })}
        </div>

        {/* Feedback */}
        {selected && selectedOpt && (
          <div className={`mt-5 rounded-xl border p-4 text-sm leading-relaxed ${
            selectedOpt.correct ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'
          }`}>
            <div className="font-semibold mb-1">
              {selectedOpt.correct ? '✓ ' : '✕ '}
              {selectedOpt.correct ? lbl('Correcto','Correct') : lbl('Incorrecto — la correcta es','Incorrect — correct answer is') + ` ${correctOpt?.id?.toUpperCase()}`}
            </div>
            <p>{selectedOpt.feedback}</p>
          </div>
        )}

        {selected && (
          <button onClick={next}
            className="mt-5 w-full bg-violet-700 text-white py-3 rounded-xl text-sm font-medium hover:bg-violet-800 transition">
            {index + 1 < questions.length
              ? lbl('Siguiente pregunta →','Next question →')
              : lbl('Ver resultados →','See results →')}
          </button>
        )}
      </div>
    </div>
  )
}
