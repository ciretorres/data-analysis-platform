# Conceptos del Nivel 1

Explicaciones en español para una principiante total. Los nombres propios de
los conceptos técnicos (props, eventos, estado reactivo, etc.) se conservan en
su forma original; el resto del texto está en español.

---

## Página y componente

### Página
Una página es el contenido que se muestra en una dirección (URL) de la
aplicación. En este proyecto, `frontend/app/pages/index.vue` es la página de
inicio: si escribes `http://localhost:3000/`, es lo que se ve. Cada archivo
dentro de `pages/` crea una ruta nueva automáticamente.

### Componente
Un componente es una pieza pequeña y reutilizable de interfaz, con su propia
plantilla y sus propios estilos. En este proyecto,
`frontend/app/components/MetricCard.vue` es un componente: dibuja una tarjeta
con un valor y un título, y la página lo usa cuatro veces sin copiarlo.

### ¿Cuándo uso uno u otra?
Usa **página** cuando el contenido es único de una dirección (la home, una
página de ayuda). Usa **componente** cuando la misma pieza se repite o cuando
quieres aislarla para reutilizarla. La página `index.vue` es como el guion de
un episodio: decide qué se ve y en qué orden; los componentes son los
actores: cada uno sabe interpretar su papel y puede aparecer varias veces.
Si mañana añades una quinta métrica, solo creas otro uso de `MetricCard`;
no reescribes la tarjeta.

---

## Piezas de una interfaz Vue

### Componentes
Archivos `.vue` que encapsulan plantilla (lo que se ve), lógica (lo que
ocurre) y estilos (cómo se ve). Nuxt los busca en `app/components/` y los
puedes usar en la plantilla con su nombre: `<MetricCard />`. Este nivel tiene
cuatro: `AppHeader` (menú), `MetricCard` (tarjetas), `FileUploader` (carga)
y `ChartPlaceholder` (área de gráficos).

### Props
Los datos que una página o componente le pasa a otro componente, como
argumentos de una función. Se declaran en `defineProps()` y se leen dentro de
la plantilla. Ejemplo: `index.vue` le pasa `titulo="Filas totales"` y
`valor="24.500"` a `MetricCard`; el componente no sabe de qué métrica se
trata, solo sabe pintar lo que le digan. Así una misma pieza sirve para
cualquier dato.

### Eventos
Avisos que emite el navegador cuando algo ocurre: un clic, la selección de un
archivo, la pulsación de una tecla. En Vue se escuchan con `@nombre` en la
plantilla. Ejemplo: en `FileUploader`, `@change="alElegirArchivo"` ejecuta la
función cada vez que la usuaria elige un archivo en el selector.

### Estado reactivo
La memoria de un componente: datos que, cuando cambian, hacen que la interfaz
se vuelva a dibujar sola. En Vue se crean con `ref()`. Ejemplo:
`FileUploader` guarda el archivo elegido en `archivo`; cuando `archivo` deja
de ser `null`, aparece en pantalla el nombre y el tamaño sin recargar nada.

### Estado local
El estado que vive dentro de un solo componente y no se comparte con el resto
de la aplicación. El nombre del archivo elegido es estado local de
`FileUploader`: solo esa pieza lo necesita. Empezar con estado local mantiene
las cosas simples; más adelante se verá cómo compartir estado entre
componentes.

### Directivas
Instrucciones en la plantilla que dan órdenes a Vue sobre cómo pintar un
elemento. Se escriben con `@` o `v-` y entre comillas. Ejemplos usados en
este nivel: `v-if` / `v-else-if` / `v-else` (renderizado condicional),
`v-for` (renderizado de listas) y `:key` (identificador de cada elemento de
una lista).

### Renderizado condicional
Mostrar o no un trozo de interfaz según una condición. Se hace con `v-if`,
`v-else-if` y `v-else`. Ejemplo: en `FileUploader` se ve el mensaje de error
solo si `error` tiene texto; si no, se ve el archivo cargado; y si tampoco,
se ve el texto de ayuda. Nunca se ven los tres a la vez.

### Renderizado de listas
Pintar un elemento por cada dato de un array con `v-for`. Ejemplo: la sección
de métricas recorre el array `metricas` y emite un `<MetricCard />` por cada
objeto, usando `:key` para que Vue identifique cada tarjeta. Si añades un
objeto al array, aparece una tarjeta nueva sin tocar la plantilla.

---

## Cómo organiza Nuxt la aplicación

### Rutas
La correspondencia entre una dirección de internet y una página. Nuxt la crea
a partir de `app/pages/`: el archivo `index.vue` atiende la dirección raíz
(`/`), y un archivo `ayuda.vue` atendería `/ayuda`. No hay que configurarlas
a mano.

### Layouts
Plantillas que envuelven a las páginas para que todas compartan lo mismo
(en este proyecto, el menú sticky y el contenido centrado). Vive en
`app/layouts/`; `default.vue` se aplica automáticamente. `app.vue` es el punto
de entrada: renderiza el layout (`<NuxtLayout>`) y dentro la página actual
(`<NuxtPage />`).

### Diseño responsive
Que la interfaz se adapta a distintos tamaños de pantalla sin versión propia
para cada uno. Se consigue con CSS flexible (cuadrículas y márgenes que se
reordenan) y con *media queries*, que aplican estilos a partir de un ancho de
pantalla. Este nivel usa dos puntos de quiebre: `768px` (pantallas medianas)
y `1024px` (escritorio). Ejemplo: las tarjetas de métricas se muestran en 1
columna en móvil, 2 en tablet y 4 en escritorio.

---

## Flujo de un archivo (nivel 1)

### Validación en el navegador
Comprobar si un archivo cumple las reglas (que su extensión sea una de las
admitidas —`.csv`, `.json` o `.pdf`— y que no esté vacío) usando solo
JavaScript dentro del navegador, sin enviarlo a ningún servidor. En este
proyecto la hacen funciones puras en
`app/utils/validacion.js` (`validarExtension`, `formatearTamano`,
`truncarNombre`), que reciben datos y devuelven un resultado sin tocar nada
más.

### Estado sin persistencia
Los datos que se pierden al recargar la página. En este nivel, si recargas,
el nombre del archivo elegido desaparece: el estado vive solo en la memoria
del componente. Guardarlo entre recargas llegará en un nivel futuro.
