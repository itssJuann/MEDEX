import API from '../utils/api'
import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useLang } from '../context/LangContext'
import Logo from '../components/Logo'

export default function Login() {
  const { login } = useAuth()
  const { t } = useLang()
  const navigate = useNavigate()
  const [form, setForm]     = useState({ email: '', password: '' })
  const [error, setError]   = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      const res = await fetch(`${API}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail || 'Error')
      login(data)
      navigate('/')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="bg-white rounded-2xl shadow p-8 w-full max-w-md border border-gray-100">
        <div className="flex flex-col items-center mb-8">
          <Logo size={48} showText={true} textColor="text-primary" variant="light" />
          <p className="text-gray-500 text-sm mt-3">{t.loginSubtitle}</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">{t.emailLabel}</label>
            <input type="email" required value={form.email}
              onChange={e => setForm(f => ({ ...f, email: e.target.value }))}
              className="w-full border border-gray-300 rounded-xl px-4 py-2.5 text-sm outline-none focus:border-primary transition"
              placeholder="tu@correo.com"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">{t.passwordLabel}</label>
            <input type="password" required value={form.password}
              onChange={e => setForm(f => ({ ...f, password: e.target.value }))}
              className="w-full border border-gray-300 rounded-xl px-4 py-2.5 text-sm outline-none focus:border-primary transition"
              placeholder="••••••••"
            />
          </div>
          {error && <div className="bg-red-50 border border-red-200 text-red-700 text-sm rounded-xl px-4 py-3">{error}</div>}
          <button type="submit" disabled={loading}
            className="w-full bg-primary text-white py-2.5 rounded-xl font-medium text-sm hover:bg-blue-900 transition disabled:opacity-60">
            {loading ? t.loggingIn : t.loginBtn}
          </button>
        </form>

        <p className="text-center text-sm text-gray-500 mt-6">
          {t.noAccount}{' '}
          <Link to="/register" className="text-primary font-medium hover:underline">{t.register}</Link>
        </p>
      </div>
    </div>
  )
}
