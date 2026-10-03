# Spec 003 — API básica con FastAPI (CRUD de Dataset)

**Nivel**: 2 · **Estado**: Revisada por QA (pendiente de aprobación de la usuaria) · **Fecha**: 2026-10-03 · **Revisada**: 2026-10-03 (QA)

## Contexto

El nivel 1 dejó la interfaz funcionando sin conexión al backend. El nivel 2 da
el salto al backend: crear una API REST sencilla con FastAPI que permita
administrar conjuntos de datos (la entidad `Dataset`) con operaciones CRUD
completas, usando una lista en memoria y validación con Pydantic. La interfaz
del nivel 1 NO se toca: este nivel es solo backend.

La entidad principal es `Dataset`:

```json
{
  "id": 1,
  "name": "Ventas mensuales",
  "description": "Datos de ventas del año actual",
  "file_name": "ventas.csv",
  "created_at": "2026-09-29"
}
```

Endpoints de la API:

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/health` | Estado del servidor (ampliado desde el nivel 0) |
| GET | `/api/datasets` | Obtener todos los conjuntos de datos |
| GET | `/api/datasets/{id}` | Obtener un conjunto específico |
| POST | `/api/datasets` | Crear un conjunto de datos |
| PUT | `/api/datasets/{id}` | Actualizar un conjunto (reemplazo completo) |
| DELETE | `/api/datasets/{id}` | Eliminar un conjunto |

## Objetivo

Que la principiante construya su primera API REST con FastAPI, entendiendo qué
es una API, qué es el CRUD y cómo se organizan rutas, modelos y validaciones,
antes de conectar la interfaz del nivel 1.

## Usuarias

- **Principiante total**: persona que ya sabe ejecutar backend y frontend por
  separado, pero nunca ha escrito una API ni un modelo de datos. Necesita
  probar cada endpoint a mano y ver la documentación generada automáticamente.

## Historia de usuaria

> Como principiante total, quiero crear una API sencilla que me permita
> crear, consultar, actualizar y eliminar conjuntos de datos, para entender
> cómo funciona una API REST antes de conectarla a la interfaz.

## Requisitos funcionales

**RF-01 — Aplicación FastAPI y endpoint de health ampliado**
La aplicación DEBERÁ levantarse con Uvicorn, DEBERÁ declarar la versión
`1.0.0` y DEBERÁ conservar la bienvenida del nivel 0 (`GET /`). El endpoint
`GET /health` DEBERÁ devolver código 200 con exactamente:

```json
{
  "status": "ok",
  "message": "API funcionando correctamente",
  "version": "1.0.0"
}
```

- CUANDO se arranque el servidor, entonces `uvicorn app.main:app --reload`
  DEBERÁ levantar la aplicación sin errores en el puerto 8000.
- CUANDO se consulte `/health`, entonces LA RESPUESTA DEBERÁ tener código 200
  y los tres campos con esos valores exactos.
- CUANDO se consulte `/`, entonces SE VERÁ el mensaje de bienvenida del nivel
  0, igual que antes.

**RF-02 — Modelo de datos Dataset con Pydantic**
La aplicación DEBERÁ definir modelos de entrada y salida con Pydantic,
separados de las rutas. El modelo DEBERÁ tener:

- `id`: entero, generado automáticamente por el servidor.
- `name`: cadena, obligatoria, no vacía, longitud máxima 100.
- `description`: cadena opcional, longitud máxima 500.
- `file_name`: cadena, obligatoria, no vacía, longitud máxima 255.
- `created_at`: fecha en formato AAAA-MM-DD.

- CUANDO se revise el modelo de creación (POST), entonces LOS CAMPOS `id` y
  `created_at` NO DEBERÁN pedirse en la entrada: los genera el servidor.
- CUANDO se revise el modelo de actualización (PUT), entonces `created_at`
  PODRÁ enviarse como parte del reemplazo completo.
- CUANDO el cliente envíe campos extra no definidos en el modelo, entonces
  ESTOS DEBERÁN ignorarse sin error.

**RF-03 — Almacenamiento en memoria**
Los datasets DEBERÁN guardarse en una lista en memoria (una variable a nivel
de módulo, sin base de datos ni ficheros).

- CUANDO se arranque o reinicie el servidor, entonces LA LISTA DEBERÁ empezar
  vacía.
- CUANDO se cree un dataset, entonces SE AÑADIRÁ a la lista con un `id`
  generado por el servidor. El `id` NO se reutiliza aunque se elimine el
  dataset.

**RF-04 — Endpoints CRUD**
La aplicación DEBERÁ exponer los 5 endpoints CRUD bajo el prefijo
`/api/datasets`, con códigos de estado HTTP apropiados:

- `GET /api/datasets` DEBERÁ devolver 200 con la lista completa de datasets.
- `GET /api/datasets/{id}` DEBERÁ devolver 200 con el dataset; si el `id` no
  existe, DEBERÁ devolver 404 con `{"detail": "Dataset no encontrado"}`.
- `POST /api/datasets` DEBERÁ devolver 201 con el dataset creado, incluyendo
  `id` y `created_at`.
- `PUT /api/datasets/{id}` DEBERÁ devolver 200 con el dataset actualizado; es
  reemplazo completo: si falta un campo obligatorio, DEBERÁ devolver 422; si el
  `id` no existe, DEBERÁ devolver 404. Si se omite `description`, DEBERÁ
  quedarse a nulo (no conserva el valor anterior).
- `DELETE /api/datasets/{id}` DEBERÁ devolver 204 sin cuerpo; si el `id` no
  existe, DEBERÁ devolver 404.

- CUANDO se cree, consulte, actualice o elimine un dataset, entonces LA LISTA
  EN MEMORIA DEBERÁ reflejar el cambio inmediatamente.
- CUANDO se elimine un dataset, entonces DESAPARECERÁ de la lista y las
  consultas posteriores DEVERÁN reflejarlo.

**RF-05 — Validación de datos**
La aplicación DEBERÁ validar los datos de entrada con Pydantic:

- SI falta `name` o está vacío, entonces LA RESPUESTA DEBERÁ ser 422.
- SI falta `file_name` o está vacío, entonces LA RESPUESTA DEBERÁ ser 422.
- SI `name` supera 100 caracteres o `description` supera 500, entonces LA
  RESPUESTA DEBERÁ ser 422.
- SI `created_at` en PUT no tiene formato AAAA-MM-DD, entonces LA RESPUESTA
  DEBERÁ ser 422.
- CUANDO se produzca un error de validación, entonces EL CUERPO DE LA
  RESPUESTA DEBERÁ seguir el formato estándar de FastAPI (422 con `detail`).

**RF-06 — Documentación automática y en español**
- CUANDO se abra `/docs`, entonces SE VERÁN los 6 endpoints con su resumen,
  parámetros y respuestas documentados en español.
- CADA endpoint DEBERÁ tener resumen y descripción en español, visibles en la
  documentación automática de FastAPI.

**RF-07 — Conceptos del nivel documentados**
La documentación del nivel 2 DEBERÁ presentar los conceptos de la ruta del
nivel (qué es una API REST, CRUD, rutas, parámetros, parámetros de ruta, cuerpos
de petición, validación de datos, respuestas HTTP, códigos de estado, métodos
HTTP, separación entre modelos y rutas, JSON, documentación automática,
servidor de desarrollo) con lenguaje comprensible para una principiante total.
Los nombres propios de conceptos técnicos se conservan en su forma original; el
resto del texto estará en español.

- DESPUÉS DE revisar la documentación, cuando se lea la sección de conceptos,
  entonces CADA concepto TENDRÁ una explicación breve en español.

**RF-08 — Separación entre modelos y rutas**
El código DEBERÁ separarse en tres piezas:

- `app/main.py`: crea la aplicación FastAPI y monta el router.
- `app/models/dataset.py`: define los modelos Pydantic.
- `app/routers/datasets.py`: define los endpoints CRUD.

- CUANDO se revise la estructura, entonces LA LÓGICA DE LAS RUTAS NO DEBERÁ
  mezclarse con la DEFINICIÓN DE LOS MODELOS.
- SI en un nivel posterior se añade persistencia, entonces PODRÁ hacerse
  tocando solo `main.py` y `routers/datasets.py`, sin reescribir los modelos.

## Requisitos no funcionales

- **RNF-01 — Legibilidad**: La documentación DEBERÁ ser comprensible para una
  principiante total.
- **RNF-02 — Idioma**: Todo texto, comentario y documentación estará en español.
  Los mensajes de error propios de la API (como el 404) estarán en español;
  los errores de validación usan el formato estándar de FastAPI.
- **RNF-03 — Todo en local**: La API DEBERÁ funcionar solo con el servidor de
  desarrollo local (Uvicorn), sin servicios externos.
- **RNF-04 — Sin persistencia**: Los datos SERÁN de ejemplo en memoria y SE
  PERDERÁN al reiniciar el servidor. NO DEBERÁ usar base de datos ni
  ficheros.
- **RNF-05 — Separación de responsabilidades**: El código DEBERÁ separar
  modelos, rutas y montaje de la aplicación para poder ampliarlo en niveles
  posteriores sin reescribirlo entero.
- **RNF-06 — Ampliación futura**: La estructura DEBERÁ permitir añadir
  persistencia real en un nivel posterior.

## Casos límite

- **CL-01**: `GET /api/datasets` con la lista vacía → 200 y `[]`.
- **CL-02**: `GET /api/datasets/{id}` con `id` inexistente → 404 con
  `{"detail": "Dataset no encontrado"}`.
- **CL-03**: `POST /api/datasets` sin `name` → 422.
- **CL-04**: `POST /api/datasets` con `name` vacío o solo espacios → 422.
- **CL-05**: `POST /api/datasets` sin `file_name` → 422.
- **CL-06**: `POST /api/datasets` con `name` de más de 100 caracteres → 422.
- **CL-07**: `POST /api/datasets` con `description` de más de 500 caracteres →
  422.
- **CL-08**: `PUT /api/datasets/{id}` con `id` inexistente → 404.
- **CL-09**: `PUT /api/datasets/{id}` que omite un campo obligatorio → 422
  (reemplazo completo).
- **CL-10**: `PUT /api/datasets/{id}` con todos los campos válidos → 200 y el
  dataset actualizado.
- **CL-11**: `PUT` con `created_at` en formato inválido → 422.
- **CL-12**: `DELETE /api/datasets/{id}` con `id` inexistente → 404.
- **CL-13**: `DELETE /api/datasets/{id}` con `id` válido → 204 y el dataset
  desaparece de la lista.
- **CL-14**: `POST /api/datasets` con datos válidos → 201 con `id` y
  `created_at` generados por el servidor.
- **CL-15**: Se reinicia el servidor → la lista vuelve a vacía.
- **CL-16**: `POST /api/datasets` con campos extra no definidos → se ignoran
  sin error.
- **CL-17**: `GET`, `PUT` o `DELETE` con `id` no numérico (ej.
  `/api/datasets/abc`) → 422 (validación automática de FastAPI).

## Fuera de alcance

- Persistencia en disco o base de datos (la lista en memoria se pierde al
  reiniciar).
- Subida real de archivos: `file_name` es solo un texto, no se guarda ningún
  archivo en el servidor.
- PATCH (actualizaciones parciales): solo PUT de reemplazo completo.
- Tests automatizados (la verificación es manual, con `/docs` y `curl`).
- Autenticación y autorización.
- Paginación, búsqueda o filtros.
- Manejador de errores de validación personalizado (se usa el formato estándar
  de FastAPI).
- Docker, CI/CD.
- Conexión con el frontend del nivel 1.

## Criterios de finalización

El nivel 2 se considera terminado cuando, con verificación manual (documentación
automática y `curl`), se cumplan TODAS:

1. `uvicorn app.main:app --reload` levanta la aplicación sin errores en el
   puerto 8000 (RF-01).
2. `GET /health` devuelve 200 con `status`, `message` y `version` exactos
   (RF-01).
3. `GET /` sigue devolviendo el mensaje de bienvenida del nivel 0 (RF-01).
4. `POST /api/datasets` con datos válidos devuelve 201 con `id` y `created_at`
   generados por el servidor (RF-02, RF-04).
5. `GET /api/datasets` lista lo creado y devuelve `[]` cuando está vacía
   (RF-04).
6. `GET /api/datasets/{id}` devuelve el dataset; un `id` inexistente devuelve
   404 en español (RF-04).
7. `PUT` actualiza con reemplazo completo (200); parcial devuelve 422; `id`
   inexistente devuelve 404 (RF-04).
8. `DELETE` devuelve 204 y el dataset desaparece de la lista; `id` inexistente
   devuelve 404 (RF-04).
9. Los errores de validación devuelven 422 con el formato estándar de FastAPI
   (RF-05).
10. Al reiniciar el servidor la lista vuelve a vacía (RF-03).
11. `/docs` muestra los 6 endpoints documentados en español (RF-06).
12. El código está separado en `models/`, `routers/` y `main.py` (RF-08).
13. Los conceptos del nivel están documentados en español (RF-07).

## Dudas abiertas

- **Desviación de la constitución (principio 4, tests obligatorios)**: la
  constitución exige tests automatizados ("Sin tests, no se mergea"), pero la
  usuaria decidió que el nivel 2 se verifica de forma manual (`/docs` + `curl`),
  igual que el nivel 1. Esta spec documenta esa desviación de forma explícita:
  los tests automatizados llegarán en un nivel posterior.
  [DECIDIDO POR LA USUARIA 2026-10-03]
