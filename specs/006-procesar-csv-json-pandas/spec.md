# Spec 006 — Procesar archivos CSV o JSON con Python y Pandas

**Nivel**: 5 · **Estado**: borrador · **Fecha**: 2026-10-10

## Contexto

El nivel 4 permitió gestionar datasets desde el frontend (CRUD completo). El
nivel 5 da el salto al **procesamiento real de datos**: permitir que la usuaria
suba un archivo CSV o JSON y obtener un resumen básico de sus datos usando
Pandas en el backend.

El backend ya tiene el router de datasets en `/api/datasets` (nivel 2). Este
nivel añade un endpoint nuevo: `POST /api/datasets/upload`. El frontend debe
permitir subir archivos y mostrar el resumen devuelto por el backend.

La respuesta esperada del endpoint es:

```json
{
  "file_name": "ventas.csv",
  "rows": 3,
  "columns": 3,
  "column_names": ["producto", "precio", "cantidad"],
  "missing_values": {
    "producto": 0,
    "precio": 1,
    "cantidad": 0
  },
  "statistics": {
    "precio": {
      "count": 2,
      "mean": 15.5,
      "std": 7.778,
      "min": 10,
      "25%": 12.75,
      "50%": 15.5,
      "75%": 18.25,
      "max": 21
    },
    "cantidad": {
      "count": 3,
      "mean": 20.0,
      "std": 8.66,
      "min": 10,
      "25%": 15.5,
      "50%": 20,
      "75%": 24.5,
      "max": 30
    }
  },
  "preview": [
    { "producto": "A", "precio": 10, "cantidad": 10 },
    { "producto": "B", "precio": null, "cantidad": 20 },
    { "producto": "C", "precio": 21, "cantidad": 30 }
  ]
}
```

Estructura de la respuesta:

- `statistics`: objeto donde cada clave es una columna numérica y cada valor es
  un objeto con las métricas `count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`,
  `max`.
- `preview`: array de objetos, donde cada objeto representa una fila con
  claves = nombres de columnas. Incluye como máximo 5 filas.

## Objetivo

Que la principiante entienda cómo se procesan archivos de datos reales con
Pandas: subir un archivo, validarlo, leerlo, calcular estadísticas básicas y
devolver un resumen estructurado al frontend.

## Usuarias

- **Principiante total**: persona que ya ha hecho un CRUD completo desde el
  frontend (nivel 4), pero nunca ha procesado archivos de datos con Python.
  Necesita ver cómo se suben archivos, cómo se validan y cómo se calculan
  estadísticas básicas con Pandas.

## Historia de usuaria

> Como principiante total, quiero subir un archivo CSV o JSON y ver un resumen
> básico de sus datos (filas, columnas, nombres, tipos, valores nulos y
> estadísticas), para entender cómo se procesan archivos de datos con Pandas.

## Requisitos funcionales

**RF-01 — Instalación de Pandas en el backend**

El backend DEBERÁ incluir Pandas como dependencia.

- CUANDO se instalen las dependencias del backend, entonces Pandas DEBERÁ
  estar disponible en el entorno virtual.
- El archivo `backend/requirements.txt` DEBERÁ listar Pandas.

**RF-02 — Endpoint `POST /api/datasets/upload`**

El backend DEBERÁ exponer un endpoint `POST /api/datasets/upload` que reciba
un archivo CSV o JSON y devuelva un resumen de sus datos.

- CUANDO se envíe un archivo CSV o JSON válido, entonces EL SERVIDOR DEBERÁ
  devolver código 200 con un JSON que contenga:
  - `file_name`: nombre del archivo original.
  - `rows`: número de filas del DataFrame.
  - `columns`: número de columnas del DataFrame.
  - `column_names`: lista con los nombres de las columnas.
  - `missing_values`: objeto con el conteo de valores nulos por columna.
- CUANDO se envíe un archivo CSV o JSON válido, entonces EL SERVIDOR DEBERÁ
  calcular estadísticas descriptivas (count, mean, std, min, 25%, 50%, 75%,
  max) para las columnas numéricas y DEBERÁ incluirlas en la respuesta bajo la
  clave `statistics`.
