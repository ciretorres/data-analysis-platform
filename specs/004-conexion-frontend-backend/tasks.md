# Tareas — Spec 004 (Nivel 3)

**Plan**: `plan.md` · **Formato**: skill spec-driven-development · **Total**: 6 tareas (sin tests automatizados: verificación manual)

- [x] **1. Endpoint `/api/health` y CORS** — `backend/app/main.py`
  - RF: RF-01, RF-02
  - Hecho cuando: `GET /api/health` devuelve 200 con `app_name`, `status`, `version` y `response_date`; el backend acepta peticiones desde `http://localhost:3000` sin errores de CORS.

- [x] **2. Composable `useApi`** — `frontend/app/composables/useApi.ts`
  - RF: RF-03, RF-04
  - Hecho cuando: el composable acepta una URL, usa `fetch`, devuelve estado de carga, error y datos; lee `NUXT_PUBLIC_API_BASE` con default `http://localhost:8000`.

- [x] **3. Sección "Estado de la API"** — `frontend/app/pages/index.vue`
  - RF: RF-05
  - Hecho cuando: la página muestra estado de carga, error en español o los 4 datos según corresponda; la petición se hace al abrir la página.

- [x] **4. Enlace en el menú** — `frontend/app/components/AppHeader.vue`
  - RF: RF-05
  - Hecho cuando: el menú incluye "Estado de la API" y desplaza a la sección.

- [x] **5. Documentación de conceptos** — `docs/conceptos-nivel-3.md`
  - RF: RF-06, RNF-01
  - Hecho cuando: los conceptos del nivel (peticiones HTTP, métodos GET/POST, JSON, fetch, composables, variables de entorno, estados de carga, manejo de errores, CORS, comunicación frontend-backend) tienen explicación breve en español.

- [x] **6. Verificación manual de criterios** — navegador + `curl`
  - RF: RF-01 … RF-06 (los 6), RNF-02, RNF-03
  - Hecho cuando: los 7 criterios de finalización de la spec se cumplen a mano, incluido backend detenido (mensaje de error en español).

**Estado**: 0/6 completadas.
