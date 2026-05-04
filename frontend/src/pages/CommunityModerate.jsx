import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useLang } from '../context/LangContext'

const DIFF_STYLE = {
  "Básico":     "bg-green-50 text-green-700",
  "Intermedio": "bg-yellow-50 text-yellow-700",
  "Avanzado":   "bg-red-50 text-red-700",
}

export default function CommunityModerate() {
  const { user } = useAuth()
  const { lang } = useLang()
  const lbl = (es, en) => lang === 'en' ? en : es

  const [cases, setCases]   = useState([])
  const [loading, setLoading] = useState(true)
  const [expanded, setExpanded] = useState(null)
  const [notes, setNotes]   = useState({})   // { [id]: noteText }
  const [busy, setBusy]     = useState({})   // { [id]: true }

  useEffect(() => {
    const token = localStorage.getItem('medex_token')
    fetch(`${API}/community-cases/pending`, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(r => r.ok ? r.json() : [])
      .then(d => { setCases(Array.isArray(d) ? d : []); setLoading(false) })
      .catch(() => setLoading(false))
  }, [])

  const moderate = async (id, action) => {
    setBusy(b => ({ ...b, [id]: true }))
    const token = localStorage.getItem('medex_token')
    try {
      const r = await fetch(`${API}/community-cases/${id}/moderate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ action, note: notes[id] ?? '' }),
      })
      if (r.ok) {
        setCases(c => c.filter(x => x.id !== id))
        setExpanded(null)
      }
    } finally {
      setBusy(b => ({ ...b, [id]: false }))
    }
  }

  if (!user?.is_admin) {
    return (
      <div className="p-10 text-center">
        <p className="text-gray-500 text-sm">{lbl('No tienes permisos de moderación.','You do not have moderation permissions.')}</p>
        <Link to="/community" className="text-violet-600 text-sm hover:underline mt-2 inline-block">← {lbl('Volver','Back')}</Link>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="bg-gradient-to-br from-gray-800 to-gray-900 text-white py-10 px-8">
        <h1 className="text-3xl font-bold">{lbl('Panel de Moderación','Moderation Panel')}</h1>
        <p className="text-gray-400 mt-1 text-sm">
          {lbl('Casos pendientes de revisión','Cases pending review')}
        </p>
      </div>

      <div className="max-w-4xl mx-auto px-6 py-8">
        {loading && <p className="text-gray-400 text-sm">{lbl('Cargando...','Loading...')}</p>}

        {!loading && cases.length === 0 && (
          <div className="text-center py-16">
            <div className="text-4xl mb-3">✅</div>
            <p className="text-gray-500">{lbl('No hay casos pendientes. ¡Todo al día!','No pending cases. All up to date!')}</p>
            <Link to="/community" className="text-violet-600 text-sm hover:underline mt-3 inline-block">← {lbl('Comunidad','Community')}</Link>
          </div>
        )}

        <div className="flex flex-col gap-5">
          {cases.map(c => (
            <div key={c.id} className="bg-white rounded-2xl border border-gray-100 shadow overflow-hidden">
              {/* Header row */}
              <div className="p-5 flex items-start justify-between gap-4">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-1 flex-wrap">
                    <span className="text-xs font-semibold text-violet-600 uppercase">{c.system}</span>
                    <span className={`text-xs px-2 py-0.5 rounded-full ${DIFF_STYLE[c.difficulty] ?? ''}`}>{c.difficulty}</span>
                    <span className="text-xs text-gray-400">{lbl('por','by')} <span className="font-medium text-gray-600">{c.author}</span></span>
                    <span className="text-xs text-gray-400">{new Date(c.created_at).toLocaleDateString()}</span>
                  </div>
                  <h2 className="font-bold text-gray-800 text-base">{c.title}</h2>
                  <p className="text-sm text-gray-500 mt-0.5">{c.summary}</p>
                </div>
                <button
                  onClick={() => setExpanded(expanded === c.id ? null : c.id)}
                  className="shrink-0 text-xs border border-gray-200 px-3 py-1.5 rounded-xl hover:border-gray-400 transition">
                  {expanded === c.id ? lbl('Cerrar','Close') : lbl('Ver caso','View case')}
                </button>
              </div>

              {/* Expanded content */}
              {expanded === c.id && (
                <div className="border-t border-gray-100 px-5 pb-5 pt-4 flex flex-col gap-4">
                  {/* Presentation */}
                  <div>
                    <div className="text-xs font-semibold text-gray-400 uppercase mb-1">{lbl('Presentación clínica','Clinical presentation')}</div>
                    <p className="text-sm text-gray-700 leading-relaxed whitespace-pre-line bg-gray-50 rounded-xl p-3">
                      {c.presentation}
                    </p>
                  </div>

                  {/* Questions */}
                  <div>
                    <div className="text-xs font-semibold text-gray-400 uppercase mb-2">
                      {lbl('Preguntas','Questions')} ({c.questions?.length})
                    </div>
                    <div className="flex flex-col gap-3">
                      {c.questions?.map((q, i) => (
                        <div key={q.id} className="bg-gray-50 rounded-xl p-3 border border-gray-100">
                          <p className="text-sm font-semibold text-gray-700 mb-2">{i+1}. {q.text}</p>
                          <div className="flex flex-col gap-1">
                            {q.options.map(o => (
                              <div key={o.id} className={`text-xs px-3 py-1.5 rounded-lg flex items-start gap-2 ${o.correct ? 'bg-green-50 text-green-800' : 'text-gray-500'}`}>
                                <span className="font-bold shrink-0">{o.id.toUpperCase()}.</span>
                                <span>{o.text}</span>
                                {o.correct && <span className="ml-auto text-green-600 font-bold">✓</span>}
                              </div>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Diagnosis */}
                  <div>
                    <div className="text-xs font-semibold text-gray-400 uppercase mb-1">{lbl('Diagnóstico','Diagnosis')}</div>
                    <p className="text-sm text-gray-700 bg-gray-50 rounded-xl p-3">{c.diagnosis}</p>
                  </div>

                  {c.pearl && (
                    <div>
                      <div className="text-xs font-semibold text-gray-400 uppercase mb-1">{lbl('Perla clínica','Clinical pearl')}</div>
                      <p className="text-sm text-gray-700 bg-blue-50 rounded-xl p-3">{c.pearl}</p>
                    </div>
                  )}

                  {/* Moderator note */}
                  <div>
                    <div className="text-xs font-semibold text-gray-400 uppercase mb-1">{lbl('Nota para el autor (opcional)','Note for the author (optional)')}</div>
                    <textarea
                      value={notes[c.id] ?? ''}
                      onChange={e => setNotes(n => ({ ...n, [c.id]: e.target.value }))}
                      placeholder={lbl('Si rechazas el caso, explica el motivo...','If rejecting, explain the reason...')}
                      rows={2}
                      className="w-full border border-gray-200 rounded-xl px-4 py-2.5 text-sm resize-none focus:outline-none focus:border-gray-400"/>
                  </div>

                  {/* Action buttons */}
                  <div className="flex gap-3">
                    <button
                      onClick={() => moderate(c.id, 'approve')}
                      disabled={busy[c.id]}
                      className="flex-1 bg-green-600 text-white py-2.5 rounded-xl text-sm font-medium hover:bg-green-700 transition disabled:opacity-40">
                      {busy[c.id] ? '...' : `✓ ${lbl('Aprobar','Approve')}`}
                    </button>
                    <button
                      onClick={() => moderate(c.id, 'reject')}
                      disabled={busy[c.id]}
                      className="flex-1 bg-red-500 text-white py-2.5 rounded-xl text-sm font-medium hover:bg-red-600 transition disabled:opacity-40">
                      {busy[c.id] ? '...' : `✕ ${lbl('Rechazar','Reject')}`}
                    </button>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
