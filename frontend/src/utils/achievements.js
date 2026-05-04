export const ACHIEVEMENTS = [
  // Cases
  { id: 'first_case',     icon: '🏥', nameEs: 'Primer Caso',          nameEn: 'First Case',          descEs: 'Completa tu primer caso clínico',                    descEn: 'Complete your first clinical case',                  condition: (p) => p.case.length >= 1 },
  { id: 'perfect_case',   icon: '⭐', nameEs: 'Sin Errores',           nameEn: 'No Mistakes',         descEs: 'Completa un caso con resultado exitoso',             descEn: 'Complete a case with a successful outcome',          condition: (p) => p.case.some(c => c.best_result === 'success') },
  { id: 'marathon',       icon: '🏃', nameEs: 'Maratonista',           nameEn: 'Marathon Runner',     descEs: 'Completa 10 casos clínicos',                         descEn: 'Complete 10 clinical cases',                         condition: (p) => p.case.length >= 10 },
  { id: 'all_cases',      icon: '🏆', nameEs: 'Expediente Completo',   nameEn: 'Complete Record',     descEs: 'Completa todos los casos disponibles',               descEn: 'Complete all available cases',                       condition: (p, totals) => totals.cases > 0 && p.case.length >= totals.cases },
  { id: 'perfectionist',  icon: '💎', nameEs: 'Perfeccionista',        nameEn: 'Perfectionist',       descEs: 'Completa 5 casos con resultado exitoso',             descEn: 'Complete 5 cases with a successful result',          condition: (p) => p.case.filter(c => c.best_result === 'success').length >= 5 },

  // Differentials
  { id: 'first_diff',     icon: '🔍', nameEs: 'Detective',             nameEn: 'Detective',           descEs: 'Completa tu primer diagnóstico diferencial',         descEn: 'Complete your first differential diagnosis',         condition: (p) => p.differential.length >= 1 },
  { id: 'diff_master',    icon: '🎯', nameEs: 'Diagnosticador',        nameEn: 'Diagnostician',       descEs: 'Completa 5 diagnósticos diferenciales',              descEn: 'Complete 5 differential diagnoses',                  condition: (p) => p.differential.length >= 5 },
  { id: 'all_diff',       icon: '🔬', nameEs: 'Sherlock',              nameEn: 'Sherlock',            descEs: 'Completa todos los diferenciales disponibles',       descEn: 'Complete all available differentials',               condition: (p, totals) => totals.differentials > 0 && p.differential.length >= totals.differentials },

  // Algorithms
  { id: 'first_algo',     icon: '⚙️', nameEs: 'Protocolar',           nameEn: 'By the Book',         descEs: 'Navega tu primer algoritmo clínico',                 descEn: 'Navigate your first clinical algorithm',             condition: (p) => p.algorithm.length >= 1 },
  { id: 'algo_master',    icon: '📋', nameEs: 'Guías al Dedillo',      nameEn: 'Guideline Expert',    descEs: 'Completa 5 algoritmos clínicos',                     descEn: 'Complete 5 clinical algorithms',                     condition: (p) => p.algorithm.length >= 5 },
  { id: 'all_algo',       icon: '🗺️', nameEs: 'Navegante',            nameEn: 'Navigator',           descEs: 'Completa todos los algoritmos disponibles',          descEn: 'Complete all available algorithms',                  condition: (p, totals) => totals.algorithms > 0 && p.algorithm.length >= totals.algorithms },

  // Images
  { id: 'first_image',    icon: '🫁', nameEs: 'Radiólogo',            nameEn: 'Radiologist',         descEs: 'Interpreta tu primera imagen clínica',               descEn: 'Interpret your first clinical image',                condition: (p) => p.image.length >= 1 },
  { id: 'ecg_expert',     icon: '💓', nameEs: 'Cardioelectro',        nameEn: 'ECG Expert',          descEs: 'Completa los 2 casos de ECG',                        descEn: 'Complete both ECG cases',                            condition: (p) => p.image.filter(i => i.item_id.includes('ecg')).length >= 2 },
  { id: 'all_images',     icon: '🩻', nameEs: 'Imagenólogo',          nameEn: 'Imaging Expert',      descEs: 'Completa todas las imágenes clínicas',               descEn: 'Complete all clinical images',                       condition: (p, totals) => totals.images > 0 && p.image.length >= totals.images },

  // Quizzes
  { id: 'first_quiz',     icon: '🧠', nameEs: 'Primera Prueba',       nameEn: 'First Test',          descEs: 'Completa tu primer micro-quiz',                      descEn: 'Complete your first micro-quiz',                     condition: (p) => p.quiz.length >= 1 },
  { id: 'quiz_ace',       icon: '🎓', nameEs: 'Quiz Master',           nameEn: 'Quiz Master',         descEs: 'Obtén éxito en un quiz completo',                    descEn: 'Score success on a complete quiz',                   condition: (p) => p.quiz.some(q => q.best_result === 'success') },
  { id: 'all_quizzes',    icon: '🌟', nameEs: 'Enciclopedia',          nameEn: 'Encyclopedia',        descEs: 'Completa todos los quizzes disponibles',             descEn: 'Complete all available quizzes',                     condition: (p, totals) => totals.quizzes > 0 && p.quiz.length >= totals.quizzes },

  // Multitarea
  { id: 'all_modules',    icon: '🚀', nameEs: 'Polifacético',          nameEn: 'Multi-Talented',      descEs: 'Usa los 6 módulos de aprendizaje',                   descEn: 'Use all 6 learning modules',                         condition: (p) => ['case','differential','algorithm','image','quiz'].every(m => p[m]?.length >= 1) },
  { id: 'centurion',      icon: '💯', nameEs: 'Centurión',             nameEn: 'Centurion',           descEs: 'Acumula 100 intentos totales en todos los módulos',  descEn: 'Accumulate 100 total attempts across all modules',   condition: (p) => Object.values(p).flat().reduce((s, r) => s + (r.attempts ?? 1), 0) >= 100 },
]

export function groupProgress(rawProgress) {
  const groups = { case: [], differential: [], algorithm: [], image: [], quiz: [] }
  if (!Array.isArray(rawProgress)) return groups
  rawProgress.forEach(r => {
    const mt = r.module_type ?? 'case'
    if (groups[mt]) groups[mt].push(r)
  })
  return groups
}

export function computeAchievements(grouped, totals) {
  return ACHIEVEMENTS.map(a => ({
    ...a,
    unlocked: a.condition(grouped, totals),
  }))
}
