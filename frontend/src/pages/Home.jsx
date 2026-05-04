import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { getProgress } from '../utils/progress'

const SYSTEMS      = ["Cardiovascular", "Respiratorio", "Digestivo", "Neurológico", "Endocrino", "Infeccioso", "Renal"]
const DIFFICULTIES = ["Básico", "Intermedio", "Avanzado"]

const DIFFICULTY_STYLES = {
  "Básico":     "bg-green-50 text-green-700 border border-green-200",
  "Intermedio": "bg-yellow-50 text-yellow-700 border border-yellow-200",
  "Avanzado":   "bg-red-50 text-red-700 border border-red-200",
}

export default function Home() {
  const { t, lang } = useLang()

  const [rawPathologies, setRawPathologies] = useState([])
  const [pathologies, setPathologies]       = useState([])
  const [search, setSearch]                 = useState("")
  const [system, setSystem]                 = useState(null)
  const [difficulty, setDifficulty]         = useState(null)

  useEffect(() => {
    fetch(`${API}/pathologies`)
      .then(r => r.json())
      .then(setRawPathologies)
      .catch(() => setRawPathologies([]))
  }, [])

  // Translate name + summary when language or raw data changes
  useEffect(() => {
    if (!rawPathologies.length) return
    if (lang === 'es') { setPathologies(rawPathologies); return }
    let cancelled = false
    Promise.all(rawPathologies.map(async p => ({
      ...p,
      name:    await translateText(p.name, lang),
      summary: await translateText(p.summary, lang),
    }))).then(translated => { if (!cancelled) setPathologies(translated) })
    return () => { cancelled = true }
  }, [rawPathologies, lang])


  const filtered = pathologies.filter(p => {
    const matchSearch     = p.name.toLowerCase().includes(search.toLowerCase())
    const matchSystem     = !system || p.system === system
    const matchDifficulty = !difficulty || p.difficulty === difficulty
    return matchSearch && matchSystem && matchDifficulty
  })

  const hasFilter = system || difficulty || search

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero */}
      <div className="bg-primary text-white py-16 px-8 text-center">
        <h1 className="text-4xl font-bold mb-3">{t.homeTitle}</h1>
        <p className="text-accent text-lg">{t.homeSubtitle}</p>
        <input
          className="mt-8 w-full max-w-xl px-5 py-3 rounded-full text-gray-800 text-sm outline-none shadow"
          placeholder={t.searchPlaceholder}
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>

      {/* Filtros */}
      <div className="px-8 pt-5 pb-2 space-y-3">
        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-16 shrink-0">{t.filterSystem}</span>
          <button
            onClick={() => setSystem(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!system ? "bg-primary text-white border-primary" : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}
          >
            {t.allSystems}
          </button>
          {SYSTEMS.map(s => (
            <button
              key={s}
              onClick={() => setSystem(s)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${system === s ? "bg-primary text-white border-primary" : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}
            >
              {t.systems?.[s] ?? s}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-16 shrink-0">{t.filterLevel}</span>
          <button
            onClick={() => setDifficulty(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!difficulty ? "bg-primary text-white border-primary" : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}
          >
            {t.allLevels}
          </button>
          {DIFFICULTIES.map(d => (
            <button
              key={d}
              onClick={() => setDifficulty(d)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${difficulty === d
                  ? d === "Básico"     ? "bg-green-600 text-white border-green-600"
                  : d === "Intermedio" ? "bg-yellow-500 text-white border-yellow-500"
                  :                     "bg-red-600 text-white border-red-600"
                  : "bg-white text-gray-600 border-gray-300 hover:border-primary"}`}
            >
              {t.difficulties?.[d] ?? d}
            </button>
          ))}
        </div>
      </div>

      {/* Contador */}
      <div className="px-8 py-3 text-xs text-gray-400">
        {filtered.length} {filtered.length === 1 ? t.pathology : (hasFilter ? t.pathologiesFound : t.pathologiesTotal)}
      </div>

      {/* Grid */}
      <div className="px-8 pb-16 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.length === 0 ? (
          <p className="text-gray-400 col-span-3 text-center py-16">{t.noResults}</p>
        ) : (
          filtered.map(p => {
            const prog  = getProgress('case', p.id)
            const badge = prog ? {
              success: { label: t.completed,  cls: 'bg-green-100 text-green-700 border-green-200' },
              warning: { label: t.withErrors,  cls: 'bg-yellow-100 text-yellow-700 border-yellow-200' },
              failure: { label: t.failed,      cls: 'bg-red-100 text-red-700 border-red-200' },
            }[prog.best_result] : null

            return (
              <a key={p.id} href={`/pathology/${p.id}`}
                 className="bg-white rounded-2xl shadow hover:shadow-md transition p-6 border border-gray-100 group">
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold text-accent uppercase tracking-wide">{t.systems?.[p.system] ?? p.system}</span>
                  <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${DIFFICULTY_STYLES[p.difficulty] ?? "text-gray-400"}`}>
                    {t.difficulties?.[p.difficulty] ?? p.difficulty}
                  </span>
                </div>
                <h2 className="text-lg font-bold text-gray-800 group-hover:text-primary transition">{p.name}</h2>
                <p className="text-sm text-gray-500 mt-2 line-clamp-2">{p.summary}</p>
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-xs text-primary font-medium">
                    {prog
                      ? `${t.retry} (${prog.attempts} ${prog.attempts === 1 ? t.attempt : t.attempts})`
                      : t.viewCase}
                  </span>
                  {badge && (
                    <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${badge.cls}`}>
                      {badge.label}
                    </span>
                  )}
                </div>
              </a>
            )
          })
        )}
      </div>
    </div>
  )
}