- CUANDO se envíe un archivo CSV o JSON válido, entonces EL SERVIDOR DEBERÁ
  incluir las primeras 5 filas del DataFrame en la respuesta bajo la clave
  `preview`.

**RF-03 — Validación de extensión**

El backend DEBERÁ validar que el archivo subido tenga una extensión permitida.

- CUANDO se envíe un archivo con extensión `.csv`, entonces EL SERVIDOR DEBERÁ
  aceptarlo.
- CUANDO se envíe un archivo con extensión `.json`, entonces EL SERVIDOR DEBERÁ
  aceptarlo.
- CUANDO se envíe un archivo con extensión no permitida (ej. `.txt`, `.xlsx`,
  `.pdf`), entonces EL SERVIDOR DEBERÁ devolver código 400 con un mensaje de
  error en español indicando que el formato no es válido.

**RF-04 — Validación de tamaño**

El backend DEBERÁ validar que el archivo subido no supere un tamaño máximo.

- CUANDO se envíe un archivo que supere 10 MB, entonces EL SERVIDOR DEBERÁ
  devolver código 400 con un mensaje de error en español indicando que el
  archivo es demasiado grande.
- CUANDO se envíe un archivo de 10 MB o menos, entonces EL SERVIDOR DEBERÁ
  aceptarlo.

**RF-05 — Lectura con Pandas**

El backend DEBERÁ leer el archivo subido con Pandas.

- CUANDO se envíe un archivo CSV, entonces EL SERVIDOR DEBERÁ leerlo con
  `pd.read_csv()`.
- CUANDO se envíe un archivo JSON, entonces EL SERVIDOR DEBERÁ leerlo con
  `pd.read_json()`.
- SI el archivo está malformado o no se puede leer, entonces EL SERVIDOR
  DEBERÁ devolver código 400 con un mensaje de error en español.

**RF-06 — Manejo de errores del endpoint**

El backend DEBERÁ manejar los errores de forma apropiada.

- SI el archivo no se puede leer (malformado, vacío, etc.), entonces EL
  SERVIDOR DEBERÁ devolver código 400 con un mensaje de error en español.
- SI ocurre un error inesperado durante el procesamiento, entonces EL SERVIDOR
  DEBERÁ devolver código 500 con un mensaje de error en español.

**RF-07 — Composable `useUpload`**

El frontend DEBERÁ incluir un composable `useUpload.ts` que encapsule la
lógica de subida de archivos. El composable usará `fetch` directamente (no
`useApi`, que está diseñado solo para peticiones GET sin cuerpo).

- CUANDO se use el composable, entonces DEBERÁ devolver el estado de carga,
  el error (si lo hay) y la función de subida.
- El composable DEBERÁ usar `FormData` para enviar el archivo.
- El composable DEBERÁ usar `fetch` directamente para la petición POST con
  `FormData`, ya que `useApi` del nivel 3 solo soporta peticiones GET sin cuerpo.
- El composable DEBERÁ exponer la siguiente interfaz:
  - `loading`: ref booleano que indica si hay una petición en curso.
  - `error`: ref con el mensaje de error (string) o `null`.
  - `summary`: ref con el resumen devuelto por el servidor o `null`.
  - `subirArchivo(archivo: File)`: función que recibe un archivo y hace
    `POST /api/datasets/upload`.

**RF-08 — Componente `FileUpload`**

El frontend DEBERÁ incluir un componente `FileUpload.vue` que permita
seleccionar y subir un archivo.

- CUANDO se muestre el componente, entonces DEBERÁ mostrar un campo de
  selección de archivo que acepte `.csv` y `.json`.
- CUANDO se seleccione un archivo, entonces SE MOSTRARÁ el nombre del archivo.
- CUANDO se pulse el botón "Subir", entonces SE LLAMARÁ a la función
  `subirArchivo` del composable.
- MIENTRAS se sube el archivo, entonces SE VERÁ un estado de carga y el botón
  de subida DEBERÁ estar deshabilitado.
- SI la subida es exitosa, entonces SE MOSTRARÁ el resumen devuelto por el
  servidor.
- SI la subida falla, entonces SE MOSTRARÁ un mensaje de error en español.

**RF-09 — Componente `DataSummary`**

