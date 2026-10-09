# Plan de implementación — Spec 003 (Nivel 2)

**Fecha**: 2026-10-03 · **Estado**: Pendiente de aprobación

## 1. Archivos a crear/modificar y responsabilidades

| Archivo | Responsabilidad | RF cubierto |
|---------|----------------|-------------|
| `backend/app/main.py` | Crea la aplicación FastAPI (versión 1.0.0), conserva `GET /` y amplía `GET /health` a `{"status","message","version"}`, y monta el router de datasets. | RF-01 |
| `backend/app/models/dataset.py` | Define los modelos Pydantic: `DatasetCreate` (entrada de POST), `DatasetUpdate` (entrada de PUT) y `Dataset` (salida). | RF-02, RF-05 |
| `backend/app/routers/datasets.py` | Define los 5 endpoints CRUD (`GET/POST /api/datasets`, `GET/PUT/DELETE /api/datasets/{id}`) con la lista en memoria y los códigos de estado 200/201/204/404/422. | RF-03, RF-04, RF-05 |
| `docs/conceptos-nivel-2.md` | Documentación de conceptos del nivel 2 (API REST, CRUD, rutas, etc.). | RF-07 |

## 2. Modelos Pydantic

| Modelo | Campos | Uso |
|--------|--------|-----|
| `DatasetCreate` | `name` (obligatorio, máx 100), `description` (opcional, máx 500), `file_name` (obligatorio, máx 255) | Entrada de `POST /api/datasets` |
| `DatasetUpdate` | Igual que `DatasetCreate` + `created_at` (fecha AAAA-MM-DD) | Entrada de `PUT /api/datasets/{id}` |
| `Dataset` | `id`, `name`, `description`, `file_name`, `created_at` | Salida de todos los endpoints |

- `id` y `created_at` NO se piden en `DatasetCreate`: los genera el servidor.
- Los campos extra no definidos se ignoran (comportamiento por defecto de
  Pydantic).

## 3. Lista en memoria

- Una variable a nivel de módulo en `app/routers/datasets.py` (ej.
  `datasets: list[Dataset] = []`).
- Al arrancar o reiniciar el servidor la lista empieza vacía.
- El `id` se genera como el mayor `id` actual + 1 (no se reutiliza tras un
  DELETE).

## 4. Decisiones técnicas y justificación

| Decisión | Justificación | RF/RNF |
|----------|---------------|--------|
| **Modelos en `app/models/`** | RF-08 exige separar modelos de rutas. | RF-08 |
| **Rutas en `app/routers/`** | RF-08 exige separar modelos de rutas; FastAPI recomienda `APIRouter`. | RF-08 |
| **Montaje en `app/main.py`** | RF-08: `main.py` crea la app y monta el router. | RF-08 |
| **Lista en memoria** | RF-03 y RNF-04 exigen sin persistencia. | RF-03, RNF-04 |
| **Códigos 200/201/204/404/422** | RF-04 exige códigos de estado apropiados. | RF-04 |
| **PUT de reemplazo completo** | La ruta del nivel define PUT (no PATCH). | RF-04 |
| **`id` y `created_at` automáticos** | RF-02: el servidor los genera en POST. | RF-02 |
| **Validación con Pydantic** | RF-05 exige validación de datos. | RF-05 |
| **Formato estándar de FastAPI en 422** | Fuera de alcance: sin manejador de errores personalizado. | RF-05 |
| **Sin tests automatizados** | Decisión de la usuaria: verificación manual (ver Dudas abiertas). | — |
| **Versión 1.0.0** | La ruta del nivel fija `version: "1.0.0"` en `/health`. | RF-01 |

## 5. Cobertura de RFs

| RF | Dónde se implementa |
|----|---------------------|
| RF-01 | `backend/app/main.py` (app, `/`, `/health`, montaje del router) |
| RF-02 | `backend/app/models/dataset.py` (modelos Pydantic) |
| RF-03 | `backend/app/routers/datasets.py` (lista en memoria) |
| RF-04 | `backend/app/routers/datasets.py` (5 endpoints CRUD) |
| RF-05 | `backend/app/models/dataset.py` (validaciones) + formato 422 de FastAPI |
| RF-06 | Docstrings en español en `backend/app/routers/datasets.py` y `backend/app/main.py` |
| RF-07 | `docs/conceptos-nivel-2.md` |
| RF-08 | Separación en `models/`, `routers/` y `main.py` |
