# Plan de implementación — Spec 006 (Nivel 5)

**Fecha**: 2026-10-10 · **Estado**: Pendiente de aprobación

## 1. Archivos a crear/modificar y responsabilidades

| Archivo | Responsabilidad | RF cubierto |
|---------|----------------|-------------|
| `backend/requirements.txt` | Añadir Pandas como dependencia del backend. | RF-01 |
| `backend/app/routers/upload.py` | Router nuevo con endpoint `POST /api/datasets/upload` que recibe archivo, valida, lee con Pandas y devuelve resumen. | RF-02, RF-03, RF-04, RF-05, RF-06 |
| `backend/app/main.py` | Registrar el router de upload incluyendo el prefijo `/api` y el tag. | RF-02 |
| `frontend/app/composables/useUpload.ts` | Composable que encapsula la lógica de subida de archivos con `fetch` y `FormData`. Devuelve estado reactivo y función de subida. | RF-07 |
| `frontend/app/components/FileUpload.vue` | Componente de selección y subida de archivo con estado de carga y manejo de errores. | RF-08 |
| `frontend/app/components/DataSummary.vue` | Componente que muestra el resumen de datos (estadísticas, preview, etc.). | RF-09 |
| `frontend/app/pages/index.vue` | Añadir sección "Procesar archivo" que integra `FileUpload` y `DataSummary`. | RF-10 |
| `frontend/app/components/AppHeader.vue` | Añadir enlace "Procesar archivo" al menú de navegación. | RF-10 |
| `docs/conceptos-nivel-5.md` | Documentación de conceptos del nivel 5 (Pandas, DataFrames, UploadFile, etc.). | RF-11 |

## 2. Decisiones técnicas y justificación

| Decisión | Justificación | RF/RNF |
|----------|---------------|--------|
| **`fetch` directo en `useUpload`** | El `useApi` del nivel 3 solo soporta GET sin cuerpo. Para POST con `FormData` se usa `fetch` directamente. | RF-07 |
| **`UploadFile` de FastAPI** | Es la forma estándar de recibir archivos en FastAPI. Proporciona `filename`, `content_type` y `file`. | RF-02, RF-05 |
| **Validación de extensión en el backend** | La validación en el frontend es solo visual; el backend debe validar realmente. | RF-03 |
| **Validación de tamaño en el backend** | El backend debe rechazar archivos > 10 MB antes de procesarlos. | RF-04 |
| **Estadísticas solo para columnas numéricas** | La spec especifica que `df.describe()` solo incluye columnas numéricas. | RF-02, CL-10, CL-11 |
| **Preview limitado a 5 filas** | La spec especifica máximo 5 filas en `preview`. | RF-02 |
| **Sin persistencia en disco** | Los archivos se procesan en memoria y no se guardan. | RNF-04 |
| **Respuesta JSON con `orient='records'`** | Para el preview se usa `df.head().to_dict(orient='records')` para obtener objetos. | RF-02 |
| **Manejo de errores con `HTTPException`** | FastAPI usa `HTTPException` para devolver errores 400 y 500 con mensajes en español. | RF-03, RF-04, RF-05, RF-06 |
| **Componentes de estado reutilizables** | Se reutilizan `LoadingState` y `ErrorMessage` del nivel 4. | RNF-06 |

## 3. Funciones puras con "hoy" como parámetro

Este nivel incluye lógica de backend con Pandas. No hay funciones puras con "hoy" como parámetro porque:
- Las estadísticas se calculan con `df.describe()` que no depende de la fecha.
- El preview se obtiene con `df.head(5)` que no depende de la fecha.
- Los valores nulos se cuentan con `df.isnull().sum()` que no depende de la fecha.
- No hay lógica de fechas en el procesamiento de archivos.

## 4. Estructura del endpoint `POST /api/datasets/upload`