El frontend DEBERÁ incluir un componente `DataSummary.vue` que muestre el
resumen de los datos subidos.

- CUANDO se muestre el componente, entonces DEBERÁ mostrar:
  - El nombre del archivo.
  - El número de filas y columnas.
  - La lista de nombres de columnas.
  - El conteo de valores nulos por columna.
  - Las estadísticas descriptivas (para columnas numéricas).
  - Una vista previa de las primeras 5 filas.
- El componente DEBERÁ recibir la siguiente prop:
  - `summary`: Objeto con el resumen devuelto por el servidor (obligatoria).

**RF-10 — Sección "Procesar archivo" en la página de inicio**

La página de inicio DEBERÁ incluir una sección "Procesar archivo" que integre
los componentes de subida y resumen.

- CUANDO se abra la página, entonces SE VERÁ la sección "Procesar archivo".
- La sección DEBERÁ tener un enlace en el menú de navegación con el texto
  "Procesar archivo".
- CUANDO se suba un archivo válido, entonces SE MOSTRARÁ el resumen en la
  misma sección.

**RF-11 — Conceptos del nivel documentados**

La documentación del nivel 5 DEBERÁ presentar los conceptos fundamentales
(subida de archivos, FormData, UploadFile, lectura de archivos con Pandas,
DataFrames, estadística descriptiva, validación de archivos, serialización
de datos, tratamiento de errores) con lenguaje comprensible para una
principiante total.

- DESPUÉS DE revisar la documentación, cuando se lea la sección de conceptos,
  entonces CADA concepto TENDRÁ una explicación breve en español.

## Requisitos no funcionales

- **RNF-01 — Legibilidad**: La documentación DEBERÁ ser comprensible para una
  principiante total.
- **RNF-02 — Idioma**: Todo texto, comentario y documentación estará en
  español.
- **RNF-03 — Todo en local**: La comunicación DEBERÁ funcionar solo con los
  servidores de desarrollo locales (frontend :3000, backend :8000).
- **RNF-04 — Sin persistencia adicional**: No se DEBERÁ añadir base de datos ni
  ficheros de datos; los archivos subidos se procesan en memoria y no se
  guardan en disco.
- **RNF-05 — Separación de responsabilidades**: El código DEBERÁ separar la
  lógica (composables) de la presentación (componentes).
- **RNF-06 — Reutilización**: Los componentes de estado (carga, error) DEBERÁN
  ser reutilizables en cualquier sección.

## Casos límite

- **CL-01**: Se sube un archivo CSV válido → se devuelve el resumen con filas,
  columnas, nombres, valores nulos, estadísticas y vista previa.
- **CL-02**: Se sube un archivo JSON válido → se devuelve el resumen con filas,
  columnas, nombres, valores nulos, estadísticas y vista previa.
- **CL-03**: Se sube un archivo con extensión no permitida (ej. `.txt`) → se
  devuelve 400 con mensaje de error en español.
- **CL-04**: Se sube un archivo que supera 10 MB → se devuelve 400 con mensaje
  de error en español.
- **CL-05**: Se sube un archivo CSV malformado → se devuelve 400 con mensaje
  de error en español.
- **CL-06**: Se sube un archivo JSON malformado → se devuelve 400 con mensaje
  de error en español.
- **CL-07**: Se sube un archivo de 0 bytes (completamente vacío) → se devuelve
  400 con mensaje de error en español.
- **CL-08**: El backend está detenido → se muestra el mensaje de error
  "No se pudo conectar con el servidor. Inténtalo de nuevo." (mensaje genérico
  del composable) en el frontend.
- **CL-09**: Se sube un archivo válido → se muestra el resumen en el frontend
  con todos los datos correctos.
- **CL-10**: Se sube un archivo con columnas numéricas → se muestran las
  estadísticas descriptivas (count, mean, std, min, 25%, 50%, 75%, max).
- **CL-11**: Se sube un archivo con columnas no numéricas → las estadísticas
  solo incluyen las columnas numéricas.
- **CL-12**: Se sube un archivo con valores nulos → se muestra el conteo de
  valores nulos por columna.
- **CL-13**: Se sube un archivo sin valores nulos → el conteo de valores nulos
  es 0 para todas las columnas.
