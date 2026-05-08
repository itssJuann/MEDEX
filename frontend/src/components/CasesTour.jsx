import { useState, useEffect, useRef } from 'react'
import { useLang } from '../context/LangContext'

const DURATION = 4200   // ms per slide
const SLIDES_ES = [
  {
    icon: '🏥',
    title: 'Casos Clínicos',
    desc: 'Enfrenta situaciones reales de urgencias médicas. Toma decisiones como si fueras el médico de guardia.',
    visual: (
      <div className="flex flex-col gap-2 w-full">
        {['Infarto Agudo de Miocardio', 'ACV Isquémico', 'Shock Séptico'].map((name, i) => (
          <div key={i} className="flex items-center gap-3 bg-white rounded-xl p-3 border border-gray-100 shadow-sm animate-fadeIn"
               style={{ animationDelay: `${i * 0.15}s` }}>
            <div className="w-2 h-2 rounded-full bg-blue-500 shrink-0" />
            <span className="text-xs font-medium text-gray-700">{name}</span>
            <span className="ml-auto text-xs bg-yellow-50 text-yellow-700 border border-yellow-200 px-2 py-0.5 rounded-full">Intermedio</span>
          </div>
        ))}
      </div>
    ),
  },
  {
    icon: '🔍',
    title: 'Filtra por sistema y nivel',
    desc: 'Usa los filtros para encontrar casos por sistema médico o por dificultad. Empieza por Básico y avanza.',
    visual: (
      <div className="flex flex-col gap-3 w-full">
        <div className="flex gap-2 flex-wrap">
          {['Cardiovascular', 'Neurológico', 'Digestivo'].map((s, i) => (
            <span key={i} className={`text-xs px-3 py-1.5 rounded-full border font-medium ${i === 0 ? 'bg-blue-900 text-white border-blue-900' : 'bg-white text-gray-500 border-gray-300'}`}>{s}</span>
          ))}
        </div>
        <div className="flex gap-2">
          {[['Básico','green'], ['Intermedio','yellow'], ['Avanzado','red']].map(([d, c], i) => (
            <span key={i} className={`text-xs px-3 py-1.5 rounded-full border font-medium bg-${c}-50 text-${c}-700 border-${c}-200`}>{d}</span>
          ))}
        </div>
      </div>
    ),
  },
  {
    icon: '💭',
    title: 'Lee el escenario y decide',
    desc: 'Cada caso te presenta un paciente real. Analiza los datos clínicos y elige la acción correcta.',
    visual: (
      <div className="w-full bg-white rounded-xl border border-gray-100 shadow-sm p-4">
        <p className="text-xs text-gray-700 leading-relaxed mb-4">
          Paciente de 58 años con dolor retroesternal de 2h, diaforesis y ECG con elevación del ST en V1-V4. ¿Cuál es tu primera acción?
        </p>
        <div className="flex flex-col gap-2">
          {['Solicitar ECG de 12 derivaciones', 'Administrar analgésico y observar', 'Solicitar radiografía de tórax'].map((opt, i) => (
            <div key={i} className={`text-xs px-3 py-2 rounded-lg border flex items-center gap-2 ${i === 0 ? 'border-blue-400 bg-blue-50 text-blue-900' : 'border-gray-200 bg-gray-50 text-gray-600'}`}>
              <span className="font-bold text-gray-400">{['A','B','C'][i]}.</span> {opt}
              {i === 0 && <span className="ml-auto text-blue-600 text-xs">← correcto</span>}
            </div>
          ))}
        </div>
      </div>
    ),
  },
  {
    icon: '🔀',
    title: 'El caso se ramifica',
    desc: 'Cada decisión abre un camino diferente. Las elecciones incorrectas tienen consecuencias realistas.',
    visual: (
      <div className="flex flex-col items-center gap-1 w-full">
        <div className="bg-blue-900 text-white text-xs px-4 py-2 rounded-xl font-medium">Tu decisión</div>
        <div className="flex gap-8 items-start mt-2">
          <div className="flex flex-col items-center gap-1">
            <div className="w-px h-6 bg-green-400" />
            <div className="bg-green-50 border border-green-300 text-green-800 text-xs px-3 py-1.5 rounded-lg text-center">Diagnóstico<br/>precoz ✓</div>
            <div className="w-px h-5 bg-green-400" />
            <div className="bg-green-100 border border-green-400 text-green-900 text-xs px-3 py-1.5 rounded-lg">Éxito 🟢</div>
          </div>
          <div className="flex flex-col items-center gap-1">
            <div className="w-px h-6 bg-red-300" />
            <div className="bg-red-50 border border-red-200 text-red-700 text-xs px-3 py-1.5 rounded-lg text-center">Retraso<br/>diagnóstico ✕</div>
            <div className="w-px h-5 bg-red-300" />
            <div className="bg-red-100 border border-red-400 text-red-900 text-xs px-3 py-1.5 rounded-lg">Fallo 🔴</div>
          </div>
        </div>
      </div>
    ),
  },
  {
    icon: '💡',
    title: 'Aprende con cada caso',
    desc: 'Al final recibes retroalimentación detallada y una perla clínica que resume lo esencial del caso.',
    visual: (
      <div className="w-full flex flex-col gap-3">
        <div className="bg-green-50 border border-green-200 rounded-xl p-3">
          <div className="text-xs font-bold text-green-700 mb-1">✓ Excelente manejo</div>
          <div className="text-xs text-green-800 leading-relaxed">Diagnóstico precoz con ECG, reperfusión con ICPP en menos de 60 minutos y tratamiento completo al alta.</div>
        </div>
        <div className="bg-amber-50 border border-amber-200 rounded-xl p-3">
          <div className="text-xs font-bold text-amber-700 mb-1">💡 Perla clínica</div>
          <div className="text-xs text-amber-900 leading-relaxed">El tiempo puerta-balón menor a 90 minutos es el indicador más importante en el IAMCEST.</div>
        </div>
      </div>
    ),
  },
]

