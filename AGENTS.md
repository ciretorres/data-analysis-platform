# AGENTS.md

## Descripción del proyecto

Plataforma web para cargar, procesar y visualizar archivos de datos CSV.
Proyecto en desarrollo progresivo por niveles de aprendizaje.

## Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | Nuxt 4, Vue 3, Node.js 20+ |
| Backend | Python 3.11+, FastAPI, Uvicorn |
| Control de versiones | Git, GitHub |
| Entorno | Ejecución local sin Docker (nivel 0) |

## Estructura del proyecto

```
data-analysis-platform/
├── frontend/              # Aplicación Nuxt (cliente)
│   ├── app/
│   │   └── app.vue        # Componente raíz
│   ├── nuxt.config.ts     # Configuración de Nuxt
│   └── package.json       # Dependencias del frontend
├── backend/               # API FastAPI (servidor)
│   ├── app/
│   │   └── main.py        # Aplicación FastAPI
│   ├── requirements.txt   # Dependencias Python
│   └── venv/              # Entorno virtual (no subir a Git)
├── docker-compose.yml     # Docker (solo futuras etapas)
├── .env.example           # Variables de entorno de ejemplo
├── .gitignore             # Archivos ignorados por Git
└── README.md              # Documentación del proyecto
```

## Comandos principales

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Endpoints del backend

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | / | Mensaje de bienvenida |
| GET | /health | Estado del servidor |
| GET | /docs | Documentación Swagger |

## Variables de entorno

Ver `.env.example`. Necesarias:
- `BACKEND_HOST`: 0.0.0.0
- `BACKEND_PORT`: 8000
- `FRONTEND_PORT`: 3000
- `NUXT_PUBLIC_API_BASE`: http://localhost:8000

## Convenciones

- Código y comentarios en español
- Commits en español con formato descriptivo
- Separación estricta entre `frontend/` y `backend/`
- Nombres de archivos en snake_case (Python) y kebab-case (componentes Vue)
- Respetar la estructura de carpetas existente

## 🧠 Memoria

- Al empezar, lee `MEMORY.md` para conocer el estado del proyecto y las decisiones tomadas.
- Al terminar una tarea, actualiza el estado actual, las decisiones importantes (con su porqué) y errores a `MEMORY.md`.
- Mantén breve (máximo ~50 líneas): resume o elimina lo que no aporte.
- Si algo se convierte en una regla permanente, proponlo moverlo a `AGENTS.md` en lugar de dejarlo en la memoria.
- No guardes nunca datos sensibles (claves, tokens, datos personales).

## Límites del nivel 0

- NO usar Docker
- NO conectar frontend con backend
- NO procesar archivos CSV
- NO usar bases de datos
- NO añadir autenticación
- NO crear CRUD de conjuntos de datos
- NO añadir funcionalidades fuera del alcance
- Siempre: actualizar `MEMORY.md` al terminar cada tarea.

## Verificación

Antes de dar por terminado cualquier cambio:
1. Backend responde en http://localhost:8000/
2. Frontend responde en http://localhost:3000/
3. Documentación API disponible en http://localhost:8000/docs
4. `git status` limpio (sin cambios sin commitear)
