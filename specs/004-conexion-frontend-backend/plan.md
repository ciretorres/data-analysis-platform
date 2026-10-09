# Plan de implementación — Spec 004 (Nivel 3)

**Fecha**: 2026-10-06 · **Estado**: Pendiente de aprobación

## 1. Archivos a crear/modificar y responsabilidades

| Archivo | Responsabilidad | RF cubierto |
|---------|----------------|-------------|
| `backend/app/main.py` | Añadir `GET /api/health` (4 campos) y configurar CORS con `CORSMiddleware`. | RF-01, RF-02 |
| `frontend/app/composables/useApi.ts` | Composable genérico que encapsula peticiones HTTP con `fetch`: devuelve estado de carga, error y datos. | RF-03, RF-04 |
| `frontend/app/pages/index.vue` | Añadir sección "Estado de la API" que usa `useApi` para consumir `/api/health`. | RF-05 |
| `frontend/app/components/AppHeader.vue` | Añadir enlace "Estado de la API" al menú de navegación. | RF-05 |
| `docs/conceptos-nivel-3.md` | Documentación de conceptos del nivel 3 (peticiones HTTP, CORS, composables, etc.). | RF-06 |

## 2. Decisiones técnicas y justificación

| Decisión | Justificación | RF/RNF |
|----------|---------------|--------|
| **`/api/health` como endpoint nuevo** | El nivel 3 pide 4 campos distintos a `/health` del nivel 2. Se conserva el existente. | RF-01 |
| **CORS con `CORSMiddleware`** | RF-02 exige aceptar peticiones desde `http://localhost:3000`. | RF-02 |
| **Composable genérico con parámetro URL** | Más educativo y reutilizable; no atado a un solo endpoint. | RF-04 |
| **`fetch` nativo del navegador** | RF-04 lo especifica; no requiere dependencias extra. | RF-04 |
| **Variable `NUXT_PUBLIC_API_BASE`** | Nuxt expone variables `NUXT_PUBLIC_*` al frontend automáticamente. | RF-03 |
| **Default `http://localhost:8000`** | RF-03: si la variable no está definida, usar esta URL. | RF-03 |
| **Sección en `index.vue`** | Opción A elegida por la usuaria: nueva sección en la página existente. | RF-05 |
| **Enlace en el menú** | La sección nueva debe ser accesible desde la navegación. | RF-05 |

## 3. Estructura del composable `useApi`

```typescript
// frontend/app/composables/useApi.ts
export function useApi<T>(url: string) {
  const datos = ref<T | null>(null)
  const cargando = ref(false)
  const error = ref<string | null>(null)

  async function pedir() {
    cargando.value = true
    error.value = null
    try {
      const respuesta = await fetch(url)
      if (!respuesta.ok) throw new Error(`Error ${respuesta.status}`)
      datos.value = await respuesta.json()
    } catch (e) {
      error.value = 'No se pudo conectar con el servidor. Inténtalo de nuevo.'
    } finally {
      cargando.value = false
    }
  }

  return { datos, cargando, error, pedir }
}
```

## 4. Cobertura de RFs

| RF | Dónde se implementa |
|----|---------------------|
| RF-01 | `backend/app/main.py` (endpoint `/api/health`) |
| RF-02 | `backend/app/main.py` (`CORSMiddleware`) |
| RF-03 | `frontend/app/composables/useApi.ts` (variable de entorno) |
| RF-04 | `frontend/app/composables/useApi.ts` (composable genérico) |
| RF-05 | `frontend/app/pages/index.vue` + `frontend/app/components/AppHeader.vue` |
| RF-06 | `docs/conceptos-nivel-3.md` |
