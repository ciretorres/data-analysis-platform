# Spec 002 — Interfaz frontend con Vue y Nuxt

**Nivel**: 1 · **Estado**: Aprobada (pendiente de implementación) · **Fecha**: 2026-09-30 · **Revisada**: 2026-10-01 (QA)

## Contexto

El nivel 0 dejó el entorno listo: frontend y backend ejecutándose por separado
en local. El nivel 1 da forma a la primera página real de la plataforma,
construida únicamente con datos de ejemplo y sin ninguna conexión al backend.
La constitución fija el stack del proyecto (Vue y Nuxt para el frontend); esta
spec define qué se construye y por qué, no cómo se organiza el código.

## Objetivo

Que la principiante construya la página de inicio de la plataforma con piezas
reutilizables, datos simulados y diseño responsive, entendiendo la diferencia
entre página y componente antes de conectar nada a un backend.

## Usuarias

- **Principiante total**: persona del nivel 0 que ya sabe ejecutar frontend y
  backend por separado, pero nunca ha escrito un componente ni una ruta.
  Necesita ver resultados visuales inmediatos y comprobaciones manuales claras.

## Historia de usuaria

> Como principiante total, quiero construir la primera interfaz de la
> plataforma con piezas reutilizables y datos de ejemplo, para entender cómo
> se organiza una interfaz en componentes antes de conectarla a un backend.

## Requisitos funcionales

**RF-01 — Página de inicio con secciones de bienvenida**
La aplicación DEBERÁ mostrar una página de inicio con el nombre de la
aplicación, un título descriptivo, una descripción del proyecto y una sección
de bienvenida. El nombre y el título DEBERÁN ser elementos visuales distintos.
- CUANDO se abra la aplicación en el navegador, entonces SE VERÁ el nombre de
  la aplicación, el título y la descripción sin necesidad de interacción.
- CUANDO la usuaria lea la sección de bienvenida, entonces EL TEXTO estará
  dirigido a alguien que empieza a programar y DEBERÁ incluir al menos un
  párrafo de bienvenida.

**RF-02 — Menú de navegación por anclas**
La página DEBERÁ incluir un menú de navegación horizontal con 4 elementos en
este orden: Bienvenida, Métricas, Carga de archivo, Gráficos.
- CUANDO la usuaria active un elemento del menú, entonces LA PÁGINA se
  desplazará a la sección correspondiente.
- SI la usuaria no usa el menú, entonces la navegación NO DEBERÁ impedir el
  uso del resto de la página.
- MIENTRAS la usuaria haga scroll, el menú DEBERÁ permanecer visible en la
  parte superior de la página.

**RF-03 — Tarjetas de métricas simuladas**
La página DEBERÁ mostrar 4 tarjetas con métricas de ejemplo, cada una con una
etiqueta visible de "datos de ejemplo".
- CUANDO se abra la página, entonces SE VERÁN 4 tarjetas con valores
  numéricos de ejemplo.
- MIENTRAS no exista backend, entonces las métricas SERÁN estáticas o
  simuladas y NO DEBERÁN presentarse como datos reales.
- CADA tarjeta DEBERÁ incluir un texto visible que indique "datos de ejemplo".

**RF-04 — Botón de carga con selector y validación básica**
La página DEBERÁ incluir un botón que abra el selector de archivos del
sistema, muestre el nombre y el tamaño del archivo elegido (en KB o MB
según corresponda) y valide su extensión en el navegador, sin enviar el
archivo a ninguna parte.
- CUANDO la usuaria active el botón, entonces SE ABRIRÁ el selector de
  archivos del sistema.
- DESPUÉS DE elegir un archivo, cuando se confirme la selección, entonces SE
  MOSTRARÁ en pantalla el nombre y el tamaño del archivo.
- SI el archivo elegido no tiene extensión .csv (insensible a mayúsculas),
  entonces SE MOSTRARÁ un mensaje de error en español y NO se mostrará como
  cargado.
