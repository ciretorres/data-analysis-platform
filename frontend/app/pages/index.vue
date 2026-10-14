<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useApi } from '~/composables/useApi'
import { useDatasets } from '~/composables/useDatasets'
import type { Dataset } from '~/composables/useDatasets'
import DatasetList from '~/components/DatasetList.vue'
import DatasetForm from '~/components/DatasetForm.vue'
import FileUpload from '~/components/FileUpload.vue'

// Métricas estáticas de ejemplo (RF-03): no vienen de ningún servidor (RF-07)
const metricas = [
  { id: 'archivos', titulo: 'Archivos cargados', valor: '3' },
  { id: 'filas', titulo: 'Filas totales', valor: '24.500' },
  { id: 'columnas', titulo: 'Columnas detectadas', valor: '12' },
  { id: 'tiempo', titulo: 'Tiempo de carga (ms)', valor: '320' },
]

// Estado de la API (RF-05): petición real al backend
interface EstadoApi {
  app_name: string
  status: string
  version: string
  response_date: string
}

const { datos, cargando, error, pedir } = useApi<EstadoApi>('http://localhost:8000/api/health')
const { datos: datosE, cargando: cargandoE, error: errorE, pedir: pedirE } = useApi<EstadoApi>('error')

// Nivel 4: gestión de datasets (RF-01, RF-06..RF-10)
const {
  datasets,
  loading,
  error: errorDatasets,
  obtenerDatasets,
  crearDataset,
  actualizarDataset,
  eliminarDataset,
} = useDatasets()

const mostrarModal = ref(false)
const modoModal = ref<'crear' | 'editar'>('crear')
const datasetEditando = ref<Dataset | null>(null)
const mensaje = ref<{ tipo: 'exito' | 'error'; texto: string } | null>(null)
const enviando = ref(false)

let temporizadorMensaje: ReturnType<typeof setTimeout> | undefined

onMounted(() => {
  pedir()
  pedirE()
  obtenerDatasets()
})

function mostrarMensaje(tipo: 'exito' | 'error', texto: string) {
  mensaje.value = { tipo, texto }

  clearTimeout(temporizadorMensaje)
  
  temporizadorMensaje = setTimeout(() => {
    mensaje.value = null
  }, 3000)
}

function abrirCrear() {
  modoModal.value = 'crear'
  datasetEditando.value = null
  mostrarModal.value = true
}

function abrirEditar(dataset: Dataset) {
  modoModal.value = 'editar'
  datasetEditando.value = dataset
  mostrarModal.value = true
}

async function alGuardar(datos: { name: string; description: string | null; file_name: string }) {
  enviando.value = true

  try {
    if (modoModal.value === 'crear') {
      await crearDataset(datos)

      mostrarMensaje('exito', 'Dataset creado correctamente.')
    } else if (datasetEditando.value) {
      await actualizarDataset(datasetEditando.value.id, {
        ...datos,
        created_at: datasetEditando.value.created_at,
      })
      
      mostrarMensaje('exito', 'Dataset actualizado correctamente.')
    }
    
    mostrarModal.value = false
  } catch {
    mostrarMensaje('error', 'No se pudo guardar el dataset. Inténtalo de nuevo.')
  } finally {
    enviando.value = false
  }
}

async function alEliminar(id: number) {
  enviando.value = true

  try {
    await eliminarDataset(id)
  
    mostrarMensaje('exito', 'Dataset eliminado correctamente.')
  } catch {
    mostrarMensaje('error', 'No se pudo eliminar el dataset. Inténtalo de nuevo.')
  } finally {
    enviando.value = false
  }
}

function alCancelar() {
  mostrarModal.value = false
}
</script>

