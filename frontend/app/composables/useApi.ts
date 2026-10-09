// Composable genérico para hacer peticiones HTTP con fetch (RF-03, RF-04).
// Devuelve el estado de carga, el error (si lo hay) y los datos.

import { ref } from 'vue'

export function useApi<T>(url?: string) {
  // Si no se pasa URL, usamos la variable de entorno con su valor por defecto (RF-03).
  // el import.meta.env.NUXT_PUBLIC_API_BASE no pasa si no existe el archivo .env con la variable
  const urlFinal = url ?? import.meta.env.NUXT_PUBLIC_API_BASE ?? 'http://localhost:8000'

  const datos = ref<T | null>(null)
  const cargando = ref(false)
  const error = ref<string | null>(null)

  async function pedir() {
    cargando.value = true
    error.value = null
    
    try {
      const respuesta = await fetch(urlFinal)
      if (!respuesta.ok) {
        throw new Error(`Error ${respuesta.status}`)
      }
      datos.value = await respuesta.json()
    } catch {
      error.value = 'No se pudo conectar con el servidor. Inténtalo de nuevo.'
    } finally {
      cargando.value = false
    }
  }

  return { datos, cargando, error, pedir }
}