- SI el archivo elegido tiene extensión .csv pero está vacío (0 bytes),
  entonces SE MOSTRARÁ un mensaje de error en español.
- DESPUÉS de elegir un archivo, cuando se revise la interfaz, entonces EL
  ARCHIVO NO SALDRÁ del navegador.
- El botón DEBERÁ permitir selección de un solo archivo (no múltiple).

**RF-05 — Área reservada para gráficos**
La página DEBERÁ incluir un área visible de al menos 300px de altura reservada
para gráficos con el texto "Los gráficos aparecerán aquí en un nivel futuro".
- CUANDO se abra la página, entonces SE VERÁ el área de gráficos con su
  texto explicativo.
- MIENTRAS no exista procesamiento de datos, entonces el área NO DEBERÁ
  mostrar gráficos reales.

**RF-06 — Diseño responsive**
La interfaz DEBERÁ adaptarse a pantallas de distintos tamaños con los
siguientes breakpoints: móvil (<768px), tablet (768-1023px), escritorio
(≥1024px).
- CUANDO se abra la aplicación en una pantalla estrecha (móvil), entonces
  TODO el contenido SERÁ visible y usable sin desplazamiento horizontal.
- CUANDO se abra en pantalla ancha (escritorio), entonces LA PÁGINA mostrará
  las secciones de forma ordenada.
- El ancho máximo del contenido DEBERÁ ser de 1200px en escritorio.

**RF-07 — Funcionamiento sin backend**
La interfaz DEBERÁ funcionar de forma independiente del backend.
- CUANDO se abra la aplicación con el backend detenido, entonces LA PÁGINA
  cargará y mostrará todo su contenido igual que con el backend en marcha.
- MIENTRAS dure el nivel 1, entonces LA INTERFAZ NO DEBERÁ realizar ninguna
  petición al backend.

**RF-08 — Interfaz en piezas reutilizables**
La interfaz DEBERÁ organizarse en al menos 4 piezas pequeñas y reutilizables
(componentes): una para el menú, una para las tarjetas de métricas, una para
el botón de carga y una para el área de gráficos.
- SI se añade una métrica nueva, entonces PODRÁ mostrarse reutilizando la
  pieza de tarjeta existente sin reescribirla.
- CUANDO se revisen las secciones repetibles de la página, entonces CADA
  sección repetible EXISTIRÁ como pieza independiente.
- Las piezas PODRÁN compartir estilos globales definidos en un archivo CSS
  común.

**RF-09 — Conceptos del nivel documentados**
La documentación del nivel 1 DEBERÁ presentar los conceptos fundamentales
(componentes, props, eventos, estado reactivo, estado local, directivas,
renderizado condicional, renderizado de listas, rutas, layouts, diseño
responsive) con lenguaje comprensible para una principiante total, incluyendo
la diferencia entre página y componente. Los nombres propios de conceptos
técnicos (props, eventos, estado reactivo, etc.) se conservan en su forma
original; el resto del texto estará en español.
- DESPUÉS DE revisar la documentación, cuando se lea la sección de conceptos,
  entonces CADA concepto TENDRÁ una explicación breve en español.
- CUANDO se lea la diferencia entre página y componente, entonces ESTARÁ
  explicada con un ejemplo sencillo del propio proyecto.

## Requisitos no funcionales

- **RNF-01 — Legibilidad**: La documentación DEBERÁ ser comprensible para una
  principiante total.
- **RNF-02 — Idioma**: Todo texto, comentario y commit estará en español.
- **RNF-03 — Todo en local**: La página DEBERÁ cargarse sin servicios externos
  ni CDNs, solo con el servidor de desarrollo local.
- **RNF-04 — Protección de datos**: Los datos mostrados SERÁN de ejemplo y
  NUNCA datos personales de usuarias reales.
