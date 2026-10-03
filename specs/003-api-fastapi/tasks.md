# Tareas — Spec 003 (Nivel 2)

**Plan**: `plan.md` · **Formato**: skill spec-driven-development · **Total**: 7 tareas (sin tests automatizados: verificación manual)

- [x] **1. Modelos Pydantic** — `backend/app/models/dataset.py`
  - RF: RF-02, RF-05
  - Hecho cuando: existen `DatasetCreate`, `DatasetUpdate` y `Dataset` con los campos y longitudes de la spec; `id` y `created_at` no se piden en `DatasetCreate`; los campos extra se ignoran.

- [x] **2. Router CRUD con lista en memoria** — `backend/app/routers/datasets.py`
  - RF: RF-03, RF-04, RF-05, CL-01, CL-02, CL-03, CL-04, CL-05, CL-06, CL-07, CL-08, CL-09, CL-10, CL-11, CL-12, CL-13, CL-14, CL-15, CL-16, CL-17
  - Hecho cuando: los 5 endpoints funcionan con la lista en memoria; POST devuelve 201 con `id`/`created_at` generados; GET devuelve 200 (o 404 en español); PUT es reemplazo completo (200/422/404); DELETE devuelve 204 (o 404); el `id` no se reutiliza; al reiniciar la lista vuelve a vacía.

- [x] **3. Aplicación principal y health** — `backend/app/main.py`
  - RF: RF-01, CL-01 (health)
  - Hecho cuando: `uvicorn app.main:app --reload` levanta sin errores en :8000; `GET /health` devuelve 200 con `{"status":"ok","message":"API funcionando correctamente","version":"1.0.0"}`; `GET /` sigue devolviendo la bienvenida; el router de datasets está montado.

- [x] **4. Documentación de endpoints en español** — docstrings en `main.py` y `routers/datasets.py`
  - RF: RF-06
  - Hecho cuando: `/docs` muestra los 6 endpoints con resumen, parámetros y respuestas documentados en español.

- [x] **5. Documentación de conceptos** — `docs/conceptos-nivel-2.md`
  - RF: RF-07, RNF-01
  - Hecho cuando: los conceptos de la ruta (API REST, CRUD, rutas, parámetros, parámetros de ruta, cuerpos de petición, validación de datos, respuestas HTTP, códigos de estado, métodos HTTP, separación entre modelos y rutas, JSON, documentación automática, servidor de desarrollo) tienen explicación breve en español.

- [x] **6. Verificación manual de criterios** — `/docs` + `curl`
  - RF: RF-01 … RF-08 (los 8), RNF-02, RNF-03, RNF-04
  - Hecho cuando: los 13 criterios de finalización de la spec se cumplen a mano con `curl` y la documentación automática.

- [x] **7. Cierre del nivel** — `MEMORY.md` + `CHANGELOG.md`
  - RF: RF-01 … RF-08 (los 8)
  - Hecho cuando: `MEMORY.md` refleja el estado del nivel 2, el `CHANGELOG.md` tiene las entradas de los commits (con hash corto, categoría y enlace) y `git status` está limpio.

**Estado**: 0/7 completadas.
