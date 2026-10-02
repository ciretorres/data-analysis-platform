# Plan de implementación — Spec 002 (Nivel 1)

**Fecha**: 2026-10-02 · **Estado**: Aprobado

## 1. Archivos a crear/modificar y responsabilidades

| Archivo | Responsabilidad | RF cubierto |
|---------|----------------|-------------|
| `frontend/pages/index.vue` | Página de inicio. Contiene las 4 secciones (bienvenida, métricas, carga, gráficos) y el menú sticky. | RF-01, RF-02, RF-06, RF-07 |
| `frontend/components/AppHeader.vue` | Menú de navegación horizontal sticky con 4 anclas (Bienvenida, Métricas, Carga de archivo, Gráficos). | RF-02 |
| `frontend/components/MetricCard.vue` | Tarjeta reutilizable con título, valor numérico y etiqueta "datos de ejemplo". | RF-03, RF-08 |
| `frontend/components/FileUploader.vue` | Botón de carga con selector de archivos, validación .csv, muestra nombre/tamaño, mensajes de error. | RF-04 |
| `frontend/components/ChartPlaceholder.vue` | Área reservada de 300px con texto "Los gráficos aparecerán aquí en un nivel futuro". | RF-05 |
| `frontend/layouts/default.vue` | Layout que envuelve la página con el menú sticky y el contenido. | RF-02, RF-06 |
| `frontend/app/app.vue` | Punto de entrada: sustituye la bienvenida de nivel 0 (o `<NuxtWelcome />`) por `<NuxtLayout>` + `<NuxtPage>` para que se rendericen página y layout. | RF-01, RF-02 |
| `frontend/assets/css/main.css` | Estilos globales compartidos (variables CSS, tipografía, colores). | RF-06, RF-08 |
| `frontend/nuxt.config.ts` | Configuración de Nuxt: puerto 3000, sin módulos extra. | RF-07 |
| `docs/conceptos-nivel-1.md` | Documentación de conceptos del nivel 1 (componentes, props, eventos, etc.). | RF-09 |

## 2. Funciones puras de lógica

| Función | Ubicación | Responsabilidad | RF |
|---------|-----------|-----------------|---|
| `validarExtension(nombreArchivo)` | `frontend/utils/validacion.js` | Retorna `true` si el archivo termina en `.csv` (insensible a mayúsculas). | RF-04 |
| `formatearTamano(bytes)` | `frontend/utils/validacion.js` | Convierte bytes a KB o MB según corresponda. | RF-04 |
| `truncarNombre(nombre, max)` | `frontend/utils/validacion.js` | Trunca nombres largos con puntos suspensivos. | RF-04, CL-08 |

## 3. Cómo se pinta la interfaz

**Layout (`layouts/default.vue`):**
- Menú sticky en la parte superior con fondo oscuro semitransparente
- Contenido centrado con ancho máximo 1200px

**Página (`pages/index.vue`):**
- Sección Bienvenida: nombre de la aplicación, título, descripción, párrafo de bienvenida
- Sección Métricas: grid de 4 tarjetas (1 col móvil, 2 col tablet, 4 col escritorio)
- Sección Carga de archivo: botón + área de estado
- Sección Gráficos: placeholder de 300px

**Componentes:**
- `AppHeader`: menú horizontal con 4 enlaces ancla
- `MetricCard`: tarjeta con título, valor, etiqueta "datos de ejemplo"
- `FileUploader`: botón + estado (vacío, cargado, error)
- `ChartPlaceholder`: área gris con texto centrado

## 4. Decisiones técnicas y justificación

| Decisión | Justificación | RF/RNF |
|----------|---------------|--------|
| **Componentes en `frontend/components/`** | RF-08 exige piezas reutilizables independientes. | RF-08 |
| **Layout en `frontend/layouts/`** | RF-02 exige menú sticky; Nuxt usa layouts para envolver páginas. | RF-02, RF-06 |
| **Página en `frontend/pages/`** | Nuxt usa pages para rutas; RF-01 exige página de inicio. | RF-01 |
| **CSS vanilla en `assets/css/`** | Fuera de alcance prohíbe frameworks CSS extra. | RNF-03 |
| **Validación en `utils/`** | Funciones puras reutilizables, fáciles de probar. | RF-04 |
| **Sin conexión al backend** | RF-07 exige independencia del backend. | RF-07 |
| **Datos simulados estáticos** | RF-03 exige métricas de ejemplo, no reales. | RF-03, RNF-04 |
| **Breakpoints 768px/1024px** | RF-06 define breakpoints concretos. | RF-06 |
| **Sin tests automatizados** | Fuera de alcance: tests llegan en nivel posterior. | — |

## 5. Cobertura de RFs

| RF | Dónde se implementa |
|----|---------------------|
| RF-01 | `pages/index.vue` (sección bienvenida) |
| RF-02 | `components/AppHeader.vue` + `layouts/default.vue` |
| RF-03 | `components/MetricCard.vue` + datos estáticos en `pages/index.vue` |
| RF-04 | `components/FileUploader.vue` + `utils/validacion.js` |
| RF-05 | `components/ChartPlaceholder.vue` |
| RF-06 | `assets/css/main.css` + `layouts/default.vue` |
| RF-07 | Ninguna referencia al backend en todo el frontend |
| RF-08 | 4 componentes independientes + `assets/css/main.css` compartido |
| RF-09 | `docs/conceptos-nivel-1.md` |
