## Ruta de aprendizaje por niveles

## Nivel 0: Preparación del entorno

### Objetivo

Configurar el entorno de desarrollo y las herramientas necesarias para comprender la estructura general de una aplicación full stack y la arquitectura cliente-servidor.

### Conceptos

- Frontend.
- Backend.
- API.
- Servidor.
- Cliente.
- Repositorio.
- Entorno virtual.
- Dependencias.
- Qué es frontend.
- Qué es backend.
- Qué es una API.
- Qué es una base de datos.
- Qué significa cliente-servidor.
- Qué función cumple Git.
- Qué diferencia existe entre desarrollo local y producción.
- Git
- GitHub
- Node.js
- Python
- Visual Studio Code
- Vue
- Nuxt
- FastAPI
- SQLite

### Instrucciones

1. Instala Python y Node.js.
2. Crea una cuenta en GitHub.
3. Configura Git.
4. Crea un repositorio para el proyecto.
5. Crea dos carpetas principales:

```text
data-analysis-platform/
├── frontend/
└── backend/
```

6. Inicializa un proyecto Nuxt dentro de `frontend`.
7. Crea un entorno virtual de Python dentro de `backend`.
8. Instala FastAPI y Uvicorn.
9. Ejecuta un servidor básico de frontend y otro de backend.

### Resultado esperado

El frontend de Nuxt y el servidor de FastAPI deben ejecutarse correctamente en local.

La persona debe poder abrir una aplicación Nuxt en el navegador y visualizar una respuesta básica procedente de un servidor FastAPI.

---

## Nivel 1: Crear una interfaz frontend con Vue y Nuxt

### Objetivo

Construir una interfaz inicial utilizando Vue y Nuxt para la plataforma de análisis de datos.

### Funcionalidades

Crear una página de inicio que incluya:

- Nombre de la aplicación.
- Página de inicio.
- Menú de navegación.
- Sección de bienvenida.
- Título y descripción del proyecto.
- Tarjetas con métricas simuladas de ejemplo.
- Botón para cargar un archivo.
- Área reservada para gráficos.
- Diseño responsive básico.

## Instrucciones

- Utiliza componentes Vue.
- Separa la interfaz en componentes pequeños.
- Crea una página principal con Nuxt.
- Utiliza datos simulados inicialmente.
- Añade un diseño responsive.
- Explica la diferencia entre página y componente.

### Componentes sugeridos

```text
frontend/
├── components/
│   ├── AppHeader.vue
│   ├── MetricCard.vue
│   ├── FileUploader.vue
│   └── ChartPlaceholder.vue
├── pages/
│   └── index.vue
├── layouts/
│   └── default.vue
└── assets/
    └── css/
```

### Conceptos

- Componentes.
- Props.
- Eventos.
- Estado reactivo.
- Estado local.
- Directivas de Vue.
- Renderizado condicional.
- Renderizado de listas.
- Rutas en Nuxt.
- Layouts.
- Diseño responsive.

## Resultado esperado

La persona debe poder construir una interfaz funcional utilizando datos estáticos, sin conectarla todavía a un backend.

--

## Nivel 2: Crear una API básica y sencilla con FastAPI

### Objetivo

Crear un backend sencillo y comprender cómo funciona una API REST y CRUD con FastAPI para administrar conjuntos de datos.

### Entidad principal

La primera entidad será `Dataset`.

Cada conjunto de datos puede incluir:

```json
{
  "id": 1,
  "name": "Ventas mensuales",
  "description": "Datos de ventas del año actual",
  "file_name": "ventas.csv",
  "created_at": "2026-09-29"
}
```

### Endpoint inicial(es)

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/health` | Estado del servidor |
| GET | `/api/datasets` | Obtener todos los conjuntos de datos |
| GET | `/api/datasets/{id}` | Obtener un conjunto específico |
| POST | `/api/datasets` | Crear un conjunto de datos |
| PUT | `/api/datasets/{id}` | Actualizar un conjunto |
| DELETE | `/api/datasets/{id}` | Eliminar un conjunto |

### Respuesta esperada

```json
{
  "status": "ok",
  "message": "API funcionando correctamente",
  "version": "1.0.0"
}
```

### Tareas

- Crear una aplicación FastAPI.
- Crear una ruta de comprobación.
- Ejecutar el servidor con Uvicorn.
- Consultar la documentación automática.
- Probar el endpoint.
- Explicar los códigos de estado HTTP.
- Comienza utilizando una lista en memoria.
- Define modelos de entrada y salida con Pydantic.
- Valida los datos recibidos.
- Utilizar una lista en memoria.
- Crear operaciones CRUD.
- Utiliza códigos de estado HTTP apropiados.
- Probar los endpoints.
- Documenta cada endpoint.
- Prueba la API con la documentación automática de FastAPI.

### Conceptos

- Qué es una API REST.
- CRUD.
- Rutas.
- Parámetros.
- Parámetros de ruta.
- Cuerpos de petición.
- Validación de datos.
- Respuestas HTTP.
- Códigos de estado HTTP.
- Métodos HTTP.
- Separación entre modelos y rutas.
- JSON.
- Códigos de estado.
- Documentación automática.
- Servidor de desarrollo.

### Resultado esperado

La persona debe poder crear, consultar, actualizar y eliminar conjuntos de datos mediante una API.

--

# Nivel 2: Conectar el frontend con una API
## Nivel 3: Conectar Nuxt con FastAPI
# Nivel 4: Integrar la API con Nuxt