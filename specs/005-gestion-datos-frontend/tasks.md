# Tareas — Spec 005 (Nivel 4)

**Plan**: `plan.md` · **Formato**: skill spec-driven-development · **Total**: 9 tareas (sin tests automatizados: verificación manual)

- [x] **1. Composable `useDatasets`** — `frontend/app/composables/useDatasets.ts`
  - RF: RF-01
  - CL: CL-04, CL-10, CL-11, CL-14, CL-16
  - Dependencias: ninguna
  - Hecho cuando: el composable devuelve `datasets`, `loading`, `error`, `obtenerDatasets()`, `crearDataset(datos)`, `actualizarDataset(id, datos)` y `eliminarDataset(id)`; usa `useApi` para GET y `fetch` para POST/PUT/DELETE; actualiza la lista localmente después de cada operación exitosa; hace un GET si recibe 404.

- [x] **2. Componentes de estado `LoadingState` y `ErrorMessage`** — `frontend/app/components/LoadingState.vue`, `frontend/app/components/ErrorMessage.vue`
  - RF: RF-05
  - CL: CL-02, CL-03
  - Dependencias: ninguna
  - Hecho cuando: `LoadingState` muestra un mensaje configurable (default "Cargando..."); `ErrorMessage` muestra un mensaje de error con botón de reintento y emite `reintentar`; ambos son reutilizables.

- [x] **3. Componente `DatasetCard`** — `frontend/app/components/DatasetCard.vue`
  - RF: RF-03
  - CL: CL-09, CL-11, CL-12
  - Dependencias: ninguna
  - Hecho cuando: muestra nombre, descripción, archivo y fecha en formato español; tiene botones de editar y eliminar; pide confirmación con `window.confirm()` antes de emitir `eliminar`.

- [x] **4. Componente `DatasetForm`** — `frontend/app/components/DatasetForm.vue`
  - RF: RF-04
  - CL: CL-05, CL-06, CL-07, CL-08, CL-15, CL-17, CL-18, CL-19
  - Dependencias: ninguna
  - Hecho cuando: en modo "crear" muestra campos vacíos; en modo "editar" muestra datos actuales; valida `name` (obligatorio, max 100) y `file_name` (obligatorio, max 255); muestra errores por campo; emite `guardar` y `cancelar`; botón deshabilitado mientras envía.

- [x] **5. Componente `DatasetList`** — `frontend/app/components/DatasetList.vue`
  - RF: RF-02
  - CL: CL-01
  - Dependencias: T2, T3
  - Hecho cuando: muestra lista de `DatasetCard`; muestra "No hay datasets" si la lista está vacía; muestra `LoadingState` si está cargando; muestra `ErrorMessage` si hay error.

- [x] **6. Integración en `index.vue`** — `frontend/app/pages/index.vue`
  - RF: RF-06, RF-07, RF-08, RF-09, RF-10
  - CL: CL-01, CL-02, CL-03, CL-04, CL-09, CL-10, CL-11, CL-12, CL-13, CL-14, CL-15, CL-16, CL-17, CL-18, CL-19, CL-20
  - Dependencias: T1, T2, T3, T4, T5
  - Hecho cuando: la página tiene una sección "Gestión de datasets" que carga la lista al abrir; muestra `LoadingState`, `ErrorMessage` o la lista; tiene botón "Nuevo dataset" que abre modal de creación; tiene modal de edición; tiene eliminación con confirmación; muestra mensajes de éxito/error que desaparecen a los 3s.

- [x] **7. Enlace en el menú** — `frontend/app/components/AppHeader.vue`
  - RF: RF-06
  - Dependencias: T6
  - Hecho cuando: el menú incluye "Gestión de datasets" y desplaza a la sección.

- [x] **8. Documentación de conceptos** — `docs/conceptos-nivel-4.md`
  - RF: RF-11, RNF-01
  - Dependencias: ninguna
  - Hecho cuando: los conceptos del nivel (formularios controlados, estado reactivo, componentes reutilizables, actualización de datos, composables de Nuxt, separación entre lógica y presentación, manejo de errores del servidor, CRUD desde el frontend, confirmación de acciones destructivas) tienen explicación breve en español.

- [x] **9. Verificación manual de criterios** — navegador + `curl`
  - RF: RF-01 … RF-11 (los 11), RNF-02, RNF-03
  - Dependencias: T1-T8
  - Hecho cuando: los 13 criterios de finalización de la spec se cumplen a mano, incluido backend detenido (mensaje de error en español), lista vacía, crear, editar, eliminar, validaciones y mensajes.

**Estado**: 9/9 completadas.
