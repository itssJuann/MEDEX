import API from '../utils/api'
import { useEffect, useState } from 'react'
import { useAuth } from '../context/AuthContext'
import { useLang } from '../context/LangContext'

const TYPE_META = {
  duda: {
    icon: '❓',
    labelEs: 'Duda',
    labelEn: 'Question',
    bg: 'bg-blue-50',
    border: 'border-blue-200',
    badge: 'bg-blue-100 text-blue-700 border-blue-200',
    ring: 'ring-blue-400',
  },
  perla: {
    icon: '💡',
    labelEs: 'Perla clínica',
    labelEn: 'Clinical pearl',
    bg: 'bg-amber-50',
    border: 'border-amber-200',
    badge: 'bg-amber-100 text-amber-700 border-amber-200',
    ring: 'ring-amber-400',
  },
  correccion: {
    icon: '✏️',
    labelEs: 'Corrección',
    labelEn: 'Correction',
    bg: 'bg-rose-50',
    border: 'border-rose-200',
    badge: 'bg-rose-100 text-rose-700 border-rose-200',
    ring: 'ring-rose-400',
  },
}

function timeAgo(iso, lang) {
  const diff = Math.floor((Date.now() - new Date(iso)) / 1000)
  if (diff < 60)   return lang === 'en' ? 'just now'          : 'ahora mismo'
  if (diff < 3600) return lang === 'en' ? `${Math.floor(diff/60)}m ago`  : `hace ${Math.floor(diff/60)} min`
  if (diff < 86400)return lang === 'en' ? `${Math.floor(diff/3600)}h ago` : `hace ${Math.floor(diff/3600)} h`
  return lang === 'en' ? `${Math.floor(diff/86400)}d ago` : `hace ${Math.floor(diff/86400)} días`
}

