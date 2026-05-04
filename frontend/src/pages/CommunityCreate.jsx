import API from '../utils/api'
import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'

const SYSTEMS     = ["Cardiovascular","Respiratorio","Digestivo","Neurológico","Endocrino","Infeccioso","Renal"]
const DIFFICULTIES = ["Básico","Intermedio","Avanzado"]

const DIFF_CLS = {
  "Básico":     "border-green-400 bg-green-50 text-green-700",
  "Intermedio": "border-yellow-400 bg-yellow-50 text-yellow-700",
  "Avanzado":   "border-red-400 bg-red-50 text-red-700",
}

function emptyQuestion() {
  return {
    text: '',
    options: [
      { text: '', correct: true,  feedback: '' },
      { text: '', correct: false, feedback: '' },
      { text: '', correct: false, feedback: '' },
    ],
  }
}

function QuestionCard({ q, index, onChange, onDelete, canDelete, lang }) {
  const lbl = (es, en) => lang === 'en' ? en : es
  const setField = (field, val) => onChange({ ...q, [field]: val })
  const setOption = (i, field, val) => {
    const opts = q.options.map((o, j) => {
      if (field === 'correct') return { ...o, correct: j === i }
      return j === i ? { ...o, [field]: val } : o
    })
    onChange({ ...q, options: opts })
  }
  const addOption = () => {
    if (q.options.length >= 4) return
    onChange({ ...q, options: [...q.options, { text: '', correct: false, feedback: '' }] })
  }
  const removeOption = (i) => {
    if (q.options.length <= 2) return
    const opts = q.options.filter((_, j) => j !== i)
    if (!opts.some(o => o.correct)) opts[0].correct = true
    onChange({ ...q, options: opts })
  }

  return (
    <div className="border border-gray-200 rounded-2xl p-5 bg-white">
      <div className="flex items-center justify-between mb-4">
        <span className="text-sm font-bold text-gray-700">
          {lbl(`Pregunta ${index + 1}`, `Question ${index + 1}`)}
        </span>
        {canDelete && (
          <button onClick={onDelete} className="text-xs text-red-400 hover:text-red-600 transition">
            {lbl('Eliminar', 'Delete')}
          </button>
        )}
      </div>

      <textarea
        value={q.text}
        onChange={e => setField('text', e.target.value)}
        placeholder={lbl('Escribe la pregunta clínica...', 'Write the clinical question...')}
        rows={2}
        className="w-full border border-gray-200 rounded-xl px-4 py-2.5 text-sm resize-none focus:outline-none focus:border-violet-400 mb-4"
      />

      <div className="text-xs font-semibold text-gray-400 uppercase mb-2">
        {lbl('Opciones', 'Options')}
      </div>
      <div className="flex flex-col gap-3">
        {q.options.map((opt, i) => (
          <div key={i} className={`border rounded-xl p-3 transition ${opt.correct ? 'border-green-300 bg-green-50' : 'border-gray-200 bg-gray-50'}`}>
            <div className="flex items-center gap-3 mb-2">
              <button
                onClick={() => setOption(i, 'correct', true)}
                title={lbl('Marcar como correcta', 'Mark as correct')}
                className={`w-5 h-5 rounded-full border-2 flex items-center justify-center shrink-0 transition
                  ${opt.correct ? 'border-green-500 bg-green-500' : 'border-gray-300 hover:border-green-400'}`}>
                {opt.correct && <span className="text-white text-xs font-bold">✓</span>}
              </button>
              <input
                value={opt.text}
                onChange={e => setOption(i, 'text', e.target.value)}
                placeholder={`${lbl('Opción', 'Option')} ${String.fromCharCode(65 + i)}`}
                className="flex-1 border border-gray-200 rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:border-violet-400 bg-white"
              />
              {q.options.length > 2 && (
                <button onClick={() => removeOption(i)} className="text-gray-300 hover:text-red-400 transition text-xs">✕</button>
              )}
            </div>
            <input
              value={opt.feedback}
              onChange={e => setOption(i, 'feedback', e.target.value)}
              placeholder={lbl('Retroalimentación al elegir esta opción...', 'Feedback when this option is selected...')}
              className="w-full border border-gray-200 rounded-lg px-3 py-1.5 text-xs focus:outline-none focus:border-violet-400 bg-white text-gray-600"
            />
          </div>
        ))}
      </div>
      {q.options.length < 4 && (
        <button onClick={addOption}
          className="mt-3 text-xs text-violet-600 hover:text-violet-800 transition">
          + {lbl('Agregar opción', 'Add option')}
        </button>
      )}
    </div>
  )
}

