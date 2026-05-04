import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { saveProgress as persistProgress } from '../utils/progress'

const PHASE = { ELIMINATING: 'eliminating', FEEDBACK: 'feedback', RESOLVED: 'resolved' }

async function translateDiffData(d, lang) {
  if (lang === 'es') return d
  const [presentation, resolution, pearl] = await Promise.all([
    translateText(d.presentation, lang),
    translateText(d.resolution, lang),
    translateText(d.pearl, lang),
  ])
  const diagnoses = await Promise.all(d.diagnoses.map(async diag => ({
    ...diag,
    initial_hint: await translateText(diag.initial_hint, lang),
  })))
  const clues = await Promise.all(d.clues.map(async clue => ({
    ...clue,
    text:     await translateText(clue.text, lang),
    question: await translateText(clue.question, lang),
    eliminates:      Object.fromEntries(await Promise.all(Object.entries(clue.eliminates).map(async ([k, v]) => [k, await translateText(v, lang)]))),
    cannot_eliminate: Object.fromEntries(await Promise.all(Object.entries(clue.cannot_eliminate).map(async ([k, v]) => [k, await translateText(v, lang)]))),
  })))
  return { ...d, presentation, resolution, pearl, diagnoses, clues }
}

export default function DifferentialCase() {
  const { id } = useParams()
  const { t, lang } = useLang()
  const [rawData, setRawData]       = useState(null)
  const [data, setData]             = useState(null)
  const [translating, setTranslating] = useState(false)
  const [clueIndex, setClueIndex]   = useState(0)
  const [phase, setPhase]           = useState(PHASE.ELIMINATING)
  const [selected, setSelected]     = useState(new Set())
  const [eliminated, setEliminated] = useState(new Set())
  const [feedback, setFeedback]     = useState(null)

  useEffect(() => {
    fetch(`${API}/differentials/${id}`)
      .then(r => r.json()).then(setRawData)
  }, [id])

  useEffect(() => {
    if (!rawData) return
    let cancelled = false
    setTranslating(lang !== 'es')
    translateDiffData(rawData, lang).then(translated => {
      if (!cancelled) { setData(translated); setTranslating(false) }
    })
    return () => { cancelled = true }
  }, [rawData, lang])

  if (!data) return <div className="p-10 text-center text-gray-400">{t.loading}</div>

  if (translating) return (
    <div className="p-10 text-center text-gray-400 flex flex-col items-center gap-2">
      <div className="w-6 h-6 border-2 border-primary border-t-transparent rounded-full animate-spin"/>
      <span className="text-sm">{lang === 'en' ? 'Translating...' : 'Traduciendo...'}</span>
    </div>
  )

  const currentClue = data.clues[clueIndex]
  const isLastClue  = clueIndex === data.clues.length - 1
  const remaining   = data.diagnoses.filter(d => !eliminated.has(d.id))

  const toggleSelect = (diagId) => {
    if (phase !== PHASE.ELIMINATING || eliminated.has(diagId)) return
    setSelected(prev => {
      const next = new Set(prev)
      next.has(diagId) ? next.delete(diagId) : next.add(diagId)
      return next
    })
  }

  const confirmEliminations = () => {
    const correctElims  = Object.keys(currentClue.eliminates)
    const cannotElimIds = Object.keys(currentClue.cannot_eliminate)
    const truePos  = [...selected].filter(id => correctElims.includes(id))
    const falsePos = [...selected].filter(id => cannotElimIds.includes(id) || (!correctElims.includes(id) && !cannotElimIds.includes(id)))
    setFeedback({ truePos, falsePos, correctElims })
    setPhase(PHASE.FEEDBACK)
    setEliminated(prev => { const next = new Set(prev); truePos.forEach(id => next.add(id)); return next })
  }

  const saveProgress = (result) => { persistProgress('differential', id, result) }

  const nextClue = () => {
    setSelected(new Set()); setFeedback(null)
    if (isLastClue) {
      setPhase(PHASE.RESOLVED)
      // Score: % of correct eliminations across all clues
      saveProgress('success')
    } else {
      setClueIndex(i => i + 1); setPhase(PHASE.ELIMINATING)
    }
  }

  const restart = () => {
    setClueIndex(0); setPhase(PHASE.ELIMINATING)
    setSelected(new Set()); setEliminated(new Set()); setFeedback(null)
  }

  const getDiagStyle = (diag) => {
    const isElim = eliminated.has(diag.id), isSel = selected.has(diag.id)
    if (phase === PHASE.RESOLVED) {
      if (diag.correct) return 'border-green-400 bg-green-50'
      if (isElim)       return 'border-gray-200 bg-gray-50 opacity-50'
      return 'border-red-300 bg-red-50'
    }
    if (isElim) return 'border-gray-200 bg-gray-50 opacity-40 cursor-default'
    if (isSel)  return 'border-red-400 bg-red-50 cursor-pointer'
    return 'border-gray-200 bg-white hover:border-primary cursor-pointer'
  }

  const missedCount = feedback ? feedback.correctElims.filter(id => ![...selected].includes(id)).length : 0

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-10 max-w-4xl mx-auto">
      <div className="mb-6">
        <Link to="/differentials" className="text-xs text-accent hover:underline mb-2 inline-block">
          {t.backToDiff}
        </Link>
        <div className="flex items-center gap-3 mt-1">
          <span className="text-xs font-semibold text-accent uppercase">{data.system}</span>
          <span className="text-xs text-gray-400">•</span>
          <span className="text-xs text-gray-400">{data.difficulty}</span>
        </div>
        <h1 className="text-2xl font-bold text-primary mt-1">{data.title}</h1>
      </div>

      <div className="bg-white rounded-2xl border border-gray-100 shadow p-5 mb-6">
        <div className="text-xs font-semibold text-gray-400 uppercase mb-2">{t.clinicalPresentation}</div>
        <p className="text-gray-700 text-sm leading-relaxed">{data.presentation}</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">
        <div className="lg:col-span-3">
          <div className="text-xs font-semibold text-gray-400 uppercase mb-3">
            {phase === PHASE.RESOLVED
              ? t.diagnosisConfirmed
              : `${t.hypotheses} — ${remaining.length} ${t.allDiff}`}
          </div>

          <div className="flex flex-col gap-3">
            {data.diagnoses.map(diag => {
              const isElim = eliminated.has(diag.id), isSel = selected.has(diag.id)
              return (
                <div key={diag.id}
                  onClick={() => phase === PHASE.ELIMINATING && toggleSelect(diag.id)}
                  className={`rounded-xl border p-4 transition-all ${getDiagStyle(diag)}`}>
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-2">
                        {isElim && <span className="text-gray-400 text-xs line-through">{diag.name}</span>}
                        {!isElim && (
                          <span className={`text-sm font-semibold ${isSel ? 'text-red-700' : 'text-gray-800'}`}>
                            {diag.name}
                          </span>
                        )}
                        {phase === PHASE.RESOLVED && diag.correct && (
                          <span className="text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded-full font-medium">
                            ✓ {t.diagnosisConfirmed}
                          </span>
                        )}
                      </div>
                      {!isElim && phase !== PHASE.RESOLVED && (
                        <p className="text-xs text-gray-500 mt-1">{diag.initial_hint}</p>
                      )}
                      {phase === PHASE.FEEDBACK && feedback && (
                        <>
                          {feedback.truePos.includes(diag.id) && currentClue.eliminates[diag.id] && (
                            <p className="text-xs text-green-700 mt-2 bg-green-50 rounded-lg p-2">
                              ✓ {currentClue.eliminates[diag.id]}
                            </p>
                          )}
                          {feedback.falsePos.includes(diag.id) && currentClue.cannot_eliminate[diag.id] && (
                            <p className="text-xs text-orange-700 mt-2 bg-orange-50 rounded-lg p-2">
                              {currentClue.cannot_eliminate[diag.id]}
                            </p>
                          )}
                        </>
                      )}
                      {phase === PHASE.RESOLVED && !diag.correct && !isElim && (
                        <p className="text-xs text-red-600 mt-1">{lang === 'en' ? 'Not eliminated — it should have been.' : 'No fue eliminado — debía serlo.'}</p>
                      )}
                    </div>
                    {phase === PHASE.ELIMINATING && !isElim && (
                      <div className={`w-5 h-5 rounded-full border-2 flex items-center justify-center shrink-0 mt-0.5 ${isSel ? 'border-red-400 bg-red-400' : 'border-gray-300'}`}>
                        {isSel && <span className="text-white text-xs font-bold">✕</span>}
                      </div>
                    )}
                    {isElim && <span className="text-gray-300 text-lg shrink-0">✕</span>}
                  </div>
                </div>
              )
            })}
          </div>

          {phase === PHASE.ELIMINATING && (
            <p className="text-xs text-gray-400 mt-3 text-center">{t.selectHypotheses}</p>
          )}
        </div>

        <div className="lg:col-span-2 flex flex-col gap-4">
          <div className="flex gap-1.5">
            {data.clues.map((_, i) => (
              <div key={i} className={`h-1.5 flex-1 rounded-full transition-all ${
                i < clueIndex ? 'bg-accent' : i === clueIndex ? 'bg-primary' : 'bg-gray-200'
              }`} />
            ))}
          </div>

          {phase !== PHASE.RESOLVED && (
            <div className="bg-blue-50 border border-blue-200 rounded-2xl p-4">
              <div className="text-xs font-semibold text-blue-600 uppercase mb-2">
                {t.newInfo} {clueIndex + 1}
              </div>
              <p className="text-sm text-blue-900 leading-relaxed">{currentClue.text}</p>
              {phase === PHASE.ELIMINATING && (
                <p className="text-xs text-blue-600 mt-3 font-medium">{currentClue.question}</p>
              )}
            </div>
          )}

          {phase === PHASE.ELIMINATING && (
            <button onClick={confirmEliminations} disabled={selected.size === 0}
              className="w-full bg-primary text-white py-2.5 rounded-xl text-sm font-medium hover:bg-blue-900 transition disabled:opacity-40">
              {selected.size === 0
                ? t.selectToEliminate
                : `${t.eliminate} ${selected.size} ${selected.size === 1 ? t.hypothesisSelected : t.hypothesesSelected}`}
            </button>
          )}

          {phase === PHASE.FEEDBACK && feedback && (
            <div className="bg-white border border-gray-100 rounded-2xl p-4 shadow-sm">
              <div className="text-sm font-bold text-gray-700 mb-3">{t.result}</div>
              {feedback.truePos.length > 0 && (
                <p className="text-xs text-green-700 mb-2">
                  ✓ {feedback.truePos.length} {feedback.truePos.length === 1 ? t.correctElim : t.correctElims}
                </p>
              )}
              {feedback.falsePos.length > 0 && (
                <p className="text-xs text-orange-600 mb-2">
                  ! {feedback.falsePos.length} {feedback.falsePos.length === 1 ? t.shouldNotElim : t.shouldNotElims}
                </p>
              )}
              {missedCount > 0 && (
                <p className="text-xs text-gray-500 mb-3">
                  {t.didNotElim} {missedCount} {missedCount === 1 ? t.diagnosis : t.diagnoses}.
                </p>
              )}
              <button onClick={nextClue}
                className="w-full bg-primary text-white py-2 rounded-xl text-sm font-medium hover:bg-blue-900 transition">
                {isLastClue ? t.seeResolution : t.nextClue}
              </button>
            </div>
          )}

          {phase === PHASE.RESOLVED && (
            <div className="bg-green-50 border border-green-200 rounded-2xl p-4">
              <div className="text-sm font-bold text-green-800 mb-2">{t.diagnosisConfirmed}</div>
              <p className="text-sm text-green-900 leading-relaxed mb-3">{data.resolution}</p>
              <div className="bg-blue-50 border border-blue-200 rounded-xl p-3 mb-4">
                <div className="text-xs font-semibold text-blue-700 mb-1">{t.clinicalPearl}</div>
                <p className="text-xs text-blue-800 leading-relaxed">{data.pearl}</p>
              </div>
              <div className="flex flex-col gap-2">
                <div className="flex gap-2">
                  <button onClick={restart}
                    className="flex-1 bg-primary text-white py-2 rounded-xl text-sm font-medium hover:bg-blue-900 transition">
                    {t.repeatDiff}
                  </button>
                  <Link to="/differentials"
                    className="flex-1 border border-primary text-primary py-2 rounded-xl text-sm font-medium hover:bg-blue-50 transition text-center">
                    {t.otherCases}
                  </Link>
                </div>
                <Link to="/"
                  className="w-full border border-gray-300 text-gray-600 py-2 rounded-xl text-sm font-medium hover:bg-gray-50 transition text-center">
                  {t.goHome ?? 'Ir al inicio'}
                </Link>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
