# Conceptos del Nivel 2

Explicaciones en español para una principiante total. Los nombres propios de
conceptos técnicos (API REST, CRUD, JSON, etc.) se conservan en su forma
original; el resto del texto está en español.

---

## Qué es una API

### API REST
Una API (Application Programming Interface) es un modo de comunicación entre
programas. En este proyecto, la API es el backend: un programa que espera
peticiones y devuelve respuestas. REST es el estilo más común: usa los métodos
HTTP (GET, POST, PUT, DELETE) para indicar qué quieres hacer con los datos, y
JSON como formato para enviarlos y recibirlos. En este nivel, la API vive en
`backend/app/` y se prueba con `curl` o con la documentación automática en
`http://localhost:8000/docs`.

### CRUD
Las cuatro operaciones básicas sobre datos: **C**reate (crear), **R**ead
(leer), **U**pdate (actualizar) y **D**elete (eliminar). En una API REST se
corresponden con los métodos HTTP: POST crea, GET lee, PUT actualiza y DELETE
elimina. En este proyecto, el CRUD de `Dataset` está en
`backend/app/routers/datasets.py`: cinco funciones, una por operación.

### JSON
Formato de texto para estructurar datos, fácil de leer para las personas y de
parsear para las máquinas. Usa llaves `{}` para objetos, corchetes `[]` para
listas, y pares `"clave": valor`. Ejemplo: la respuesta de `GET /health` es
`{"status": "ok", "message": "API funcionando correctamente", "version": "1.0.0"}`.
FastAPI convierte automáticamente los modelos Pydantic a JSON en las respuestas.

---

## Las piezas de una petición HTTP

### Métodos HTTP
La acción que el cliente quiere hacer sobre un recurso. Los cuatro de este
nivel: `GET` (leer, no modifica nada), `POST` (crear), `PUT` (actualizar,
reemplazo completo) y `DELETE` (eliminar). En `routers/datasets.py` cada
función lleva un decorador con el método: `@router.get("/")`,
`@router.post("/")`, etc.

### Rutas
La dirección dentro de la API a la que se dirige la petición. En este proyecto
las rutas son `/health`, `/api/datasets/` y `/api/datasets/{id}`. Se declaran
en el decorador de cada función. El router se monta en `main.py` con
`app.include_router(datasets_router)`, y el prefijo `/api/datasets` se define
una sola vez en el `APIRouter`.

### Parámetros
Datos que el cliente envía a la API para que esta sepa qué hacer. En una API
REST pueden ir en la ruta, en la URL (query) o en el cuerpo de la petición.
En este nivel solo se usan parámetros de ruta y cuerpos de petición.

### Parámetros de ruta
Datos que van dentro de la propia dirección, como el `{id}` de
`/api/datasets/{id}`. Se declaran en la función con `Annotated[int, Path(ge=1)]`:
el tipo `int` hace que FastAPI valide que sea un número (si no, devuelve 422)
y `Path(ge=1)` exige que sea 1 o más. Ejemplo: en `obtener_dataset(id)`, el
`id` que llega de la ruta se usa para buscar en la lista.

### Cuerpos de petición
Los datos que el cliente envía en el interior de la petición, normalmente en
JSON, para crear o actualizar algo. En FastAPI se declaran con un modelo
Pydantic como parámetro: `def crear_dataset(datos: DatasetCreate)`. FastAPI
lee el JSON, lo valida contra el modelo y lo convierte en un objeto Python.
Si el JSON no cumple las reglas, devuelve 422 sin llamar a la función.

### Validación de datos
Comprobar que los datos recibidos cumplen las reglas antes de usarlos. En este
proyecto la hace Pydantic en `backend/app/models/dataset.py`: `name` es
obligatorio y de máximo 100 caracteres, `file_name` es obligatorio y de máximo
255, `created_at` debe ser una fecha válida. Si algo falla, FastAPI devuelve
422 con un `detail` que explica el error. Así la lógica de los endpoints puede
confiar en que los datos que recibe son correctos.

---

## Las respuestas HTTP

### Respuestas HTTP
Lo que la API devuelve al cliente: un código de estado y, normalmente, un cuerpo
en JSON. En FastAPI se devuelven diccionarios o modelos Pydantic y el framework
los convierte a JSON. El código de estado se indica en el decorador
(`status_code=status.HTTP_201_CREATED` en POST) o se deja el 200 por defecto.

### Códigos de estado HTTP
Números de tres dígitos que indican el resultado de la petición. Los de este
nivel: **200** (OK, todo fue bien), **201** (creado, en POST), **204** (sin
contenido, en DELETE), **404** (no encontrado, cuando el `id` no existe) y
**422** (error de validación, cuando los datos no cumplen las reglas). FastAPI
los devuelve automáticamente; para el 404 se usa
`raise HTTPException(status_code=404, detail="Dataset no encontrado")`.

### Códigos de estado
(Ver "Códigos de estado HTTP".) En la práctica, los códigos de estado HTTP son
los códigos de estado que se usan en la web: 2xx para éxito, 4xx para errores
del cliente y 5xx para errores del servidor. Este nivel usa 200, 201, 204, 404
y 422.

---

## Cómo se organiza el código

### Separación entre modelos y rutas
Dividir el código según su responsabilidad: los **modelos** (en
`app/models/dataset.py`) definen cómo son los datos y sus reglas de
validación; las **rutas** (en `app/routers/datasets.py`) definen qué peticiones
se atienden y qué hacen con los datos. Así, si mañana cambian las reglas de
validación, solo toca `models/`; si cambian los endpoints, solo toca
`routers/`. `main.py` solo crea la aplicación y monta el router.

### Documentación automática
FastAPI genera una página interactiva en `/docs` (Swagger) a partir del código:
lee los docstrings, los tipos de los parámetros y los modelos Pydantic para
mostrar qué endpoints hay, qué parámetros aceptan y qué devuelven. Por eso es
importante escribir buenos docstrings y descripciones en los campos: se ven
directamente en `/docs`. En este proyecto, `/docs` es la herramienta principal
para probar la API a mano.

### Servidor de desarrollo
El programa que ejecuta la API y la hace accesible por red. En este proyecto es
Uvicorn, que se arranca con `uvicorn app.main:app --reload` desde
`backend/`. El flag `--reload` hace que el servidor se reinicie solo cuando
cambias el código, para no tener que pararlo y arrancarlo a mano en cada cambio.
Mientras está corriendo, la API responde en `http://localhost:8000`.
