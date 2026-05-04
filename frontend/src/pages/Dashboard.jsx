import API from '../utils/api'
import { useEffect, useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useLang } from '../context/LangContext'
import { groupProgress, computeAchievements } from '../utils/achievements'
import { getAllProgress } from '../utils/progress'

const ICONS = {
  cases: (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10">
      <rect x="8" y="6" width="32" height="36" rx="4" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.4)" strokeWidth="1.5"/>
      <rect x="19" y="2" width="10" height="8" rx="2" fill="rgba(255,255,255,0.3)"/>
      <line x1="16" y1="18" x2="32" y2="18" stroke="white" strokeWidth="2" strokeLinecap="round"/>
      <line x1="16" y1="24" x2="28" y2="24" stroke="rgba(255,255,255,0.6)" strokeWidth="2" strokeLinecap="round"/>
      <line x1="16" y1="30" x2="26" y2="30" stroke="rgba(255,255,255,0.6)" strokeWidth="2" strokeLinecap="round"/>
      <circle cx="36" cy="36" r="8" fill="#00b4d8"/>
      <path d="M33 36h6M36 33v6" stroke="white" strokeWidth="2" strokeLinecap="round"/>
    </svg>
  ),
  differentials: (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10">
      <circle cx="24" cy="24" r="16" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.4)" strokeWidth="1.5"/>
      <path d="M24 14v10l6 6" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
      <circle cx="24" cy="24" r="2" fill="#00b4d8"/>
      <path d="M14 8l2 4M34 8l-2 4M8 20l4 1M40 20l-4 1" stroke="rgba(255,255,255,0.4)" strokeWidth="1.5" strokeLinecap="round"/>
    </svg>
  ),
  images: (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10">
      <rect x="6" y="10" width="36" height="28" rx="3" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.3)" strokeWidth="1.5"/>
      <circle cx="18" cy="22" r="5" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.5)" strokeWidth="1.5"/>
      <path d="M22 26l8 8" stroke="rgba(255,255,255,0.5)" strokeWidth="2.5" strokeLinecap="round"/>
      <path d="M28 18h6M28 22h4" stroke="rgba(255,255,255,0.4)" strokeWidth="1.5" strokeLinecap="round"/>
    </svg>
  ),
  algorithms: (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10">
      <rect x="16" y="6" width="16" height="10" rx="3" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.5)" strokeWidth="1.5"/>
      <rect x="4" y="32" width="16" height="10" rx="3" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.3)" strokeWidth="1.5"/>
      <rect x="28" y="32" width="16" height="10" rx="3" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.3)" strokeWidth="1.5"/>
      <path d="M24 16v8M24 24l-12 8M24 24l12 8" stroke="rgba(255,255,255,0.5)" strokeWidth="1.5" strokeLinecap="round"/>
    </svg>
  ),
  quizzes: (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10">
      <rect x="6" y="8" width="36" height="32" rx="5" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.4)" strokeWidth="1.5"/>
      <circle cx="16" cy="18" r="4" fill="rgba(255,255,255,0.3)" stroke="rgba(255,255,255,0.6)" strokeWidth="1.2"/>
      <text x="16" y="22" textAnchor="middle" fill="white" fontSize="6" fontWeight="bold" fontFamily="sans-serif">?</text>
      <line x1="24" y1="16" x2="38" y2="16" stroke="rgba(255,255,255,0.5)" strokeWidth="2" strokeLinecap="round"/>
      <line x1="24" y1="20" x2="34" y2="20" stroke="rgba(255,255,255,0.3)" strokeWidth="1.5" strokeLinecap="round"/>
      <circle cx="16" cy="30" r="4" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.5)" strokeWidth="1.2"/>
      <line x1="14" y1="28" x2="18" y2="32" stroke="white" strokeWidth="1.5" strokeLinecap="round"/>
      <line x1="18" y1="28" x2="14" y2="32" stroke="white" strokeWidth="1.5" strokeLinecap="round"/>
      <line x1="24" y1="28" x2="38" y2="28" stroke="rgba(255,255,255,0.5)" strokeWidth="2" strokeLinecap="round"/>
      <line x1="24" y1="32" x2="34" y2="32" stroke="rgba(255,255,255,0.3)" strokeWidth="1.5" strokeLinecap="round"/>
    </svg>
  ),
  anatomy: (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10">
      <ellipse cx="24" cy="10" rx="9" ry="10" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.5)" strokeWidth="1.5"/>
      <rect x="20" y="19" width="8" height="6" rx="2" fill="rgba(255,255,255,0.15)"/>
      <path d="M12 25 Q8 30 8 38 Q8 44 12 46 L14 44 Q11 42 11 38 Q11 32 14 28 Z" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.4)" strokeWidth="1"/>
      <path d="M36 25 Q40 30 40 38 Q40 44 36 46 L34 44 Q37 42 37 38 Q37 32 34 28 Z" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.4)" strokeWidth="1"/>
      <path d="M14 25 Q10 28 10 32 L13 32 Q13 30 15 28 Z" fill="rgba(255,255,255,0.15)"/>
      <path d="M34 25 Q38 28 38 32 L35 32 Q35 30 33 28 Z" fill="rgba(255,255,255,0.15)"/>
      <rect x="19" y="25" width="10" height="16" rx="3" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.4)" strokeWidth="1.2"/>
      <path d="M19 34 Q15 36 14 42 L16 43 Q17 38 20 36 Z" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.3)" strokeWidth="1"/>
      <path d="M29 34 Q33 36 34 42 L32 43 Q31 38 28 36 Z" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.3)" strokeWidth="1"/>
      <circle cx="24" cy="29" r="2" fill="rgba(255,255,255,0.4)"/>
    </svg>
  ),
  community: (
    <svg viewBox="0 0 48 48" fill="none" className="w-10 h-10">
      {/* Three people silhouettes */}
      <circle cx="24" cy="12" r="7" fill="rgba(255,255,255,0.25)" stroke="rgba(255,255,255,0.6)" strokeWidth="1.5"/>
      <path d="M14 34 Q14 26 24 26 Q34 26 34 34" stroke="rgba(255,255,255,0.6)" strokeWidth="2" fill="rgba(255,255,255,0.15)" strokeLinecap="round"/>
      <circle cx="10" cy="18" r="5" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.4)" strokeWidth="1.2"/>
      <path d="M2 36 Q2 30 10 30 Q15 30 17 33" stroke="rgba(255,255,255,0.35)" strokeWidth="1.5" fill="none" strokeLinecap="round"/>
      <circle cx="38" cy="18" r="5" fill="rgba(255,255,255,0.15)" stroke="rgba(255,255,255,0.4)" strokeWidth="1.2"/>
      <path d="M46 36 Q46 30 38 30 Q33 30 31 33" stroke="rgba(255,255,255,0.35)" strokeWidth="1.5" fill="none" strokeLinecap="round"/>
      {/* Small plus badge */}
      <circle cx="38" cy="10" r="6" fill="rgba(255,255,255,0.3)"/>
      <path d="M35 10h6M38 7v6" stroke="white" strokeWidth="1.8" strokeLinecap="round"/>
    </svg>
  ),
}

