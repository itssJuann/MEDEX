import API from '../utils/api'
import { useState, useEffect } from 'react'
import { useAuth } from '../context/AuthContext'
import { useLang } from '../context/LangContext'
import { Link } from 'react-router-dom'

function Section({ title, children }) {
  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 mb-5">
      <h2 className="text-sm font-bold text-gray-500 uppercase tracking-wide mb-5">{title}</h2>
      {children}
    </div>
  )
}

export default function Settings() {
  const { user, login } = useAuth()
  const { lang, changeLang, t } = useLang()

  const [name, setName]               = useState(user?.name || '')
  const [profileMsg, setProfileMsg]   = useState('')
  const [profileErr, setProfileErr]   = useState('')
  const [profileLoading, setProfileLoading] = useState(false)

  const [adminCode, setAdminCode]     = useState('')
  const [adminMsg, setAdminMsg]       = useState('')
  const [adminErr, setAdminErr]       = useState('')
  const [adminLoading, setAdminLoading] = useState(false)

  const [curPwd, setCurPwd]           = useState('')
  const [newPwd, setNewPwd]           = useState('')
  const [pwdMsg, setPwdMsg]           = useState('')
  const [pwdErr, setPwdErr]           = useState('')
  const [pwdLoading, setPwdLoading]   = useState(false)

  const [progress, setProgress]       = useState([])

  useEffect(() => {
    const token = localStorage.getItem('medex_token')
    if (!token) return
    fetch(`${API}/progress`, {
      headers: { Authorization: `Bearer ${token}` }
    }).then(r => r.json()).then(setProgress).catch(() => {})
  }, [])

  const saveProfile = async (e) => {
    e.preventDefault()
    setProfileMsg(''); setProfileErr('')
    setProfileLoading(true)
    try {
      const token = localStorage.getItem('medex_token')
      const res = await fetch(`${API}/me`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ name }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail)
      login({ ...user, name: data.name })
      setProfileMsg(t.saved)
    } catch (err) {
      setProfileErr(err.message)
    } finally {
      setProfileLoading(false)
    }
  }

  const savePassword = async (e) => {
    e.preventDefault()
    setPwdMsg(''); setPwdErr('')
    setPwdLoading(true)
    try {
      const token = localStorage.getItem('medex_token')
      const res = await fetch(`${API}/me/password`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ current_password: curPwd, new_password: newPwd }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail)
      setCurPwd(''); setNewPwd('')
      setPwdMsg(t.passwordUpdated)
    } catch (err) {
      setPwdErr(err.message)
    } finally {
      setPwdLoading(false)
    }
  }

  const claimAdmin = async (e) => {
    e.preventDefault()
    setAdminMsg(''); setAdminErr('')
    setAdminLoading(true)
    try {
      const token = localStorage.getItem('medex_token')
      const res = await fetch(`${API}/admin/claim`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ code: adminCode }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail)
      login({ ...user, is_admin: true })
      setAdminMsg(lang === 'en' ? '✓ You are now an administrator.' : '✓ Ahora eres administrador.')
      setAdminCode('')
    } catch (err) {
      setAdminErr(err.message)
    } finally {
      setAdminLoading(false)
    }
  }

  const totalAttempts = progress.reduce((s, r) => s + r.attempts, 0)
  const countSuccess  = progress.filter(r => r.best_result === 'success').length
  const countWarning  = progress.filter(r => r.best_result === 'warning').length
  const countFailure  = progress.filter(r => r.best_result === 'failure').length

  return (
    <div className="min-h-screen bg-gray-50 px-6 py-10 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold text-primary mb-7">{t.settingsTitle}</h1>

      {/* Perfil */}
      <Section title={t.profile}>
        <form onSubmit={saveProfile} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">{t.name}</label>
            <input
              type="text"
              required
              value={name}
              onChange={e => { setName(e.target.value); setProfileMsg('') }}
              className="w-full border border-gray-300 rounded-xl px-4 py-2.5 text-sm outline-none focus:border-primary transition"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">{t.email}</label>
            <input
              type="email"
              value={user?.email || ''}
              disabled
              className="w-full border border-gray-200 rounded-xl px-4 py-2.5 text-sm bg-gray-50 text-gray-400 cursor-not-allowed"
            />
          </div>
          {profileMsg && <p className="text-green-600 text-sm">{profileMsg}</p>}
          {profileErr && <p className="text-red-500 text-sm">{profileErr}</p>}
          <button
            type="submit"
            disabled={profileLoading}
            className="bg-primary text-white px-6 py-2.5 rounded-xl text-sm font-medium hover:bg-blue-900 transition disabled:opacity-60"
          >
            {profileLoading ? t.saving : t.saveChanges}
          </button>
        </form>
      </Section>

      {/* Contraseña */}
      <Section title={t.changePassword}>
        <form onSubmit={savePassword} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">{t.currentPassword}</label>
            <input
              type="password"
              required
              value={curPwd}
              onChange={e => { setCurPwd(e.target.value); setPwdMsg('') }}
              className="w-full border border-gray-300 rounded-xl px-4 py-2.5 text-sm outline-none focus:border-primary transition"
              placeholder="••••••••"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">{t.newPassword}</label>
            <input
              type="password"
              required
              value={newPwd}
              onChange={e => { setNewPwd(e.target.value); setPwdMsg('') }}
              className="w-full border border-gray-300 rounded-xl px-4 py-2.5 text-sm outline-none focus:border-primary transition"
              placeholder={lang === 'en' ? 'Minimum 6 characters' : 'Mínimo 6 caracteres'}
            />
          </div>
          {pwdMsg && <p className="text-green-600 text-sm">{pwdMsg}</p>}
          {pwdErr && <p className="text-red-500 text-sm">{pwdErr}</p>}
          <button
            type="submit"
            disabled={pwdLoading}
            className="bg-primary text-white px-6 py-2.5 rounded-xl text-sm font-medium hover:bg-blue-900 transition disabled:opacity-60"
          >
            {pwdLoading ? t.saving : t.updatePassword}
          </button>
        </form>
      </Section>

      {/* Idioma */}
      <Section title={t.language}>
        <p className="text-sm text-gray-500 mb-4">{t.chooseLanguage}</p>
        <div className="flex gap-3">
          {[
            { code: 'es', label: '🇪🇸 Español' },
            { code: 'en', label: '🇬🇧 English' },
          ].map(l => (
            <button
              key={l.code}
              onClick={() => changeLang(l.code)}
              className={`px-5 py-2.5 rounded-xl text-sm font-medium border transition ${
                lang === l.code
                  ? 'bg-primary text-white border-primary'
                  : 'bg-white text-gray-600 border-gray-300 hover:border-primary'
              }`}
            >
              {l.label}
            </button>
          ))}
        </div>
      </Section>

      {/* Administrador */}
      <Section title={lang === 'en' ? 'Administrator / Moderator' : 'Administrador / Moderador'}>
        {user?.is_admin ? (
          <div className="flex flex-col gap-3">
            <div className="flex items-center gap-3 bg-green-50 border border-green-200 rounded-xl px-4 py-3">
              <span className="text-green-600 text-xl">🛡️</span>
              <div>
                <p className="text-sm font-semibold text-green-700">
                  {lang === 'en' ? 'You have administrator privileges' : 'Tienes privilegios de administrador'}
                </p>
                <p className="text-xs text-green-600 mt-0.5">
                  {lang === 'en' ? 'You can moderate community cases.' : 'Puedes moderar los casos de la comunidad.'}
                </p>
              </div>
            </div>
            <Link to="/community/moderate"
              className="inline-flex items-center gap-2 text-sm text-violet-700 font-medium hover:underline">
              → {lang === 'en' ? 'Go to moderation panel' : 'Ir al panel de moderación'}
            </Link>
          </div>
        ) : (
          <form onSubmit={claimAdmin} className="space-y-4">
            <p className="text-sm text-gray-500">
              {lang === 'en'
                ? 'Enter the administrator code provided by your educator to unlock moderation features.'
                : 'Introduce el código de administrador proporcionado por tu docente para desbloquear las funciones de moderación.'}
            </p>
            <div className="flex gap-3">
              <input
                type="password"
                value={adminCode}
                onChange={e => { setAdminCode(e.target.value); setAdminMsg(''); setAdminErr('') }}
                placeholder={lang === 'en' ? 'Administrator code' : 'Código de administrador'}
                className="flex-1 border border-gray-300 rounded-xl px-4 py-2.5 text-sm outline-none focus:border-primary transition"
              />
              <button
                type="submit"
                disabled={adminLoading || !adminCode.trim()}
                className="bg-primary text-white px-5 py-2.5 rounded-xl text-sm font-medium hover:bg-blue-900 transition disabled:opacity-50">
                {adminLoading ? '...' : (lang === 'en' ? 'Apply' : 'Aplicar')}
              </button>
            </div>
            {adminMsg && <p className="text-green-600 text-sm">{adminMsg}</p>}
            {adminErr && <p className="text-red-500 text-sm">{adminErr}</p>}
          </form>
        )}
      </Section>

      {/* Estadísticas */}
      <Section title={t.stats}>
        {progress.length === 0 ? (
          <p className="text-sm text-gray-400">{t.notPlayed}</p>
        ) : (
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            {[
              { label: t.casesCompleted, value: countSuccess,  color: 'text-green-600' },
              { label: t.casesWarning,   value: countWarning,  color: 'text-yellow-600' },
              { label: t.casesFailed,    value: countFailure,  color: 'text-red-500' },
              { label: t.totalAttempts,  value: totalAttempts, color: 'text-primary' },
            ].map(stat => (
              <div key={stat.label} className="bg-gray-50 rounded-xl p-4 text-center border border-gray-100">
                <div className={`text-3xl font-bold ${stat.color}`}>{stat.value}</div>
                <div className="text-xs text-gray-500 mt-1">{stat.label}</div>
              </div>
            ))}
          </div>
        )}
      </Section>
    </div>
  )
}