export default function CommunityCreate() {
  const { lang } = useLang()
  const navigate = useNavigate()
  const lbl = (es, en) => lang === 'en' ? en : es

  const STEPS = [
    { label: lbl('Información',  'Information'), icon: '📋' },
    { label: lbl('Presentación', 'Presentation'), icon: '🩺' },
    { label: lbl('Preguntas',    'Questions'),    icon: '❓' },
    { label: lbl('Resolución',   'Resolution'),   icon: '✅' },
  ]

  const [step, setStep]             = useState(0)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError]           = useState(null)

  const [info, setInfo]               = useState({ title: '', system: '', difficulty: '', summary: '' })
  const [presentation, setPresentation] = useState('')
  const [questions, setQuestions]     = useState([emptyQuestion(), emptyQuestion()])
  const [resolution, setResolution]   = useState({ diagnosis: '', pearl: '' })

  const updateQ = (i, val) => setQuestions(qs => qs.map((q, j) => j === i ? val : q))
  const addQ    = () => setQuestions(qs => [...qs, emptyQuestion()])
  const delQ    = (i) => setQuestions(qs => qs.filter((_, j) => j !== i))

  const stepValid = () => {
    if (step === 0) return info.title.trim() && info.system && info.difficulty && info.summary.trim()
    if (step === 1) return presentation.trim().length >= 50
    if (step === 2) return questions.every(q =>
      q.text.trim() &&
      q.options.every(o => o.text.trim() && o.feedback.trim()) &&
      q.options.some(o => o.correct)
    ) && questions.length >= 2
    if (step === 3) return resolution.diagnosis.trim().length >= 20
    return true
  }

  const handleSubmit = async () => {
    setSubmitting(true)
    setError(null)
    const token = localStorage.getItem('medex_token')
    try {
      const r = await fetch(`${API}/community-cases`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({
          ...info,
          presentation,
          questions: questions.map((q, i) => ({
            id: `q${i + 1}`,
            text: q.text.trim(),
            options: q.options.map((o, j) => ({
              id: String.fromCharCode(97 + j),
              text: o.text.trim(),
              correct: o.correct,
              feedback: o.feedback.trim(),
            })),
          })),
          diagnosis: resolution.diagnosis.trim(),
          pearl: resolution.pearl.trim(),
        }),
      })
      if (!r.ok) { const d = await r.json(); throw new Error(d.detail ?? 'Error') }
      navigate('/community')
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-10 max-w-2xl mx-auto">
      <Link to="/community" className="text-xs text-violet-600 hover:underline mb-6 inline-block">
        ← {lbl('Volver a la comunidad', 'Back to community')}
      </Link>
      <h1 className="text-2xl font-bold text-gray-800 mb-1">{lbl('Crear caso clínico', 'Create clinical case')}</h1>
      <p className="text-sm text-gray-500 mb-8">
        {lbl('Tu caso será revisado por un moderador antes de publicarse.', 'Your case will be reviewed by a moderator before publishing.')}
      </p>

      {/* Step indicator */}
      <div className="flex items-center gap-2 mb-8">
        {STEPS.map((s, i) => (
          <div key={i} className="flex items-center gap-2">
            <div className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold transition
              ${i === step ? 'bg-violet-700 text-white' : i < step ? 'bg-violet-100 text-violet-600' : 'bg-gray-100 text-gray-400'}`}>
              <span>{s.icon}</span>
              <span className="hidden sm:inline">{s.label}</span>
            </div>
            {i < STEPS.length - 1 && <div className={`h-0.5 w-6 ${i < step ? 'bg-violet-400' : 'bg-gray-200'}`}/>}
          </div>
        ))}
      </div>

      {/* ── Step 0: Info ── */}
      {step === 0 && (
        <div className="bg-white rounded-2xl border border-gray-100 shadow p-6 flex flex-col gap-4">
          <h2 className="font-bold text-gray-700">{lbl('Información del caso', 'Case information')}</h2>
          <input value={info.title} onChange={e => setInfo(p => ({ ...p, title: e.target.value }))}
            placeholder={lbl('Título del caso (ej. Paciente con disnea brusca...)', 'Case title (e.g. Patient with sudden dyspnea...)')}
            className="border border-gray-200 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-violet-400"/>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="text-xs font-semibold text-gray-400 uppercase mb-1 block">{lbl('Sistema', 'System')}</label>
              <div className="flex flex-col gap-1.5">
                {SYSTEMS.map(s => (
                  <button key={s} onClick={() => setInfo(p => ({ ...p, system: s }))}
                    className={`text-left px-3 py-2 rounded-xl border text-sm transition
                      ${info.system === s ? 'border-violet-500 bg-violet-50 text-violet-700 font-medium' : 'border-gray-200 hover:border-violet-300'}`}>
                    {s}
                  </button>
                ))}
              </div>
            </div>
            <div>
              <label className="text-xs font-semibold text-gray-400 uppercase mb-1 block">{lbl('Dificultad', 'Difficulty')}</label>
              <div className="flex flex-col gap-1.5">
                {DIFFICULTIES.map(d => (
                  <button key={d} onClick={() => setInfo(p => ({ ...p, difficulty: d }))}
                    className={`text-left px-3 py-2 rounded-xl border text-sm font-medium transition
                      ${info.difficulty === d ? DIFF_CLS[d] : 'border-gray-200 hover:border-gray-400'}`}>
                    {d}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-400 uppercase mb-1 block">{lbl('Resumen breve', 'Brief summary')}</label>
            <textarea value={info.summary} onChange={e => setInfo(p => ({ ...p, summary: e.target.value }))}
              placeholder={lbl('1-2 frases describiendo el caso...', '1-2 sentences describing the case...')}
              rows={2}
              className="w-full border border-gray-200 rounded-xl px-4 py-2.5 text-sm resize-none focus:outline-none focus:border-violet-400"/>
          </div>
        </div>
      )}

      {/* ── Step 1: Presentation ── */}
      {step === 1 && (
        <div className="bg-white rounded-2xl border border-gray-100 shadow p-6">
          <h2 className="font-bold text-gray-700 mb-1">{lbl('Presentación clínica', 'Clinical presentation')}</h2>
          <p className="text-xs text-gray-400 mb-4">
            {lbl(
              'Describe el caso con detalle: edad, sexo, síntomas, signos vitales, exámenes iniciales. Mínimo 50 caracteres.',
              'Describe the case in detail: age, sex, symptoms, vital signs, initial tests. Minimum 50 characters.'
            )}
          </p>
          <textarea
            value={presentation}
            onChange={e => setPresentation(e.target.value)}
            placeholder={lbl(
              'Paciente masculino de 65 años que consulta por...\nAntecedentes: ...\nExamen físico: TA... FC... FR... SpO2...\nExámenes: ...',
              '65-year-old male presenting with...\nHistory: ...\nPhysical exam: BP... HR... RR... SpO2...\nTests: ...'
            )}
            rows={12}
            className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm resize-none focus:outline-none focus:border-violet-400 font-mono leading-relaxed"/>
          <div className="text-xs text-gray-400 mt-2 text-right">
            {presentation.length} {lbl('caracteres', 'characters')}
          </div>
        </div>
      )}

      {/* ── Step 2: Questions ── */}
      {step === 2 && (
        <div className="flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="font-bold text-gray-700">{lbl('Preguntas clínicas', 'Clinical questions')}</h2>
              <p className="text-xs text-gray-400 mt-0.5">
                {lbl('Mínimo 2, máximo 5. Marca la opción correcta (verde).', 'Minimum 2, max 5. Mark the correct option (green).')}
              </p>
            </div>
            {questions.length < 5 && (
              <button onClick={addQ}
                className="text-sm bg-violet-700 text-white px-4 py-2 rounded-xl hover:bg-violet-800 transition">
                + {lbl('Pregunta', 'Question')}
              </button>
            )}
          </div>
          {questions.map((q, i) => (
            <QuestionCard key={i} q={q} index={i} lang={lang}
              onChange={val => updateQ(i, val)}
              onDelete={() => delQ(i)}
              canDelete={questions.length > 2}/>
          ))}
        </div>
      )}

      {/* ── Step 3: Resolution ── */}
      {step === 3 && (
        <div className="bg-white rounded-2xl border border-gray-100 shadow p-6 flex flex-col gap-4">
          <h2 className="font-bold text-gray-700">{lbl('Resolución del caso', 'Case resolution')}</h2>
          <div>
            <label className="text-xs font-semibold text-gray-400 uppercase mb-1 block">
              {lbl('Diagnóstico y resolución', 'Diagnosis and resolution')} <span className="text-red-400">*</span>
            </label>
            <textarea value={resolution.diagnosis}
              onChange={e => setResolution(p => ({ ...p, diagnosis: e.target.value }))}
              placeholder={lbl(
                'Explica el diagnóstico correcto, el razonamiento clínico y el manejo. Mínimo 20 caracteres.',
                'Explain the correct diagnosis, clinical reasoning and management. Minimum 20 characters.'
              )}
              rows={6}
              className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm resize-none focus:outline-none focus:border-violet-400"/>
          </div>
          <div>
            <label className="text-xs font-semibold text-gray-400 uppercase mb-1 block">
              {lbl('Perla clínica', 'Clinical pearl')} <span className="text-gray-300">({lbl('opcional', 'optional')})</span>
            </label>
            <textarea value={resolution.pearl}
              onChange={e => setResolution(p => ({ ...p, pearl: e.target.value }))}
              placeholder={lbl('Un dato clave, regla mnemotécnica o truco diagnóstico...', 'A key fact, mnemonic or diagnostic tip...')}
              rows={3}
              className="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm resize-none focus:outline-none focus:border-violet-400"/>
          </div>
          <div className="bg-yellow-50 border border-yellow-200 rounded-xl p-4 text-sm text-yellow-800">
            <span className="font-semibold">⚠ {lbl('Revisión pendiente:', 'Pending review:')}</span>{' '}
            {lbl(
              'Tu caso pasará por moderación antes de publicarse. Recibirás retroalimentación en tu perfil de casos.',
              'Your case will go through moderation before publishing. You will receive feedback in your case profile.'
            )}
          </div>
          {error && <p className="text-sm text-red-500">{error}</p>}
        </div>
      )}

      {/* Navigation */}
      <div className="flex items-center justify-between mt-6">
        {step > 0 ? (
          <button onClick={() => setStep(s => s - 1)}
            className="px-5 py-2.5 rounded-xl border border-gray-300 text-sm text-gray-600 hover:bg-gray-100 transition">
            ← {lbl('Atrás', 'Back')}
          </button>
        ) : <div/>}

        {step < STEPS.length - 1 ? (
          <button onClick={() => setStep(s => s + 1)} disabled={!stepValid()}
            className="px-6 py-2.5 rounded-xl bg-violet-700 text-white text-sm font-medium hover:bg-violet-800 transition disabled:opacity-40">
            {lbl('Siguiente', 'Next')} →
          </button>
        ) : (
          <button onClick={handleSubmit} disabled={!stepValid() || submitting}
            className="px-6 py-2.5 rounded-xl bg-violet-700 text-white text-sm font-medium hover:bg-violet-800 transition disabled:opacity-40">
            {submitting ? lbl('Enviando...', 'Sending...') : lbl('Enviar para revisión', 'Submit for review')}
          </button>
        )}
      </div>
    </div>
  )
}