export default function DiscussionSection({ pathologyId }) {
  const { user, logout } = useAuth()
  const { lang } = useLang()
  const lbl = (es, en) => lang === 'en' ? en : es

  const [comments, setComments]     = useState([])
  const [filter, setFilter]         = useState(null)   // null | 'duda' | 'perla' | 'correccion'
  const [type, setType]             = useState('duda')
  const [content, setContent]       = useState('')
  const [submitting, setSubmitting] = useState(false)
  const [error, setError]           = useState(null)
  const [open, setOpen]             = useState(false)

  useEffect(() => {
    fetch(`${API}/pathologies/${pathologyId}/comments`)
      .then(r => r.json())
      .then(data => Array.isArray(data) ? setComments(data) : setComments([]))
      .catch(() => setComments([]))
  }, [pathologyId])

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!content.trim()) return
    setSubmitting(true)
    setError(null)
    const token = localStorage.getItem('medex_token')
    try {
      const r = await fetch(`${API}/pathologies/${pathologyId}/comments`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ type, content: content.trim() }),
      })
      if (r.status === 401) {
        logout()
        setError(lbl('Sesión expirada. Por favor vuelve a iniciar sesión.', 'Session expired. Please log in again.'))
        return
      }
      if (!r.ok) { const d = await r.json(); throw new Error(d.detail ?? 'Error') }
      const newComment = await r.json()
      setComments(prev => [...prev, newComment])
      setContent('')
      setOpen(false)
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  const handleDelete = async (id) => {
    const token = localStorage.getItem('medex_token')
    try {
      const r = await fetch(`${API}/comments/${id}`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${token}` },
      })
      if (r.ok) setComments(prev => prev.filter(c => c.id !== id))
    } catch {}
  }

  const visible = filter ? comments.filter(c => c.type === filter) : comments
  const count = (t) => comments.filter(c => c.type === t).length

  return (
    <div className="mt-8 bg-white rounded-2xl border border-gray-100 shadow-sm p-6">

      {/* Header */}
      <div className="flex items-center justify-between mb-5 flex-wrap gap-3">
        <div className="flex items-center gap-3">
          <h3 className="text-base font-bold text-gray-800">
            {lbl('Discusión académica', 'Academic discussion')}
          </h3>
          <span className="text-xs text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">
            {comments.length}
          </span>
        </div>

        {/* Type filter pills */}
        <div className="flex items-center gap-2 flex-wrap">
          <button
            onClick={() => setFilter(null)}
            className={`px-3 py-1 rounded-full text-xs font-medium border transition
              ${!filter ? 'bg-gray-800 text-white border-gray-800' : 'bg-white text-gray-500 border-gray-200 hover:border-gray-400'}`}>
            {lbl('Todos', 'All')} {comments.length > 0 && `(${comments.length})`}
          </button>
          {Object.entries(TYPE_META).map(([key, m]) => (
            <button key={key} onClick={() => setFilter(filter === key ? null : key)}
              className={`px-3 py-1 rounded-full text-xs font-medium border transition flex items-center gap-1
                ${filter === key ? `${m.badge} border` : 'bg-white text-gray-500 border-gray-200 hover:border-gray-400'}`}>
              <span>{m.icon}</span>
              <span>{lang === 'en' ? m.labelEn : m.labelEs}</span>
              {count(key) > 0 && <span className="opacity-70">({count(key)})</span>}
            </button>
          ))}
        </div>
      </div>

      {/* Comment list */}
      {visible.length === 0 ? (
        <div className="text-center py-10 text-gray-400 text-sm">
          {filter
            ? lbl('No hay comentarios de este tipo aún.', 'No comments of this type yet.')
            : lbl('Sé el primero en comentar.', 'Be the first to comment.')}
        </div>
      ) : (
        <div className="flex flex-col gap-3 mb-5">
          {visible.map(c => {
            const m = TYPE_META[c.type]
            const isOwn = user?.email && c.user_id === user?.id
            return (
              <div key={c.id}
                className={`rounded-xl border p-4 ${m.bg} ${m.border}`}>
                <div className="flex items-start justify-between gap-3">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className={`text-xs font-semibold px-2 py-0.5 rounded-full border ${m.badge} flex items-center gap-1`}>
                      <span>{m.icon}</span>
                      <span>{lang === 'en' ? m.labelEn : m.labelEs}</span>
                    </span>
                    <span className="text-xs font-semibold text-gray-700">{c.user_name}</span>
                    <span className="text-xs text-gray-400">{timeAgo(c.created_at, lang)}</span>
                  </div>
                  {isOwn && (
                    <button
                      onClick={() => handleDelete(c.id)}
                      className="text-gray-300 hover:text-red-400 transition text-xs shrink-0"
                      title={lbl('Eliminar', 'Delete')}>
                      ✕
                    </button>
                  )}
                </div>
                <p className="mt-2 text-sm text-gray-700 leading-relaxed whitespace-pre-line">
                  {c.content}
                </p>
              </div>
            )
          })}
        </div>
      )}

      {/* New comment form */}
      {user ? (
        !open ? (
          <button
            onClick={() => setOpen(true)}
            className="w-full py-2.5 rounded-xl border border-dashed border-gray-300 text-sm text-gray-400
              hover:border-primary hover:text-primary transition">
            + {lbl('Agregar comentario académico', 'Add academic comment')}
          </button>
        ) : (
          <form onSubmit={handleSubmit} className="border border-gray-200 rounded-xl p-4 bg-gray-50">
            {/* Type selector */}
            <div className="flex gap-2 mb-3 flex-wrap">
              {Object.entries(TYPE_META).map(([key, m]) => (
                <button key={key} type="button" onClick={() => setType(key)}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-medium transition
                    ${type === key ? `${m.badge} border ring-2 ${m.ring} ring-offset-1` : 'bg-white text-gray-500 border-gray-200 hover:border-gray-400'}`}>
                  <span>{m.icon}</span>
                  <span>{lang === 'en' ? m.labelEn : m.labelEs}</span>
                </button>
              ))}
            </div>

            {/* Placeholder hints per type */}
            <textarea
              value={content}
              onChange={e => setContent(e.target.value)}
              rows={3}
              maxLength={1000}
              placeholder={
                type === 'duda'
                  ? lbl('Escribe tu duda sobre este caso...', 'Write your question about this case...')
                  : type === 'perla'
                  ? lbl('Comparte una perla clínica relevante...', 'Share a relevant clinical pearl...')
                  : lbl('Propón una corrección razonada con evidencia...', 'Propose a reasoned correction with evidence...')
              }
              className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-700 resize-none
                focus:outline-none focus:border-primary bg-white"
            />
            <div className="flex items-center justify-between mt-3 gap-3">
              <span className="text-xs text-gray-400">{content.length}/1000</span>
              {error && <span className="text-xs text-red-500 flex-1 text-center">{error}</span>}
              <div className="flex gap-2">
                <button type="button" onClick={() => { setOpen(false); setContent(''); setError(null) }}
                  className="px-4 py-2 rounded-xl text-xs text-gray-500 hover:bg-gray-200 transition">
                  {lbl('Cancelar', 'Cancel')}
                </button>
                <button type="submit" disabled={submitting || !content.trim()}
                  className="px-5 py-2 rounded-xl bg-primary text-white text-xs font-medium hover:bg-blue-900 transition disabled:opacity-40">
                  {submitting ? lbl('Enviando...', 'Sending...') : lbl('Publicar', 'Post')}
                </button>
              </div>
            </div>
          </form>
        )
      ) : (
        <p className="text-center text-xs text-gray-400 py-3">
          {lbl('Inicia sesión para participar en la discusión.', 'Log in to join the discussion.')}
        </p>
      )}
    </div>
  )
}
