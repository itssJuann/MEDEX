import API from '../utils/api'
const RANK = { success: 2, warning: 1, failure: 0 }

function lsKey() {
  try {
    const user = JSON.parse(localStorage.getItem('medex_user') || 'null')
    return user?.email ? `medex_progress_${user.email}` : 'medex_progress_anonymous'
  } catch {
    return 'medex_progress_anonymous'
  }
}

function storeKey(moduleType, itemId) {
  return moduleType === 'case' ? itemId : `${moduleType}:${itemId}`
}

function readAll() {
  try { return JSON.parse(localStorage.getItem(lsKey()) || '{}') } catch { return {} }
}

export function getProgress(moduleType, itemId) {
  return readAll()[storeKey(moduleType, itemId)] ?? null
}

export function getAllProgress() {
  return Object.values(readAll())
}

export function saveProgress(moduleType, itemId, result) {
  const key      = storeKey(moduleType, itemId)
  const all      = readAll()
  const existing = all[key]
  const best     = !existing || (RANK[result] ?? -1) > (RANK[existing.best_result] ?? -1)
    ? result : existing.best_result
  all[key] = { module_type: moduleType, item_id: itemId, best_result: best, attempts: (existing?.attempts ?? 0) + 1 }
  localStorage.setItem(lsKey(), JSON.stringify(all))

  const token = localStorage.getItem('medex_token')
  if (token) {
    fetch(`${API}/progress`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body:    JSON.stringify({ module_type: moduleType, item_id: itemId, result }),
    }).catch(() => {})
  }

  return all[key]
}