```python
# backend/app/routers/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io

router = APIRouter()

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {'.csv', '.json'}

@router.post("/datasets/upload")
async def subir_archivo(archivo: UploadFile = File(...)):
    # Validar extensión
    nombre = archivo.filename or ""
    extension = "." + nombre.split(".")[-1].lower() if "." in nombre else ""
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Formato no válido. Solo se permiten archivos .csv y .json."
        )

    # Leer contenido
    contenido = await archivo.read()

    # Validar tamaño
    if len(contenido) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="El archivo es demasiado grande. El máximo es 10 MB."
        )

    # Validar que no esté vacío
    if len(contenido) == 0:
        raise HTTPException(
            status_code=400,
            detail="El archivo está vacío."
        )

    # Leer con Pandas
    try:
        if extension == ".csv":
            df = pd.read_csv(io.BytesIO(contenido))
        else:
            df = pd.read_json(io.BytesIO(contenido))
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="No se pudo leer el archivo. Verifica que esté bien formado."
        )

    # Validar JSON tabular
    if extension == ".json" and df.empty and not df.columns.tolist():
        raise HTTPException(
            status_code=400,
            detail="El JSON no tiene un formato tabular válido."
        )

    # Calcular estadísticas
    estadisticas = {}
    for columna in df.select_dtypes(include="number").columns:
        desc = df[columna].describe()
        estadisticas[columna] = {
            "count": int(desc["count"]),
            "mean": float(desc["mean"]),
            "std": float(desc["std"]),
            "min": float(desc["min"]),
            "25%": float(desc["25%"]),
            "50%": float(desc["50%"]),
            "75%": float(desc["75%"]),
            "max": float(desc["max"]),
        }

    # Valores nulos
    valores_nulos = {col: int(df[col].isnull().sum()) for col in df.columns}

    # Preview (primeras 5 filas)
    preview = df.head(5).to_dict(orient="records")

    return {
        "file_name": nombre,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist(),
        "missing_values": valores_nulos,
        "statistics": estadisticas,
        "preview": preview,
    }
```

## 5. Estructura del composable `useUpload`

```typescript
// frontend/app/composables/useUpload.ts
import { ref } from 'vue'

export interface DataSummary {
  file_name: string
  rows: number
  columns: number
  column_names: string[]
  missing_values: Record<string, number>
  statistics: Record<string, {
    count: number
    mean: number
    std: number
    min: number
    '25%': number
    '50%': number
    '75%': number
    max: number
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
```

## 6. Estructura de los componentes

### `FileUpload.vue`

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { useUpload } from '~/composables/useUpload'
import LoadingState from './LoadingState.vue'
import ErrorMessage from './ErrorMessage.vue'

const { loading, error, summary, subirArchivo } = useUpload()

const archivoSeleccionado = ref<File | null>(null)
const nombreArchivo = ref('')

function alSeleccionar(event: Event) {
  const input = event.target as HTMLInputElement
  if (input.files && input.files.length > 0) {
    archivoSeleccionado.value = input.files[0]
    nombreArchivo.value = input.files[0].name
  }
}

async function alSubir() {
  if (!archivoSeleccionado.value) return
  await subirArchivo(archivoSeleccionado.value)
}
</script>

<template>
  <section class="subida">
    <h2>Procesar archivo</h2>
    <p>Selecciona un archivo CSV o JSON para ver un resumen de sus datos.</p>

    <div class="subida__controles">
      <input
        type="file"
        accept=".csv,.json"
        @change="alSeleccionar"
        :disabled="loading"
      />
      <button @click="alSubir" :disabled="!archivoSeleccionado || loading">
        Subir
      </button>
    </div>

    <p v-if="nombreArchivo" class="subida__nombre">
      Archivo seleccionado: <strong>{{ nombreArchivo }}</strong>
    </p>

    <LoadingState v-if="loading" mensaje="Procesando archivo..." />
    <ErrorMessage v-else-if="error" :mensaje="error" @reintentar="alSubir" />

    <DataSummary v-else-if="summary" :summary="summary" />
  </section>
</template>
```

### `DataSummary.vue`

```vue
<script setup lang="ts">
import type { DataSummary } from '~/composables/useUpload'

const props = defineProps<{ summary: DataSummary }>()

function formatearNumero(n: number): string {
  return new Intl.NumberFormat('es-ES', { maximumFractionDigits: 2 }).format(n)
}
</script>

