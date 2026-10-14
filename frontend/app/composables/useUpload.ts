// Composable para la subida de archivos (RF-07).
// Usa fetch directamente con FormData para enviar archivos al backend.
// Devuelve el estado de carga, el error (si lo hay) y el resumen.

import { ref } from 'vue'

export interface DataSummary {
  file_name: string
  rows: number
  columns: number
  column_names: string[]
  missing_values: Record<string, number>
  statistics: Record<string, {
    count: number
    mean: number | null
    std: number | null
    min: number | null
    '25%': number | null
    '50%': number | null
    '75%': number | null
    max: number | null
  }>
  preview: Record<string, any>[]
}

export function useUpload() {
  const urlApi = 'http://localhost:8000/api/datasets/upload'

  const loading = ref(false)
  const error = ref<string | null>(null)
  const summary = ref<DataSummary | null>(null)

  async function subirArchivo(archivo: File) {
    loading.value = true
    error.value = null
    summary.value = null

    try {
      const formData = new FormData()
      formData.append('archivo', archivo)

      const respuesta = await fetch(urlApi, {
        method: 'POST',
        body: formData,
      })

      if (!respuesta.ok) {
        const errorData = await respuesta.json().catch(() => null)
        throw new Error(errorData?.detail ?? `Error ${respuesta.status}`)
      }

      summary.value = await respuesta.json()
    } catch (e: any) {
      error.value = e.message === 'Failed to fetch'
        ? 'No se pudo conectar con el servidor. Inténtalo de nuevo.'
        : (e.message || 'Error inesperado. Inténtalo de nuevo.')
    } finally {
      loading.value = false
    }
  }

  return {
    loading,
    error,
    summary,
    subirArchivo,
  }
}
