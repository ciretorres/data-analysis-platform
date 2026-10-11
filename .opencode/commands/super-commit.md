---
description: Agrupa cambios en commits semánticos, actualiza el changelog y ofrece hacer push
---

Agrupa los cambios actuales en commits semánticos, actualiza `CHANGELOG.md` después de crear los commits y ofrece hacer push de la rama actual.

Contexto opcional para los mensajes de commit: `$ARGUMENTS`

Reglas:

- Escribe todos los mensajes de commit en español.
- Si `$ARGUMENTS` no está vacío, úsalo como contexto para ajustar los mensajes, pero no lo fuerces si no describe correctamente los cambios.
- Usa mensajes claros, semánticos y concisos, acordes con el estilo reciente del repositorio.
- Crea commits separados para cambios independientes. No mezcles cambios sin relación.
- Incluye los archivos nuevos, modificados y eliminados que pertenezcan a cada grupo.
- No reviertas cambios existentes.
- No uses `--no-verify`.
- No enmiendes commits existentes.
- No hagas push forzado.
- Nunca crees, muevas, elimines ni publiques tags. Los tags los gestionaré manualmente.
- En cada ejecución, comprueba si hay tags nuevos que todavía no estén documentados en `CHANGELOG.md`.
- Para detectar tags nuevos, compara los tags locales y los del remoto `origin` con las versiones documentadas en `CHANGELOG.md`. No dependas solo del tag más reciente.
- Si un tag nuevo existe y su versión no tiene una sección en el changelog:
  - Verifica que el tag exista, su fecha y los commits que comprende.
  - Añade una sección para esa versión, siguiendo el formato existente.
  - Enlaza la versión al tag de GitHub y actualiza el enlace comparativo de `Unreleased` para usar como base el tag válido más reciente.
  - Incluye solo cambios comprobables asociados a esa versión. No inventes entradas, hashes, fechas ni versiones.
- Si el tag ya está documentado, no dupliques ni recrees su sección.
- Si cambia la versión en los archivos del proyecto, pero no existe un tag correspondiente, no la trates como un lanzamiento ni crees una sección de versión por ese motivo.
- Antes de hacer commits, revisa si hay archivos sensibles o sospechosos (`.env`, tokens, credenciales, claves o secretos). Si encuentras alguno, detente y consulta.
- No incluyas en el changelog el commit que actualiza el propio changelog.
- No elimines ni sobrescribas contenido del changelog que no corresponda a los cambios de esta ejecución.

Flujo:

1. Inspecciona el estado completo del repositorio:
   - `git status --short`
   - `git diff --stat`
   - `git diff`
   - `git log --oneline -10`
   - `git branch --show-current`
   - `git tag --sort=-version:refname`
   - `git ls-remote --tags origin`
   - Revisa `CHANGELOG.md` completo y sigue exactamente su formato, categorías, idioma y estilo de enlaces.
   - Identifica los archivos de versión del proyecto (por ejemplo, `package.json`, archivos de configuración del backend u otros manifiestos aplicables) y lee sus versiones actuales.

2. Identifica los grupos de cambios según su intención: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `release` o `config`.

3. Prepara un plan inicial de commits. Para cada uno, indica:
   - El mensaje propuesto en español.
   - Los archivos que incluirá.
   - La categoría correspondiente del changelog.

4. Comprueba si hay archivos sensibles o sospechosos. Si los hay, detente y consulta antes de continuar.

5. Si hay ambigüedad real sobre cómo agrupar los cambios, consulta antes de modificar archivos o crear commits.

6. Crea los commits de los cambios del proyecto, sin incluir todavía los cambios de `CHANGELOG.md` que se generen durante esta ejecución:
   - Añade solo los archivos de ese grupo con `git add <archivos>`.
   - Revisa el staging con `git diff --cached`.
   - Crea el commit con su mensaje semántico en español.
   - No incluyas cambios nuevos de `CHANGELOG.md` en los commits de código.
   - Si `CHANGELOG.md` ya tenía cambios del usuario antes de empezar, consérvalos. Si no puedes separarlos con seguridad, consulta antes de modificarlos o confirmarlos.

7. Después de crear todos los commits de código:
   - Obtén los hashes reales con `git log` y confirma qué archivos incluyó cada commit.
   - Actualiza `CHANGELOG.md` para registrar únicamente los cambios de código creados en esta ejecución en la sección `Unreleased`.
   - Reemplaza cualquier indicador temporal como `(pendiente de commit)` que corresponda a esos cambios por enlaces con el hash real, siguiendo el formato existente. Por ejemplo:
     `- feat: descripción [`abc1234`](https://github.com/OWNER/REPO/commit/abc1234)`
   - No inventes ni reutilices hashes.
   - Agrupa las entradas en las categorías existentes, como `### ✨ Features`, `### 🐛 Bug Fixes` y `### 📦 Other Changes`. Añade una categoría solo si el cambio lo requiere y el formato del archivo lo justifica.
   - Conserva las entradas y secciones que no estén relacionadas con esta ejecución.

8. Comprueba si hay tags nuevos que aún no estén documentados:
   - Compara los tags locales con los tags del remoto `origin` y con las secciones de versiones existentes en `CHANGELOG.md`.
   - Considera nuevo un tag si existe en Git localmente o en `origin` y su versión aún no tiene una sección correspondiente en el changelog.
   - Para cada tag sin documentar, verifica su nombre, fecha y commits asociados. Compara su contenido con el tag de versión anterior para identificar los cambios incluidos.
   - Si el tag existe en el remoto, pero no localmente, puedes consultarlo desde `origin`; no lo descargues ni alteres referencias locales sin necesidad.
   - Añade la sección de esa versión únicamente si puedes verificar la información. Sigue el formato existente para el enlace de versión, fecha, categorías y enlaces a commits.
   - Actualiza el enlace de comparación de `Unreleased` para que use como base el tag válido más reciente y termine en `HEAD`. Por ejemplo:
     `https://github.com/OWNER/REPO/compare/v1.0.0...HEAD`
   - Si el tag ya tiene una sección, no la dupliques ni la reescribas innecesariamente.
   - Si una versión cambió en un archivo del proyecto, pero no hay un tag correspondiente, no la trates como un lanzamiento.
   - No crees, muevas, elimines ni publiques tags bajo ninguna circunstancia.
   - Si no puedes verificar un tag, su fecha o los cambios que comprende, detente y consulta antes de añadir información no comprobada.

9. Antes de confirmar el changelog, muestra:
   - Los commits de código creados y sus hashes.
   - Los tags nuevos detectados, si los hay, y cómo se verificaron.
   - Los cambios de versión de los archivos del proyecto, si los hay.
   - El diff completo de `CHANGELOG.md`.
   - El mensaje propuesto para el commit del changelog.
   Si el diff incorpora cambios ajenos a esta ejecución o información no comprobada, detente y consulta.

10. Confirma la actualización de `CHANGELOG.md` en un commit separado:
    - Añade únicamente `CHANGELOG.md` con `git add CHANGELOG.md`.
    - Revisa el staging con `git diff --cached`.
    - Crea un commit semántico en español, por ejemplo: `docs: actualizar changelog`.
    - No añadas ese commit a las entradas del changelog ni intentes incluir su propio hash.

11. Verifica el estado final con:
    - `git status --short`
    - `git log --oneline -10`

12. Pregúntame si quiero ejecutar `git push` o hacerlo manualmente. No hagas push sin mi confirmación.

13. Al terminar, resume los commits creados, indica si se detectó un tag nuevo o un cambio de versión y, si se hizo push, especifica la rama enviada.
