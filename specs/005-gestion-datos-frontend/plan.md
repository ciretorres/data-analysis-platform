# Plan de implementación — Spec 005 (Nivel 4)

**Fecha**: 2026-10-08 · **Estado**: Pendiente de aprobación

## 1. Archivos a crear/modificar y responsabilidades

| Archivo | Responsabilidad | RF cubierto |
|---------|----------------|-------------|
| `frontend/app/composables/useDatasets.ts` | Composable que encapsula toda la lógica CRUD de datasets usando `useApi` para GET y `fetch` para POST/PUT/DELETE. Devuelve estado reactivo y funciones de operación. | RF-01 |
| `frontend/app/components/LoadingState.vue` | Componente reutilizable de estado de carga con mensaje configurable. | RF-05 |
| `frontend/app/components/ErrorMessage.vue` | Componente reutilizable de mensaje de error con botón de reintento. | RF-05 |
| `frontend/app/components/DatasetCard.vue` | Tarjeta individual de dataset con botones de editar y eliminar. | RF-03 |
| `frontend/app/components/DatasetForm.vue` | Formulario de crear/editar con validación y manejo de errores 422. | RF-04 |
| `frontend/app/components/DatasetList.vue` | Lista de datasets que integra `DatasetCard` y maneja estados. | RF-02 |
| `frontend/app/pages/index.vue` | Añadir sección "Gestión de datasets" con modal, mensajes y enlace en menú. | RF-06, RF-07, RF-08, RF-09, RF-10 |
| `frontend/app/components/AppHeader.vue` | Añadir enlace "Gestión de datasets" al menú de navegación. | RF-06 |
| `docs/conceptos-nivel-4.md` | Documentación de conceptos del nivel 4 (CRUD, formularios, modales, etc.). | RF-11 |

## 2. Decisiones técnicas y justificación

| Decisión | Justificación | RF/RNF |
|----------|---------------|--------|
| **`useApi` solo para GET** | El `useApi` del nivel 3 solo soporta GET. Para POST/PUT/DELETE se usa `fetch` directamente dentro de `useDatasets`. | RF-01 |
| **Actualización local sin GET** | La spec exige actualizar la lista con la respuesta del servidor, no con otra petición. | RF-01, CL-04, CL-10, CL-11 |
| **Modal con overlay fixed** | La spec pide modal superpuesto sin navegación a otra página. | RF-07, RF-08, CL-20 |
| **`window.confirm()` para eliminar** | La spec especifica este método nativo. | RF-09 |
| **Componentes de estado genéricos** | `LoadingState` y `ErrorMessage` son reutilizables en cualquier sección. | RF-05, RNF-06 |
| **Validación en cliente y servidor** | El formulario valida en cliente, pero también maneja errores 422 del servidor. | RF-04, CL-15 |
| **Mensajes con auto-cierre a 3s** | La spec exige que los mensajes desaparezcan automáticamente. | RF-10 |
| **`ref` para campos del formulario** | Formulario controlado con estado reactivo en Vue. | RF-04 |
| **Formato de fecha con `Intl.DateTimeFormat`** | Formato local español sin dependencias extra. | RF-02, RF-03 |

## 3. Funciones puras con "hoy" como parámetro

Este nivel es **solo frontend**. No hay funciones puras con "hoy" como parámetro porque:
- Las fechas (`created_at`) las genera el backend y vienen en las respuestas.
- El frontend solo las muestra con formato local usando `Intl.DateTimeFormat`.
- No hay lógica de fechas en el frontend.

## 4. Estructura del composable `useDatasets`

```typescript
// frontend/app/composables/useDatasets.ts
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
```

## 5. Estructura de los componentes

### `DatasetCard.vue`

```vue
<script setup lang="ts">
interface Dataset {
  id: number
  name: string
  description: string | null
  file_name: string
  created_at: string
}

const props = defineProps<{ dataset: Dataset }>()
const emit = defineEmits<{
  editar: [dataset: Dataset]
  eliminar: [id: number]
}>()

function formatearFecha(fecha: string): string {
  return new Intl.DateTimeFormat('es-ES', { dateStyle: 'long' }).format(new Date(fecha))
}

function confirmarEliminar() {
  if (window.confirm('¿Seguro que quieres eliminar este dataset?')) {
    emit('eliminar', props.dataset.id)
  }
}
</script>

<template>
  <article class="tarjeta">
    <h3>{{ dataset.name }}</h3>
    <p v-if="dataset.description">{{ dataset.description }}</p>
    <p><strong>Archivo:</strong> {{ dataset.file_name }}</p>
    <p><strong>Creado:</strong> {{ formatearFecha(dataset.created_at) }}</p>
    <div class="tarjeta__acciones">
      <button @click="emit('editar', dataset)">Editar</button>
      <button @click="confirmarEliminar">Eliminar</button>
    </div>
  </article>
</template>
```

