# Spec 001 — Preparación del entorno

**Nivel**: 0 · **Estado**: Completado · **Fecha**: 2026-09-30 · **Revisada**: 2026-10-01 (QA)

## Contexto

Data Analysis Platform es un proyecto educativo que avanza por niveles de
aprendizaje. El nivel 0 es la primera toma de contacto de una principiante total
con las herramientas y con la arquitectura cliente-servidor. Esta spec documenta
lo que ya está construido en el repositorio y queda marcada como completada: su
propósito es servir de registro y de estándar verificable del nivel.

## Objetivo

Que la principiante configure un entorno de desarrollo local con un frontend y un
backend ejecutándose por separado, comprenda los conceptos fundamentales
(cliente-servidor, frontend, backend, API) y tenga su código versionado y
publicado en GitHub.

## Usuarias

- **Principiante total**: persona que nunca ha programado. No conoce qué es un
  frontend, un backend, una API, Git ni un entorno virtual. Necesita explicaciones
  en lenguaje simple y comprobaciones claras de que "está funcionando".

## Historia de usuaria

> Como principiante total, quiero preparar mi equipo y entender qué es un
> frontend, un backend y una API, para poder ejecutar mi primera aplicación
> full stack en local y publicar mi progreso en GitHub con confianza.

## Requisitos funcionales

**RF-01 — Estructura base del proyecto**
El proyecto DEBERÁ organizarse en dos áreas principales separadas: frontend y
backend.
- DESPUÉS DE crear la estructura, cuando se liste la raíz del proyecto,
  entonces EXISTIRÁN las carpetas `frontend/` y `backend/` como directorios
  independientes.
- MIENTRAS el proyecto esté en el nivel 0, el código del frontend NO DEBERÁ
  mezclarse con el del backend.

**RF-02 — Control de versiones local**
El proyecto DEBERÁ estar gestionado con Git, con al menos un commit que registre
el estado inicial.
- DESPUÉS DE inicializar el repositorio, cuando se consulte el historial,
  entonces EXISTIRÁ al menos un commit con mensaje en español.
- DESPUÉS DE cualquier cambio, cuando se ejecute `git status`, entonces los
  cambios pendientes ESTARÁN visibles de forma explícita.

**RF-03 — Publicación en GitHub**
El código DEBERÁ publicarse en un repositorio remoto público en GitHub.
- DESPUÉS DE crear la cuenta y el repositorio, cuando se abra en GitHub,
  entonces CONTENDRÁ el código del proyecto y su visibilidad será pública.
- DESPUÉS DE configurar el remoto, cuando se ejecute el push, entonces la rama
  local ESTARÁ sincronizada con la rama remota.

**RF-04 — Entorno de Python aislado**
El backend DEBERÁ usar un entorno virtual de Python con FastAPI (>=0.115.0) y
Uvicorn (>=0.30.0) instalados dentro, y sus dependencias DEBERÁN quedar
declaradas de forma reproducible.
- DESPUÉS DE preparar el backend, cuando se active el entorno virtual, entonces
  las dependencias ESTARÁN disponibles solo dentro de él.
- DESPUÉS DE instalar las dependencias, cuando se revise la declaración de
  dependencias, entonces FIGURARÁN FastAPI y Uvicorn con versión mínima.

**RF-05 — Frontend ejecutable en local**
CUANDO se ejecute el frontend, un servidor DEBERÁ responder y mostrar una
página web accesible desde el navegador.
- CUANDO se abra `http://localhost:3000` en el navegador, entonces SE VERÁ una
  página de bienvenida de la aplicación.
- MIENTRAS el frontend esté en ejecución, cuando se recargue la página,
  entonces SE VUELVE A MOSTRAR sin errores.

**RF-06 — Backend ejecutable con respuesta básica**
CUANDO se ejecute el backend, el servidor DEBERÁ responder con una respuesta
básica que confirme que está funcionando.
- CUANDO se realice una petición HTTP GET a `http://localhost:8000/`, entonces SE
  RECIBIRÁ una respuesta JSON con un mensaje de bienvenida.
