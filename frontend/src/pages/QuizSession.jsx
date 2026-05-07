import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { saveProgress as persistProgress } from '../utils/progress'
import { translateText } from '../utils/translate'

const TYPE_LABELS = {
  next_step:    { es: '¿Cuál es el siguiente paso?',          en: "What's the next step?",             icon: '➜', color: 'text-blue-600   bg-blue-50   border-blue-200'   },
  common_error: { es: '¿Cuál es el error más frecuente?',     en: "What's the most common error?",     icon: '⚠', color: 'text-red-600    bg-red-50    border-red-200'    },
  diagnosis:    { es: '¿Cuál es la conducta correcta?',       en: "What's the correct approach?",      icon: '✦', color: 'text-green-600  bg-green-50  border-green-200'  },
  complication: { es: '¿Cuál es la complicación más temida?', en: "What's the most feared complication?", icon: '💢', color: 'text-orange-600 bg-orange-50 border-orange-200' },
  multi:        { es: 'Selecciona TODAS las correctas',        en: 'Select ALL that apply',             icon: '☑', color: 'text-purple-600 bg-purple-50 border-purple-200' },
  order:        { es: 'Ordena los pasos',                      en: 'Put the steps in order',            icon: '⟳', color: 'text-teal-600   bg-teal-50   border-teal-200'   },
}

