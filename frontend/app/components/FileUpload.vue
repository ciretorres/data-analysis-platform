<script setup lang="ts">
import { ref } from 'vue'
import { useUpload } from '~/composables/useUpload'
import LoadingState from './LoadingState.vue'
import ErrorMessage from './ErrorMessage.vue'
import DataSummary from './DataSummary.vue'

const { loading, error, summary, subirArchivo } = useUpload()

const archivoSeleccionado = ref<File | null>(null)
const nombreArchivo = ref('')

function alSeleccionar(event: Event) {
  const input = event.target as HTMLInputElement
  const archivo = input.files?.[0]

  if (archivo) {
    archivoSeleccionado.value = archivo
    nombreArchivo.value = archivo.name
  }
}

async function alSubir() {
  if (!archivoSeleccionado.value) return
  await subirArchivo(archivoSeleccionado.value)
}
</script>

<template>
  <section id="procesar-archivo" class="seccion">
    <h2>Procesar archivo</h2>
    <p class="seccion__intro">
      Selecciona un archivo CSV o JSON para ver un resumen de sus datos.
    </p>

    <div class="subida__controles">
      <input
        type="file"
        accept=".csv,.json"
        @change="alSeleccionar"
        :disabled="loading"
      />
      <button @click="alSubir" :disabled="!archivoSeleccionado || loading">
        Subir
      </button>
    </div>

    <p v-if="nombreArchivo" class="subida__nombre">
      Archivo seleccionado: <strong>{{ nombreArchivo }}</strong>
    </p>

    <LoadingState v-if="loading" mensaje="Procesando archivo..." />
    <ErrorMessage v-else-if="error" :mensaje="error" @reintentar="alSubir" />

    <DataSummary v-else-if="summary" :summary="summary" />
  </section>
</template>

<style scoped>
.subida__controles {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  flex-wrap: wrap;
}

.subida__nombre {
  margin: 0.75rem 0;
  color: var(--color-texto-tenue);
}
</style>
