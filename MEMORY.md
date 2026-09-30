# MEMORY.md

## Estado actual

- **Nivel**: 0 (entorno de desarrollo local)
- **Fase**: Estructura inicial completada
- **Última actualización**: 2026-09-30

## Decisiones técnicas

| Decisión | Por qué |
|----------|---------|
| Nuxt 4 con template minimal | Punto de partida simple, sin módulos extra |
| FastAPI + Uvicorn | API rápida con documentación automática Swagger |
| Entorno virtual en backend/venv | Aislar dependencias del sistema |
| Git configurado con usuario ciretorres | Identidad para commits |
| Repositorio público en GitHub | Visibilidad y colaboración |

## Errores y soluciones

| Error | Solución |
|-------|----------|
| gh no instalado | Instalado con brew install gh |
| nuxi init requiere template | Usado --template minimal |
| Carpeta frontend ya existía | Usado --force en nuxi init |

## Pendiente

- Crear repositorio en GitHub y subir código
- Conectar frontend con backend (nivel futuro)
- Implementar CRUD de datos (nivel futuro)
