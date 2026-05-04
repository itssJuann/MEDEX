import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { saveProgress as persistProgress } from '../utils/progress'

async function translateAlgoNodes(nodes, lang) {
  if (lang === 'es') return nodes
  const result = {}
  await Promise.all(Object.entries(nodes).map(async ([key, node]) => {
    const n = { ...node }
    if (n.text)    n.text    = await translateText(n.text, lang)
    if (n.context) n.context = await translateText(n.context, lang)
    if (n.title)   n.title   = await translateText(n.title, lang)
    if (n.pearl)   n.pearl   = await translateText(n.pearl, lang)
    if (n.details) n.details = await Promise.all(n.details.map(d => translateText(d, lang)))
    if (n.options) n.options = await Promise.all(n.options.map(async opt => ({
      ...opt, label: await translateText(opt.label, lang),
    })))
    result[key] = n
  }))
  return result
}

export default function AlgorithmCase() {
  const { id } = useParams()
  const { t, lang } = useLang()
  const [rawData, setRawData]         = useState(null)
  const [data, setData]               = useState(null)
  const [translating, setTranslating] = useState(false)
  const [nodeId, setNodeId]           = useState(null)
  const [path, setPath]               = useState([])

  useEffect(() => {
    fetch(`${API}/algorithms/${id}`)
      .then(r => r.json())
      .then(d => { setRawData(d); setNodeId(d.start); setPath([]) })
  }, [id])

  useEffect(() => {
    if (!rawData) return
    let cancelled = false
    setTranslating(lang !== 'es')
    translateAlgoNodes(rawData.nodes, lang).then(translatedNodes => {
      if (!cancelled) {
        setData({ ...rawData, nodes: translatedNodes })
        setTranslating(false)
      }
    })
    return () => { cancelled = true }
  }, [rawData, lang])

  if (!data || !nodeId) return <div className="p-10 text-center text-gray-400">{t.loading}</div>

  if (translating) return (
    <div className="p-10 text-center text-gray-400 flex flex-col items-center gap-2">
      <div className="w-6 h-6 border-2 border-emerald-600 border-t-transparent rounded-full animate-spin"/>
      <span className="text-sm">{lang === 'en' ? 'Translating...' : 'Traduciendo...'}</span>
    </div>
  )

  const SEVERITY = {
    critical: { bar: 'bg-red-500',    badge: 'bg-red-50 border-red-300 text-red-800',    icon: '🔴', label: t.severityCritical },
    warning:  { bar: 'bg-yellow-400', badge: 'bg-yellow-50 border-yellow-300 text-yellow-800', icon: '🟡', label: t.severityWarning },
    info:     { bar: 'bg-blue-400',   badge: 'bg-blue-50 border-blue-300 text-blue-800',   icon: '🔵', label: t.severityInfo },
    success:  { bar: 'bg-green-500',  badge: 'bg-green-50 border-green-300 text-green-800', icon: '🟢', label: t.severitySuccess },
  }

  const current    = data.nodes[nodeId]
  const isTerminal = current.type === 'terminal'
  const sev        = isTerminal ? SEVERITY[current.severity] : null

  const choose = (opt) => {
    setPath(p => [...p, { nodeId, label: opt.label }])
    const nextNode = data.nodes[opt.next]
    if (nextNode?.type === 'terminal') saveProgress()
    setNodeId(opt.next)
  }

  const saveProgress = () => { persistProgress('algorithm', id, 'success') }

  const restart = () => { setNodeId(data.start); setPath([]) }

  const goBack = () => {
    if (path.length === 0) return
    const prev = path[path.length - 1]
    setNodeId(prev.nodeId)
    setPath(p => p.slice(0, -1))
  }

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-10 max-w-4xl mx-auto">
      <div className="mb-6">
        <Link to="/algorithms" className="text-xs text-emerald-600 hover:underline mb-2 inline-block">
          {t.backToAlgo}
        </Link>
        <div className="flex items-center gap-3 mt-1 flex-wrap">
          <span className="text-xs font-semibold text-emerald-600 uppercase">{data.specialty}</span>
          <span className="text-xs text-gray-400">•</span>
          <span className="text-xs text-gray-400">{data.difficulty}</span>
          <span className="text-xs text-gray-400">•</span>
          <span className="text-xs text-gray-400">{t.basedOn} {data.guideline}</span>
        </div>
        <h1 className="text-2xl font-bold text-gray-800 mt-1">{data.title}</h1>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">
        <div className="lg:col-span-2">
          <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-4">
            <div className="text-xs font-semibold text-gray-400 uppercase mb-3">{t.yourRoute}</div>
            {path.length === 0 ? (
              <p className="text-xs text-gray-400">{t.noDecisions}</p>
            ) : (
              <ol className="flex flex-col gap-2">
                {path.map((step, i) => {
                  const node = data.nodes[step.nodeId]
                  return (
                    <li key={i} className="text-xs">
                      <div className="text-gray-400 line-clamp-2 mb-0.5">{node?.text}</div>
                      <div className="flex items-center gap-1.5">
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 shrink-0"/>
                        <span className="font-semibold text-emerald-700">{step.label}</span>
                      </div>
                      {i < path.length - 1 && <div className="border-l border-dashed border-gray-200 ml-0.5 h-3 mt-1"/>}
                    </li>
                  )
                })}
              </ol>
            )}
            {path.length > 0 && (
              <button onClick={goBack}
                className="mt-4 w-full text-xs text-gray-500 border border-gray-200 rounded-xl py-2 hover:border-gray-400 transition">
                {t.goBack}
              </button>
            )}
          </div>
        </div>

        <div className="lg:col-span-3">
          {isTerminal && sev && <div className={`h-1.5 w-full rounded-full mb-4 ${sev.bar}`} />}

          <div className="bg-white rounded-2xl border border-gray-100 shadow p-6">
            {!isTerminal && (
              <>
                <div className="text-xs font-semibold text-gray-400 uppercase mb-4">
                  {t.decisionLabel} {path.length + 1}
                </div>
                <p className="text-gray-800 font-semibold text-base leading-snug mb-3">{current.text}</p>
                {current.context && (
                  <div className="bg-gray-50 border border-gray-200 rounded-xl p-3 mb-5">
                    <p className="text-xs text-gray-500 leading-relaxed">{current.context}</p>
                  </div>
                )}
                <div className="flex flex-col gap-3">
                  {current.options.map(opt => (
                    <button key={opt.id} onClick={() => choose(opt)}
                      className="text-left px-4 py-3.5 rounded-xl border border-gray-200 bg-gray-50
                        hover:border-emerald-500 hover:bg-emerald-50 hover:text-emerald-800
                        text-sm text-gray-700 font-medium transition-all">
                      {opt.label}
                    </button>
                  ))}
                </div>
              </>
            )}

            {isTerminal && sev && (
              <>
                <div className={`inline-flex items-center gap-2 text-xs font-semibold px-3 py-1.5 rounded-full border mb-4 ${sev.badge}`}>
                  <span>{sev.icon}</span>
                  <span>{sev.label}</span>
                </div>
                <h2 className="text-lg font-bold text-gray-800 mb-3">{current.title}</h2>
                <p className="text-sm text-gray-600 leading-relaxed mb-5">{current.text}</p>
                {current.details?.length > 0 && (
                  <div className="bg-gray-50 rounded-xl border border-gray-200 p-4 mb-5">
                    <div className="text-xs font-semibold text-gray-400 uppercase mb-3">{t.actions}</div>
                    <ul className="flex flex-col gap-2">
                      {current.details.map((d, i) => (
                        <li key={i} className="flex gap-2 text-sm text-gray-700">
                          <span className="text-emerald-500 shrink-0 mt-0.5">▸</span>
                          <span>{d}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
                {current.pearl && (
                  <div className="bg-blue-50 border border-blue-200 rounded-xl p-4 mb-5">
                    <div className="text-xs font-semibold text-blue-600 mb-1">{t.clinicalPearl}</div>
                    <p className="text-xs text-blue-800 leading-relaxed">{current.pearl}</p>
                  </div>
                )}
                <div className="flex gap-3 flex-wrap">
                  <button onClick={restart}
                    className="bg-emerald-700 text-white px-6 py-2.5 rounded-xl text-sm font-medium hover:bg-emerald-800 transition">
                    {t.restartAlgo}
                  </button>
                  <Link to="/algorithms"
                    className="border border-emerald-700 text-emerald-700 px-6 py-2.5 rounded-xl text-sm font-medium hover:bg-emerald-50 transition">
                    {t.otherAlgorithms}
                  </Link>
                  <Link to="/"
                    className="border border-gray-300 text-gray-600 px-6 py-2.5 rounded-xl text-sm font-medium hover:bg-gray-50 transition">
                    {t.goHome ?? 'Ir al inicio'}
                  </Link>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