<template>
  <div class="inicio">
    <!-- RF-01: nombre, título, descripción y bienvenida -->
    <section id="bienvenida" class="seccion">
      <p class="nombre-app">Data Analysis Platform</p>
      <h1 class="titulo">Tu primera plataforma de análisis de datos</h1>
      <p class="descripcion">
        Plataforma web para cargar, procesar y visualizar archivos CSV.
        Proyecto educativo que se construye por niveles de aprendizaje.
      </p>

      <h2>Bienvenida</h2>
      <p>
        Si estás empezando a programar, esta página es el primer paso de tu
        proyecto: una interfaz hecha con piezas pequeñas y datos de ejemplo.
        Aquí verás cómo se organiza una página en componentes, cómo se mueve
        entre secciones con un menú y cómo se reserva un sitio para cargar tus
        archivos (CSV, JSON o PDF). Todo funciona en tu propio ordenador, sin
        enviar nada a
        ningún servidor.
      </p>
    </section>

    <!-- RF-03: 4 tarjetas de métricas reutilizando MetricCard (RF-08) -->
    <section id="metricas" class="seccion">
      <h2>Métricas</h2>
      <p class="seccion__intro">
        Valores de ejemplo que más adelante se calcularán con tus datos
        reales. Ahora mismo son datos de ejemplo, no medidas reales.
      </p>
      <div class="metricas">
        <MetricCard
          v-for="metrica in metricas"
          :key="metrica.id"
          :titulo="metrica.titulo"
          :valor="metrica.valor"
        />
      </div>
    </section>

    <!-- RF-04: carga de archivo con validación en el navegador -->
    <section id="carga-archivo" class="seccion">
      <h2>Carga de archivo</h2>
      <p class="seccion__intro">
        Elige un archivo .csv, .json o .pdf desde tu equipo. Solo se comprueba
        el nombre y
        el tamaño en el navegador: el archivo no se envía a ningún sitio.
      </p>
      <FileUploader />
    </section>

    <!-- RF-05: área reservada para gráficos -->
    <section id="graficos" class="seccion">
      <h2>Gráficos</h2>
      <ChartPlaceholder />
    </section>

    <!-- Nivel 3: estado de la API (RF-05) -->
    <section id="estado-api" class="seccion">
      <h2>Estado de la API</h2>
      <p class="seccion__intro">
        Esta sección hace una petición real al backend y muestra su respuesta.
      </p>

      <!-- Estado de carga -->
      <p v-if="cargando" class="estado-api estado-api--cargando">
        Cargando estado de la API…
      </p>

      <!-- Error -->
      <p v-else-if="error" class="estado-api estado-api--error">
        {{ error }}
      </p>

      <!-- Datos -->
      <div v-else-if="datos" class="estado-api__datos">
        <p><strong>Aplicación:</strong> {{ datos.app_name }}</p>
        <p><strong>Estado:</strong> {{ datos.status }}</p>
        <p><strong>Versión:</strong> {{ datos.version }}</p>
        <p><strong>Fecha de respuesta:</strong> {{ datos.response_date }}</p>
      </div>
    </section>

    <section id="estado-api-error" class="seccion">
      <h2>Estado de la API con error</h2>
      <p class="seccion__intro">
        Esta sección hace una petición real al backend y muestra su respuesta.
      </p>

      <!-- Estado de carga -->
      <p v-if="cargandoE" class="estado-api estado-api--cargando">
        Cargando estado de la API…
      </p>

      <!-- Error -->
      <p v-else-if="errorE" class="estado-api estado-api--error">
        {{ errorE }}
      </p>

      <!-- Datos -->
      <div v-else-if="datosE" class="estado-api__datos">
        <p><strong>Aplicación:</strong> {{ datosE.app_name }}</p>
        <p><strong>Estado:</strong> {{ datosE.status }}</p>
        <p><strong>Versión:</strong> {{ datosE.version }}</p>
        <p><strong>Fecha de respuesta:</strong> {{ datosE.response_date }}</p>
      </div>
    </section>

    <!-- Nivel 4: gestión de datasets (RF-06..RF-10) -->
    <section id="gestion-datasets" class="seccion">
      <h2>Gestión de datasets</h2>
      <p class="seccion__intro">
        Lista, crea, edita y elimina conjuntos de datos.
      </p>

      <button @click="abrirCrear">Nuevo dataset</button>

      <!-- Mensajes de éxito/error (RF-10) -->
      <p v-if="mensaje" class="mensaje" :class="`mensaje--${mensaje.tipo}`">
        {{ mensaje.texto }}
      </p>

      <DatasetList
        :datasets="datasets"
        :loading="loading"
        :error="errorDatasets"
        @editar="abrirEditar"
        @eliminar="alEliminar"
        @reintentar="obtenerDatasets"
      />
    </section>

    <!-- Nivel 5: procesar archivo (RF-02..RF-10) -->
    <FileUpload />
  </div>

  <!-- Modal de crear/editar (RF-07, RF-08) -->
  <div v-if="mostrarModal" class="modal-overlay" @click.self="alCancelar">
    <div 
      class="modal" 
      role="dialog" 
      aria-modal="true" 
      :aria-labelledby="`modal-${modoModal}`"
      >
      <h3 :id="`modal-${modoModal}`">
        {{ modoModal === 'crear' ? 'Nuevo dataset' : 'Editar dataset' }}
      </h3>

      <DatasetForm
        :modo="modoModal"
        :dataset="datasetEditando ?? undefined"
        @guardar="alGuardar"
        @cancelar="alCancelar"
      />
    </div>
  </div>
</template>

<style scoped>
.nombre-app {
  display: inline-block;
  margin-bottom: 0.75rem;
  padding: 0.25rem 0.75rem;
  border: 1px solid rgba(0, 220, 130, 0.3);
  border-radius: 999px;
  background-color: rgba(0, 220, 130, 0.1);
  color: var(--color-acento);
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.titulo {
  font-size: clamp(1.75rem, 4vw, 2.5rem);
}

.descripcion {
  color: var(--color-texto-tenue);
  max-width: 65ch;
  font-size: 1.0625rem;
}

/* RF-06: 1 columna en móvil, 2 en tablet (≥768px), 4 en escritorio (≥1024px) */
.metricas {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

@media (min-width: 768px) {
  .metricas {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .metricas {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

/* Nivel 3: estilos de la sección "Estado de la API" */
.estado-api {
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid var(--color-borde);
}

.estado-api--cargando {
  color: var(--color-texto-tenue);
  font-style: italic;
}

.estado-api--error {
  color: #f87171;
  border-color: rgba(248, 113, 113, 0.3);
  background-color: rgba(248, 113, 113, 0.05);
}

.estado-api__datos p {
  margin: 0.25rem 0;
}

/* Nivel 4: estilos de la sección "Gestión de datasets" */
.mensaje {
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  margin: 0.75rem 0;
}

.mensaje--exito {
  border: 1px solid rgba(0, 220, 130, 0.3);
  background-color: rgba(0, 220, 130, 0.1);
  color: var(--color-acento);
}

.mensaje--error {
  border: 1px solid rgba(248, 113, 113, 0.3);
  background-color: rgba(248, 113, 113, 0.05);
  color: #f87171;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.6);
  padding: 1rem;
}

.modal {
  width: 100%;
  max-width: 32rem;
  padding: 1.5rem;
  border-radius: 0.75rem;
  background-color: var(--color-fondo);
  border: 1px solid var(--color-borde);
}

.modal h3 {
  margin-top: 0;
}
</style>
