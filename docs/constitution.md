# Constitución de Data Analysis Platform

## Propósito
Construir y mantener el proyecto con código seguro, legible y fácil de probar.

## Principios
- Prioriza la claridad y la simplicidad sobre soluciones ingeniosas.
- Sigue los patrones y convenciones que ya existen en el repositorio.
- Antes de añadir una dependencia, comprueba si el proyecto ya ofrece una alternativa.
- No inventes requisitos: si falta información importante, explica la suposición que vas a usar.

## Forma de trabajar
- Antes de modificar código, revisa los archivos relacionados y entiende el flujo existente.
- Mantén los cambios enfocados en la tarea solicitada.
- No sobrescribas cambios del usuario ni modifiques archivos no relacionados.
- Si un cambio afecta varias partes del sistema, resume brevemente el plan antes de implementarlo.
- Español siempre. Código, comentarios, commits y documentación en español.

## Código
- Usa nombres descriptivos para variables, funciones y tipos.
- Prefiere funciones pequeñas y módulos con responsabilidades claras.
- Valida los datos que llegan desde usuarios, archivos o servicios externos.
- Maneja los errores de forma explícita; evita ocultarlos o ignorarlos.
- No añadas comentarios que solo repitan lo que el código ya dice.

## Seguridad
- No incluyas claves, contraseñas ni tokens en el código o los registros.
- No desactives controles de seguridad para hacer pasar una prueba.
- Pide confirmación antes de ejecutar acciones destructivas o difíciles de revertir.
- Datos protegidos. Nunca guardar datos reales de usuarias. Usar datos de ejemplo o anonimizados.

## Comunicación
- Explica brevemente qué cambiaste y qué verificaste.
- Si detectas un problema fuera del alcance de la tarea, menciónalo sin corregirlo automáticamente.

1. **Stack simple**: Nuxt + Vue + FastAPI + Uvicorn. Sin frameworks extra sin acuerdo previo.
2. **Spec primero**: Cada nivel define su spec antes de escribir código. El código implementa la spec, nunca al revés.
3. **Separación estricta**: `frontend/` y `backend/` no se mezclan. La comunicación solo vía API HTTP/JSON.
4. **Tests obligatorios**: Toda funcionalidad nueva incluye tests. Sin tests, no se mergea.

