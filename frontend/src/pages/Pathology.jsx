import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { saveProgress as persistProgress } from '../utils/progress'
import DiscussionSection from '../components/DiscussionSection'

async function translateLearning(L, lang) {
  if (!L || lang === 'es') return L
  const [summary, flow, phases, complications, pearls] = await Promise.all([
    translateText(L.pathophysiology?.summary, lang),
    Promise.all((L.pathophysiology?.flow ?? []).map(async s => ({
      ...s,
      label:  await translateText(s.label, lang),
      detail: await translateText(s.detail, lang),
    }))),
    Promise.all((L.treatment?.phases ?? []).map(async ph => ({
      ...ph,
      name:    await translateText(ph.name, lang),
      actions: await Promise.all(ph.actions.map(a => translateText(a, lang))),
    }))),
    Promise.all((L.complications ?? []).map(async c => ({
      ...c,
      name:        await translateText(c.name, lang),
      description: await translateText(c.description, lang),
    }))),
    Promise.all((L.pearls ?? []).map(p => translateText(p, lang))),
  ])
  return {
    ...L,
    pathophysiology: { ...L.pathophysiology, summary, flow },
    treatment:       { ...L.treatment, phases },
    complications,
    pearls,
  }
}

async function translateNodes(nodes, lang) {
  if (lang === 'es') return nodes
  const result = {}
  await Promise.all(Object.entries(nodes).map(async ([key, node]) => {
    const n = { ...node }
    if (n.description) n.description = await translateText(n.description, lang)
    if (n.pearl)       n.pearl       = await translateText(n.pearl, lang)
    if (n.options) {
      n.options = await Promise.all(n.options.map(async opt => ({
        ...opt,
        text:     await translateText(opt.text, lang),
        feedback: await translateText(opt.feedback, lang),
      })))
    }
    result[key] = n
  }))
  return result
}

