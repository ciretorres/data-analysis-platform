# AGENTS.md

## Descripción del proyecto

Plataforma web para cargar, procesar y visualizar archivos de datos CSV.
Proyecto educativo en desarrollo progresivo por niveles de aprendizaje.

## Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | Nuxt 4, Vue 3, Node.js 20+ |
| Backend | Python 3.11+, FastAPI, Uvicorn |
| Control de versiones | Git, GitHub |
| Entorno | Ejecución local sin Docker (niveles 0-1) |

## Estructura del proyecto

```
data-analysis-platform/
├── specs/                  # Especificaciones por nivel (spec primero)
│   ├── 001-preparacion-entorno/
│   └── 002-interfaz-frontend/
├── frontend/               # Aplicación Nuxt (cliente)
│   ├── app/
│   │   └── app.vue         # Componente raíz
│   ├── nuxt.config.ts      # Configuración de Nuxt
│   └── package.json        # Dependencias del frontend
├── backend/                # API FastAPI (servidor)
│   ├── app/
│   │   └── main.py         # Aplicación FastAPI
│   ├── requirements.txt    # Dependencias Python
│   └── venv/               # Entorno virtual (no subir a Git)
├── .agents/skills/         # Skills del agente (fastapi, nuxt, accessibility, seo, find-skills)
├── .opencode/              # Comandos y configuración de OpenCode
├── docker-compose.yml      # Docker (solo futuras etapas)
├── .env.example            # Variables de entorno de ejemplo
├── .gitignore              # Archivos ignorados por Git
├── AGENTS.md               # Este archivo
├── MEMORY.md               # Memoria del proyecto
├── package.json            # Versionado del proyecto
└── README.md               # Documentación del proyecto
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
- **NO hacer commit ni push a GitHub sin preguntar antes al usuario**
- **Actualizar `CHANGELOG.md` con cada commit o versionado** (entrada con hash corto, categoría y enlace)

## 📐 Spec primero

- Antes de trabajar en un nivel, lee su spec en `specs/`.
- El código implementa la spec, nunca al revés.
- Si algo se convierte en una regla permanente, proponlo moverlo a este archivo.
- Al terminar una tarea, actualiza `MEMORY.md`.

## 🧰 Herramientas del agente

| Herramienta | Ámbito | Cuándo se usa |
|-------------|--------|---------------|
| Skill `fastapi` | `backend/` | Escribir o revisar código FastAPI |
| Skill `nuxt` | `frontend/` | Escribir o revisar código Nuxt |
| Skill `accessibility` | UI | Crear o auditar componentes, formularios, tablas |
| Skill `seo` | `frontend/` | Solo cuando existan páginas propias (nivel ≥ 1) |
| Skill `find-skills` | utilidad | Solo para descubrir e instalar otras skills |
| MCP `context7` | documentación | Consultar documentación oficial de Nuxt 4 / Vue / FastAPI |

Reglas de uso:
- Las skills son **referencia de estilo**, no permiso para ampliar el alcance.
- Mantener `uvicorn app.main:app --reload` como comando del backend.
- No crear `pages/`, `components/`, `server/` ni añadir uv/Ruff/OpenTelemetry/Nuxt UI por sugerencia de una skill.
- Actualizar con `npx skills update` y revisar el diff antes de commitear.
- Todas las skills son de proyecto; ninguna se instala con `-g`.
- La skill `nuxt` da el **estilo**; `context7` da la **API al día**. Si chocan, manda la documentación oficial.

## 🧠 Memoria

- Al empezar, lee `MEMORY.md` para conocer el estado del proyecto y las decisiones tomadas.
- Al terminar una tarea, actualiza el estado actual, las decisiones importantes (con su porqué) y errores a `MEMORY.md`.
- Mantén breve (máximo ~50 líneas): resume o elimina lo que no aporte.
- No guardes nunca datos sensibles (claves, tokens, datos personales).

## Límites del nivel 1

- NO conectar frontend con backend
- NO procesar archivos CSV (solo selección y validación visual)
- NO enviar el archivo a ningún servidor
- NO usar librerías de gráficos (placeholder con texto)
- NO tests automatizados (este nivel se verifica manualmente)
- NO usar bases de datos
- NO añadir autenticación
- NO usar Docker
- NO añadir funcionalidades fuera del alcance de la spec
- ✅ Siempre: actualizar `MEMORY.md` al terminar cada tarea.
- ⚠️ Pregunta antes: crear archivos nuevos, cambiar el formato de los datos guardados, hacer commit o push.

## Verificación

Antes de dar por terminado cualquier cambio:
1. Backend responde en http://localhost:8000/
2. Frontend responde en http://localhost:3000/
3. Documentación API disponible en http://localhost:8000/docs
4. `git status` limpio (sin cambios sin commitear)
5. MCP conectado *(solo si cambió `opencode.json`)*: desde la raíz, `opencode mcp list` → `✓ context7 connected`
