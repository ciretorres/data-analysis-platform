<script setup lang="ts">
interface Dataset {
  id: number
  name: string
  description: string | null
  file_name: string
  created_at: string
}

const props = defineProps<{ dataset: Dataset }>()
const emit = defineEmits<{
  editar: [dataset: Dataset]
  eliminar: [id: number]
}>()

function formatearFecha(fecha: string): string {
  return new Intl.DateTimeFormat('es-ES', { dateStyle: 'long' }).format(new Date(fecha))
}

function confirmarEliminar() {
  if (window.confirm('¿Seguro que quieres eliminar este dataset?')) {
    emit('eliminar', props.dataset.id)
  }
}
</script>

<template>
  <article class="tarjeta">
    <h3>{{ dataset.name }}</h3>
    <p v-if="dataset.description">{{ dataset.description }}</p>
    <p><strong>Archivo:</strong> {{ dataset.file_name }}</p>
    <p><strong>Creado:</strong> {{ formatearFecha(dataset.created_at) }}</p>
    
    <div class="tarjeta__acciones">
      <button @click="emit('editar', dataset)">Editar</button>
      <button @click="confirmarEliminar">Eliminar</button>
    </div>
  </article>
</template>

<style scoped>
.tarjeta {
  padding: 1rem;
  border: 1px solid var(--color-borde);
  border-radius: 0.5rem;
}

.tarjeta h3 {
  margin-top: 0;
}

.tarjeta__acciones {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.75rem;
}
</style>
