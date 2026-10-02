---
description: SSD - Genera un plan técnico a partir de una especificación
agent: plan
---

A partir de specs/$1/spec.md, genera specs/$1/plan.md siguiendo el formato de la skill ssd.

Requisitos:

- Lee primero el contenido completo de specs/$1/spec.md.
- Convierte los requisitos funcionales y no funcionales en un plan técnico concreto.
- Organiza el plan por fases o bloques de trabajo, respetando el orden de dependencia.
- Para cada bloque incluye:
  - Objetivo.
  - Cambios necesarios.
  - Archivos o componentes afectados, si se pueden determinar.
  - Dependencias.
  - Decisiones técnicas relevantes.
  - Riesgos o casos límite.
- No implementes código.
- No inventes requisitos que no aparezcan en el spec.md.
- Si falta información importante, indícala explícitamente como una decisión pendiente.
- El resultado debe ser accionable para dividirlo posteriormente en tareas pequeñas.
- Relaciona cada parte del plan con los RF correspondientes.
- Mantén el plan lo bastante detallado como para que otro comando pueda generar tasks.md a partir de él.
- Guarda el resultado exclusivamente en specs/$1/plan.md.
