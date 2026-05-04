import { useState, useRef, useEffect } from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useLang } from '../context/LangContext'
import Logo from './Logo'

const NAV_LINKS = [
  { to: '/cases',          labelKey: 'cases',        icon: '🏥' },
  { to: '/differentials',  labelKey: 'differentials', icon: '🔍' },
  { to: '/algorithms',     labelKey: 'algorithms',    icon: '⚙️' },
  { to: '/clinical-images',labelKey: 'images',        icon: '🫁' },
  { to: '/anatomy',        labelKey: 'anatomy',       icon: '🫀' },
  { to: '/quizzes',        labelKey: 'quizzes',       icon: '🧠' },
  { to: '/community',      labelKey: 'community',     icon: '🤝' },
  { to: '/settings',       labelKey: 'settings',      icon: '⚙️' },
]

const LABELS = {
  cases:         { es: 'Casos',          en: 'Cases' },
  differentials: { es: 'Diferenciales',  en: 'Differentials' },
  algorithms:    { es: 'Algoritmos',     en: 'Algorithms' },
  images:        { es: 'Imágenes',       en: 'Images' },
  anatomy:       { es: 'Anatomía',       en: 'Anatomy' },
  quizzes:       { es: 'Quizzes',        en: 'Quizzes' },
  community:     { es: 'Comunidad',      en: 'Community' },
  settings:      { es: 'Configuración',  en: 'Settings' },
}

export default function Navbar() {
  const { user, logout } = useAuth()
  const { lang, t } = useLang()
  const navigate  = useNavigate()
  const location  = useLocation()
  const [open, setOpen] = useState(false)
  const menuRef = useRef(null)

  const lbl = (key) => lang === 'en' ? LABELS[key].en : LABELS[key].es

  const handleLogout = () => {
    logout()
    navigate('/login')
  }

  // Close menu on route change
  useEffect(() => { setOpen(false) }, [location.pathname])

  // Close menu on outside click
  useEffect(() => {
    const handler = (e) => { if (menuRef.current && !menuRef.current.contains(e.target)) setOpen(false) }
    document.addEventListener('mousedown', handler)
    return () => document.removeEventListener('mousedown', handler)
  }, [])

  const isActive = (to) => location.pathname === to || location.pathname.startsWith(to + '/')

  return (
    <nav className="bg-primary text-white shadow-md sticky top-0 z-50">
      <div className="px-6 py-3 flex items-center justify-between max-w-7xl mx-auto">

        {/* Logo */}
        <Link to="/" className="flex-shrink-0">
          <Logo size={32} />
        </Link>

        {/* Desktop links */}
        <div className="hidden lg:flex items-center gap-1 flex-1 justify-center">
          {NAV_LINKS.map(({ to, labelKey }) => (
            <Link key={to} to={to}
              className={`px-3 py-1.5 rounded-lg text-sm font-medium transition
                ${isActive(to)
                  ? 'bg-white/20 text-white'
                  : 'text-blue-200 hover:text-white hover:bg-white/10'}`}>
              {lbl(labelKey)}
            </Link>
          ))}
        </div>

        {/* Right side */}
        <div className="flex items-center gap-3 flex-shrink-0">
          {/* Greeting (desktop) */}
          <span className="hidden md:block text-sm text-blue-200">
            {t.hello}, <span className="font-semibold text-white">{user?.name?.split(' ')[0]}</span>
          </span>

          {/* Logout (desktop) */}
          <button onClick={handleLogout}
            className="hidden md:block text-sm border border-blue-400 px-4 py-1.5 rounded-full hover:bg-blue-800 transition">
            {t.logout}
          </button>

          {/* Hamburger (mobile/tablet) */}
          <button
            ref={menuRef}
            onClick={() => setOpen(v => !v)}
            className="lg:hidden flex flex-col gap-1.5 p-2 rounded-lg hover:bg-white/10 transition"
            aria-label="Menu"
          >
            <span className={`block w-5 h-0.5 bg-white transition-all duration-200 ${open ? 'rotate-45 translate-y-2' : ''}`}/>
            <span className={`block w-5 h-0.5 bg-white transition-all duration-200 ${open ? 'opacity-0' : ''}`}/>
            <span className={`block w-5 h-0.5 bg-white transition-all duration-200 ${open ? '-rotate-45 -translate-y-2' : ''}`}/>
          </button>
        </div>
      </div>

      {/* Mobile dropdown */}
      {open && (
        <div className="lg:hidden border-t border-white/10 bg-[#0d3d6e] px-4 py-3 flex flex-col gap-1">
          {/* Greeting */}
          <p className="text-xs text-blue-300 mb-2 px-2">
            {t.hello}, <span className="font-semibold text-white">{user?.name?.split(' ')[0]}</span>
          </p>

          {NAV_LINKS.map(({ to, labelKey, icon }) => (
            <Link key={to} to={to}
              className={`flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition
                ${isActive(to)
                  ? 'bg-white/20 text-white'
                  : 'text-blue-200 hover:bg-white/10 hover:text-white'}`}>
              <span className="text-base leading-none">{icon}</span>
              {lbl(labelKey)}
            </Link>
          ))}

          <div className="border-t border-white/10 mt-2 pt-2">
            <button onClick={handleLogout}
              className="w-full text-left flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm text-blue-200 hover:bg-white/10 hover:text-white transition">
              <span>🚪</span> {t.logout}
            </button>
          </div>
        </div>
      )}
    </nav>
  )
}
