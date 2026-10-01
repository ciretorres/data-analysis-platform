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

- Decidir si `.agents/`, `.opencode/` y `skills-lock.json` se commitean o van a `.gitignore`
- Conectar frontend con backend (nivel futuro)
- Implementar CRUD de datos (nivel futuro)
- *(Opcional)* Tipos de respuesta en `main.py` según la skill `fastapi`