export default function QuizSession() {
  const { id }   = useParams()
  const { lang } = useLang()
  const lbl      = (es, en) => lang === 'en' ? en : es

  const [rawData, setRawData]       = useState(null)
  const [data, setData]             = useState(null)
  const [index, setIndex]           = useState(0)

  // single-choice state
  const [selected, setSelected]     = useState(null)

  // multi-choice state
  const [selectedSet, setSelectedSet] = useState(new Set())
  const [confirmed, setConfirmed]   = useState(false)

  // order state
  const [orderList, setOrderList]   = useState([])

  // hint
  const [hintShown, setHintShown]   = useState(false)

  const [results, setResults]       = useState([])
  const [streak, setStreak]         = useState(0)
  const [maxStreak, setMaxStreak]   = useState(0)
  const [done, setDone]             = useState(false)

  useEffect(() => {
    fetch(`${API}/quizzes/${id}`).then(r => r.json()).then(setRawData)
  }, [id])

  useEffect(() => {
    if (!rawData) return
    if (lang === 'es') { setData(rawData); return }
    let cancelled = false
    const go = async () => {
      const questions = await Promise.all(rawData.questions.map(async q => {
        const base = { ...q, text: await translateText(q.text, lang) }
        if (q.hint) base.hint = await translateText(q.hint, lang)
        if (q.type === 'order') {
          return {
            ...base,
            items:       await Promise.all((q.items ?? []).map(async it => ({ ...it, text: await translateText(it.text, lang) }))),
            explanation: await translateText(q.explanation ?? '', lang),
          }
        }
        return {
          ...base,
          options: await Promise.all(q.options.map(async opt => ({
            ...opt,
            text:        await translateText(opt.text, lang),
            explanation: await translateText(opt.explanation ?? '', lang),
          }))),
          ...(q.multi_explanation ? { multi_explanation: await translateText(q.multi_explanation, lang) } : {}),
        }
      }))
      if (!cancelled) setData({ ...rawData, questions })
    }
    go()
    return () => { cancelled = true }
  }, [rawData, lang])

  // Reset per-question state when moving to next question
  useEffect(() => {
    setSelected(null); setSelectedSet(new Set())
    setOrderList([]); setConfirmed(false); setHintShown(false)
  }, [index])

  if (!data) return <div className="p-10 text-center text-gray-400">{lbl('Cargando...', 'Loading...')}</div>

  const questions = data.questions
  const current   = questions[index]
  const typeMeta  = TYPE_LABELS[current?.type] ?? TYPE_LABELS.next_step
  const score     = results.filter(r => r.correct).length
  const pct       = results.length ? Math.round((score / questions.length) * 100) : 0

  /* ──────── handlers ──────── */

  const addResult = (correct, sid) => {
    setResults(r => [...r, { correct, selectedId: sid }])
    if (correct) { const ns = streak + 1; setStreak(ns); setMaxStreak(m => Math.max(m, ns)) }
    else setStreak(0)
  }

  const handleSelect = (opt) => {
    if (selected) return
    setSelected(opt.id)
    addResult(opt.correct, opt.id)
  }

  const handleMultiToggle = (optId) => {
    if (confirmed) return
    setSelectedSet(prev => { const n = new Set(prev); n.has(optId) ? n.delete(optId) : n.add(optId); return n })
  }

  const handleMultiConfirm = () => {
    if (confirmed || selectedSet.size === 0) return
    setConfirmed(true)
    const correctIds = new Set(current.options.filter(o => o.correct).map(o => o.id))
    const isCorrect  = correctIds.size === selectedSet.size && [...correctIds].every(id => selectedSet.has(id))
    addResult(isCorrect, [...selectedSet].join(','))
  }

  const handleOrderClick = (item) => {
    if (confirmed) return
    setOrderList(prev =>
      prev.find(o => o.id === item.id) ? prev.filter(o => o.id !== item.id) : [...prev, item]
    )
  }

  const handleOrderConfirm = () => {
    if (confirmed || orderList.length !== (current.items?.length ?? 0)) return
    setConfirmed(true)
    const isCorrect = orderList.map(o => o.id).join(',') === (current.correct_order ?? []).join(',')
    addResult(isCorrect, orderList.map(o => o.id).join(','))
  }

  const next = () => {
    if (index + 1 >= questions.length) {
      persistProgress('quiz', id, pct >= 80 ? 'success' : pct >= 50 ? 'warning' : 'failure')
      setDone(true)
    } else {
      setIndex(i => i + 1)
    }
  }

  const restart = () => {
    setIndex(0); setSelected(null); setSelectedSet(new Set()); setOrderList([])
    setConfirmed(false); setHintShown(false)
    setResults([]); setStreak(0); setMaxStreak(0); setDone(false)
  }

  const isAnswered = current?.type === 'multi' || current?.type === 'order' ? confirmed : !!selected

  /* ──────── results screen ──────── */

  if (done) {
    const grade = pct >= 80 ? 'success' : pct >= 50 ? 'warning' : 'failure'
    const gs = {
      success: { bg: 'from-green-500 to-emerald-600',  msg: lbl('¡Excelente!', 'Excellent!'),          sub: lbl('Dominas este tema.', 'You master this topic.') },
      warning: { bg: 'from-yellow-400 to-orange-500',  msg: lbl('Bien hecho', 'Well done'),             sub: lbl('Repasa los errores.', 'Review your mistakes.') },
      failure: { bg: 'from-red-500 to-rose-600',       msg: lbl('Sigue practicando', 'Keep practicing'), sub: lbl('Revisa los casos clínicos.', 'Review the clinical cases.') },
    }[grade]

    return (
      <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center px-4 py-10">
        <div className={`w-full max-w-md rounded-3xl bg-gradient-to-br ${gs.bg} text-white p-8 mb-6 text-center shadow-xl`}>
          <div className="text-6xl font-bold mb-2">{pct}%</div>
          <div className="text-2xl font-bold mb-1">{gs.msg}</div>
          <div className="text-white/80 text-sm">{gs.sub}</div>
          <div className="mt-6 flex justify-center gap-8 text-sm">
            <div><div className="text-2xl font-bold">{score}/{questions.length}</div><div className="text-white/70">{lbl('Correctas', 'Correct')}</div></div>
            <div><div className="text-2xl font-bold">{maxStreak}</div><div className="text-white/70">{lbl('Racha máx.', 'Max streak')}</div></div>
          </div>
        </div>

        <div className="w-full max-w-md bg-white rounded-2xl border border-gray-100 shadow p-5 mb-5">
          <div className="text-xs font-semibold text-gray-400 uppercase mb-3">{lbl('Resumen de respuestas', 'Answer summary')}</div>
          <div className="flex flex-col gap-2">
            {questions.map((q, i) => {
              const r       = results[i]
              const correct = q.type === 'order' ? null : q.options?.find(o => o.correct)
              const chosen  = q.type === 'order' ? null : q.options?.find(o => o.id === r?.selectedId)
              return (
                <div key={q.id} className={`rounded-xl p-3 border text-xs ${r?.correct ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`}>
                  <div className="flex items-center gap-1.5 mb-1">
                    <span className={`font-bold ${r?.correct ? 'text-green-600' : 'text-red-500'}`}>{r?.correct ? '✓' : '✕'}</span>
                    <span className="font-semibold text-gray-700 line-clamp-2">{i + 1}. {q.text}</span>
                  </div>
                  {!r?.correct && q.type === 'order' && (
                    <div className="text-gray-500 mt-0.5">{lbl('Orden correcto:', 'Correct order:')} {q.correct_order?.map(id => q.items?.find(it => it.id === id)?.text).join(' → ')}</div>
                  )}
                  {!r?.correct && q.type !== 'order' && correct && (
                    <div className="text-green-700">✓ {correct.text}</div>
                  )}
                </div>
              )
            })}
          </div>
        </div>

        <div className="flex gap-3 w-full max-w-md flex-wrap">
          <button onClick={restart} className="flex-1 bg-indigo-700 text-white py-3 rounded-2xl font-medium text-sm hover:bg-indigo-800 transition">
            {lbl('Repetir quiz', 'Repeat quiz')}
          </button>
          <Link to="/quizzes" className="flex-1 border border-indigo-700 text-indigo-700 py-3 rounded-2xl font-medium text-sm hover:bg-indigo-50 transition text-center">
            {lbl('Otros quizzes', 'Other quizzes')}
          </Link>
          <Link to="/" className="w-full border border-gray-300 text-gray-600 py-3 rounded-2xl font-medium text-sm hover:bg-gray-50 transition text-center">
            {lbl('Ir al inicio', 'Go to home')}
          </Link>
        </div>
      </div>
    )
  }

  /* ──────── question renderers ──────── */

  const renderSingle = () => {
    const selectedOpt = current.options.find(o => o.id === selected)
    const correctOpt  = current.options.find(o => o.correct)
    return (
      <>
        <div className="flex flex-col gap-3">
          {current.options.map(opt => {
            const isSelected = selected === opt.id
            const showResult = !!selected
            let cls = 'text-left px-4 py-3.5 rounded-xl border text-sm transition '
            if (!showResult)           cls += 'border-gray-200 bg-gray-50 hover:border-indigo-400 hover:bg-indigo-50 cursor-pointer'
            else if (opt.correct)      cls += 'border-green-400 bg-green-50 text-green-800'
            else if (isSelected)       cls += 'border-red-400   bg-red-50   text-red-800'
            else                       cls += 'border-gray-100  bg-gray-50  text-gray-400 opacity-60'
            return (
              <button key={opt.id} onClick={() => handleSelect(opt)} disabled={!!selected} className={cls}>
                <span className="font-semibold text-gray-400 mr-2">{opt.id.toUpperCase()}.</span>
                {opt.text}
                {showResult && opt.correct  && <span className="ml-2 text-green-600">✓</span>}
                {showResult && isSelected && !opt.correct && <span className="ml-2 text-red-500">✕</span>}
              </button>
            )
          })}
        </div>
        {selected && selectedOpt && (
          <div className={`mt-5 rounded-xl border p-4 text-sm leading-relaxed ${
            selectedOpt.correct ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'
          }`}>
            <div className="font-semibold mb-1">
              {selectedOpt.correct ? `✓ ${lbl('Correcto', 'Correct')}` : `✕ ${lbl('Incorrecto', 'Incorrect')} — ${lbl('La correcta es', 'Correct answer is')} ${correctOpt?.id?.toUpperCase()}`}
            </div>
            <p>{selectedOpt.explanation}</p>
          </div>
        )}
      </>
    )
  }

  const renderMulti = () => {
    const correctIds = new Set(current.options.filter(o => o.correct).map(o => o.id))
    const multiCorrect = confirmed && correctIds.size === selectedSet.size && [...correctIds].every(id => selectedSet.has(id))
    return (
      <>
        <p className="text-xs text-purple-600 bg-purple-50 border border-purple-200 rounded-lg px-3 py-2 mb-4">
          {lbl('Puede haber más de una respuesta correcta. Selecciona todas las que apliquen y luego confirma.', 'There may be more than one correct answer. Select all that apply, then confirm.')}
        </p>
        <div className="flex flex-col gap-3">
          {current.options.map(opt => {
            const isSel = selectedSet.has(opt.id)
            let cls = 'text-left px-4 py-3.5 rounded-xl border text-sm transition flex items-center gap-3 '
            if (!confirmed) {
              cls += isSel ? 'border-purple-400 bg-purple-50 text-purple-900 cursor-pointer' : 'border-gray-200 bg-gray-50 hover:border-purple-300 hover:bg-purple-50 cursor-pointer'
            } else if (opt.correct) {
              cls += 'border-green-400 bg-green-50 text-green-800'
            } else if (isSel) {
              cls += 'border-red-400 bg-red-50 text-red-800'
            } else {
              cls += 'border-gray-100 bg-gray-50 text-gray-400 opacity-60'
            }
            return (
              <button key={opt.id} onClick={() => handleMultiToggle(opt.id)} disabled={confirmed} className={cls}>
                <div className={`w-5 h-5 rounded border-2 flex-shrink-0 flex items-center justify-center transition ${isSel ? 'bg-purple-500 border-purple-500' : 'border-gray-300 bg-white'}`}>
                  {isSel && <span className="text-white text-xs font-bold">✓</span>}
                </div>
                <span className="flex-1">{opt.text}</span>
                {confirmed && opt.correct && <span className="text-green-600 font-bold">✓</span>}
                {confirmed && isSel && !opt.correct && <span className="text-red-500 font-bold">✕</span>}
              </button>
            )
          })}
        </div>
        {!confirmed && (
          <button onClick={handleMultiConfirm} disabled={selectedSet.size === 0}
            className="mt-4 w-full bg-purple-700 text-white py-3 rounded-xl text-sm font-medium hover:bg-purple-800 transition disabled:opacity-40">
            {lbl('Confirmar selección', 'Confirm selection')}
          </button>
        )}
        {confirmed && (
          <div className={`mt-4 rounded-xl border p-4 text-sm leading-relaxed ${multiCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
            <div className="font-semibold mb-1">
              {multiCorrect
                ? lbl('✓ Correcto — seleccionaste exactamente las opciones correctas', '✓ Correct — you selected exactly the right options')
                : lbl('✕ Incorrecto — las opciones correctas están marcadas en verde', '✕ Incorrect — correct options are marked in green')}
            </div>
            <p>{current.multi_explanation}</p>
          </div>
        )}
      </>
    )
  }

  const renderOrder = () => {
    const orderMap = Object.fromEntries(orderList.map((o, i) => [o.id, i + 1]))
    const allPlaced = orderList.length === (current.items?.length ?? 0)
    const lastResult = results[results.length - 1]
    return (
      <>
        <p className="text-xs text-teal-600 bg-teal-50 border border-teal-200 rounded-lg px-3 py-2 mb-4">
          {lbl('Haz clic en los pasos en el orden correcto. Haz clic de nuevo para deseleccionar.', 'Click the steps in the correct order. Click again to deselect.')}
        </p>
        <div className="flex flex-col gap-3">
          {current.items.map(item => {
            const pos = orderMap[item.id]
            const isPlaced = pos !== undefined
            const correctPos = confirmed ? (current.correct_order ?? []).indexOf(item.id) + 1 : null
            const myPos = confirmed ? orderList.map(o => o.id).indexOf(item.id) + 1 : null
            const posCorrect = confirmed && correctPos === myPos

            let cls = 'text-left px-4 py-3.5 rounded-xl border text-sm transition flex items-center gap-3 '
            if (!confirmed) {
              cls += isPlaced ? 'border-teal-400 bg-teal-50 text-teal-900 cursor-pointer' : 'border-gray-200 bg-gray-50 hover:border-teal-300 hover:bg-teal-50 cursor-pointer'
            } else {
              cls += posCorrect ? 'border-green-400 bg-green-50 text-green-800' : 'border-red-400 bg-red-50 text-red-800'
            }

            return (
              <button key={item.id} onClick={() => handleOrderClick(item)} disabled={confirmed} className={cls}>
                <div className={`w-8 h-8 rounded-full flex-shrink-0 flex items-center justify-center text-sm font-bold transition ${
                  isPlaced ? 'bg-teal-500 text-white' : 'bg-gray-200 text-gray-400'
                }`}>
                  {isPlaced ? pos : '?'}
                </div>
                <span className="flex-1">{item.text}</span>
                {confirmed && (
                  <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${posCorrect ? 'bg-green-200 text-green-800' : 'bg-red-200 text-red-800'}`}>
                    {lbl('Correcto:', 'Correct:')} {correctPos}
                  </span>
                )}
              </button>
            )
          })}
        </div>
        {!confirmed && (
          <button onClick={handleOrderConfirm} disabled={!allPlaced}
            className="mt-4 w-full bg-teal-700 text-white py-3 rounded-xl text-sm font-medium hover:bg-teal-800 transition disabled:opacity-40">
            {allPlaced ? lbl('Confirmar orden', 'Confirm order') : lbl(`Selecciona ${(current.items?.length ?? 0) - orderList.length} más`, `Select ${(current.items?.length ?? 0) - orderList.length} more`)}
          </button>
        )}
        {confirmed && (
          <div className={`mt-4 rounded-xl border p-4 text-sm leading-relaxed ${lastResult?.correct ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
            <div className="font-semibold mb-1">
              {lastResult?.correct ? lbl('✓ ¡Orden correcto!', '✓ Correct order!') : lbl('✕ Orden incorrecto — revisa las posiciones correctas', '✕ Incorrect order — see the correct positions')}
            </div>
            <p>{current.explanation}</p>
          </div>
        )}
      </>
    )
  }

  /* ──────── main render ──────── */

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-8 max-w-2xl mx-auto">

      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <Link to="/quizzes" className="text-xs text-indigo-600 hover:underline">
          ← {lbl('Quizzes', 'Quizzes')}
        </Link>
        <div className="flex items-center gap-4 text-sm">
          {streak > 1 && (
            <div className="flex items-center gap-1 bg-orange-50 border border-orange-200 text-orange-600 px-3 py-1 rounded-full text-xs font-bold">
              🔥 {streak} {lbl('en racha', 'streak')}
            </div>
          )}
          <div className="text-xs text-gray-500">{score}/{index} {lbl('correctas', 'correct')}</div>
        </div>
      </div>

      {/* Progress */}
      <div className="w-full bg-gray-100 rounded-full h-2 mb-2 overflow-hidden">
        <div className="h-2 rounded-full bg-indigo-600 transition-all" style={{ width: `${(index / questions.length) * 100}%` }} />
      </div>
      <div className="text-xs text-gray-400 mb-6 text-right">{index + 1} / {questions.length}</div>

      {/* Question card */}
      <div className="bg-white rounded-2xl shadow border border-gray-100 p-6">

        {/* Type badge */}
        <div className={`inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-full border mb-4 ${typeMeta.color}`}>
          <span>{typeMeta.icon}</span>
          <span>{lang === 'en' ? typeMeta.en : typeMeta.es}</span>
        </div>

        {/* Question text */}
        <p className="text-gray-800 font-semibold text-base leading-snug mb-5">{current.text}</p>

        {/* Hint button */}
        {current.hint && !isAnswered && (
          <div className="mb-4">
            {!hintShown ? (
              <button onClick={() => setHintShown(true)}
                className="text-xs text-amber-600 border border-amber-300 bg-amber-50 px-3 py-1.5 rounded-full hover:bg-amber-100 transition">
                💡 {lbl('Ver pista', 'Show hint')}
              </button>
            ) : (
              <div className="text-sm bg-amber-50 border border-amber-200 text-amber-900 rounded-xl px-4 py-3">
                <span className="font-semibold">💡 {lbl('Pista:', 'Hint:')} </span>{current.hint}
              </div>
            )}
          </div>
        )}

        {/* Render by type */}
        {current.type === 'multi' ? renderMulti()
         : current.type === 'order' ? renderOrder()
         : renderSingle()}

        {/* Next button */}
        {isAnswered && (
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