export default function Dashboard() {
  const { user } = useAuth()
  const { t, lang } = useLang()
  const location = useLocation()
  const [rawProgress, setRawProgress] = useState([])
  const [counts, setCounts] = useState({ cases: 0, differentials: 0, algorithms: 0, images: 0, quizzes: 6, community: 0 })

  const fetchProgress = () => {
    setRawProgress(getAllProgress())
  }

  // Re-fetch progress every time the user navigates to this page
  useEffect(() => {
    fetchProgress()
  }, [location.key])

  useEffect(() => {
    Promise.all([
      fetch(`${API}/pathologies`).then(r => r.json()),
      fetch(`${API}/differentials`).then(r => r.json()),
      fetch(`${API}/algorithms`).then(r => r.json()),
      fetch(`${API}/clinical-images`).then(r => r.json()),
      fetch(`${API}/community-cases`).then(r => r.json()),
    ]).then(([paths, diffs, algos, imgs, comm]) => setCounts(c => ({
      ...c, cases: paths.length, differentials: diffs.length,
      algorithms: algos.length, images: imgs.length,
      community: Array.isArray(comm) ? comm.length : 0,
    }))).catch(() => {})
  }, []) // totals only need to load once

  // Re-fetch progress when tab/window regains focus (usuario vuelve de otro módulo)
  useEffect(() => {
    const onFocus = () => fetchProgress()
    window.addEventListener('focus', onFocus)
    return () => window.removeEventListener('focus', onFocus)
  }, [])

  // Built inside component so they use t (translated)
  const MODULES = [
    {
      id: 'cases', title: t.modCasesTitle, subtitle: t.modCasesSubtitle,
      description: t.modCasesDesc, gradient: 'from-[#0f4c81] to-[#1565a8]',
      accent: '#00b4d8', link: '/cases', available: true,
    },
    {
      id: 'differentials', title: t.modDiffTitle, subtitle: t.modDiffSubtitle,
      description: t.modDiffDesc, gradient: 'from-[#0e7490] to-[#0891b2]',
      accent: '#67e8f9', link: '/differentials', available: true,
    },
    {
      id: 'images', title: t.modImgTitle, subtitle: t.modImgSubtitle,
      description: t.modImgDesc, gradient: 'from-[#5b21b6] to-[#7c3aed]',
      accent: '#c4b5fd', link: '/clinical-images', available: true,
    },
    {
      id: 'algorithms', title: t.modAlgoTitle, subtitle: t.modAlgoSubtitle,
      description: t.modAlgoDesc, gradient: 'from-[#065f46] to-[#059669]',
      accent: '#6ee7b7', link: '/algorithms', available: true,
    },
    {
      id: 'anatomy', title: t.modAnatTitle, subtitle: t.modAnatSubtitle,
      description: t.modAnatDesc, gradient: 'from-[#374151] to-[#1f2937]',
      accent: '#9ca3af', link: '/anatomy', available: true,
    },
    {
      id: 'quizzes', title: t.modQuizTitle, subtitle: t.modQuizSubtitle,
      description: t.modQuizDesc, gradient: 'from-[#1e1b4b] to-[#312e81]',
      accent: '#a5b4fc', link: '/quizzes', available: true,
    },
    {
      id: 'community', title: t.modCommunityTitle, subtitle: t.modCommunitySubtitle,
      description: t.modCommunityDesc, gradient: 'from-[#9d174d] to-[#db2777]',
      accent: '#fbcfe8', link: '/community', available: true,
    },
  ]

  const grouped      = groupProgress(rawProgress)
  const totals       = { cases: counts.cases, differentials: counts.differentials, algorithms: counts.algorithms, images: counts.images, quizzes: counts.quizzes }
  const achievements = computeAchievements(grouped, totals)
  const unlocked     = achievements.filter(a => a.unlocked)

  const successCount  = rawProgress.filter(p => p.best_result === 'success').length
  const totalAttempts = rawProgress.reduce((s, p) => s + (p.attempts ?? 1), 0)
  const firstName     = user?.name?.split(' ')[0] || (lang === 'en' ? 'student' : 'estudiante')
  const lbl           = (es, en) => lang === 'en' ? en : es

  const MODULE_BARS = [
    { key: 'case',         label: lbl('Casos',          'Cases'),          total: counts.cases,         done: grouped.case?.length ?? 0,         color: '#0f4c81', link: '/cases' },
    { key: 'differential', label: lbl('Diferenciales',  'Differentials'),  total: counts.differentials, done: grouped.differential?.length ?? 0, color: '#0e7490', link: '/differentials' },
    { key: 'algorithm',    label: lbl('Algoritmos',     'Algorithms'),     total: counts.algorithms,    done: grouped.algorithm?.length ?? 0,    color: '#059669', link: '/algorithms' },
    { key: 'image',        label: lbl('Imágenes',       'Images'),         total: counts.images,        done: grouped.image?.length ?? 0,        color: '#7c3aed', link: '/clinical-images' },
    { key: 'quiz',         label: lbl('Quizzes',        'Quizzes'),        total: counts.quizzes,       done: grouped.quiz?.length ?? 0,         color: '#312e81', link: '/quizzes' },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      <style>{`
        @keyframes fadeUp { from { opacity:0; transform:translateY(24px); } to { opacity:1; transform:translateY(0); } }
        @keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
        @keyframes float  { 0%,100% { transform:translateY(0px) rotate(0deg); } 50% { transform:translateY(-10px) rotate(1deg); } }
        @keyframes pulse-ring {
          0%   { transform:scale(0.95); box-shadow:0 0 0 0 rgba(0,180,216,0.4); }
          70%  { transform:scale(1);    box-shadow:0 0 0 14px rgba(0,180,216,0); }
          100% { transform:scale(0.95); box-shadow:0 0 0 0 rgba(0,180,216,0); }
        }
        .anim-fadeup { animation: fadeUp 0.5s ease both; }
        .anim-fadein { animation: fadeIn 0.4s ease both; }
        .card-float:hover .card-icon { animation: float 2.5s ease-in-out infinite; }
        .module-card { transition: transform 0.25s ease, box-shadow 0.25s ease; }
        .module-card:hover { transform: translateY(-6px) scale(1.02); box-shadow: 0 20px 40px rgba(0,0,0,0.18); }
        .module-card.disabled { filter: saturate(0.4); cursor: not-allowed; }
        .module-card.disabled:hover { transform: none; box-shadow: none; }
      `}</style>

      {/* Hero */}
      <div className="bg-gradient-to-br from-[#0a3660] via-[#0f4c81] to-[#1565a8] text-white px-8 py-14 relative overflow-hidden">
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-10 -right-10 w-64 h-64 rounded-full bg-white opacity-5"/>
          <div className="absolute bottom-0 -left-16 w-80 h-80 rounded-full bg-accent opacity-5"/>
        </div>
        <div className="max-w-5xl mx-auto relative">
          <div className="anim-fadein">
            <p className="text-accent text-sm font-semibold uppercase tracking-widest mb-2">{t.dashboardBadge}</p>
            <h1 className="text-4xl sm:text-5xl font-bold mb-2">{t.hello}, {firstName} 👋</h1>
            <p className="text-blue-200 text-lg">{t.dashboardSubtitle}</p>
          </div>
          {totalAttempts > 0 && (
            <div className="mt-8 flex gap-6 flex-wrap anim-fadeup" style={{ animationDelay: '150ms' }}>
              {[
                { value: successCount,  label: t.casesCompleted },
                { value: totalAttempts, label: t.totalAttempts },
                { value: counts.cases + counts.differentials + counts.algorithms + (counts.images ?? 0), label: t.totalAvailable },
              ].map(stat => (
                <div key={stat.label} className="bg-white/10 backdrop-blur rounded-2xl px-5 py-3 border border-white/20">
                  <div className="text-2xl font-bold">{stat.value}</div>
                  <div className="text-blue-200 text-xs">{stat.label}</div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Módulos */}
      <div className="max-w-5xl mx-auto px-6 py-12">
        <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-8">{t.modulesTitle}</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {MODULES.map((mod, i) => {
            const card = (
              <div
                className={`module-card card-float rounded-3xl bg-gradient-to-br ${mod.gradient} text-white p-7 shadow-lg relative overflow-hidden ${!mod.available ? 'disabled opacity-70' : ''}`}
              >
                <div className="absolute -bottom-6 -right-6 w-32 h-32 rounded-full bg-white opacity-5"/>
                <div className="absolute top-0 right-0 w-20 h-20 rounded-full bg-white opacity-5 -translate-y-4 translate-x-4"/>

                {!mod.available && (
                  <span className="absolute top-4 right-4 text-xs bg-white/20 backdrop-blur px-3 py-1 rounded-full font-medium">
                    {t.comingSoon}
                  </span>
                )}

                <div className="card-icon mb-5 w-fit">{ICONS[mod.id]}</div>

                <div className="text-xs font-semibold uppercase tracking-widest mb-1" style={{ color: mod.accent }}>
                  {mod.subtitle}
                </div>
                <h3 className="text-2xl font-bold mb-2">{mod.title}</h3>
                <p className="text-white/70 text-sm leading-relaxed mb-6">{mod.description}</p>

                <div className="flex items-center justify-between">
                  {mod.available ? (
                    <>
                      <span className="text-xs font-medium bg-white/15 px-3 py-1.5 rounded-full">
                        {mod.id === 'cases'         ? `${counts.cases} ${t.pathologies}`
                         : mod.id === 'differentials' ? `${counts.differentials} ${t.casesWord}`
                         : mod.id === 'algorithms'    ? `${counts.algorithms} ${t.algorithmsWord}`
                         : mod.id === 'images'        ? `${counts.images ?? 0} ${lang === 'en' ? 'cases' : 'casos'}`
                         : mod.id === 'anatomy'       ? `6 ${lang === 'en' ? 'regions' : 'regiones'}`
                         : mod.id === 'quizzes'       ? `6 ${lang === 'en' ? 'packs' : 'packs'}`
                         : mod.id === 'community'     ? `${counts.community} ${lang === 'en' ? 'cases' : 'casos'}`
                         : ''}
                      </span>
                      <span className="text-sm font-semibold">{t.explore}</span>
                    </>
                  ) : (
                    <span className="text-xs text-white/50">{t.comingSoonSub}</span>
                  )}
                </div>
              </div>
            )

            return mod.available
              ? <Link key={mod.id} to={mod.link} className="anim-fadeup block" style={{ animationDelay: `${i * 80 + 200}ms` }}>{card}</Link>
              : <div  key={mod.id}               className="anim-fadeup"       style={{ animationDelay: `${i * 80 + 200}ms` }}>{card}</div>
          })}
        </div>

        {/* ── Progress bars ── */}
        {totalAttempts > 0 && (
          <div className="mt-12">
            <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-5">
              {lbl('Tu progreso por módulo', 'Your progress by module')}
            </h2>
            <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-5 flex flex-col gap-4">
              {MODULE_BARS.map(m => {
                const pct = m.total > 0 ? Math.round((m.done / m.total) * 100) : 0
                return (
                  <Link key={m.key} to={m.link} className="group">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-sm font-medium text-gray-700 group-hover:text-primary transition">{m.label}</span>
                      <span className="text-xs text-gray-400">{m.done}/{m.total} · {pct}%</span>
                    </div>
                    <div className="w-full bg-gray-100 rounded-full h-2.5 overflow-hidden">
                      <div
                        className="h-2.5 rounded-full transition-all duration-700"
                        style={{ width: `${pct}%`, backgroundColor: m.color }}
                      />
                    </div>
                  </Link>
                )
              })}
            </div>
          </div>
        )}

        {/* ── Achievements ── */}
        <div className="mt-10 pb-10">
          <div className="flex items-center justify-between mb-5">
            <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-widest">
              {lbl('Logros', 'Achievements')} — {unlocked.length}/{achievements.length}
            </h2>
            {unlocked.length > 0 && (
              <span className="text-xs text-yellow-600 font-semibold bg-yellow-50 border border-yellow-200 px-3 py-1 rounded-full">
                🏆 {unlocked.length} {lbl('desbloqueados', 'unlocked')}
              </span>
            )}
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
            {achievements.map(a => (
              <div key={a.id}
                className={`rounded-2xl border p-4 transition-all ${
                  a.unlocked
                    ? 'bg-white border-yellow-200 shadow-sm'
                    : 'bg-gray-50 border-gray-100 opacity-50 grayscale'
                }`}>
                <div className="text-2xl mb-2">{a.icon}</div>
                <div className={`text-xs font-bold mb-0.5 ${a.unlocked ? 'text-gray-800' : 'text-gray-400'}`}>
                  {lang === 'en' ? a.nameEn : a.nameEs}
                </div>
                <div className="text-xs text-gray-400 leading-tight">
                  {lang === 'en' ? a.descEn : a.descEs}
                </div>
                {a.unlocked && (
                  <div className="mt-2 text-xs text-yellow-600 font-semibold">✓ {lbl('Desbloqueado', 'Unlocked')}</div>
                )}
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  )
}