<template>
  <section class="resumen">
    <h3>Resumen: {{ summary.file_name }}</h3>

    <div class="resumen__grid">
      <div class="resumen__item">
        <span class="resumen__label">Filas:</span>
        <span class="resumen__valor">{{ summary.rows }}</span>
      </div>
      <div class="resumen__item">
        <span class="resumen__label">Columnas:</span>
        <span class="resumen__valor">{{ summary.columns }}</span>
      </div>
    </div>

    <div class="resumen__seccion">
      <h4>Columnas</h4>
      <ul>
        <li v-for="col in summary.column_names" :key="col">{{ col }}</li>
      </ul>
    </div>

    <div class="resumen__seccion">
      <h4>Valores nulos por columna</h4>
      <ul>
        <li v-for="(valor, col) in summary.missing_values" :key="col">
          {{ col }}: {{ valor }}
        </li>
      </ul>
    </div>

    <div v-if="Object.keys(summary.statistics).length > 0" class="resumen__seccion">
      <h4>Estadísticas descriptivas</h4>
      <div v-for="(stats, col) in summary.statistics" :key="col" class="resumen__stats">
        <h5>{{ col }}</h5>
        <ul>
          <li>Count: {{ stats.count }}</li>
          <li>Mean: {{ formatearNumero(stats.mean) }}</li>
          <li>Std: {{ formatearNumero(stats.std) }}</li>
          <li>Min: {{ formatearNumero(stats.min) }}</li>
          <li>25%: {{ formatearNumero(stats['25%']) }}</li>
          <li>50%: {{ formatearNumero(stats['50%']) }}</li>
          <li>75%: {{ formatearNumero(stats['75%']) }}</li>
          <li>Max: {{ formatearNumero(stats.max) }}</li>
        </ul>
      </div>
    </div>

    <div class="resumen__seccion">
      <h4>Vista previa (primeras 5 filas)</h4>
      <table class="resumen__tabla">
        <thead>
          <tr>
            <th v-for="col in summary.column_names" :key="col">{{ col }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(fila, i) in summary.preview" :key="i">
            <td v-for="col in summary.column_names" :key="col">
              {{ fila[col] ?? 'null' }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>
```

### Integración en `index.vue`

```vue
<script setup lang="ts">
// ... imports existentes
import FileUpload from '~/components/FileUpload.vue'

// ... resto del script
</script>

<template>
  <div>
    <!-- ... secciones existentes -->

    <FileUpload />
  </div>
</template>
```

### Enlace en `AppHeader.vue`

```vue
<script setup lang="ts">
// ... existente
const enlaces = [
  { texto: 'Gestión de datasets', href: '#gestion-datasets' },
  { texto: 'Procesar archivo', href: '#procesar-archivo' },
]
</script>
```

## 7. Cobertura de RFs

| RF | Dónde se implementa |
|----|---------------------|
| RF-01 | `backend/requirements.txt` |
| RF-02 | `backend/app/routers/upload.py` |
| RF-03 | `backend/app/routers/upload.py` |
| RF-04 | `backend/app/routers/upload.py` |
| RF-05 | `backend/app/routers/upload.py` |
| RF-06 | `backend/app/routers/upload.py` |
| RF-07 | `frontend/app/composables/useUpload.ts` |
| RF-08 | `frontend/app/components/FileUpload.vue` |
| RF-09 | `frontend/app/components/DataSummary.vue` |
| RF-10 | `frontend/app/pages/index.vue` + `frontend/app/components/AppHeader.vue` |
| RF-11 | `docs/conceptos-nivel-5.md` |

## 8. Orden de implementación

1. **T1**: Instalar Pandas en `backend/requirements.txt`
2. **T2**: Crear `backend/app/routers/upload.py` con endpoint de subida
3. **T3**: Registrar router en `backend/app/main.py`
4. **T4**: Crear `frontend/app/composables/useUpload.ts`
5. **T5**: Crear `frontend/app/components/FileUpload.vue`
6. **T6**: Crear `frontend/app/components/DataSummary.vue`
7. **T7**: Integrar sección en `frontend/app/pages/index.vue`
8. **T8**: Añadir enlace en `frontend/app/components/AppHeader.vue`
9. **T9**: Documentar conceptos en `docs/conceptos-nivel-5.md`
10. **T10**: Verificación manual de criterios

## 9. Estrategia de verificación

- **Sin tests automatizados**: la verificación es manual con navegador (decisión de la usuaria).
- **Pasos de verificación**:
  1. Instalar Pandas: `pip install pandas` en el entorno virtual.
  2. Arrancar backend (`uvicorn app.main:app --reload`) y frontend (`npm run dev`).
  3. Probar endpoint con `curl` o frontend:
     - Subir CSV válido → verificar resumen correcto.
     - Subir JSON válido → verificar resumen correcto.
     - Subir archivo con extensión no permitida → verificar 400.
     - Subir archivo > 10 MB → verificar 400.
     - Subir archivo malformado → verificar 400.
  4. En el frontend:
     - Seleccionar archivo → verificar que se muestra el nombre.
     - Subir archivo → verificar estado de carga.
     - Verificar resumen mostrado correctamente.
     - Verificar mensajes de error.
  5. Detener backend → verificar mensaje de error en frontend.
