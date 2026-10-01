# Constitución de Data Analysis Platform

1. **Stack simple**: Nuxt + Vue + FastAPI + Uvicorn. Sin frameworks extra sin acuerdo previo.
2. **Spec primero**: Cada nivel define su spec antes de escribir código. El código implementa la spec, nunca al revés.
3. **Separación estricta**: `frontend/` y `backend/` no se mezclan. La comunicación solo vía API HTTP/JSON.
4. **Tests obligatorios**: Toda funcionalidad nueva incluye tests. Sin tests, no se mergea.
5. **Datos protegidos**: Nunca guardar datos reales de usuarias. Usar datos de ejemplo o anonimizados.
6. **Español siempre**: Código, comentarios, commits y documentación en español.
