import { useState, useEffect, useRef } from 'react'
import { useLang } from '../context/LangContext'
import { translateText, translateMany } from '../utils/translate'

// Translate a single string
export function useTranslate(text) {
  const { lang } = useLang()
  const [result, setResult] = useState(text)

  useEffect(() => {
    if (lang === 'es') { setResult(text); return }
    let cancelled = false
    translateText(text, lang).then(t => { if (!cancelled) setResult(t) })
    return () => { cancelled = true }
  }, [text, lang])

  return result
}

// Translate a whole data object when the language changes
// Keys: array of string keys to translate
export function useTranslateData(data, keys) {
  const { lang } = useLang()
  const [translated, setTranslated] = useState(data)
  const prevLang = useRef(lang)

  useEffect(() => {
    if (!data) return
    if (lang === 'es') { setTranslated(data); return }

    let cancelled = false
    const run = async () => {
      const result = { ...data }
      await Promise.all(
        keys.filter(k => typeof data[k] === 'string' && data[k]).map(async k => {
          result[k] = await translateText(data[k], lang)
        })
      )
      if (!cancelled) setTranslated(result)
    }
    run()
    return () => { cancelled = true }
  }, [data, lang])

  return translated
}
