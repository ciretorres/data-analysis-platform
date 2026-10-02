# Plan de implementación — Spec 001 (Nivel 0)

**Fecha**: 2026-10-01 · **Estado**: Aprobado

## 1. Archivos a crear/modificar y responsabilidades

| Archivo | Responsabilidad | RF cubierto |
|---------|----------------|-------------|
| `frontend/app/app.vue` | Componente raíz de Nuxt. Renderiza la página de bienvenida con el nombre de la aplicación y un mensaje para principiantes. | RF-05 |
| `frontend/nuxt.config.ts` | Configuración de Nuxt: puerto 3000, sin módulos extra, sin conexión al backend. | RF-05, RF-09 |
| `frontend/package.json` | Dependencias del frontend (nuxt, vue). Script `dev` para ejecutar el servidor. | RF-05 |
| `backend/app/main.py` | Aplicación FastAPI con dos endpoints: `/` (bienvenida JSON) y `/health` (estado "ok"). | RF-06, RF-07 |
| `backend/requirements.txt` | Declaración reproducible de dependencias: `fastapi>=0.115.0`, `uvicorn[standard]>=0.30.0`. | RF-04 |
| `backend/venv/` | Entorno virtual de Python (no se sube a Git). | RF-04 |
| `.gitignore` | Excluye `venv/`, `node_modules/`, `.nuxt/`, archivos sensibles. | RF-01, RF-02 |
| `package.json` (raíz) | Versionado del proyecto (1.0.0) y scripts de conveniencia (`dev:frontend`, `dev:backend`). | RF-02 |
| `AGENTS.md` | Convenciones, estructura, comandos, límites del nivel. | RF-08 |
| `MEMORY.md` | Estado del proyecto, decisiones, notas. | RF-08 |
| `docs/constitution.md` | 6 principios innegociables del proyecto. | RF-08 |
| `specs/001-preparacion-entorno/spec.md` | Especificación del nivel (ya existe). | RF-08 |

## 2. Funciones puras de lógica

El nivel 0 no tiene lógica de negocio, pero estas funciones puras existen:

| Función | Ubicación | Responsabilidad | RF |
|---------|-----------|-----------------|---|
| `root()` | `backend/app/main.py` | Retorna `{"message": "¡Bienvenido a Data Analysis Platform!"}` | RF-06 |
| `health_check()` | `backend/app/main.py` | Retorna `{"status": "ok"}` | RF-06 |

No se necesitan más funciones puras: el nivel 0 es configuración y verificación, no procesamiento.

## 3. Cómo se pinta la interfaz

**Frontend (`app.vue`):**
- Estructura HTML simple: `<template>` con un `<h1>` (nombre de la aplicación) y un `<p>` (mensaje de bienvenida).
- Sin componentes reutilizables (no hay nada que reutilizar todavía).
- Sin estilos complejos: CSS básico centrado, legible, responsive con `viewport` meta.
- Sin imágenes ni assets externos (RNF-04: todo en local).

**Backend (respuestas JSON):**
- `GET /` → `{"message": "¡Bienvenido a Data Analysis Platform!"}`
- `GET /health` → `{"status": "ok"}`
- `GET /docs` → Swagger UI generado automáticamente por FastAPI.

## 4. Decisiones técnicas y justificación

| Decisión | Justificación | RF/RNF |
|----------|---------------|--------|
| **Nuxt 4 + Vue 3** | Lo fija la constitución (#1). No se discute. | RF-05 |
| **FastAPI + Uvicorn** | Lo fija la constitución (#1). No se discute. | RF-06 |
| **Sin módulos extra de Nuxt** | La constitución prohíbe frameworks extra sin acuerdo previo. | RF-05 |
| **Sin conexión frontend-backend en nivel 0** | RF-09 exige comprobación independiente. | RF-09 |
| **Puertos 3000 (frontend) y 8000 (backend)** | Convención estándar; no entran en conflicto. | RF-05, RF-06 |
| **`requirements.txt` con versiones mínimas** | RF-04 exige declaración reproducible. | RF-04 |
| **`.gitignore` excluye `venv/` y `node_modules/`** | Evita subir dependencias al repo (CL-17). | RF-02 |
| **Sin tests automatizados en nivel 0** | El nivel 0 no tiene funcionalidad de negocio; los tests llegan en niveles posteriores (Fuera de alcance). | — |
| **Documentación de conceptos en la spec misma** | RF-08 exige explicaciones en español; la spec es el documento de referencia del nivel. | RF-08 |
| **Sin base de datos** | Fuera de alcance: solo se explica el concepto. | RF-08 |

## 5. Cobertura de RFs

| RF | Dónde se implementa |
|----|---------------------|
| RF-01 | Estructura de carpetas `frontend/` y `backend/` separadas |
| RF-02 | `.gitignore`, commits en español, `git status` visible |
| RF-03 | Repositorio público en GitHub con push completado |
| RF-04 | `backend/venv/`, `backend/requirements.txt` |
| RF-05 | `frontend/app/app.vue`, `frontend/nuxt.config.ts` |
| RF-06 | `backend/app/main.py` (endpoints `/` y `/health`) |
| RF-07 | FastAPI genera `/docs` automáticamente |
| RF-08 | `AGENTS.md`, `MEMORY.md`, `docs/constitution.md`, spec |
| RF-09 | Frontend y backend sin referencias cruzadas |