export default function Pathology() {
  const { id } = useParams()
  const { t, lang } = useLang()

  const RESULT_STYLES = {
    success: { bg: 'bg-green-50',  border: 'border-green-300',  text: 'text-green-800',  icon: '✓', label: t.caseSuccess },
    warning: { bg: 'bg-yellow-50', border: 'border-yellow-300', text: 'text-yellow-800', icon: '!', label: t.caseWarning },
    failure: { bg: 'bg-red-50',    border: 'border-red-300',    text: 'text-red-800',    icon: '✕', label: t.caseFailure },
  }

  const [rawData, setRawData]   = useState(null)
  const [data, setData]         = useState(null)
  const [translating, setTranslating] = useState(false)
  const [nodeId, setNodeId]     = useState(null)
  const [selected, setSelected] = useState(null)
  const [history, setHistory]   = useState([])
  const [error, setError]       = useState(null)
  const [saved, setSaved]         = useState(false)
  const [activeTab, setActiveTab] = useState('case')
  const [translatedL, setTranslatedL] = useState(null)

  useEffect(() => {
    fetch(`${API}/pathologies/${id}`)
      .then(r => {
        if (!r.ok) throw new Error(`Error del servidor: ${r.status}`)
        return r.json()
      })
      .then(d => {
        if (!d.clinical_case?.nodes || !d.clinical_case?.start) {
          throw new Error('Estructura de datos inválida. Reinicia el servidor backend.')
        }
        setRawData(d)
        setNodeId(d.clinical_case.start)
        setHistory([d.clinical_case.start])
      })
      .catch(e => setError(e.message))
  }, [id])

  // Translate case nodes whenever rawData or language changes
  useEffect(() => {
    if (!rawData) return
    let cancelled = false
    setTranslating(lang !== 'es')
    const run = async () => {
      const translatedNodes = await translateNodes(rawData.clinical_case.nodes, lang)
      if (cancelled) return
      setData({ ...rawData, clinical_case: { ...rawData.clinical_case, nodes: translatedNodes } })
      setTranslating(false)
    }
    run()
    return () => { cancelled = true }
  }, [rawData, lang])

  // Translate learning content whenever rawData.learning or language changes
  useEffect(() => {
    if (!rawData?.learning) { setTranslatedL(null); return }
    if (lang === 'es') { setTranslatedL(rawData.learning); return }
    let cancelled = false
    translateLearning(rawData.learning, lang).then(result => {
      if (!cancelled) setTranslatedL(result)
    })
    return () => { cancelled = true }
  }, [rawData, lang])

  const saveProgress = (result) => {
    persistProgress('case', id, result)
    setSaved(true)
  }

  if (error) return (
    <div className="p-10 text-center">
      <div className="text-red-500 font-semibold mb-2">{t.errorLoading}</div>
      <div className="text-gray-500 text-sm mb-4">{error}</div>
      <div className="text-gray-400 text-xs">{lang === 'en' ? 'Make sure the backend server is running.' : 'Asegúrate de que el backend esté corriendo.'}</div>
    </div>
  )

  if (!data || !nodeId) return (
    <div className="p-10 text-center text-gray-400">{t.loading}</div>
  )

  if (translating) return (
    <div className="p-10 text-center text-gray-400 flex flex-col items-center gap-2">
      <div className="w-6 h-6 border-2 border-primary border-t-transparent rounded-full animate-spin"/>
      <span className="text-sm">{lang === 'en' ? 'Translating...' : 'Traduciendo...'}</span>
    </div>
  )

  const nodes      = data.clinical_case.nodes
  const current    = nodes[nodeId]
  const isTerminal = current.terminal === true
  const resultStyle = isTerminal ? RESULT_STYLES[current.result] : null

  const handleOption = (opt) => setSelected(opt.id)

  const advance = () => {
    const opt = current.options.find(o => o.id === selected)
    if (!opt?.next) return
    const nextNode = rawData?.clinical_case?.nodes[opt.next]
    if (nextNode?.terminal) saveProgress(nextNode.result)
    setNodeId(opt.next)
    setHistory(h => [...h, opt.next])
    setSelected(null)
  }

  const restart = () => {
    setNodeId(data.clinical_case.start)
    setHistory([data.clinical_case.start])
    setSelected(null)
    setSaved(false)
  }

  const selectedOpt = current.options?.find(o => o.id === selected)
  const L = translatedL   // learning data (translated when lang !== 'es')

  const PHASE_COLOR = { red:'bg-red-500', orange:'bg-orange-500', yellow:'bg-amber-400', blue:'bg-blue-500', green:'bg-green-500' }
  const SEV = { alta: 'bg-red-50 border-red-200 text-red-700', media: 'bg-yellow-50 border-yellow-200 text-yellow-700', baja: 'bg-green-50 border-green-200 text-green-700' }

  const TABS = [
    { id: 'case',         icon: '🎯', label: t.clinicalCase ?? 'Caso clínico' },
    { id: 'patho',        icon: '🧬', label: lang === 'en' ? 'Pathophysiology' : 'Fisiopatología' },
    { id: 'differential', icon: '🔍', label: lang === 'en' ? 'Differential' : 'Diferencial' },
    { id: 'treatment',    icon: '💊', label: lang === 'en' ? 'Treatment' : 'Tratamiento' },
    { id: 'complications',icon: '⚠️', label: lang === 'en' ? 'Complications' : 'Complicaciones' },
    { id: 'pearls',       icon: '💡', label: lang === 'en' ? 'Pearls' : 'Perlas' },
  ]

  const ComingSoon = () => (
    <div className="flex flex-col items-center justify-center py-14 text-center text-gray-400 gap-2">
      <span className="text-3xl">🚧</span>
      <p className="text-sm">{lang === 'en' ? 'Content coming soon for this pathology.' : 'Contenido próximamente para esta patología.'}</p>
    </div>
  )

  return (
    <div className="min-h-screen bg-gray-50 px-6 py-10 max-w-3xl mx-auto">

      <div className="mb-6">
        <Link to="/cases" className="text-xs text-accent hover:underline mb-2 inline-block">
          {t.backToRepo}
        </Link>
        <span className="block text-xs font-semibold text-accent uppercase mt-1">{data.system}</span>
        <h1 className="text-3xl font-bold text-primary mt-1">{data.name}</h1>
        <p className="text-gray-500 mt-2 text-sm">{data.summary}</p>
      </div>

      {/* ── Tab navigation ── */}
      <div className="flex gap-1 bg-gray-100 p-1 rounded-2xl mb-6 flex-wrap">
        {TABS.map(tab => (
          <button key={tab.id} onClick={() => setActiveTab(tab.id)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-medium transition flex-shrink-0
              ${activeTab === tab.id ? 'bg-white text-gray-800 shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}>
            <span>{tab.icon}</span>
            <span className="hidden sm:inline">{tab.label}</span>
          </button>
        ))}
      </div>

      {/* ══ TAB: FISIOPATOLOGÍA ══ */}
      {activeTab === 'patho' && (
        !L?.pathophysiology ? <ComingSoon /> : (
          <div className="flex flex-col gap-5">
            <div className="bg-white rounded-2xl border border-gray-100 shadow p-5">
              <p className="text-sm text-gray-700 leading-relaxed">{L.pathophysiology.summary}</p>
            </div>
            {/* Flow diagram */}
            <div className="bg-white rounded-2xl border border-gray-100 shadow p-5">
              <h3 className="text-xs font-semibold text-gray-400 uppercase mb-4">
                {lang === 'en' ? 'Pathophysiological mechanism' : 'Mecanismo fisiopatológico'}
              </h3>
              <div className="flex flex-col gap-3">
                {L.pathophysiology.flow.map((step, i) => (
                  <div key={i} className="flex items-start gap-3">
                    <div className="flex flex-col items-center shrink-0">
                      <div className="w-7 h-7 rounded-full bg-primary text-white text-xs font-bold flex items-center justify-center">
                        {i + 1}
                      </div>
                      {i < L.pathophysiology.flow.length - 1 && (
                        <div className="w-0.5 h-6 bg-primary opacity-20 mt-1" />
                      )}
                    </div>
                    <div className="pb-3">
                      <p className="text-sm font-semibold text-gray-800">{step.label}</p>
                      <p className="text-xs text-gray-500 mt-0.5 leading-relaxed">{step.detail}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )
      )}

      {/* ══ TAB: DIFERENCIAL ══ */}
      {activeTab === 'differential' && (
        !L?.related_differential ? <ComingSoon /> : (
          <div className="flex flex-col gap-4">
            <div className="bg-white rounded-2xl border border-gray-100 shadow p-5">
              <p className="text-xs text-gray-400 mb-3">
                {lang === 'en'
                  ? 'This pathology is part of the following differential diagnosis case:'
                  : 'Esta patología forma parte del siguiente caso de diagnóstico diferencial:'}
              </p>
              <Link to={`/differential/${L.related_differential}`}
                className="flex items-center justify-between bg-blue-50 border border-blue-200 rounded-xl px-5 py-4 hover:bg-blue-100 transition group">
                <div>
                  <p className="text-sm font-bold text-blue-800 group-hover:underline">
                    {lang === 'en' ? 'Open differential diagnosis case' : 'Abrir caso de diagnóstico diferencial'}
                  </p>
                  <p className="text-xs text-blue-600 mt-0.5">{L.related_differential}</p>
                </div>
                <span className="text-blue-500 text-xl">→</span>
              </Link>
            </div>
            <div className="bg-blue-50 border border-blue-100 rounded-2xl p-4 text-sm text-blue-700">
              {lang === 'en'
                ? 'In the differential diagnosis module you will actively eliminate hypotheses as new information appears — you\'ll learn to reason, not memorize.'
                : 'En el módulo de diagnóstico diferencial eliminarás hipótesis activamente a medida que aparece nueva información — aprenderás a razonar, no a memorizar.'}
            </div>
          </div>
        )
      )}

      {/* ══ TAB: TRATAMIENTO ══ */}
      {activeTab === 'treatment' && (
        !L?.treatment ? <ComingSoon /> : (
          <div className="flex flex-col gap-4">
            {L.treatment.phases.map((phase, i) => (
              <div key={i} className="bg-white rounded-2xl border border-gray-100 shadow overflow-hidden">
                <div className={`${PHASE_COLOR[phase.color] ?? 'bg-primary'} px-5 py-2.5 flex items-center gap-2`}>
                  <span className="w-5 h-5 rounded-full bg-white/30 text-white text-xs font-bold flex items-center justify-center shrink-0">
                    {i + 1}
                  </span>
                  <span className="text-white text-sm font-semibold">{phase.name}</span>
                </div>
                <ul className="px-5 py-4 flex flex-col gap-2">
                  {phase.actions.map((action, j) => (
                    <li key={j} className="flex items-start gap-2.5 text-sm text-gray-700">
                      <span className="text-primary shrink-0 mt-0.5 font-bold">▸</span>
                      <span>{action}</span>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        )
      )}

      {/* ══ TAB: COMPLICACIONES ══ */}
      {activeTab === 'complications' && (
        !L?.complications?.length ? <ComingSoon /> : (
          <div className="flex flex-col gap-3">
            <p className="text-xs text-gray-400 px-1">
              {lang === 'en' ? 'Ordered by clinical severity' : 'Ordenadas por gravedad clínica'}
            </p>
            {L.complications.map((c, i) => (
              <div key={i} className={`rounded-2xl border p-4 ${SEV[c.severity] ?? 'bg-gray-50 border-gray-200 text-gray-700'}`}>
                <div className="flex items-center gap-2 mb-1 flex-wrap">
                  <span className="font-semibold text-sm">{c.name}</span>
                  <span className={`text-xs px-2 py-0.5 rounded-full font-medium
                    ${c.severity === 'alta' ? 'bg-red-100 text-red-700' : c.severity === 'media' ? 'bg-yellow-100 text-yellow-700' : 'bg-green-100 text-green-700'}`}>
                    {lang === 'en'
                      ? (c.severity === 'alta' ? 'High' : c.severity === 'media' ? 'Medium' : 'Low')
                      : (c.severity === 'alta' ? 'Alta' : c.severity === 'media' ? 'Media' : 'Baja')}
                  </span>
                </div>
                <p className="text-xs leading-relaxed opacity-85">{c.description}</p>
              </div>
            ))}
          </div>
        )
      )}

      {/* ══ TAB: PERLAS CLÍNICAS ══ */}
      {activeTab === 'pearls' && (
        !L?.pearls?.length ? <ComingSoon /> : (
          <div className="flex flex-col gap-3">
            {L.pearls.map((pearl, i) => (
              <div key={i} className="bg-amber-50 border border-amber-200 rounded-2xl px-5 py-4 flex items-start gap-3">
                <span className="text-amber-400 text-lg shrink-0">💡</span>
                <p className="text-sm text-amber-900 leading-relaxed">{pearl}</p>
              </div>
            ))}
            {/* Quiz link */}
            {L.related_quiz && (
              <Link to={`/quiz/${L.related_quiz}`}
                className="mt-2 flex items-center justify-between bg-indigo-50 border border-indigo-200 rounded-2xl px-5 py-4 hover:bg-indigo-100 transition group">
                <div>
                  <p className="text-sm font-bold text-indigo-800">{lang === 'en' ? '🧠 Final quiz' : '🧠 Quiz final'}</p>
                  <p className="text-xs text-indigo-500 mt-0.5">
                    {lang === 'en' ? 'Test your knowledge on this system' : 'Pon a prueba tus conocimientos sobre este sistema'}
                  </p>
                </div>
                <span className="text-indigo-400 text-xl group-hover:translate-x-1 transition-transform">→</span>
              </Link>
            )}
          </div>
        )
      )}

      {/* ══ TAB: CASO CLÍNICO ══ */}
      {activeTab === 'case' && (<>

      {/* Progreso de decisiones */}
      <div className="mb-6 flex items-center gap-2">
        {history.map((nid, i) => {
          const isLast = i === history.length - 1
          const isTerm = nodes[nid]?.terminal
          return (
            <div key={i} className="flex items-center gap-2">
              <div className={`w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold border-2 transition-all
                ${isLast && isTerm && current.result === 'success' ? 'bg-green-500 border-green-500 text-white'
                  : isLast && isTerm && current.result === 'failure' ? 'bg-red-500 border-red-500 text-white'
                  : isLast && isTerm && current.result === 'warning' ? 'bg-yellow-400 border-yellow-400 text-white'
                  : isLast ? 'bg-primary border-primary text-white'
                  : 'bg-white border-primary text-primary'}`}>
                {i + 1}
              </div>
              {!isLast && <div className="w-6 h-0.5 bg-primary opacity-30" />}
            </div>
          )
        })}
      </div>

      <div className="bg-white rounded-2xl shadow p-6 border border-gray-100">

        {!isTerminal && (
          <>
            <div className="flex items-center justify-between mb-5">
              <h2 className="font-bold text-gray-700">{t.clinicalCase}</h2>
              <span className="text-xs text-gray-400">{t.decision} {history.length}</span>
            </div>

            <p className="text-gray-700 mb-6 leading-relaxed">{current.description}</p>

            <div className="flex flex-col gap-3">
              {current.options.map(opt => {
                const isSelected = selected === opt.id
                const showResult = !!selected
                let cls = 'text-left px-4 py-3 rounded-xl border text-sm transition cursor-pointer '
                if (!showResult)       cls += 'bg-gray-50 border-gray-200 hover:border-primary hover:bg-blue-50'
                else if (isSelected)   cls += opt.correct ? 'bg-green-50 border-green-400 text-green-800' : 'bg-red-50 border-red-400 text-red-800'
                else                   cls += 'bg-gray-50 border-gray-100 text-gray-400 opacity-60'
                return (
                  <button key={opt.id} onClick={() => !selected && handleOption(opt)} disabled={!!selected} className={cls}>
                    <span className="font-semibold mr-2 text-gray-400">{opt.id.toUpperCase()}.</span>
                    {opt.text}
                  </button>
                )
              })}
            </div>

            {selectedOpt && (
              <div className={`mt-5 p-4 rounded-xl text-sm border ${selectedOpt.correct ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                <span className="font-semibold mr-1">
                  {selectedOpt.correct ? t.correctLabel : t.incorrectLabel}
                </span>
                {selectedOpt.feedback}
              </div>
            )}

            {selected && (
              <button onClick={advance}
                className="mt-6 bg-primary text-white px-6 py-2.5 rounded-full text-sm font-medium hover:bg-blue-900 transition">
                {t.continueBtn}
              </button>
            )}
          </>
        )}

        {isTerminal && resultStyle && (
          <div>
            <div className={`rounded-xl p-4 border mb-5 ${resultStyle.bg} ${resultStyle.border}`}>
              <div className={`font-bold text-base mb-1 ${resultStyle.text}`}>
                {resultStyle.icon} {resultStyle.label}
              </div>
              <p className={`text-sm leading-relaxed ${resultStyle.text}`}>{current.description}</p>
            </div>

            {current.pearl && (
              <div className="bg-blue-50 border border-blue-200 rounded-xl p-4 text-sm text-blue-800 mb-5">
                <span className="font-semibold block mb-1">{t.clinicalPearl}</span>
                {current.pearl}
              </div>
            )}

            {saved && (
              <div className="flex items-center gap-1.5 text-xs text-green-600 mb-4">
                <span>✓</span><span>{t.progressSaved}</span>
              </div>
            )}

            <div className="flex gap-3 flex-wrap">
              <button onClick={restart}
                className="bg-primary text-white px-6 py-2.5 rounded-full text-sm font-medium hover:bg-blue-900 transition">
                {t.repeatCase}
              </button>
              <Link to="/cases"
                className="border border-primary text-primary px-6 py-2.5 rounded-full text-sm font-medium hover:bg-blue-50 transition">
                {t.viewOtherPathologies}
              </Link>
              <Link to="/"
                className="border border-gray-300 text-gray-600 px-6 py-2.5 rounded-full text-sm font-medium hover:bg-gray-50 transition">
                {t.goHome ?? 'Ir al inicio'}
              </Link>
            </div>
          </div>
        )}
      </div>

      {history.length > 1 && (
        <div className="mt-6 bg-white rounded-2xl shadow-sm p-5 border border-gray-100">
          <h3 className="text-xs font-semibold text-gray-400 uppercase mb-3">{t.yourPath}</h3>
          <ol className="flex flex-col gap-2">
            {history.slice(0, -1).map((nid, i) => {
              const node = nodes[nid]
              const chosenOpt = (() => { const nextNid = history[i + 1]; return node?.options?.find(o => o.next === nextNid) })()
              if (!chosenOpt) return null
              return (
                <li key={i} className="text-xs text-gray-500 flex gap-2">
                  <span className="font-bold text-primary w-4 shrink-0">{i + 1}.</span>
                  <span className={chosenOpt.correct ? 'text-green-700' : 'text-red-600'}>
                    {chosenOpt.correct ? '✓' : '✕'} {chosenOpt.text}
                  </span>
                </li>
              )
            })}
          </ol>
        </div>
      )}

      <DiscussionSection pathologyId={id} />

      </>)} {/* end activeTab === 'case' */}
    </div>
  )
}