- **RNF-05 — Ampliación futura**: La interfaz DEBERÁ organizarse en piezas
  pequeñas para poder añadir funcionalidades en niveles posteriores sin
  reescribirla entera.

## Casos límite

- **CL-01**: La usuaria elige un archivo que no es .csv → se muestra error en
  español y no se muestra como cargado.
- **CL-02**: La usuaria abre el selector y cierra sin elegir nada → la
  interfaz no cambia y no muestra errores.
- **CL-03**: La usuaria elige un archivo ya elegido antes → se reemplaza la
  información mostrada por la nueva.
- **CL-04**: Pantalla muy estrecha (<768px) → las tarjetas y el menú se apilan
  sin romper el diseño.
- **CL-05**: La usuaria recarga la página → el nombre del archivo elegido se
  pierde (no hay persistencia en este nivel).
- **CL-06**: El backend está detenido → la interfaz se comporta igual.
- **CL-07**: Archivo con extensión .csv pero vacío (0 bytes) → se muestra
  error en español.
- **CL-08**: Archivo con nombre muy largo (>100 caracteres) → se trunca la
  visualización con puntos suspensivos.
- **CL-09**: Archivo con caracteres especiales en el nombre → se muestra
  correctamente sin romper el diseño.
- **CL-10**: Archivo con doble extensión (ej. datos.csv.txt) → se rechaza
  por no terminar en .csv.
- **CL-11**: Archivo con extensión en mayúsculas (.CSV) → se acepta como
  válido.
- **CL-12**: Zoom del navegador al 200% → el contenido sigue siendo usable.
- **CL-13**: El usuario arrastra y suelta un archivo → no está soportado en
  este nivel; solo se usa el botón.
- **CL-14**: El usuario selecciona un archivo válido y luego uno no válido →
  se muestra el error y se limpia la selección anterior.
- **CL-15**: El usuario navega a otra sección con un archivo seleccionado →
  el estado del archivo se mantiene.

## Fuera de alcance

- Conectar el frontend con el backend (ninguna petición HTTP/JSON).
- Enviar, guardar o procesar el archivo elegido (solo selección y validación
  visual en el navegador).
- Gráficos reales o librerías de gráficos.
- Tests automatizados (llegan en un nivel posterior; este nivel se verifica
  manualmente).
- Base de datos, autenticación, Docker, CI/CD.
- Métricas reales de datos.
- Selección múltiple de archivos.
- Arrastrar y soltar archivos (drag & drop).
- Librerías de UI o frameworks CSS extra (solo CSS vanilla).

## Criterios de finalización

El nivel 1 se considera terminado cuando, con verificación manual en el
navegador, se cumplan TODAS:
1. La página muestra nombre, título, descripción y bienvenida (RF-01).
2. Cada elemento del menú desplaza a su sección y el menú permanece visible
   al hacer scroll (RF-02).
3. Las 4 tarjetas muestran métricas de ejemplo con etiqueta visible "datos de
   ejemplo" (RF-03).
4. El botón abre el selector, muestra nombre y tamaño, valida la extensión
   .csv (insensible a mayúsculas) y rechaza archivos vacíos sin enviar el
   archivo (RF-04).
5. El área de gráficos muestra su placeholder con texto (RF-05).
6. La página es usable en móvil (<768px), tablet (768-1023px) y escritorio
   (≥1024px) sin scroll horizontal (RF-06).
7. La interfaz funciona igual con el backend detenido (RF-07).
8. Las secciones repetibles se reutilizan como piezas independientes (RF-08).
9. Los conceptos del nivel están documentados en español, incluida la
   diferencia página/componente (RF-09).

## Dudas abiertas

- ¿En qué nivel entran los tests automatizados exigidos por la constitución? [NECESITA ACLARACIÓN]
- ¿Aplica desde el nivel 1 la revisión de accesibilidad (skill accessibility)? [NECESITA ACLARACIÓN]
