// Composable para la gestión de datasets (RF-01).
// Usa useApi para GET y fetch directo para POST/PUT/DELETE.
// Actualiza la lista localmente después de cada operación exitosa.

import { ref } from 'vue'
import { useApi } from '~/composables/useApi'

export interface Dataset {
  id: number
  name: string
  description: string | null
  file_name: string
  created_at: string
}

export function useDatasets() {
  const urlApi = 'http://localhost:8000/api/datasets'

  // Para GET (listar) usamos useApi del nivel 3
  const { datos, cargando, error, pedir } = useApi<Dataset[]>(urlApi)

  const datasets = ref<Dataset[]>([])
  const loading = ref(false)
  const errorDatasets = ref<string | null>(null)

  async function obtenerDatasets() {
    loading.value = true
    errorDatasets.value = null
    
    await pedir()
    
    if (datos.value) {
      datasets.value = datos.value
    } else if (error.value) {
      errorDatasets.value = error.value
    }

    loading.value = false
  }

  async function crearDataset(datos: { name: string; description: string | null; file_name: string }) {
    loading.value = true
    errorDatasets.value = null

    try {
      const respuesta = await fetch(urlApi, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos),
      })

      if (!respuesta.ok) {
        throw new Error(`Error ${respuesta.status}`)
      }
      
      const nuevo: Dataset = await respuesta.json()
      datasets.value.push(nuevo)
      
      return nuevo
    } catch (e) {
      errorDatasets.value = 'No se pudo crear el dataset. Inténtalo de nuevo.'
      throw e
    } finally {
      loading.value = false
    }
  }

  async function actualizarDataset(id: number, datos: { name: string; description: string | null; file_name: string; created_at: string }) {
    loading.value = true
    errorDatasets.value = null

    try {
      const respuesta = await fetch(`${urlApi}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos),
      })
    
      if (!respuesta.ok) {
        if (respuesta.status === 404) {
          await obtenerDatasets()
        }
    
        throw new Error(`Error ${respuesta.status}`)
      }
    
      const actualizado: Dataset = await respuesta.json()
      const indice = datasets.value.findIndex((d) => d.id === id)
    
      if (indice !== -1) {
        datasets.value[indice] = actualizado
      }
    
      return actualizado
    } catch (e) {
      errorDatasets.value = 'No se pudo actualizar el dataset. Inténtalo de nuevo.'
      throw e
    } finally {
      loading.value = false
    }
  }

  async function eliminarDataset(id: number) {
    loading.value = true
    errorDatasets.value = null

    try {
      const respuesta = await fetch(`${urlApi}/${id}`, {
        method: 'DELETE',
      })
    
      if (!respuesta.ok) {
        if (respuesta.status === 404) {
          await obtenerDatasets()
        }
    
        throw new Error(`Error ${respuesta.status}`)
      }
    
      datasets.value = datasets.value.filter((d) => d.id !== id)
    } catch (e) {
      errorDatasets.value = 'No se pudo eliminar el dataset. Inténtalo de nuevo.'
      throw e
    } finally {
      loading.value = false
    }
  }

  return {
    datasets,
    loading,
    error: errorDatasets,
    obtenerDatasets,
    crearDataset,
    actualizarDataset,
    eliminarDataset,
  }
}
