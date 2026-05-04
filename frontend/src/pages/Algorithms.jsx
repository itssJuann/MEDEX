import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { translateText } from '../utils/translate'
import { getProgress } from '../utils/progress'

const DIFFICULTIES = ["Básico", "Intermedio", "Avanzado"]

const DIFFICULTY_STYLES = {
  "Básico":     "bg-green-50 text-green-700 border border-green-200",
  "Intermedio": "bg-yellow-50 text-yellow-700 border border-yellow-200",
  "Avanzado":   "bg-red-50 text-red-700 border border-red-200",
}

export default function Algorithms() {
  const { t, lang } = useLang()
  const [rawAlgorithms, setRawAlgorithms] = useState([])
  const [algorithms, setAlgorithms]       = useState([])
  const [search, setSearch]               = useState("")
  const [specialty, setSpecialty]         = useState(null)
  const [difficulty, setDifficulty]       = useState(null)

  useEffect(() => {
    fetch(`${API}/algorithms`)
      .then(r => r.json()).then(setRawAlgorithms).catch(() => setRawAlgorithms([]))
  }, [])

  useEffect(() => {
    if (!rawAlgorithms.length) return
    if (lang === 'es') { setAlgorithms(rawAlgorithms); return }
    let cancelled = false
    Promise.all(rawAlgorithms.map(async a => ({
      ...a,
      title:       await translateText(a.title, lang),
      description: await translateText(a.description, lang),
    }))).then(translated => { if (!cancelled) setAlgorithms(translated) })
    return () => { cancelled = true }
  }, [rawAlgorithms, lang])

  const availableSpecialties = [...new Set(rawAlgorithms.map(a => a.specialty))]

  const filtered = algorithms.filter(a => {
    const matchSearch     = a.title.toLowerCase().includes(search.toLowerCase())
    const matchSpecialty  = !specialty || a.specialty === specialty
    const matchDifficulty = !difficulty || a.difficulty === difficulty
    return matchSearch && matchSpecialty && matchDifficulty
  })

  const hasFilter = specialty || difficulty || search

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="bg-gradient-to-br from-[#065f46] to-[#059669] text-white py-14 px-8 text-center">
        <div className="text-emerald-200 text-sm font-semibold uppercase tracking-widest mb-2">{t.guidesMode}</div>
        <h1 className="text-4xl font-bold mb-3">{t.algorithmsTitle}</h1>
        <p className="text-emerald-100 text-base max-w-xl mx-auto mb-6">{t.algorithmsSubtitle}</p>
        <input
          className="w-full max-w-xl px-5 py-3 rounded-full text-gray-800 text-sm outline-none shadow"
          placeholder={t.searchAlgo}
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>

      <div className="px-8 pt-5 pb-2 space-y-3 max-w-5xl mx-auto">
        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-20 shrink-0">{t.specialty}</span>
          <button onClick={() => setSpecialty(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!specialty ? "bg-emerald-700 text-white border-emerald-700" : "bg-white text-gray-600 border-gray-300 hover:border-emerald-600"}`}>
            {t.allSpecialties}
          </button>
          {availableSpecialties.map(s => (
            <button key={s} onClick={() => setSpecialty(s)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${specialty === s ? "bg-emerald-700 text-white border-emerald-700" : "bg-white text-gray-600 border-gray-300 hover:border-emerald-600"}`}>
              {t.specialties?.[s] ?? s}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-3 flex-wrap">
          <span className="text-xs font-semibold text-gray-400 uppercase w-20 shrink-0">{t.filterLevel}</span>
          <button onClick={() => setDifficulty(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!difficulty ? "bg-emerald-700 text-white border-emerald-700" : "bg-white text-gray-600 border-gray-300 hover:border-emerald-600"}`}>
            {t.allSpecialties}
          </button>
          {DIFFICULTIES.map(d => (
            <button key={d} onClick={() => setDifficulty(d)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${difficulty === d
                  ? d === "Básico" ? "bg-green-600 text-white border-green-600"
                  : d === "Intermedio" ? "bg-yellow-500 text-white border-yellow-500"
                  : "bg-red-600 text-white border-red-600"
                  : "bg-white text-gray-600 border-gray-300 hover:border-emerald-600"}`}>
              {t.difficulties?.[d] ?? d}
            </button>
          ))}
        </div>
      </div>

      <div className="px-8 py-3 text-xs text-gray-400 max-w-5xl mx-auto">
        {filtered.length} {filtered.length === 1 ? t.algorithm : (hasFilter ? t.algorithmsFound : t.algorithmsTotal)}
      </div>

      <div className="px-8 pb-16 max-w-5xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.length === 0 ? (
          <p className="text-gray-400 col-span-3 text-center py-16">{t.noResultsAlgo}</p>
        ) : (
          filtered.map(a => {
            const prog  = getProgress('algorithm', a.id)
            const BADGE = { success: { label: t.completed, cls: 'bg-green-100 text-green-700 border-green-200' }, warning: { label: t.withErrors, cls: 'bg-yellow-100 text-yellow-700 border-yellow-200' }, failure: { label: t.failed, cls: 'bg-red-100 text-red-700 border-red-200' } }
            const badge = prog ? BADGE[prog.best_result] : null
            return (
              <Link key={a.id} to={`/algorithm/${a.id}`}
                className="bg-white rounded-2xl shadow hover:shadow-md transition p-6 border border-gray-100 group">
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold text-emerald-600 uppercase tracking-wide">{t.specialties?.[a.specialty] ?? a.specialty}</span>
                  <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${DIFFICULTY_STYLES[a.difficulty] ?? ''}`}>
                    {t.difficulties?.[a.difficulty] ?? a.difficulty}
                  </span>
                </div>
                <h2 className="text-lg font-bold text-gray-800 group-hover:text-emerald-700 transition mb-2">{a.title}</h2>
                <p className="text-sm text-gray-500 line-clamp-2 mb-3">{a.description}</p>
                <div className="text-xs text-gray-400 mb-3">{t.basedOn} {a.guideline}</div>
                <div className="flex items-center justify-between">
                  <span className="text-xs text-emerald-600 font-medium">
                    {prog ? `${t.retry} (${prog.attempts} ${prog.attempts === 1 ? t.attempt : t.attempts})` : t.startAlgorithm}
                  </span>
                  {badge
                    ? <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${badge.cls}`}>{badge.label}</span>
                    : <span className="text-xs text-gray-400">{a.node_count} {t.nodes}</span>}
                </div>
              </Link>
            )
          })
        )}
      </div>
    </div>
  )
}
