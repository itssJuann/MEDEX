import { useState, useEffect, useRef } from 'react'
import { useLang } from '../context/LangContext'

const DURATION = 4200

export default function TourGuide({ slides, onClose }) {
  const { lang } = useLang()
  const lbl = (es, en) => lang === 'en' ? en : es

  const [step, setStep]         = useState(0)
  const [paused, setPaused]     = useState(false)
  const [progress, setProgress] = useState(0)
  const frameRef = useRef(null)
  const startRef = useRef(null)

  const goTo = (i) => { setStep(i); setProgress(0); startRef.current = null }
  const next = () => { if (step < slides.length - 1) goTo(step + 1); else onClose() }

  useEffect(() => {
    if (paused) return
    startRef.current = null
    const tick = (ts) => {
      if (!startRef.current) startRef.current = ts
      const pct = Math.min(((ts - startRef.current) / DURATION) * 100, 100)
      setProgress(pct)
      if (pct < 100) frameRef.current = requestAnimationFrame(tick)
      else next()
    }
    frameRef.current = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(frameRef.current)
  }, [step, paused]) // eslint-disable-line

  const slide = slides[step]

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4"
         onClick={onClose}>
      <div className="w-full max-w-sm bg-white rounded-3xl shadow-2xl overflow-hidden"
           onClick={e => e.stopPropagation()}
           onMouseEnter={() => setPaused(true)}
           onMouseLeave={() => setPaused(false)}>

        {/* Continuous progress bar */}
        <div className="h-1 bg-gray-100">
          <div className="h-1 bg-blue-900 transition-none" style={{ width: `${progress}%` }} />
        </div>

        {/* Slide segments */}
        <div className="flex gap-0.5 px-5 pt-3">
          {slides.map((_, i) => (
            <button key={i} onClick={() => goTo(i)}
              className={`h-1 flex-1 rounded-full transition-colors ${
                i === step ? 'bg-blue-900' : i < step ? 'bg-blue-300' : 'bg-gray-200'
              }`} />
          ))}
        </div>

        {/* Content */}
        <div className="px-6 pt-5 pb-4">
          <div className="text-center mb-4">
            <div className="text-4xl mb-2">{slide.icon}</div>
            <h2 className="text-lg font-bold text-gray-900">{slide.title}</h2>
            <p className="text-sm text-gray-500 mt-1 leading-relaxed">{slide.desc}</p>
          </div>
          <div className="bg-gray-50 rounded-2xl p-4 min-h-36 flex items-center justify-center">
            {slide.visual}
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 pb-5 flex items-center justify-between gap-3">
          <button onClick={onClose} className="text-xs text-gray-400 hover:text-gray-600 transition">
            {lbl('Saltar', 'Skip')}
          </button>
          <div className="flex items-center gap-1.5">
            {slides.map((_, i) => (
              <button key={i} onClick={() => goTo(i)}
                className={`rounded-full transition-all ${
                  i === step ? 'w-5 h-2 bg-blue-900' : 'w-2 h-2 bg-gray-300 hover:bg-gray-400'
                }`} />
            ))}
          </div>
          <button onClick={next}
            className="text-xs font-semibold bg-blue-900 text-white px-4 py-2 rounded-full hover:bg-blue-800 transition">
            {step < slides.length - 1 ? lbl('Siguiente →', 'Next →') : lbl('¡Empezar!', "Let's go!")}
          </button>
        </div>
      </div>
    </div>
  )
}
