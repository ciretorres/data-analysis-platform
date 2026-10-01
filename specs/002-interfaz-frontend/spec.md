# Spec 002 — Interfaz frontend con Vue y Nuxt

**Nivel**: 1 · **Estado**: Aprobada (pendiente de implementación) · **Fecha**: 2026-09-30

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
aplicación, el título y la descripción del proyecto, y una sección de
bienvenida.
- CUANDO se abra la aplicación en el navegador, entonces SE VERÁ el nombre de
  la aplicación, el título y la descripción sin necesidad de interacción.
- CUANDO la usuaria lea la sección de bienvenida, entonces EL TEXTO estará
  dirigido a alguien que empieza a programar.

**RF-02 — Menú de navegación por anclas**
La página DEBERÁ incluir un menú de navegación que enlace a las secciones de
la propia página (bienvenida, métricas, carga de archivo, gráficos).
- CUANDO la usuaria active un elemento del menú, entonces LA PÁGINA se
  desplazará a la sección correspondiente.
- SI la usuaria no usa el menú, entonces la navegación NO DEBERÁ impedir el
  uso del resto de la página.

**RF-03 — Tarjetas de métricas simuladas**
La página DEBERÁ mostrar tarjetas con métricas de ejemplo, claramente de
origen simulado.
- CUANDO se abra la página, entonces SE VERÁN tarjetas con valores de ejemplo.
- MIENTRAS no exista backend, entonces las métricas SERÁN estáticas o
  simuladas y NO DEBERÁN presentarse como datos reales.

**RF-04 — Botón de carga con selector y validación básica**
La página DEBERÁ incluir un botón que abra el selector de archivos del
sistema, muestre el nombre y el tamaño del archivo elegido y valide su
extensión en el navegador, sin enviar el archivo a ninguna parte.
- CUANDO la usuaria active el botón, entonces SE ABRIRÁ el selector de
  archivos del sistema.
- DESPUÉS DE elegir un archivo, cuando se confirme la selección, entonces SE
  MOSTRARÁ en pantalla el nombre y el tamaño del archivo.
- SI el archivo elegido no tiene extensión .csv, entonces SE MOSTRARÁ un
  mensaje de error en español y NO se mostrará como cargado.
- DESPUÉS de elegir un archivo, cuando se revise la interfaz, entonces EL
  ARCHIVO NO SALDRÁ del navegador.

**RF-05 — Área reservada para gráficos**
La página DEBERÁ incluir un área visible reservada para gráficos con un
mensaje que explique que llegarán en un nivel futuro.
- CUANDO se abra la página, entonces SE VERÁ el área de gráficos con su
  texto explicativo.
- MIENTRAS no exista procesamiento de datos, entonces el área NO DEBERÁ
  mostrar gráficos reales.

**RF-06 — Diseño responsive**
La interfaz DEBERÁ adaptarse a pantallas de distintos tamaños.
- CUANDO se abra la aplicación en una pantalla estrecha (móvil), entonces
  TODO el contenido SERÁ visible y usable sin desplazamiento horizontal.
- CUANDO se abra en pantalla ancha (escritorio), entonces LA PÁGINA mostrará
  las secciones de forma ordenada.

**RF-07 — Funcionamiento sin backend**
La interfaz DEBERÁ funcionar de forma independiente del backend.
- CUANDO se abra la aplicación con el backend detenido, entonces LA PÁGINA
  cargará y mostrará todo su contenido igual que con el backend en marcha.
- MIENTRAS dure el nivel 1, entonces LA INTERFAZ NO DEBERÁ realizar ninguna
  petición al backend.

**RF-08 — Interfaz en piezas reutilizables**
La interfaz DEBERÁ organizarse en piezas pequeñas y reutilizables
(componentes) en lugar de un único bloque.
- SI se añade una métrica nueva, entonces PODRÁ mostrarse reutilizando la
  pieza de tarjeta existente sin reescribirla.
- CUANDO se revisen las secciones repetibles de la página, entonces CADA
  sección repetible EXISTIRÁ como pieza independiente.

**RF-09 — Conceptos del nivel documentados**
La documentación del nivel 1 DEBERÁ presentar los conceptos fundamentales
(componentes, props, eventos, estado reactivo, estado local, directivas,
renderizado condicional, renderizado de listas, rutas, layouts, diseño
responsive) con lenguaje comprensible para una principiante total, incluyendo
la diferencia entre página y componente.
- DESPUÉS DE revisar la documentación, cuando se lea la sección de conceptos,
  entonces CADA concepto TENDRÁ una explicación breve en español.
- CUANDO se lea la diferencia entre página y componente, entonces ESTARÁ
  explicada con un ejemplo sencillo del propio proyecto.

## Requisitos no funcionales

- **RNF-01 — Legibilidad**: La documentación DEBERÁ ser comprensible para una
  principiante total.
- **RNF-02 — Idioma**: Todo texto, comentario y commit estará en español.
- **RNF-03 — Todo en local**: La página DEBERÁ cargarse sin servicios externos
  más allá del servidor de desarrollo local.
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
- **CL-04**: Pantalla muy estrecha → las tarjetas y el menú se apilan sin
  romper el diseño.
- **CL-05**: La usuaria recarga la página → el nombre del archivo elegido se
  pierde (no hay persistencia en este nivel).
- **CL-06**: El backend está detenido → la interfaz se comporta igual.

## Fuera de alcance

- Conectar el frontend con el backend (ninguna petición HTTP/JSON).
- Enviar, guardar o procesar el archivo elegido (solo selección y validación
  visual en el navegador).
- Gráficos reales o librerías de gráficos.
- Tests automatizados (llegan en un nivel posterior; este nivel se verifica
  manualmente).
- Base de datos, autenticación, Docker, CI/CD.
- Métricas reales de datos.

## Criterios de finalización

El nivel 1 se considera terminado cuando, con verificación manual en el
navegador, se cumplan TODAS:
1. La página muestra nombre, título, descripción y bienvenida (RF-01).
2. Cada elemento del menú desplaza a su sección (RF-02).
3. Las tarjetas muestran métricas de ejemplo sin pasar por datos reales (RF-03).
4. El botón abre el selector, muestra nombre y tamaño y valida la extensión
   .csv sin enviar el archivo (RF-04).
5. El área de gráficos muestra su placeholder con texto (RF-05).
6. La página es usable en móvil y escritorio sin scroll horizontal (RF-06).
7. La interfaz funciona igual con el backend detenido (RF-07).
8. Las secciones repetibles se reutilizan como piezas independientes (RF-08).
9. Los conceptos del nivel están documentados en español, incluida la
   diferencia página/componente (RF-09).

## Dudas abiertas

- ¿Qué tamaño máximo de archivo se acepta en la validación? [NECESITA ACLARACIÓN]
- ¿En qué nivel entran los tests automatizados exigidos por la constitución? [NECESITA ACLARACIÓN]
- ¿Aplica desde el nivel 1 la revisión de accesibilidad (skill accessibility)? [NECESITA ACLARACIÓN]
- ¿Las métricas simuladas deben llevar una etiqueta visible de "datos de
  ejemplo"? [NECESITA ACLARACIÓN]
- ¿El menú debe quedar fijo al hacer scroll o basta con que esté al
  inicio? [NECESITA ACLARACIÓN]
