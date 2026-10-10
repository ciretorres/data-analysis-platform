# Conceptos del Nivel 4 — Gestión de datos desde el frontend

Este documento explica los conceptos fundamentales que se usan en el nivel 4,
con lenguaje sencillo para alguien que está empezando a programar.

---

## 1. Formularios controlados

Un **formulario controlado** es un formulario cuyos campos están ligados al
estado de Vue. Cada vez que la usuaria escribe en un campo, el valor se guarda
automáticamente en una variable reactiva (`ref`). Al revés: si cambia la
variable, el campo se actualiza solo.

En este proyecto, `DatasetForm.vue` usa `v-model` para ligar cada input a un
`ref`:

```vue
<input v-model="name" type="text" />
```

Así, cuando la usuaria escribe "Ventas", `name.value` pasa a ser "Ventas".
Cuando se envía el formulario, leemos `name.value` para enviarlo al servidor.

**Ventaja**: el formulario y el estado siempre están sincronizados, y podemos
validar o transformar los datos antes de enviarlos.

---

## 2. Estado reactivo

El **estado reactivo** es la información que puede cambiar con el tiempo y que
Vue observa automáticamente. Cuando el estado cambia, la interfaz se
actualiza sola.

En Vue 3 se crea con `ref` o `Reactive`:

```typescript
const cargando = ref(false)
cargando.value = true  // Vue detecta el cambio y actualiza la interfaz
```

En este nivel usamos estado reactivo para:

- Saber si se está cargando (`loading`).
- Guardar el mensaje de error (`error`).
- Guardar la lista de datasets (`datasets`).
- Saber si el modal está abierto (`mostrarModal`).

---

## 3. Componentes reutilizables

Un **componente reutilizable** es un trozo de interfaz que se puede usar en
varias partes de la aplicación sin repetir código.

En este nivel, `LoadingState.vue` y `ErrorMessage.vue` son componentes
reutilizables: se usan en la sección "Gestión de datasets" y podrían usarse en
cualquier otra sección que necesite mostrar carga o error.

```vue
<LoadingState mensaje="Cargando datasets..." />
<ErrorMessage mensaje="No se pudo conectar" @reintentar="reintentar" />
```

---

## 4. Actualización de datos (sin recargar la página)

Cuando se crea, edita o elimina un dataset, la lista se actualiza **sin
recargar la página** y **sin hacer otra petición GET**. El servidor devuelve
el dataset creado/actualizado, y nosotros lo añadimos o reemplazamos en la
lista local:

```typescript
// Crear: añadir el nuevo dataset a la lista
datasets.value.push(nuevo)

// Actualizar: reemplazar el dataset en su posición
datasets.value[indice] = actualizado

// Eliminar: quitar el dataset de la lista
datasets.value = datasets.value.filter((d) => d.id !== id)
```

Esto hace que la interfaz se sienta rápida: no hay que esperar a que el
servidor devuelva la lista completa otra vez.

---

## 5. Composables de Nuxt

Un **composable** es una función que encapsula lógica reactiva y se puede
compartir entre componentes. En Nuxt, los composables viven en la carpeta
`composables/` y se importan con `~/composables/...`.

En este nivel, `useDatasets.ts` es un composable que encapsula toda la
comunicación con la API de datasets:

```typescript
const { datasets, loading, error, obtenerDatasets, crearDataset } = useDatasets()
```

El componente no necesita saber cómo se hace la petición: solo llama a
`crearDataset(datos)` y el composable se encarga del resto.

---

## 6. Separación entre lógica y presentación

La **separación entre lógica y presentación** significa que el código que
comunica con el servidor (lógica) está separado del código que muestra la
interfaz (presentación).

- **Lógica**: `useDatasets.ts` — hace las peticiones, maneja errores,
  actualiza la lista.
- **Presentación**: `DatasetList.vue`, `DatasetCard.vue`, `DatasetForm.vue` —
  muestran los datos y emiten eventos cuando la usuaria interactúa.

Esto hace que el código sea más fácil de entender, mantener y reutilizar.

---

## 7. Manejo de errores del servidor

El servidor puede devolver errores: 404 (no encontrado), 422 (datos inválidos),
500 (error interno). El frontend debe mostrar un mensaje claro en español.

En `useDatasets.ts`, cuando una petición falla, se guarda un mensaje de error:

```typescript
if (!respuesta.ok) {
  errorDatasets.value = 'No se pudo crear el dataset. Inténtalo de nuevo.'
  throw e
}
```

En `index.vue`, cuando la operación falla, se muestra un mensaje de error que
desaparece a los 3 segundos:

```typescript
catch {
  mostrarMensaje('error', 'No se pudo guardar el dataset. Inténtalo de nuevo.')
}
```

---

## 8. CRUD desde el frontend

**CRUD** son las cuatro operaciones básicas sobre datos:

| Operación | Método HTTP | Función en `useDatasets` |
|-----------|-------------|--------------------------|
| **C**reate (crear) | POST | `crearDataset(datos)` |
| **R**ead (leer) | GET | `obtenerDatasets()` |
| **U**pdate (actualizar) | PUT | `actualizarDataset(id, datos)` |
| **D**elete (eliminar) | DELETE | `eliminarDataset(id)` |

En este nivel, todas estas operaciones se hacen desde la interfaz: la usuaria
pulsa botones, el frontend hace la petición, y la lista se actualiza.

---

## 9. Confirmación de acciones destructivas

Una **acción destructiva** es una operación que no se puede deshacer, como
eliminar un dataset. Antes de ejecutarla, se pide confirmación a la usuaria.

En este proyecto se usa `window.confirm()`, que muestra un diálogo nativo del
navegador:

```typescript
if (window.confirm('¿Seguro que quieres eliminar este dataset?')) {
  emit('eliminar', props.dataset.id)
}
```

Si la usuaria pulsa "Aceptar", se emite el evento y se hace la petición. Si
pulsa "Cancelar", no se hace nada.

---

## Resumen

| Concepto | Dónde se aplica |
|----------|-----------------|
| Formularios controlados | `DatasetForm.vue` con `v-model` |
| Estado reactivo | `ref` en `index.vue` y `useDatasets.ts` |
| Componentes reutilizables | `LoadingState.vue`, `ErrorMessage.vue` |
| Actualización de datos | `useDatasets.ts` (push, reemplazar, filter) |
| Composables de Nuxt | `useDatasets.ts` |
| Separación lógica/presentación | Composables vs. componentes |
| Manejo de errores | `try/catch` en `useDatasets.ts` y `index.vue` |
| CRUD desde el frontend | Botones en `DatasetCard.vue` y `index.vue` |
| Confirmación de acciones destructivas | `window.confirm()` en `DatasetCard.vue` |