- CUANDO se realice una petición HTTP GET a `http://localhost:8000/health`,
  entonces SE RECIBIRÁ una respuesta que indique que el servidor está "ok".

**RF-07 — Documentación automática de la API**
El backend DEBERÁ exponer documentación automática de la API accesible desde el
navegador.
- CUANDO se abra `http://localhost:8000/docs` en el navegador, entonces SE VERÁ
  la documentación generada automáticamente con los endpoints disponibles.

**RF-08 — Conceptos del nivel documentados**
La documentación del nivel 0 DEBERÁ presentar los conceptos fundamentales
(frontend, backend, API, servidor, cliente, repositorio, entorno virtual,
dependencias, base de datos, cliente-servidor, Git, GitHub, Node.js, Python,
editor de código, Vue, Nuxt, FastAPI, desarrollo local vs producción) con
lenguaje comprensible para una principiante total. Los nombres propios de
tecnologías (Git, GitHub, Node.js, Python, Vue, Nuxt, FastAPI) se conservan en
su forma original; el resto del texto estará en español.
- DESPUÉS DE revisar la documentación, cuando se lea la sección de conceptos,
  entonces CADA concepto de la lista TENDRÁ una explicación breve en español.
- SI un concepto corresponde a un nivel posterior (por ejemplo, base de datos),
  entonces se indicará explícitamente que su uso es futuro.

**RF-09 — Comprobación independiente de frontend y backend**
El nivel 0 DEBERÁ permitir comprobar frontend y backend por separado, sin que se
conecten entre sí.
- CUANDO se compruebe el frontend por separado, entonces RESPONDERÁ aunque el
  backend esté detenido.
- CUANDO se compruebe el backend por separado, entonces RESPONDERÁ aunque el
  frontend esté detenido.

## Requisitos no funcionales

- **RNF-01 — Legibilidad**: La documentación DEBERÁ ser comprensible para una
  principiante total sin conocimientos previos de programación.
- **RNF-02 — Idioma**: Todo texto, comentario y commit estará en español.
- **RNF-03 — Plataforma**: La spec DEBERÁ ser ejecutable en macOS, Linux y
  Windows; se documentarán las notas específicas de cada plataforma sin
  afirmar compatibilidad no probada.
- **RNF-04 — Todo en local**: El nivel 0 DEBERÁ ejecutarse en el equipo de la
  usuaria, sin más servicios externos que la descarga de dependencias y la
  publicación en GitHub.
- **RNF-05 — Protección de datos**: El nivel 0 NO DEBERÁ almacenar datos
  personales de usuarias; solo datos de ejemplo.
- **RNF-06 — Reproducibilidad**: DESPUÉS DE seguir los pasos en orden, cualquier
  persona con Python 3.11+, Node.js 20+, Git y cuenta de GitHub DEBERÁ poder
  recrear el entorno desde cero.

## Casos límite

- **CL-01**: Python o Node.js ya están instalados con versión adecuada (Python
  3.11+, Node.js 20+) → se verifica la versión y no se reinstala.
- **CL-02**: Las versiones instaladas no cumplen la mínima → se detiene el
  proceso hasta actualizar.
- **CL-03**: No hay conexión a internet para instalar dependencias → no se
  puede completar; se pausa hasta recuperarla.
- **CL-04**: El puerto 3000 o el 8000 está ocupado por otro proceso → la
  verificación del servicio afectado fallará; debe liberarse el puerto.
- **CL-05**: Git o GitHub ya están configurados en la máquina → se reutilizan
  los datos existentes.
- **CL-06**: La autenticación con GitHub falla → el push no se completa y el
  nivel queda incompleto hasta autenticarse.
- **CL-07**: La usuaria trabaja en un sistema operativo distinto al de origen
  → la spec se ejecuta en la plataforma del entorno; se documentan las notas
  pertinentes sin afirmar compatibilidad no probada.
- **CL-08**: Solo uno de los dos puertos (3000 u 8000) está ocupado → se
  verifica el servicio cuyo puerto está libre y se informa del conflicto en
  el otro.
