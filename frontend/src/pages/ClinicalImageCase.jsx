import API from '../utils/api'
import { useEffect, useState, useRef } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { saveProgress as persistProgress } from '../utils/progress'

const PHASE = { HOTSPOT: 'hotspot', MCQ: 'mcq', DONE: 'done' }

async function translateImageData(d, lang) {
  if (lang === 'es') return d
  const [presentation, resolution, pearl] = await Promise.all([
    translateText(d.presentation, lang),
    translateText(d.resolution, lang),
    translateText(d.pearl, lang),
  ])
  const hotspots = await Promise.all(d.hotspots.map(async h => ({
    ...h,
    label:       await translateText(h.label, lang),
    explanation: await translateText(h.explanation, lang),
  })))
  const questions = await Promise.all(d.questions.map(async q => {
    const base = {
      ...q,
      text: await translateText(q.text, lang),
      hint: q.hint ? await translateText(q.hint, lang) : q.hint,
    }
    if (q.options) {
      base.options = await Promise.all(q.options.map(async o => ({
        ...o,
        text:     await translateText(o.text, lang),
        feedback: await translateText(o.feedback, lang),
      })))
    }
    return base
  }))
  return { ...d, presentation, resolution, pearl, hotspots, questions }
}

export default function ClinicalImageCase() {
  const { id } = useParams()
  const { lang } = useLang()
  const svgRef = useRef(null)

  const [rawData, setRawData]           = useState(null)
  const [data, setData]                 = useState(null)
  const [translating, setTranslating]   = useState(false)
  const [phase, setPhase]           = useState(PHASE.HOTSPOT)
  const [qIndex, setQIndex]         = useState(0)
  const [hotspotResult, setHotspotResult] = useState(null)   // {correct, label, explanation}
  const [selectedOpt, setSelectedOpt]     = useState(null)
  const [answeredQs, setAnsweredQs]       = useState([])     // {id, correct}
  const [showAllFindings, setShowAllFindings] = useState(false)

  useEffect(() => {
    fetch(`${API}/clinical-images/${id}`)
      .then(r => r.json()).then(setRawData)
  }, [id])

  useEffect(() => {
    if (!rawData) return
    let cancelled = false
    setTranslating(lang !== 'es')
    translateImageData(rawData, lang).then(translated => {
      if (!cancelled) { setData(translated); setTranslating(false) }
    })
    return () => { cancelled = true }
  }, [rawData, lang])

  if (!data) return <div className="p-10 text-center text-gray-400">{lang === 'en' ? 'Loading...' : 'Cargando...'}</div>

  if (translating) return (
    <div className="p-10 text-center text-gray-400 flex flex-col items-center gap-2">
      <div className="w-6 h-6 border-2 border-purple-600 border-t-transparent rounded-full animate-spin"/>
      <span className="text-sm">{lang === 'en' ? 'Translating...' : 'Traduciendo...'}</span>
    </div>
  )

  const questions   = data.questions
  const currentQ    = phase === PHASE.MCQ ? questions.filter(q => q.type === 'mcq')[qIndex] : null
  const mcqQuestions = questions.filter(q => q.type === 'mcq')
  const hotspotQ    = questions.find(q => q.type === 'hotspot')

  const handleHotspotClick = (e) => {
    if (hotspotResult) return
    const rect = svgRef.current.getBoundingClientRect()
    const xPct = ((e.clientX - rect.left) / rect.width) * 100
    const yPct = ((e.clientY - rect.top) / rect.height) * 100

    let hit = null
    let minDist = Infinity
    data.hotspots.forEach(hs => {
      const dist = Math.sqrt((xPct - hs.x) ** 2 + (yPct - hs.y) ** 2)
      if (dist < hs.radius && dist < minDist) { minDist = dist; hit = hs }
    })

    if (hit) {
      setHotspotResult({ correct: hit.correct, label: hit.label, explanation: hit.explanation })
    } else {
      const nearest = data.hotspots.reduce((a, b) => {
        const da = Math.sqrt((xPct - a.x) ** 2 + (yPct - a.y) ** 2)
        const db = Math.sqrt((xPct - b.x) ** 2 + (yPct - b.y) ** 2)
        return da < db ? a : b
      })
      setHotspotResult({
        correct: false,
        label: lang === 'en' ? 'Missed — click closer to a finding' : 'No acertaste — haz clic más cerca de un hallazgo',
        explanation: lang === 'en'
          ? `The main finding is: ${nearest.label}`
          : `El hallazgo principal es: ${nearest.label}`
      })
    }
  }

  const advanceFromHotspot = () => {
    if (mcqQuestions.length === 0) { setPhase(PHASE.DONE); return }
    setPhase(PHASE.MCQ)
    setQIndex(0)
  }

  const handleMCQ = (opt) => {
    if (selectedOpt) return
    setSelectedOpt(opt.id)
    setAnsweredQs(prev => [...prev, { id: currentQ.id, correct: opt.correct }])
  }

  const saveProgress = (result) => { persistProgress('image', id, result) }

  const nextMCQ = () => {
    setSelectedOpt(null)
    if (qIndex + 1 >= mcqQuestions.length) {
      const pct = Math.round(((answeredQs.filter(q => q.correct).length + (currentQ && answeredQs.find(a=>a.id===currentQ.id)?.correct ? 0 : 0)) / mcqQuestions.length) * 100)
      const result = pct >= 80 ? 'success' : pct >= 50 ? 'warning' : 'failure'
      saveProgress(result)
      setPhase(PHASE.DONE)
    } else {
      setQIndex(i => i + 1)
    }
  }

  const restart = () => {
    setPhase(hotspotQ ? PHASE.HOTSPOT : PHASE.MCQ)
    setQIndex(0)
    setHotspotResult(null)
    setSelectedOpt(null)
    setAnsweredQs([])
    setShowAllFindings(false)
  }

  const correctCount = answeredQs.filter(q => q.correct).length
  const totalMCQ     = mcqQuestions.length

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-10 max-w-5xl mx-auto">

      {/* Header */}
      <div className="mb-6">
        <Link to="/clinical-images" className="text-xs text-purple-600 hover:underline mb-2 inline-block">
          ← {lang === 'en' ? 'Back to clinical images' : 'Volver a imágenes clínicas'}
        </Link>
        <div className="flex items-center gap-3 mt-1 flex-wrap">
          <span className="text-xs font-semibold text-purple-600 uppercase">
            {lang === 'en' ? ({ "TC":"CT Scan","RM":"MRI","RxTx":"X-Ray","Histopatología":"Histopathology" }[data.modality] ?? data.modality) : data.modality}
          </span>
          <span className="text-xs text-gray-400">•</span>
          <span className="text-xs text-gray-400">{data.system}</span>
          <span className="text-xs text-gray-400">•</span>
          <span className="text-xs text-gray-400">{data.difficulty}</span>
        </div>
        <h1 className="text-2xl font-bold text-gray-800 mt-1">{data.title}</h1>
      </div>

      {/* Progress bar */}
      <div className="flex gap-1.5 mb-6">
        {hotspotQ && (
          <div className={`h-1.5 flex-1 rounded-full ${hotspotResult ? 'bg-purple-500' : 'bg-gray-200'}`}/>
        )}
        {mcqQuestions.map((_, i) => (
          <div key={i} className={`h-1.5 flex-1 rounded-full ${
            phase === PHASE.DONE || (phase === PHASE.MCQ && i < qIndex) || (phase === PHASE.MCQ && i === qIndex && selectedOpt)
              ? answeredQs.find(a => a.id === mcqQuestions[i]?.id)?.correct ? 'bg-green-500' : 'bg-red-400'
              : phase === PHASE.MCQ && i === qIndex ? 'bg-purple-500'
              : 'bg-gray-200'
          }`}/>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">

        {/* Image column */}
        <div className="lg:col-span-3">
          <div className="bg-black rounded-2xl overflow-hidden shadow-lg relative">
            {/* SVG image */}
            <div
              ref={svgRef}
              onClick={phase === PHASE.HOTSPOT && !hotspotResult ? handleHotspotClick : undefined}
              className={`relative w-full ${phase === PHASE.HOTSPOT && !hotspotResult ? 'cursor-crosshair' : 'cursor-default'}`}
              dangerouslySetInnerHTML={{ __html: data.svg }}
            />

            {/* Hotspot overlays */}
            {(showAllFindings || phase === PHASE.DONE) && data.hotspots.map(hs => (
              <div
                key={hs.id}
                className={`absolute rounded-full border-2 flex items-center justify-center pointer-events-none ${
                  hs.correct ? 'border-yellow-400 bg-yellow-400/20' : 'border-blue-400 bg-blue-400/10'
                }`}
                style={{
                  left:   `calc(${hs.x}% - ${hs.radius * 0.8}%)`,
                  top:    `calc(${hs.y}% - ${hs.radius * 1.0}%)`,
                  width:  `${hs.radius * 1.6}%`,
                  height: `${hs.radius * 2.0}%`,
                }}
              >
                <span className="text-yellow-300 text-xs font-bold">
                  {hs.correct ? '★' : ''}
                </span>
              </div>
            ))}

            {/* Hotspot cursor hint */}
            {phase === PHASE.HOTSPOT && !hotspotResult && (
              <div className="absolute bottom-2 left-0 right-0 text-center">
                <span className="text-xs text-white/60 bg-black/40 px-3 py-1 rounded-full">
                  {hotspotQ?.hint ?? (lang === 'en' ? 'Click on the image' : 'Haz clic en la imagen')}
                </span>
              </div>
            )}
          </div>

          {/* Show findings toggle */}
          {phase !== PHASE.HOTSPOT && (
            <button
              onClick={() => setShowAllFindings(v => !v)}
              className="mt-3 w-full text-xs text-purple-600 border border-purple-200 rounded-xl py-2 hover:bg-purple-50 transition"
            >
              {showAllFindings
                ? (lang === 'en' ? 'Hide findings' : 'Ocultar hallazgos')
                : (lang === 'en' ? 'Show findings on image' : 'Mostrar hallazgos en imagen')}
            </button>
          )}
        </div>

        {/* Question column */}
        <div className="lg:col-span-2 flex flex-col gap-4">

          {/* Presentation */}
          <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-4">
            <div className="text-xs font-semibold text-gray-400 uppercase mb-2">
              {lang === 'en' ? 'Clinical presentation' : 'Presentación clínica'}
            </div>
            <p className="text-xs text-gray-600 leading-relaxed">{data.presentation}</p>
          </div>

          {/* HOTSPOT phase */}
          {phase === PHASE.HOTSPOT && (
            <div className="bg-white rounded-2xl border border-gray-100 shadow p-5">
              <div className="text-xs font-semibold text-purple-600 uppercase mb-3">
                {lang === 'en' ? 'Find the finding' : 'Encuentra el hallazgo'}
              </div>
              <p className="text-sm font-medium text-gray-800 mb-4">{hotspotQ?.text}</p>

              {!hotspotResult && (
                <div className="flex items-center gap-2 text-xs text-gray-400 bg-gray-50 rounded-xl p-3">
                  <span className="text-lg">👆</span>
                  <span>{lang === 'en' ? 'Click directly on the image' : 'Haz clic directamente sobre la imagen'}</span>
                </div>
              )}

              {hotspotResult && (
                <>
                  <div className={`rounded-xl p-4 mb-4 ${hotspotResult.correct ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'}`}>
                    <div className={`font-semibold text-sm mb-1 ${hotspotResult.correct ? 'text-green-700' : 'text-red-700'}`}>
                      {hotspotResult.correct
                        ? (lang === 'en' ? '✓ Correct!' : '✓ ¡Correcto!')
                        : (lang === 'en' ? '✕ Not quite' : '✕ No del todo')}
                    </div>
                    <p className="text-xs text-gray-700 leading-relaxed">{hotspotResult.explanation}</p>
                  </div>
                  <button onClick={advanceFromHotspot}
                    className="w-full bg-purple-700 text-white py-2.5 rounded-xl text-sm font-medium hover:bg-purple-800 transition">
                    {mcqQuestions.length > 0
                      ? (lang === 'en' ? 'Next questions →' : 'Siguientes preguntas →')
                      : (lang === 'en' ? 'See resolution →' : 'Ver resolución →')}
                  </button>
                </>
              )}
            </div>
          )}

          {/* MCQ phase */}
          {phase === PHASE.MCQ && currentQ && (
            <div className="bg-white rounded-2xl border border-gray-100 shadow p-5">
              <div className="text-xs font-semibold text-purple-600 uppercase mb-3">
                {lang === 'en' ? `Question ${qIndex + 1} of ${mcqQuestions.length}` : `Pregunta ${qIndex + 1} de ${mcqQuestions.length}`}
              </div>
              <p className="text-sm font-medium text-gray-800 mb-4">{currentQ.text}</p>

              <div className="flex flex-col gap-2">
                {currentQ.options.map(opt => {
                  const isSelected = selectedOpt === opt.id
                  let cls = 'text-left px-3 py-2.5 rounded-xl border text-xs transition '
                  if (!selectedOpt) cls += 'border-gray-200 bg-gray-50 hover:border-purple-400 hover:bg-purple-50 cursor-pointer'
                  else if (isSelected) cls += opt.correct ? 'border-green-400 bg-green-50 text-green-800' : 'border-red-400 bg-red-50 text-red-800'
                  else if (opt.correct) cls += 'border-green-300 bg-green-50 text-green-700'
                  else cls += 'border-gray-100 bg-gray-50 text-gray-400 opacity-60'

                  return (
                    <button key={opt.id} onClick={() => handleMCQ(opt)} disabled={!!selectedOpt} className={cls}>
                      <span className="font-semibold mr-1.5 text-gray-400">{opt.id.toUpperCase()}.</span>
                      {opt.text}
                    </button>
                  )
                })}
              </div>

              {selectedOpt && (
                <>
                  <div className={`mt-4 p-3 rounded-xl text-xs border leading-relaxed ${
                    currentQ.options.find(o => o.id === selectedOpt)?.correct
                      ? 'bg-green-50 border-green-200 text-green-800'
                      : 'bg-red-50 border-red-200 text-red-800'
                  }`}>
                    {currentQ.options.find(o => o.id === selectedOpt)?.feedback}
                  </div>
                  <button onClick={nextMCQ}
                    className="mt-4 w-full bg-purple-700 text-white py-2.5 rounded-xl text-sm font-medium hover:bg-purple-800 transition">
                    {qIndex + 1 < mcqQuestions.length
                      ? (lang === 'en' ? 'Next →' : 'Siguiente →')
                      : (lang === 'en' ? 'See resolution →' : 'Ver resolución →')}
                  </button>
                </>
              )}
            </div>
          )}

          {/* Resolution */}
          {phase === PHASE.DONE && (
            <div className="bg-white rounded-2xl border border-gray-100 shadow p-5">
              <div className="flex items-center gap-3 mb-4">
                <div className={`text-2xl font-bold ${correctCount === totalMCQ ? 'text-green-600' : correctCount >= totalMCQ / 2 ? 'text-yellow-600' : 'text-red-500'}`}>
                  {correctCount}/{totalMCQ}
                </div>
                <div className="text-xs text-gray-500">
                  {lang === 'en' ? 'correct answers' : 'respuestas correctas'}
                </div>
              </div>

              <div className="bg-purple-50 border border-purple-200 rounded-xl p-3 mb-4">
                <div className="text-xs font-semibold text-purple-700 mb-1">
                  {lang === 'en' ? 'Radiological diagnosis' : 'Diagnóstico radiológico'}
                </div>
                <p className="text-xs text-purple-900 leading-relaxed">{data.resolution}</p>
              </div>

              <div className="bg-blue-50 border border-blue-200 rounded-xl p-3 mb-4">
                <div className="text-xs font-semibold text-blue-600 mb-1">
                  {lang === 'en' ? 'Clinical pearl' : 'Perla clínica'}
                </div>
                <p className="text-xs text-blue-800 leading-relaxed">{data.pearl}</p>
              </div>

              <div className="flex flex-col gap-2">
                <div className="flex gap-2">
                  <button onClick={restart}
                    className="flex-1 bg-purple-700 text-white py-2 rounded-xl text-sm font-medium hover:bg-purple-800 transition">
                    {lang === 'en' ? 'Repeat' : 'Repetir'}
                  </button>
                  <Link to="/clinical-images"
                    className="flex-1 border border-purple-700 text-purple-700 py-2 rounded-xl text-sm font-medium hover:bg-purple-50 transition text-center">
                    {lang === 'en' ? 'Other cases' : 'Otros casos'}
                  </Link>
                </div>
                <Link to="/"
                  className="w-full border border-gray-300 text-gray-600 py-2 rounded-xl text-sm font-medium hover:bg-gray-50 transition text-center">
                  {lang === 'en' ? 'Go to home' : 'Ir al inicio'}
                </Link>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
