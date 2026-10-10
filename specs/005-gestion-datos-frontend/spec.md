# Spec 005 — Gestión de datos desde el frontend (CRUD de datasets)

**Nivel**: 4 · **Estado**: borrador · **Fecha**: 2026-10-08

## Contexto

El nivel 3 conectó el frontend con el backend: la página de inicio hace una
petición a `/api/health` y muestra el estado de carga, error o datos. El nivel 4
da el siguiente paso: **consumir el CRUD completo de datasets** desde la
interfaz.

El backend ya tiene los endpoints CRUD en `/api/datasets` (creados en el nivel 2).
Este nivel es **solo frontend**: no se toca el backend.

La entidad `Dataset` tiene esta forma:

```json
{
  "id": 1,
  "name": "Ventas mensuales",
  "description": "Datos de ventas del año actual",
  "file_name": "ventas.csv",
  "created_at": "2026-09-29"
}
```

Endpoints disponibles:

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/datasets` | Obtener todos los datasets |
| GET | `/api/datasets/{id}` | Obtener un dataset |
| POST | `/api/datasets` | Crear un dataset |
| PUT | `/api/datasets/{id}` | Actualizar un dataset (reemplazo completo) |
| DELETE | `/api/datasets/{id}` | Eliminar un dataset |

## Objetivo

Que la principiante entienda cómo una aplicación Vue consume una API REST
completa: listar, crear, editar y eliminar datos, mostrando estados de carga,
mensajes de éxito y error, y actualizando la interfaz después de cada operación.

## Usuarias

- **Principiante total**: persona que ya ha conectado el frontend con el backend
  (nivel 3), pero nunca ha hecho un CRUD completo desde la interfaz. Necesita
  ver cómo se gestionan datos reales con formularios, cómo se actualiza la
  lista y cómo se manejan los errores del servidor.

## Historia de usuaria

> Como principiante total, quiero ver la lista de conjuntos de datos, crear
> nuevos, editarlos y eliminarlos desde la interfaz, para entender cómo una
> aplicación frontend gestiona datos con una API REST.

## Requisitos funcionales

**RF-01 — Composable `useDatasets`**

El frontend DEBERÁ incluir un composable `useDatasets.ts` que encapsule toda la
lógica de comunicación con la API de datasets.

- CUANDO se use el composable, entonces DEBERÁ devolver la lista de datasets,
  el estado de carga, el error (si lo hay) y las funciones para cada operación.
- El composable DEBERÁ usar el composable `useApi` del nivel 3 para las
  peticiones.
- El composable DEBERÁ incluir funciones para: obtener la lista, crear, actualizar
  y eliminar.
- El composable DEBERÁ actualizar la lista automáticamente después de cada
  operación exitosa.
- El composable DEBERÁ exponer la siguiente interfaz:
  - `datasets`: ref reactivo con la lista de datasets.
  - `loading`: ref booleano que indica si hay una petición en curso.
  - `error`: ref con el mensaje de error (string) o `null`.
  - `obtenerDatasets()`: función sin parámetros que hace `GET /api/datasets`.
  - `crearDataset(datos)`: función que recibe un objeto `{ name, description, file_name }` y hace `POST /api/datasets`.
  - `actualizarDataset(id, datos)`: función que recibe el id y un objeto `{ name, description, file_name }` y hace `PUT /api/datasets/{id}`.
  - `eliminarDataset(id)`: función que recibe el id y hace `DELETE /api/datasets/{id}`.
- DEPUÉS DE cada operación de escritura exitosa, el composable ACTUALIZARÁ la lista localmente con la respuesta del servidor, SIN necesidad de hacer otra petición `GET`.

**RF-02 — Componente `DatasetList`**

El frontend DEBERÁ incluir un componente `DatasetList.vue` que muestre la lista
de datasets.

- CUANDO se muestre el componente, entonces DEBERÁ mostrar cada dataset con su
  nombre, descripción, nombre de archivo y fecha de creación.
- SI la lista está vacía, entonces SE VERÁ un mensaje indicando que no hay
  datasets.
- MIENTRAS se cargan los datos, entonces SE VERÁ un estado de carga.
- SI hay un error, entonces SE VERÁ un mensaje de error en español.
- El componente DEBERÁ recibir las siguientes props:
  - `datasets`: Array de objetos Dataset (obligatoria).
  - `loading`: Booleano que indica si están cargando (obligatorio, default `false`).
  - `error`: String con mensaje de error o `null` (obligatorio, default `null`).
- El componente DEBERÁ emitir los siguientes eventos:
  - `editar`: cuando se pulse el botón "Editar" en una tarjeta (carga el dataset).
  - `eliminar`: cuando se confirme la eliminación de un dataset (carga el id).
- El componente DEBERÁ mostrar la fecha de creación en formato local español (`es-ES`, ej. "29 de septiembre de 2026").

**RF-03 — Componente `DatasetCard`**

El frontend DEBERÁ incluir un componente `DatasetCard.vue` que represente un
dataset individual.

- CUANDO se muestre el componente, entonces DEBERÁ mostrar los datos del
  dataset (nombre, descripción, archivo, fecha).
- El componente DEBERÁ incluir botones para editar y eliminar el dataset.
- CUANDO se pulse el botón de eliminar, entonces SE PEDIRÁ confirmación antes
  de proceder.
- El componente DEBERÁ recibir la siguiente prop:
  - `dataset`: Objeto Dataset (obligatoria).
- El componente DEBERÁ emitir los siguientes eventos:
  - `editar`: cuando se pulse el botón "Editar".
  - `eliminar`: cuando se pulse el botón "Eliminar".
- El componente DEBERÁ mostrar la fecha en formato local español (`es-ES`).

**RF-04 — Componente `DatasetForm`**

El frontend DEBERÁ incluir un componente `DatasetForm.vue` para crear y editar
datasets.

- CUANDO se use para crear, entonces EL FORMULARIO DEBERÁ tener los campos
  `name`, `description` y `file_name` vacíos.
- CUANDO se use para editar, entonces EL FORMULARIO DEBERÁ mostrar los datos
  actuales del dataset.
- El formulario DEBERÁ validar los campos antes de enviarlos:
  - `name` DEBERÁ ser obligatorio y no vacío ni solo espacios.
  - `name` DEBERÁ tener una longitud máxima de 100 caracteres.
  - `file_name` DEBERÁ ser obligatorio y no vacío ni solo espacios.
  - `file_name` DEBERÁ tener una longitud máxima de 255 caracteres.
  - `description` DEBERÁ ser opcional.
- SI la validación falla, entonces SE VERÁN mensajes de error junto a cada campo.
- CUANDO se envíe el formulario, entonces SE LLAMARÁ a la función correspondiente
  del composable.
- El componente DEBERÁ recibir la siguiente prop:
  - `modo`: String con valor `"crear"` o `"editar"` (obligatorio).
  - `dataset`: Objeto Dataset con los datos actuales (solo necesario en modo `"editar"`).
- El componente DEBERÁ emitir los siguientes eventos:
  - `guardar`: cuando se envíe el formulario con datos válidos (carga `{ name, description, file_name }`).
  - `cancelar`: cuando se pulse el botón "Cancelar".
- El botón de envío DEBERÁ estar deshabilitado mientras se realiza la petición.

**RF-05 — Componentes de estado `LoadingState` y `ErrorMessage`**

El frontend DEBERÁ incluir componentes reutilizables para mostrar estados de
carga y mensajes de error.

- `LoadingState.vue` DEBERÁ mostrar un mensaje de carga configurable.
- `ErrorMessage.vue` DEBERÁ mostrar un mensaje de error configurable con un
  botón para reintentar.
- Ambos componentes DEBERÁN ser reutilizables en cualquier sección de la
  aplicación.
- `LoadingState.vue` DEBERÁ recibir la siguiente prop:
  - `mensaje`: String con el texto a mostrar (opcional, default "Cargando...").
- `ErrorMessage.vue` DEBERÁ recibir la siguiente prop:
  - `mensaje`: String con el texto de error (obligatorio).
- `ErrorMessage.vue` DEBERÁ emitir el siguiente evento:
  - `reintentar`: cuando se pulse el botón de reintentar.

**RF-06 — Sección "Gestión de datasets" en la página de inicio**

La página de inicio DEBERÁ incluir una sección "Gestión de datasets" que integre
todos los componentes.

- CUANDO se abra la página, entonces SE INICIARÁ una petición a
  `GET /api/datasets`.
- MIENTRAS la petición esté en curso, entonces SE VERÁ el componente
  `LoadingState`.
- SI la petición falla, entonces SE VERÁ el componente `ErrorMessage`.
- CUANDO la petición sea exitosa, entonces SE VERÁ la lista de datasets o un
  mensaje de "No hay datasets".
- La sección DEBERÁ tener un enlace en el menú de navegación con el texto
  "Gestión de datasets".

**RF-07 — Crear un nuevo dataset**

La interfaz DEBERÁ permitir crear un nuevo dataset.

- CUANDO se pulse el botón "Nuevo dataset", entonces SE MOSTRARÁ el formulario
  en modo creación en un modal superpuesto a la página actual (sin navegación
  a otra página).
- CUANDO se envíe el formulario con datos válidos, entonces SE HARÁ una
  petición `POST /api/datasets`.
- SI la petición es exitosa, entonces SE AÑADIRÁ el dataset a la lista con la
  respuesta del servidor y SE MOSTRARÁ un mensaje de éxito.
- SI la petición falla, entonces SE MOSTRARÁ un mensaje de error en español.
- DEPUÉS DE cerrar el modal, la usuaria VOLVERÁ a la lista de datasets.

**RF-08 — Editar un dataset existente**

La interfaz DEBERÁ permitir editar un dataset.

- CUANDO se pulse el botón "Editar" en una tarjeta, entonces SE MOSTRARÁ el
  formulario en modo edición con los datos actuales en un modal superpuesto.
- CUANDO se envíe el formulario con datos válidos, entonces SE HARÁ una
  petición `PUT /api/datasets/{id}`.
- SI la petición es exitosa, entonces SE ACTUALIZARÁ el dataset en la lista con
  la respuesta del servidor y SE MOSTRARÁ un mensaje de éxito.
- SI la petición falla, entonces SE MOSTRARÁ un mensaje de error en español.

**RF-09 — Eliminar un dataset**

La interfaz DEBERÁ permitir eliminar un dataset.

- CUANDO se pulse el botón "Eliminar" en una tarjeta, entonces SE PEDIRÁ
  confirmación usando `window.confirm()` con el mensaje "¿Seguro que quieres
  eliminar este dataset?".
- SI se confirma, entonces SE HARÁ una petición `DELETE /api/datasets/{id}`.
- SI la petición es exitosa, entonces SE ELIMINARÁ el dataset de la lista y SE
  MOSTRARÁ un mensaje de éxito.
- SI la petición falla, entonces SE MOSTRARÁ un mensaje de error en español.
- SI se cancela, entonces NO SE HARÁ ninguna petición.

**RF-10 — Mensajes de éxito y error**

La interfaz DEBERÁ mostrar mensajes de éxito y error después de cada operación.

- CUANDO una operación sea exitosa, entonces SE MOSTRARÁ un mensaje de éxito
  en español (ej. "Dataset creado correctamente").
- CUANDO una operación falle, entonces SE MOSTRARÁ un mensaje de error en
  español (ej. "No se pudo crear el dataset. Inténtalo de nuevo.").
- Los mensajes DEBERÁN ser visibles durante 3 segundos y DESPUÉS desaparecerán
  automáticamente.

**RF-11 — Conceptos del nivel documentados**

La documentación del nivel 4 DEBERÁ presentar los conceptos fundamentales
(formularios controlados, estado reactivo, componentes reutilizables,
actualización de datos, composables de Nuxt, separación entre lógica y
presentación, manejo de errores del servidor, CRUD desde el frontend,
confirmación de acciones destructivas) con lenguaje comprensible para una
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
  ficheros de datos; la conexión es directa frontend ↔ backend. Los archivos de
  código (componentes, composables) SÍ forman parte del nivel.
- **RNF-05 — Separación de responsabilidades**: El código DEBERÁ separar la
  lógica (composables) de la presentación (componentes).
- **RNF-06 — Reutilización**: Los componentes de estado (carga, error) DEBERÁN
  ser reutilizables en cualquier sección.

## Casos límite

- **CL-01**: La lista de datasets está vacía → se muestra un mensaje indicando
  que no hay datasets.
- **CL-02**: El backend está detenido → se muestra un mensaje de error en
  español.
- **CL-03**: El backend tarda más de lo normal (más de 1 segundo) → se muestra
  el estado de carga hasta que responda.
- **CL-04**: Se crea un dataset con datos válidos → aparece en la lista
  inmediatamente después de la respuesta exitosa del servidor.
- **CL-05**: Se crea un dataset con `name` vacío o solo espacios → el formulario
  muestra un error y no se envía.
- **CL-06**: Se crea un dataset con `file_name` vacío o solo espacios → el
  formulario muestra un error y no se envía.
- **CL-07**: Se crea un dataset con `name` de más de 100 caracteres → el
  formulario muestra un error y no se envía.
- **CL-08**: Se crea un dataset con `file_name` de más de 255 caracteres → el
  formulario muestra un error y no se envía.
- **CL-09**: Se edita un dataset → el formulario muestra los datos actuales.
- **CL-10**: Se edita un dataset y se cambian los datos → la lista se actualiza
  con los valores de la respuesta del servidor.
- **CL-11**: Se elimina un dataset → desaparece de la lista.
- **CL-12**: Se cancela la eliminación → no se hace ninguna petición.
- **CL-13**: El servidor devuelve 404 al eliminar → se muestra un mensaje de
  error en español.
- **CL-14**: El servidor devuelve 404 al actualizar o eliminar un dataset que
  ya no existe (otro usuario lo eliminó) → se muestra un mensaje de error y se
  actualiza la lista haciendo un `GET /api/datasets` nuevo.
- **CL-15**: El servidor devuelve 422 al crear o editar → se muestra un
  mensaje de error específico junto a cada campo con error, y se mantiene lo que
  la usuaria escribió en el formulario.
- **CL-16**: El servidor devuelve 500 → se muestra un mensaje de error en
  español.
- **CL-17**: Se pulsa "Nuevo dataset" → el formulario se muestra vacío.
- **CL-18**: Se pulsa "Editar" → el formulario se muestra con los datos del
  dataset.
- **CL-19**: Se envía el formulario varias veces rápido → solo se hace una
  petición (se deshabilita el botón mientras se envía).
- **CL-20**: Se recarga la página mientras el formulario está abierto → se
  pierde el estado del formulario y se vuelve a la lista de datasets.

## Fuera de alcance

- Autenticación y autorización.
- Subida real de archivos: `file_name` es solo un texto.
- Tests automatizados (la verificación es manual, con el navegador).
- Docker, CI/CD.
- Paginación, búsqueda o filtros.
- PATCH (actualizaciones parciales): solo PUT de reemplazo completo.
- Modificar el backend.

## Criterios de finalización

El nivel 4 se considera terminado cuando, con verificación manual (navegador),
se cumplan TODAS:

1. El composable `useDatasets.ts` existe y encapsula la lógica del CRUD (RF-01).
2. El componente `DatasetList.vue` muestra la lista de datasets (RF-02).
3. El componente `DatasetCard.vue` muestra un dataset con botones de editar y
   eliminar (RF-03).
4. El componente `DatasetForm.vue` permite crear y editar con validación (RF-04).
5. Los componentes `LoadingState.vue` y `ErrorMessage.vue` existen y son
   reutilizables (RF-05).
6. La página de inicio tiene una sección "Gestión de datasets" con enlace en el
   menú (RF-06).
7. Se puede crear un dataset desde la interfaz (RF-07).
8. Se puede editar un dataset desde la interfaz (RF-08).
9. Se puede eliminar un dataset con confirmación (RF-09).
10. Se muestran mensajes de éxito y error (RF-10).
11. Los conceptos del nivel están documentados en español (RF-11).
12. Con el backend detenido, se muestra un mensaje de error (CL-02).
13. Con la lista vacía, se muestra un mensaje indicando que no hay datasets
    (CL-01).

## Dudas abiertas

- **Tests automatizados**: la constitución dice "tests obligatorios: Toda
  funcionalidad nueva incluye tests. Sin tests, no se mergea". Este nivel
  excluye los tests automatizados (RNF en "Fuera de alcance") porque el proyecto
  es educativo y la verificación es manual con navegador.

  [DECIDIDO POR LA USUARIA 2026-10-03]: La verificación de este nivel es
  manual, con el navegador, igual que se hizo en los niveles anteriores. No se
  incluyen tests automatizados.

- **Estructura de carpetas**: la petición original sugería rutas como
  `frontend/components/` y `frontend/composables/`, pero el proyecto usa
  `frontend/app/` como srcDir (Nuxt 4).

  [DECIDIDO POR LA USUARIA 2026-10-03]: La estructura real será:
  - `frontend/app/composables/useDatasets.ts`
  - `frontend/app/components/DatasetList.vue`
  - `frontend/app/components/DatasetCard.vue`
  - `frontend/app/components/DatasetForm.vue`
  - `frontend/app/components/LoadingState.vue`
  - `frontend/app/components/ErrorMessage.vue`
  - `frontend/app/pages/index.vue` (actualizado con la sección "Gestión de datasets")