- **CL-09**: La usuaria no tiene cuenta de GitHub → el nivel queda incompleto
  hasta crearla.
- **CL-10**: El repositorio remoto ya existe con contenido previo → se solicita
  confirmación antes de sobrescribir o fusionar.
- **CL-11**: El entorno virtual ya existe → se reutiliza si es válido; si no,
  se recrea.
- **CL-12**: Las dependencias ya están instaladas globalmente → se prioriza el
  entorno virtual y se documenta la diferencia.
- **CL-13**: `npm install` o `pip install` fallan por permisos o red → se
  documenta el error y se pausa hasta resolverlo.
- **CL-14**: El frontend o el backend tardan más de 30 segundos en arrancar →
  se considera timeout y se revisa el proceso.
- **CL-15**: La usuaria cierra el terminal mientras los servidores están en
  ejecución → los servicios se detienen; el nivel puede reanudarse ejecutando
  los comandos de nuevo.
- **CL-16**: Conflictos de merge en Git al sincronizar con el remoto → se
  documenta el conflicto y se pausa hasta resolverlo manualmente.
- **CL-17**: El archivo `.gitignore` no existe o está mal configurado → se
  crea o corrige para excluir `venv/`, `node_modules/` y archivos sensibles.
- **CL-18**: La usuaria no tiene permisos para crear carpetas en el directorio
  de trabajo → se solicitan permisos o se cambia el directorio.
- **CL-19**: Conexión a internet intermitente o lenta → se reintentan las
  descargas y se documenta la inestabilidad.
- **CL-20**: Ya existe un repositorio con el mismo nombre en la cuenta de
  GitHub → se solicita elegir otro nombre o eliminar el existente.
- **CL-21**: El tag `v1.0.0` ya existe en el remoto → se solicita confirmación
  antes de forzar el tag.
- **CL-22**: La rama `main` remota tiene commits que no existen localmente →
  se documenta la divergencia y se pausa hasta sincronizar.

## Fuera de alcance

- Conectar el frontend con el backend (comunicación Nuxt ↔ FastAPI).
- Procesar archivos CSV.
- Usar una base de datos (SQLite, PostgreSQL) más allá de explicar el concepto.
- Autenticación de usuarias.
- Docker, despliegue en producción o CI/CD.
- CRUD de conjuntos de datos.
- Visualizaciones y gráficas.
- Tests automatizados (el nivel 0 no tiene funcionalidad de negocio; los tests
  se introducen en niveles posteriores).

## Criterios de finalización

El nivel 0 se considera terminado cuando se cumplan TODAS:
1. La estructura con `frontend/` y `backend/` existe y están separados (RF-01).
2. Existe repositorio Git local con al menos un commit en español (RF-02).
3. Cuenta en GitHub creada, repositorio remoto público publicado y push
   completado (RF-03).
4. Entorno virtual creado con FastAPI (>=0.115.0) y Uvicorn (>=0.30.0)
   instalados y dependencias declaradas (RF-04).
5. El frontend responde en `http://localhost:3000` con página de bienvenida
   (RF-05).
6. El backend responde en `http://localhost:8000/` con bienvenida y en
   `/health` con estado "ok" (RF-06).
7. La documentación automática de la API es visible en `http://localhost:8000/docs`
   (RF-07).
8. Los conceptos del nivel están documentados en español para principiantes
   (RF-08).
9. Frontend y backend se comprueban por separado, sin conexión (RF-09).

## Dudas abiertas

- ¿Cómo se comprueba que la usuaria entendió los conceptos del nivel (quiz,
  conversación con el mentor, autoevaluación)? [NECESITA ACLARACIÓN]
- ¿Se explica SQLite solo como concepto futuro o se instala ya en este
  nivel? [NECESITA ACLARACIÓN]
- ¿El editor de código (Visual Studio Code) es requisito obligatorio del nivel
  o solo una recomendación? [NECESITA ACLARACIÓN]
- ¿La publicación en GitHub debe incluir un tag de versión (v1.0.0) o basta
  con el push? [NECESITA ACLARACIÓN]