### `DatasetForm.vue`

```vue
<script setup lang="ts">
import { ref, watch } from 'vue'

interface Dataset {
  id: number
  name: string
  description: string | null
  file_name: string
  created_at: string
}

const props = defineProps<{
  modo: 'crear' | 'editar'
  dataset?: Dataset
}>()

const emit = defineEmits<{
  guardar: [datos: { name: string; description: string | null; file_name: string }]
  cancelar: []
}>()

const name = ref('')
const description = ref('')
const file_name = ref('')
const errores = ref<{ name?: string; file_name?: string; general?: string }>({})
const enviando = ref(false)

watch(() => props.dataset, (nuevo) => {
  if (nuevo && props.modo === 'editar') {
    name.value = nuevo.name
    description.value = nuevo.description ?? ''
    file_name.value = nuevo.file_name
  }
}, { immediate: true })

function validar(): boolean {
  errores.value = {}
  if (!name.value.trim()) {
    errores.value.name = 'El nombre es obligatorio.'
  } else if (name.value.length > 100) {
    errores.value.name = 'El nombre no puede tener más de 100 caracteres.'
  }
  if (!file_name.value.trim()) {
    errores.value.file_name = 'El nombre de archivo es obligatorio.'
  } else if (file_name.value.length > 255) {
    errores.value.file_name = 'El nombre de archivo no puede tener más de 255 caracteres.'
  }
  return Object.keys(errores.value).length === 0
}

async function enviar() {
  if (!validar()) return
  enviando.value = true
  try {
    emit('guardar', {
      name: name.value.trim(),
      description: description.value.trim() || null,
      file_name: file_name.value.trim(),
    })
  } finally {
    enviando.value = false
  }
}
</script>

<template>
  <form @submit.prevent="enviar">
    <div>
      <label for="name">Nombre *</label>
      <input id="name" v-model="name" type="text" maxlength="100" />
      <p v-if="errores.name" class="error">{{ errores.name }}</p>
    </div>
    <div>
      <label for="description">Descripción</label>
      <textarea id="description" v-model="description"></textarea>
    </div>
    <div>
      <label for="file_name">Nombre de archivo *</label>
      <input id="file_name" v-model="file_name" type="text" maxlength="255" />
      <p v-if="errores.file_name" class="error">{{ errores.file_name }}</p>
    </div>
    <p v-if="errores.general" class="error">{{ errores.general }}</p>
    <div>
      <button type="submit" :disabled="enviando">
        {{ modo === 'crear' ? 'Crear dataset' : 'Guardar cambios' }}
      </button>
      <button type="button" @click="emit('cancelar')">Cancelar</button>
    </div>
  </form>
</template>
```

### `DatasetList.vue`

```vue
<script setup lang="ts">
import DatasetCard from './DatasetCard.vue'
import LoadingState from './LoadingState.vue'
import ErrorMessage from './ErrorMessage.vue'

interface Dataset {
  id: number
  name: string
  description: string | null
  file_name: string
  created_at: string
}

defineProps<{
  datasets: Dataset[]
  loading: boolean
  error: string | null
}>()

const emit = defineEmits<{
  editar: [dataset: Dataset]
  eliminar: [id: number]
  reintentar: []
}>()
</script>

<template>
  <div class="lista">
    <LoadingState v-if="loading" mensaje="Cargando datasets..." />
    <ErrorMessage v-else-if="error" :mensaje="error" @reintentar="emit('reintentar')" />
    <p v-else-if="datasets.length === 0" class="lista__vacio">
      No hay datasets todavía.
    </p>
    <div v-else class="lista__tarjetas">
      <DatasetCard
        v-for="dataset in datasets"
        :key="dataset.id"
        :dataset="dataset"
        @editar="emit('editar', $event)"
        @eliminar="emit('eliminar', $event)"
      />
    </div>
  </div>
</template>
```

### `LoadingState.vue`

```vue
<script setup lang="ts">
defineProps<{ mensaje?: string }>()
</script>

<template>
  <div class="cargando" role="status">
    <p>{{ mensaje ?? 'Cargando...' }}</p>
  </div>
</template>
```

### `ErrorMessage.vue`

```vue
<script setup lang="ts">
defineProps<{ mensaje: string }>()
const emit = defineEmits<{ reintentar: [] }>()
</script>

<template>
  <div class="error" role="alert">
    <p>{{ mensaje }}</p>
    <button @click="emit('reintentar')">Reintentar</button>
  </div>
</template>
```

### Modal en `index.vue`

