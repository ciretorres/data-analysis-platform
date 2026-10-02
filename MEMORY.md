# MEMORY.md

## Estado actual

- **Nivel**: 0 (entorno de desarrollo local)
- **Fase**: Estructura inicial + skills del agente configuradas
- **Versión**: 1.1.0
- **Última actualización**: 2026-09-30

## Decisiones técnicas

| Decisión | Por qué |
|----------|---------|
| Nuxt 4 con template minimal | Punto de partida simple, sin módulos extra |
| FastAPI + Uvicorn | API rápida con documentación automática Swagger |
| Entorno virtual en backend/venv | Aislar dependencias del sistema |
| Git configurado con usuario ciretorres | Identidad para commits |
| Repositorio público en GitHub | Visibilidad y colaboración |
| Skill `fastapi` oficial (0.142.1) | Es la misma que trae el venv → sin desajuste de versión |
| Skill `nuxt` de `onmax/nuxt-skills` (2026.6.22) | Es la variante Nuxt 4.x; la de `antfu/skills` es Nuxt 5 y no coincide con `nuxt ^4.5.2` |
| Skills solo a nivel de proyecto | Reproducibles con `skills-lock.json` y `npx skills update`; nada global |
| MCP context7 (remoto) | Tener la documentación oficial de Nuxt 4 a mano, sin salir de la terminal |

## Errores y soluciones

| Error | Solución |
|-------|----------|
| gh no instalado | Instalado con brew install gh |
| nuxi init requiere template | Usado --template minimal |
| Carpeta frontend ya existía | Usado --force en nuxi init |
| `find-skills` instalada en `~/.agents` (global) | Eliminada de lo global e instalada en el proyecto |

## Pendiente

- Conectar frontend con backend (nivel futuro)
- Implementar CRUD de datos (nivel futuro)
- *(Opcional)* Tipos de respuesta en `main.py` según la skill `fastapi`

## Notas

- Constitución creada en `docs/constitution.md` con 6 principios innegociables
- Skills del agente configuradas en `.agents/skills/` (fastapi, nuxt, accessibility, seo, find-skills)
- MCP context7 configurado en `opencode.json` para documentación oficial de Nuxt 4
- Spec 001 (nivel 0) creada en `specs/001-preparacion-entorno/spec.md`, estado: completado
- Spec 001 revisada por QA (2026-10-01): 33 hallazgos corregidos (12 ambigüedades, 3 contradicciones, 15 casos límite, 3 conflictos con constitución)
- Plan de implementación de spec 001 creado en `specs/001-preparacion-entorno/plan.md` (2026-10-01)
- Tasks de spec 001 creadas en `specs/001-preparacion-entorno/tasks.md` (2026-10-01)
- T1 completada: estructura base frontend/ y backend/ ya existía desde commit inicial (RF-01)
- T4-T8 completadas (2026-10-01): venv existe, app.vue actualizada con bienvenida personalizada, nuxt.config.ts con puerto 3000, .gitignore creado
- T2 y T3 omitidas por decisión del usuario (Git/GitHub/versionado ya implementado)
- RF-08 implementado (2026-10-01): documentación de conceptos en `docs/conceptos-nivel-0.md` y `specs/001-preparacion-entorno/conceptos.md`
- app.vue actualizado con estilos modernos tipo Nuxt (gradiente oscuro, tarjeta con info de endpoints)
- Spec 002 revisada por QA (2026-10-01): 43 hallazgos corregidos (20 ambigüedades, 5 contradicciones, 15 casos límite, 3 conflictos con constitución)
- Plan de implementación de spec 002 creado en `specs/002-interfaz-frontend/plan.md` (2026-10-02)
- Spec 002 (nivel 1) creada en `specs/002-interfaz-frontend/spec.md`, estado: aprobada (pendiente de implementación)
- AGENTS.md reorganizado: specs/ añadido a estructura, sección "Spec primero", límites actualizados a nivel 1, Skills+MCP fusionados
- CHANGELOG.md creado con estilo midudev/autoskills (versiones enlazadas, categorías con emojis, enlaces a commits)
- Spec 002: creado `specs/002-interfaz-frontend/tasks.md` (10 tareas en orden de dependencia, con RF y "Hecho cuando:") y añadida `app/app.vue` al plan
- Regla añadida a AGENTS.md: actualizar CHANGELOG.md con cada commit o versionado
- Regla: no hacer commit ni push a GitHub sin preguntar antes al usuario (movida a AGENTS.md como regla permanente)
