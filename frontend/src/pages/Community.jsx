import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'
import { useAuth } from '../context/AuthContext'
import { getProgress } from '../utils/progress'

const DIFF_STYLE = {
  "Básico":     "bg-green-50 text-green-700 border border-green-200",
  "Intermedio": "bg-yellow-50 text-yellow-700 border border-yellow-200",
  "Avanzado":   "bg-red-50 text-red-700 border border-red-200",
}

export default function Community() {
  const { lang } = useLang()
  const { user } = useAuth()
  const lbl = (es, en) => lang === 'en' ? en : es

  const [cases, setCases]   = useState([])
  const [mine, setMine]     = useState([])
  const [search, setSearch] = useState('')
  const [system, setSystem] = useState(null)
  const [tab, setTab]       = useState('all')  // 'all' | 'mine'

  useEffect(() => {
    fetch(`${API}/community-cases`)
      .then(r => r.json()).then(d => Array.isArray(d) ? setCases(d) : setCases([]))
      .catch(() => setCases([]))
  }, [])

  useEffect(() => {
    const token = localStorage.getItem('medex_token')
    if (!token) return
    fetch(`${API}/community-cases/mine`, {
      headers: { Authorization: `Bearer ${token}` }
    }).then(r => r.json()).then(d => Array.isArray(d) ? setMine(d) : setMine([]))
      .catch(() => setMine([]))
  }, [user])

  const systems = [...new Set(cases.map(c => c.system))]
  const source  = tab === 'mine' ? mine : cases

  const filtered = source.filter(c => {
    const matchSearch = c.title.toLowerCase().includes(search.toLowerCase())
    const matchSystem = !system || c.system === system
    return matchSearch && matchSystem
  })

  const STATUS_BADGE = {
    pending:  { label: lbl('En revisión', 'Under review'), cls: 'bg-yellow-100 text-yellow-700 border-yellow-200' },
    approved: { label: lbl('Aprobado', 'Approved'),       cls: 'bg-green-100 text-green-700 border-green-200'  },
    rejected: { label: lbl('Rechazado', 'Rejected'),      cls: 'bg-red-100 text-red-700 border-red-200'        },
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero */}
      <div className="bg-gradient-to-br from-violet-700 to-purple-800 text-white py-14 px-8 text-center">
        <div className="text-violet-200 text-sm font-semibold uppercase tracking-widest mb-2">
          {lbl('Contribución académica', 'Academic contribution')}
        </div>
        <h1 className="text-4xl font-bold mb-3">{lbl('Casos de la Comunidad', 'Community Cases')}</h1>
        <p className="text-violet-200 text-base max-w-xl mx-auto mb-6">
          {lbl(
            'Casos clínicos creados por estudiantes y revisados por moderadores. ¿Tienes un caso interesante?',
            'Clinical cases created by students and reviewed by moderators. Got an interesting case?'
          )}
        </p>
        <div className="flex items-center justify-center gap-3 flex-wrap">
          <input
            className="w-full max-w-md px-5 py-3 rounded-full text-gray-800 text-sm outline-none shadow"
            placeholder={lbl('Buscar caso...', 'Search case...')}
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
          <Link to="/community/create"
            className="bg-white text-violet-700 font-semibold px-6 py-3 rounded-full text-sm hover:bg-violet-50 transition shadow">
            + {lbl('Crear caso', 'Create case')}
          </Link>
          {user?.is_admin && (
            <Link to="/community/moderate"
              className="border border-white/50 text-white px-5 py-3 rounded-full text-sm hover:bg-white/10 transition">
              {lbl('Moderar', 'Moderate')}
            </Link>
          )}
        </div>
      </div>

      {/* Tabs */}
      <div className="max-w-5xl mx-auto px-6 pt-6">
        <div className="flex gap-1 bg-gray-100 p-1 rounded-xl w-fit">
          {[
            { key: 'all',  label: lbl('Todos los casos', 'All cases') },
            { key: 'mine', label: lbl('Mis casos', 'My cases') },
          ].map(t => (
            <button key={t.key} onClick={() => setTab(t.key)}
              className={`px-5 py-2 rounded-lg text-sm font-medium transition
                ${tab === t.key ? 'bg-white text-gray-800 shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}>
              {t.label}
            </button>
          ))}
        </div>
      </div>

      {/* Filters */}
      {tab === 'all' && (
        <div className="max-w-5xl mx-auto px-6 pt-4 flex gap-2 flex-wrap">
          <button onClick={() => setSystem(null)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
              ${!system ? 'bg-violet-700 text-white border-violet-700' : 'bg-white text-gray-600 border-gray-300 hover:border-violet-500'}`}>
            {lbl('Todos', 'All')}
          </button>
          {systems.map(s => (
            <button key={s} onClick={() => setSystem(s === system ? null : s)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium border transition
                ${system === s ? 'bg-violet-700 text-white border-violet-700' : 'bg-white text-gray-600 border-gray-300 hover:border-violet-500'}`}>
              {s}
            </button>
          ))}
        </div>
      )}

      {/* Counter */}
      <div className="max-w-5xl mx-auto px-6 py-3 text-xs text-gray-400">
        {filtered.length} {lbl('casos', 'cases')}
      </div>

      {/* Grid */}
      <div className="max-w-5xl mx-auto px-6 pb-16 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        {filtered.length === 0 ? (
          <div className="col-span-3 text-center py-16 text-gray-400">
            {tab === 'mine'
              ? lbl('Aún no has creado casos. ¡Anímate!', "You haven't created any cases yet. Give it a try!")
              : lbl('No hay casos disponibles.', 'No cases available.')}
          </div>
        ) : filtered.map(c => {
          const prog  = getProgress('community', String(c.id))
          const BADGE = {
            success: { label: lbl('Completado','Completed'), cls:'bg-green-100 text-green-700 border-green-200' },
            warning: { label: lbl('Con errores','With errors'), cls:'bg-yellow-100 text-yellow-700 border-yellow-200' },
            failure: { label: lbl('Fallido','Failed'), cls:'bg-red-100 text-red-700 border-red-200' },
          }
          const progBadge = prog ? BADGE[prog.best_result] : null
          const statusBadge = tab === 'mine' ? STATUS_BADGE[c.status] : null

          return (
            <div key={c.id}
              className="bg-white rounded-2xl shadow hover:shadow-md transition p-5 border border-gray-100 flex flex-col">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-semibold text-violet-600 uppercase tracking-wide">{c.system}</span>
                <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${DIFF_STYLE[c.difficulty] ?? ''}`}>
                  {c.difficulty}
                </span>
              </div>
              <h2 className="text-base font-bold text-gray-800 mb-1 line-clamp-2">{c.title}</h2>
              <p className="text-xs text-gray-500 line-clamp-2 mb-2">{c.summary}</p>
              <p className="text-xs text-gray-400 mb-3">
                {lbl('Por', 'By')} <span className="font-medium text-gray-600">{c.author}</span>
              </p>
              <div className="mt-auto flex items-center justify-between gap-2 flex-wrap">
                {c.status === 'approved' ? (
                  <Link to={`/community/case/${c.id}`}
                    className="text-xs text-violet-700 font-medium hover:underline">
                    {prog ? lbl('Reintentar →','Retry →') : lbl('Resolver →','Solve →')}
                  </Link>
                ) : (
                  <span className="text-xs text-gray-400">{lbl('No disponible aún','Not available yet')}</span>
                )}
                <div className="flex gap-1.5 flex-wrap">
                  {progBadge && (
                    <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${progBadge.cls}`}>
                      {progBadge.label}
                    </span>
                  )}
                  {statusBadge && (
                    <span className={`text-xs font-medium px-2 py-0.5 rounded-full border ${statusBadge.cls}`}>
                      {statusBadge.label}
                    </span>
                  )}
                  {tab === 'mine' && c.status === 'rejected' && c.mod_note && (
                    <span className="text-xs text-gray-400 italic">"{c.mod_note}"</span>
                  )}
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
