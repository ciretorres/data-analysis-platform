# Spec 004 — Conectar el frontend de Nuxt con FastAPI

**Nivel**: 3 · **Estado**: Revisada por QA (pendiente de aprobación de la usuaria) · **Fecha**: 2026-10-06 · **Revisada**: 2026-10-06 (QA)

## Contexto

El nivel 2 dejó una API FastAPI funcionando con CRUD de `Dataset` en memoria.
El nivel 3 da el salto más importante: **conectar el frontend con el backend**.
Hasta ahora la interfaz funcionaba con datos de ejemplo y sin ninguna petición.
Este nivel consume información real del servidor desde Nuxt, mostrando estado
de carga, manejo de errores y los datos cuando la petición es exitosa.

**Nota**: el nivel 2 ya tiene `GET /health` (3 campos: `status`, `message`,
`version`). Este nivel añade `GET /api/health` (4 campos: `app_name`,
`status`, `version`, `response_date`). Ambos coexisten; no se modifica el
existente.

## Objetivo

Que la principiante entienda cómo una aplicación Vue obtiene información de un
servidor externo: realizar peticiones HTTP, mostrar estados de carga, manejar
errores y presentar los datos recibidos.

## Usuarias

- **Principiante total**: persona que ya sabe ejecutar frontend y backend por
  separado, pero nunca ha conectado ambos. Necesita ver el flujo completo:
  petición → carga → respuesta/error → datos en pantalla.

## Historia de usuaria

> Como principiante total, quiero que mi aplicación Nuxt pida información al
> backend y la muestre en pantalla, para entender cómo se comunican el
> frontend y el backend.

## Requisitos funcionales

**RF-01 — Endpoint `/api/health` en el backend**
El backend DEBERÁ exponer `GET /api/health` que devuelva código 200 con:

```json
{
  "app_name": "Data Analysis Platform",
  "status": "ok",
  "version": "1.0.0",
  "response_date": "2026-10-06"
}
```

- CUANDO se consulte `/api/health`, entonces LA RESPUESTA DEBERÁ tener código
  200 y los cuatro campos.
- El campo `response_date` DEBERÁ ser la fecha del servidor en formato
  AAAA-MM-DD.
- El endpoint DEBERÁ estar documentado en español, visible en `/docs`.

**RF-02 — CORS configurado en el backend**
El backend DEBERÁ aceptar peticiones desde el origen del frontend
(`http://localhost:3000`).

- CUANDO el frontend haga una petición a `/api/health`, entonces EL BACKEND
  DEBERÁ responder sin errores de CORS.
- El backend DEBERÁ usar el middleware `CORSMiddleware` de FastAPI.

**RF-03 — Variable de entorno para la URL de la API**
El frontend DEBERÁ leer la URL base de la API desde la variable de entorno
`NUXT_PUBLIC_API_BASE`.

- CUANDO se configure `NUXT_PUBLIC_API_BASE`, entonces EL FRONTEND DEBERÁ
  usarla como base para las peticiones.
- SI la variable no está definida, entonces EL FRONTEND DEBERÁ usar
  `http://localhost:8000` como valor por defecto.
- El archivo `.env.example` ya contiene `NUXT_PUBLIC_API_BASE`; la usuaria
  PODRÁ copiarlo a `.env` si quiere cambiar la URL.

**RF-04 — Composable `useApi` genérico**
El frontend DEBERÁ incluir un composable `useApi.ts` **genérico** que
encapsule la lógica de peticiones HTTP.

- CUANDO se use el composable, entonces DEBERÁ devolver el estado de carga,
  el error (si lo hay) y los datos.
- El composable DEBERÁ aceptar una URL como parámetro y usar `fetch` para
  hacer la petición.
- El composable DEBERÁ ser reutilizable para cualquier endpoint, no solo para
  `/api/health`.

**RF-05 — Sección "Estado de la API" en la página de inicio**
La página de inicio DEBERÁ incluir una sección "Estado de la API" que muestre
la información devuelta por `/api/health`.

- CUANDO se abra la página, entonces SE INICIARÁ una petición a `/api/health`.
- MIENTRAS la petición esté en curso, entonces SE VERÁ un estado de carga.
- SI la petición falla, entonces SE VERÁ un mensaje de error en español (ej.
  "No se pudo conectar con el servidor. Inténtalo de nuevo.").
- CUANDO la petición sea exitosa, entonces SE VERÁN los datos: nombre de la
  aplicación, estado, versión y fecha de respuesta.
- La sección DEBERÁ tener un enlace en el menú de navegación.

**RF-06 — Conceptos del nivel documentados**
La documentación del nivel 3 DEBERÁ presentar los conceptos fundamentales
(peticiones HTTP, métodos GET y POST, JSON, fetch, composables, variables de
entorno, estados de carga, manejo de errores, CORS, comunicación
frontend-backend) con lenguaje comprensible para una principiante total.

- DESPUÉS DE revisar la documentación, cuando se lea la sección de conceptos,
  entonces CADA concepto TENDRÁ una explicación breve en español.

## Requisitos no funcionales

- **RNF-01 — Legibilidad**: La documentación DEBERÁ ser comprensible para una
  principiante total.
- **RNF-02 — Idioma**: Todo texto, comentario y documentación estará en
  español.
- **RNF-03 — Todo en local**: La comunicación DEBERÁ funcionar solo con los
  servidores de desarrollo locales (frontend :3000, backend :8000).
- **RNF-04 — Sin persistencia adicional**: No se DEBERÁ añadir base de datos ni
  ficheros nuevos; la conexión es directa frontend ↔ backend.

## Casos límite

- **CL-01**: El backend está detenido → se muestra un mensaje de error en
  español en la sección "Estado de la API".
- **CL-02**: El backend tarda más de lo normal → se muestra el estado de carga
  hasta que responda.
- **CL-03**: La variable `NUXT_PUBLIC_API_BASE` no está definida → se usa
  `http://localhost:8000` por defecto.
- **CL-04**: El backend devuelve un error (500) → se muestra un mensaje de
  error en español.
- **CL-05**: El backend devuelve datos correctos → se muestran los 4 campos en
  pantalla.
- **CL-06**: La usuaria recarga la página → se vuelve a hacer la petición y se
  muestran los datos actualizados.

## Fuera de alcance

- Autenticación y autorización.
- CRUD desde el frontend (solo lectura de `/api/health`).
- Tests automatizados (la verificación es manual, con el navegador y `curl`).
- Docker, CI/CD.
- Paginación, búsqueda o filtros.
- Métodos POST desde el frontend (solo GET en este nivel).

## Criterios de finalización

El nivel 3 se considera terminado cuando, con verificación manual (navegador y
`curl`), se cumplan TODAS:

1. `GET /api/health` devuelve 200 con `app_name`, `status`, `version` y
   `response_date` (RF-01).
2. El backend acepta peticiones desde `http://localhost:3000` sin errores de
   CORS (RF-02).
3. El frontend lee `NUXT_PUBLIC_API_BASE` y usa `http://localhost:8000` por
   defecto (RF-03).
4. El composable `useApi.ts` existe, es genérico y devuelve estado de carga,
   error y datos (RF-04).
5. La página muestra estado de carga, error y datos según corresponda, y la
   sección tiene enlace en el menú (RF-05).
6. Los conceptos del nivel están documentados en español (RF-06).
7. Con el backend detenido, la página muestra un mensaje de error en español
   (CL-01).

## Dudas abiertas

Ninguna: todas las preguntas se resolvieron con la usuaria o se decidieron
durante la revisión QA.
