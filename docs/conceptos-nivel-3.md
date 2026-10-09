# Conceptos del Nivel 3

Explicaciones en español para una principiante total. Los nombres propios de
conceptos técnicos (API REST, CORS, fetch, etc.) se conservan en su forma
original; el resto del texto está en español.

---

## Comunicación frontend-backend

### Comunicación frontend-backend
El diálogo entre la interfaz (lo que ve la usuaria en el navegador) y el
servidor (donde viven los datos y la lógica). El frontend hace peticiones HTTP
y el servidor responde. En este proyecto, el frontend está en `frontend/` y el
backend en `backend/`; hasta ahora funcionaban por separado y este nivel los
conecta por primera vez.

### Peticiones HTTP
Un mensaje que el navegador envía al servidor para pedir o enviar datos. Tiene
un método (qué quiere hacer), una ruta (dónde), y a veces un cuerpo (los datos).
En este nivel, el frontend hace una petición GET a `/api/health` para pedir
el estado de la API.

### Métodos HTTP
La acción que el cliente quiere hacer sobre un recurso. Los cuatro de este
nivel: `GET` (leer, no modifica nada), `POST` (crear), `PUT` (actualizar,
reemplazo completo) y `DELETE` (eliminar). En `routers/datasets.py` cada
función lleva un decorador con el método: `@router.get("/")`,
`@router.post("/")`, etc.

### JSON
Formato de texto para estructurar datos, fácil de leer para las personas y de
parsear para las máquinas. Usa llaves `{}` para objetos, corchetes `[]` para
listas, y pares `"clave": valor`. Ejemplo: la respuesta de `GET /api/health` es
`{"app_name": "Data Analysis Platform", "status": "ok", "version": "1.0.0",
"response_date": "2026-10-06"}`. FastAPI convierte automáticamente los modelos
Pydantic a JSON en las respuestas.

---

## CORS

### CORS
(Cross-Origin Resource Sharing) Mecanismo de seguridad de los navegadores que
bloquea peticiones entre orígenes distintos (por ejemplo, de
`http://localhost:3000` a `http://localhost:8000`) salvo que el servidor lo
permita explícitamente. Sin CORS configurado, el navegador bloquearía la
petición del frontend al backend. En este proyecto se configura con
`CORSMiddleware` en `backend/app/main.py`, permitiendo el origen
`http://localhost:3000`.

---

## El lado del frontend

### fetch
Función nativa del navegador para hacer peticiones HTTP. Devuelve una
promesa que se resuelve con la respuesta del servidor. En este proyecto, el
composable `useApi` usa `fetch` para pedir datos a la API. Es la alternativa
moderna a `XMLHttpRequest` y no requiere librerías extra.

### Composables
Funciones reutilizables de Vue que encapsulan lógica y estado. Se crean en
`app/composables/` y se usan en cualquier componente. En este proyecto,
`useApi.ts` es un composable genérico que encapsula la lógica de peticiones
HTTP: devuelve el estado de carga, el error y los datos, y una función `pedir()`
para lanzar la petición. Así, cualquier componente puede pedir datos sin
repetir la lógica.

### Variables de entorno
Valores de configuración que viven fuera del código, para que este no tenga
datos fijos (como URLs) que cambian según el entorno. En Nuxt, las variables
que empiezan por `NUXT_PUBLIC_` están disponibles en el frontend. En este
proyecto, `NUXT_PUBLIC_API_BASE` define la URL base de la API (por defecto
`http://localhost:8000`). El archivo `.env.example` muestra las variables
disponibles.

### Estados de carga
Los momentos por los que pasa una petición: **cargando** (la petición está en
curso), **error** (algo salió mal) y **éxito** (llegaron los datos). En este
proyecto, la sección "Estado de la API" muestra un texto de carga mientras
`cargando` es `true`, un mensaje de error si `error` tiene valor, y los datos
cuando llegan. Así la usuaria siempre sabe qué está pasando.

### Manejo de errores
El código que se ejecuta cuando algo sale mal. En este proyecto, el composable
`useApi` captura los errores con `try/catch` y guarda un mensaje en español en
la variable `error`. Si el backend está detenido o devuelve un error, la
ve en pantalla en lugar de quedarse en silencio o romperse.

---

## Resumen del flujo

1. La usuaria abre la página → `onMounted` llama a `pedir()`.
2. `pedir()` pone `cargando = true` y hace `fetch` a la URL de la API.
3. El navegador envía la petición HTTP al backend.
4. El backend verifica CORS y responde con JSON.
5. `fetch` recibe la respuesta → `pedir()` guarda los datos o el error.
6. Vue actualiza la interfaz: carga, error o datos.