const SLIDES_EN = [
  {
    icon: '🏥',
    title: 'Clinical Cases',
    desc: 'Face real emergency medicine scenarios. Make decisions as if you were the attending physician.',
    visual: SLIDES_ES[0].visual,
  },
  {
    icon: '🔍',
    title: 'Filter by system and level',
    desc: 'Use the filters to find cases by medical system or difficulty. Start with Basic and work up.',
    visual: SLIDES_ES[1].visual,
  },
  {
    icon: '💭',
    title: 'Read the scenario and decide',
    desc: 'Each case presents a real patient. Analyze the clinical data and choose the right action.',
    visual: SLIDES_ES[2].visual,
  },
  {
    icon: '🔀',
    title: 'The case branches',
    desc: 'Every decision opens a different path. Wrong choices have realistic consequences.',
    visual: SLIDES_ES[3].visual,
  },
  {
    icon: '💡',
    title: 'Learn from every case',
    desc: 'At the end you get detailed feedback and a clinical pearl summarizing the key takeaway.',
    visual: SLIDES_ES[4].visual,
  },
]

export default function CasesTour({ onClose }) {
  const { lang } = useLang()
  const SLIDES = lang === 'en' ? SLIDES_EN : SLIDES_ES
  const lbl    = (es, en) => lang === 'en' ? en : es

  const [step, setStep]       = useState(0)
  const [paused, setPaused]   = useState(false)
  const [progress, setProgress] = useState(0)
  const intervalRef = useRef(null)
  const frameRef    = useRef(null)
  const startRef    = useRef(null)

  const goTo = (i) => {
    setStep(i)
    setProgress(0)
    startRef.current = null
  }

  const next = () => {
    if (step < SLIDES.length - 1) goTo(step + 1)
    else onClose()
  }

  // Smooth progress bar animation
  useEffect(() => {
    if (paused) return
    startRef.current = null

    const tick = (ts) => {
      if (!startRef.current) startRef.current = ts
      const elapsed = ts - startRef.current
      const pct = Math.min((elapsed / DURATION) * 100, 100)
      setProgress(pct)
      if (pct < 100) {
        frameRef.current = requestAnimationFrame(tick)
      } else {
        next()
      }
    }

    frameRef.current = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(frameRef.current)
  }, [step, paused])   // eslint-disable-line

  const slide = SLIDES[step]

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4"
         onClick={onClose}>
      <div className="w-full max-w-sm bg-white rounded-3xl shadow-2xl overflow-hidden"
           onClick={e => e.stopPropagation()}
           onMouseEnter={() => setPaused(true)}
           onMouseLeave={() => setPaused(false)}>

        {/* Progress bar */}
        <div className="h-1 bg-gray-100">
          <div className="h-1 bg-blue-900 transition-none" style={{ width: `${progress}%` }} />
        </div>

        {/* Slide segments */}
        <div className="flex gap-0.5 px-5 pt-3">
          {SLIDES.map((_, i) => (
            <button key={i} onClick={() => goTo(i)}
              className={`h-1 flex-1 rounded-full transition-colors ${i === step ? 'bg-blue-900' : i < step ? 'bg-blue-300' : 'bg-gray-200'}`} />
          ))}
        </div>

        {/* Content */}
        <div className="px-6 pt-5 pb-4">
          <div className="text-center mb-4">
            <div className="text-4xl mb-2">{slide.icon}</div>
            <h2 className="text-lg font-bold text-gray-900">{slide.title}</h2>
            <p className="text-sm text-gray-500 mt-1 leading-relaxed">{slide.desc}</p>
          </div>

          {/* Visual */}
          <div className="bg-gray-50 rounded-2xl p-4 min-h-36 flex items-center justify-center">
            {slide.visual}
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 pb-5 flex items-center justify-between gap-3">
          <button onClick={onClose}
            className="text-xs text-gray-400 hover:text-gray-600 transition">
            {lbl('Saltar', 'Skip')}
          </button>

          <div className="flex items-center gap-1.5">
            {SLIDES.map((_, i) => (
              <button key={i} onClick={() => goTo(i)}
                className={`rounded-full transition-all ${i === step ? 'w-5 h-2 bg-blue-900' : 'w-2 h-2 bg-gray-300 hover:bg-gray-400'}`} />
            ))}
          </div>

          <button onClick={next}
            className="text-xs font-semibold bg-blue-900 text-white px-4 py-2 rounded-full hover:bg-blue-800 transition">
            {step < SLIDES.length - 1 ? lbl('Siguiente →', 'Next →') : lbl('¡Empezar!', "Let's go!")}
          </button>
        </div>
      </div>
    </div>
  )
}