- **CL-14**: Se selecciona un archivo en el frontend → se muestra el nombre
  del archivo.
- **CL-15**: Se pulsa "Subir" sin seleccionar archivo → no se hace ninguna
  petición.
- **CL-16**: Se envía el formulario varias veces rápido → solo se hace una
  petición (se deshabilita el botón mientras se envía).
- **CL-17**: Se recarga la página mientras se muestra el resumen → se pierde
  el resumen y se vuelve al estado inicial.
- **CL-18**: Se sube un CSV con cabecera pero 0 filas de datos, o un JSON con
  array vacío `[]` → se devuelve 200 con `rows: 0`, `statistics: {}` y
  `preview: []`.
- **CL-19**: Se sube un JSON válido sintácticamente pero no tabular (ej. un
  objeto anidado como `{"datos": {...}}` o un objeto plano sin array) → se
  devuelve 400 con mensaje de error en español indicando que el JSON no tiene
  un formato tabular válido.

## Fuera de alcance

- Autenticación y autorización.
- Persistencia de archivos subidos en disco.
- Tests automatizados (la verificación es manual, con el navegador).
  **[DECIDIDO POR LA USUARIA]**: Desviación documentada de la constitución
  (ver specs 003 y 005). La verificación es manual con navegador.
- Docker, CI/CD.
- Paginación, búsqueda o filtros.
- Visualización de gráficos (placeholder con texto).
- Procesamiento de archivos Excel (`.xlsx`).
- Modificar los endpoints CRUD existentes del nivel 2.

## Criterios de finalización

El nivel 5 se considera terminado cuando, con verificación manual (navegador),
se cumplan TODAS:

1. Pandas está instalado y listado en `backend/requirements.txt` (RF-01).
2. El endpoint `POST /api/datasets/upload` devuelve el resumen correcto para un
   CSV válido (RF-02).
3. El endpoint `POST /api/datasets/upload` devuelve el resumen correcto para un
   JSON válido (RF-02).
4. El endpoint rechaza archivos con extensión no permitida con 400 (RF-03).
5. El endpoint rechaza archivos que superan 10 MB con 400 (RF-04).
6. El endpoint devuelve 400 con mensaje en español si el archivo está
   malformado (RF-05).
7. El composable `useUpload.ts` existe y encapsula la lógica de subida (RF-07).
8. El componente `FileUpload.vue` permite seleccionar y subir archivos (RF-08).
9. El componente `DataSummary.vue` muestra el resumen completo (RF-09).
10. La página de inicio tiene una sección "Procesar archivo" con enlace en el
    menú (RF-10).
11. Se puede subir un CSV válido y ver el resumen en el frontend (CL-01).
12. Se puede subir un JSON válido y ver el resumen en el frontend (CL-02).
13. Se muestra un error al subir un archivo con extensión no permitida (CL-03).
14. Se muestra un error al subir un archivo demasiado grande (CL-04).
15. Se muestra un error al subir un archivo malformado (CL-05, CL-06).
16. Con el backend detenido, se muestra un mensaje de error en el frontend
    (CL-08).
17. Los conceptos del nivel están documentados en español (RF-11).

## Dudas abiertas

- **Tests automatizados**: igual que en niveles anteriores, la verificación es
  manual con navegador. No se incluyen tests automatizados.
  **[DECIDIDO POR LA USUARIA]**: Desviación de la constitución documentada
  explícitamente, como se hizo en specs 003 (líneas 254-261) y 005 (líneas
  330-338). El proyecto educativo prioriza la verificación manual con navegador
  sobre tests automatizados.

- **Tamaño máximo de archivo**: se establece 10 MB como límite razonable para
  un proyecto educativo. Este valor puede ajustarse en niveles posteriores.

- **Estadísticas para columnas no numéricas**: solo se calculan estadísticas
  descriptivas para columnas numéricas. Las columnas de texto o fecha no
  incluyen estadísticas en este nivel.

- **Numeración de carpeta vs. nivel**: la carpeta es `006` pero el nivel es 5.
  Se mantiene la numeración actual por consistencia con el repositorio (004 =
  nivel 3, 006 = nivel 5). Las specs anteriores usan el mismo patrón.
