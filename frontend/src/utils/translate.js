const CACHE_KEY = 'mediclinic_translations'

const getCache = () => {
  try { return JSON.parse(localStorage.getItem(CACHE_KEY) || '{}') }
  catch { return {} }
}

const saveCache = (key, value) => {
  try {
    const cache = getCache()
    cache[key] = value
    // Limit cache size to ~200 entries
    const keys = Object.keys(cache)
    if (keys.length > 200) delete cache[keys[0]]
    localStorage.setItem(CACHE_KEY, JSON.stringify(cache))
  } catch {}
}

export async function translateText(text, targetLang) {
  if (!text || typeof text !== 'string' || targetLang === 'es') return text

  const cacheKey = `${targetLang}::${text.slice(0, 80)}`
  const cache = getCache()
  if (cache[cacheKey]) return cache[cacheKey]

  try {
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=${targetLang}&dt=t&q=${encodeURIComponent(text)}`
    const res  = await fetch(url)
    const json = await res.json()
    const translated = json[0].map(x => x[0]).join('')
    saveCache(cacheKey, translated)
    return translated
  } catch {
    return text
  }
}

// Translate multiple texts in parallel
export async function translateMany(texts, targetLang) {
  if (targetLang === 'es') return texts
  return Promise.all(texts.map(t => translateText(t, targetLang)))
}

// Translate all string values of an object (1 level deep)
export async function translateObject(obj, targetLang, keys) {
  if (targetLang === 'es') return obj
  const result = { ...obj }
  await Promise.all(
    keys.filter(k => typeof obj[k] === 'string' && obj[k]).map(async k => {
      result[k] = await translateText(obj[k], targetLang)
    })
  )
  return result
}
