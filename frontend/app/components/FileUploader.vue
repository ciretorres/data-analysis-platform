<script setup>
import { validarExtension, formatearTamano, truncarNombre, EXTENSIONES_PERMITIDAS } from '~/utils/validacion.js'

// Formatos admitidos del nivel 1: ".csv, .json, .pdf" y ".csv, .json o .pdf"
const formatos = EXTENSIONES_PERMITIDAS.map((extension) => `.${extension}`)
const formatosTexto = formatos.join(', ')
const formatosLegible = formatos.length > 1
  ? [formatos.slice(0, -1).join(', '), formatos.at(-1)].join(' o ')
  : formatos.join('')
const acceptFormatos = formatos.flatMap((formato) => [formato, formato.toUpperCase()]).join(',')

// Estado local del componente (RF-04): el archivo solo se valida en el
// navegador, nunca se envía a un servidor (RF-07).
const archivo = ref(null) // { nombre, tamano } | null
const error = ref('') // mensaje en español; vacío si no hay error

// Ref de plantilla al input (RF-08): sin id fijos, la pieza puede instanciarse
// varias veces en la misma página sin pisarse.
const inputArchivo = ref(null)

function abrirSelector() {
  inputArchivo.value?.click()
}

function alElegirArchivo(evento) {
  const elegido = evento.target.files?.[0]

  // CL-02: al cancelar el selector no llega archivo y nada cambia.
  // Reiniciar el valor permite volver a elegir el mismo archivo (CL-03).
  evento.target.value = ''
  if (!elegido) return

  // CL-14: una selección nueva reemplaza a la anterior
  error.value = ''
  archivo.value = null

  // CL-01 / CL-10 / CL-11: validación de extensión (.csv, .json o .pdf)
  if (!validarExtension(elegido.name)) {
    error.value = `«${truncarNombre(elegido.name)}» no tiene una extensión admitida (${formatosTexto}). Elige un archivo ${formatosLegible}.`
    return
  }

  // CL-07: archivo admitido pero vacío
  if (elegido.size === 0) {
    error.value = `El archivo «${truncarNombre(elegido.name)}» está vacío (0 bytes).`
    return
  }

  archivo.value = {
    nombre: elegido.name,
    tamano: formatearTamano(elegido.size),
  }
}
</script>

<template>
  <div class="cargador">
    <!-- Selector del sistema. El input está oculto y lo abre el botón.
         Sin atributo multiple: selección de un solo archivo.
         Se referencia por ref (no por id) para que el componente sea
         reutilizable si se usa más de una vez (RF-08). -->
    <input
      ref="inputArchivo"
      class="visually-hidden"
      type="file"
      :accept="acceptFormatos"
      :aria-label="`Elegir archivo (${formatosTexto})`"
      @change="alElegirArchivo"
    />

    <button class="boton" type="button" @click="abrirSelector">
      Elegir archivo ({{ formatosTexto }})
    </button>

    <!-- Renderizado condicional: error, cargado o estado inicial -->
    <p v-if="error" class="cargador__error" role="alert">{{ error }}</p>

    <p v-else-if="archivo" class="cargador__ok" role="status">
      <strong>{{ truncarNombre(archivo.nombre) }}</strong>
      · {{ archivo.tamano }}
      <span class="cargador__nota">
        (solo se validó en el navegador: el archivo no ha salido de tu equipo)
      </span>
    </p>

    <p v-else class="cargador__ayuda">
      Ningún archivo seleccionado todavía. Se admite un único archivo
      {{ formatosLegible }} (mayúsculas o minúsculas) con contenido.
    </p>
  </div>
</template>

<style scoped>
.cargador {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.75rem;
}

.cargador__error {
  margin: 0;
  color: var(--color-error);
  font-weight: 600;
}

.cargador__ok {
  margin: 0;
  padding: 0.75rem 1rem;
  border: 1px solid rgba(0, 220, 130, 0.4);
  border-radius: 8px;
  background-color: rgba(0, 220, 130, 0.08);
  overflow-wrap: anywhere;
}

.cargador__nota {
  display: block;
  color: var(--color-texto-tenue);
  font-size: 0.875rem;
}

.cargador__ayuda {
  margin: 0;
  color: var(--color-texto-tenue);
}
</style>
