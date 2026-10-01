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
├── opencode.json          # Configuración de OpenCode (MCP context7)
├── .agents/skills/        # Skills del agente (fastapi, nuxt, accessibility, seo, find-skills)
├── skills-lock.json       # Versión exacta de las skills instaladas
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

## 🎯 Skills del agente

| Skill | Ámbito | Cuándo se usa | Fuente |
|-------|--------|---------------|--------|
| `fastapi` | `backend/` | Escribir o revisar código FastAPI | `fastapi/fastapi` (oficial, v0.142.1) |
| `nuxt` | `frontend/` | Escribir o revisar código Nuxt | `onmax/nuxt-skills` (variante **Nuxt 4.x**, 2026.6.22) |
| `accessibility` | UI | Crear o auditar componentes, formularios, tablas | `addyosmani/web-quality-skills` |
| `seo` | `frontend/` | Solo cuando existan páginas propias (nivel ≥ 1) | `addyosmani/web-quality-skills` |
| `find-skills` | utilidad | Solo para descubrir e instalar otras skills | `vercel-labs/skills` |

Reglas de uso:
- Las skills son **referencia de estilo**, no permiso para ampliar el alcance.
- Mantener `uvicorn app.main:app --reload` como comando del backend (no cambiar a `fastapi dev` sin acordarlo).
- No crear `pages/`, `components/`, `server/` ni añadir uv/Ruff/OpenTelemetry/Nuxt UI por sugerencia de una skill.
- Actualizar con `npx skills update` y revisar el diff antes de commitear.
- Todas las skills son de proyecto; ninguna se instala con `-g`.

## 📚 MCP de documentación (context7)

| Servidor | Cuándo se usa | Configuración |
|----------|---------------|---------------|
| `context7` (remoto) | Consultar la **documentación oficial y actualizada de Nuxt 4** antes de escribir o revisar código del frontend (`resolve-library-id` → `query-docs`). También sirve para Vue y FastAPI. | `opencode.json` |

Reglas de uso:
- La skill `nuxt` da el **estilo**; `context7` da la **API al día**. Si chocan, manda la documentación oficial.
- Preferir `query-docs` antes que asumir APIs de memoria (Nuxt cambia entre versiones).
- Si el MCP no tiene docs de algo, no se inventa: se consulta o se pregunta.
- Es solo lectura de documentación; no modifica el proyecto ni toca `frontend/`.

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
- 🚫 NO añadir funcionalidades fuera del alcance
- ✅ Siempre: actualizar `MEMORY.md` al terminar cada tarea.
- ⚠️ Pregunta antes: crear archivos nuevos, cambiar el formato de los datos guardados.

## Verificación

Antes de dar por terminado cualquier cambio:
1. Backend responde en http://localhost:8000/
2. Frontend responde en http://localhost:3000/
3. Documentación API disponible en http://localhost:8000/docs
4. `git status` limpio (sin cambios sin commitear)
5. MCP conectado *(solo si cambió `opencode.json`)*: desde la raíz, `opencode mcp list` → `✓ context7 connected`