```vue
<script setup lang="ts">
// ... imports existentes

const {
  datasets,
  loading,
  error: errorDatasets,
  obtenerDatasets,
  crearDataset,
  actualizarDataset,
  eliminarDataset,
} = useDatasets()

const mostrarModal = ref(false)
const modoModal = ref<'crear' | 'editar'>('crear')
const datasetEditando = ref<Dataset | null>(null)
const mensaje = ref<{ tipo: 'exito' | 'error'; texto: string } | null>(null)
const enviando = ref(false)

let temporizadorMensaje: ReturnType<typeof setTimeout> | undefined

onMounted(() => {
  obtenerDatasets()
  // ... resto del onMounted existente
})

function mostrarMensaje(tipo: 'exito' | 'error', texto: string) {
  mensaje.value = { tipo, texto }
  clearTimeout(temporizadorMensaje)
  temporizadorMensaje = setTimeout(() => {
    mensaje.value = null
  }, 3000)
}

function abrirCrear() {
  modoModal.value = 'crear'
  datasetEditando.value = null
  mostrarModal.value = true
}

function abrirEditar(dataset: Dataset) {
  modoModal.value = 'editar'
  datasetEditando.value = dataset
  mostrarModal.value = true
}

async function alGuardar(datos: { name: string; description: string | null; file_name: string }) {
  enviando.value = true
  try {
    if (modoModal.value === 'crear') {
      await crearDataset(datos)
      mostrarMensaje('exito', 'Dataset creado correctamente.')
    } else if (datasetEditando.value) {
      await actualizarDataset(datasetEditando.value.id, {
        ...datos,
        created_at: datasetEditando.value.created_at,
      })
      mostrarMensaje('exito', 'Dataset actualizado correctamente.')
    }
    mostrarModal.value = false
  } catch {
    mostrarMensaje('error', 'No se pudo guardar el dataset. Inténtalo de nuevo.')
  } finally {
    enviando.value = false
  }
}

async function alEliminar(id: number) {
  enviando.value = true
  try {
    await eliminarDataset(id)
    mostrarMensaje('exito', 'Dataset eliminado correctamente.')
  } catch {
    mostrarMensaje('error', 'No se pudo eliminar el dataset. Inténtalo de nuevo.')
  } finally {
    enviando.value = false
  }
}

function alCancelar() {
  mostrarModal.value = false
}
</script>
```

## 6. Cobertura de RFs

| RF | Dónde se implementa |
|----|---------------------|
| RF-01 | `frontend/app/composables/useDatasets.ts` |
| RF-02 | `frontend/app/components/DatasetList.vue` |
| RF-03 | `frontend/app/components/DatasetCard.vue` |
| RF-04 | `frontend/app/components/DatasetForm.vue` |
| RF-05 | `frontend/app/components/LoadingState.vue` + `frontend/app/components/ErrorMessage.vue` |
| RF-06 | `frontend/app/pages/index.vue` + `frontend/app/components/AppHeader.vue` |
| RF-07 | `frontend/app/pages/index.vue` (modal de creación) |
| RF-08 | `frontend/app/pages/index.vue` (modal de edición) |
| RF-09 | `frontend/app/pages/index.vue` (eliminación con confirmación) |
| RF-10 | `frontend/app/pages/index.vue` (mensajes de éxito/error) |
| RF-11 | `docs/conceptos-nivel-4.md` |

## 7. Orden de implementación

1. **T1**: `useDatasets.ts` — Composable base
2. **T2**: `LoadingState.vue` + `ErrorMessage.vue` — Componentes de estado
3. **T3**: `DatasetCard.vue` — Tarjeta individual
4. **T4**: `DatasetForm.vue` — Formulario
5. **T5**: `DatasetList.vue` — Lista
6. **T6**: Integración en `index.vue` — Sección completa
7. **T7**: Enlace en `AppHeader.vue` — Menú
8. **T8**: Documentación — Conceptos
9. **T9**: Verificación manual de criterios

## 8. Estrategia de verificación

- **Sin tests automatizados**: la verificación es manual con navegador (decisión de la usuaria, 2026-10-03).
- **Pasos de verificación**:
  1. Arrancar backend (`uvicorn app.main:app --reload`) y frontend (`npm run dev`).
  2. Abrir `http://localhost:3000` y comprobar que la sección "Gestión de datasets" carga la lista.
  3. Crear un dataset y comprobar que aparece en la lista.
  4. Editar un dataset y comprobar que la lista se actualiza.
  5. Eliminar un dataset con confirmación y comprobar que desaparece.
  6. Comprobar validaciones del formulario (campos vacíos, longitudes).
  7. Comprobar mensajes de éxito/error y su auto-cierre a 3s.
  8. Detener el backend y comprobar que se muestra un mensaje de error en español.
