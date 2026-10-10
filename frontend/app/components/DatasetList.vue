<script setup lang="ts">
import DatasetCard from './DatasetCard.vue'
import LoadingState from './LoadingState.vue'
import ErrorMessage from './ErrorMessage.vue'

interface Dataset {
  id: number
  name: string
  description: string | null
  file_name: string
  created_at: string
}

defineProps<{
  datasets: Dataset[]
  loading: boolean
  error: string | null
}>()

const emit = defineEmits<{
  editar: [dataset: Dataset]
  eliminar: [id: number]
  reintentar: []
}>()
</script>

<template>
  <div class="lista">
    <LoadingState 
      v-if="loading" 
      mensaje="Cargando datasets..." />
    
    <ErrorMessage 
      v-else-if="error" 
      :mensaje="error" @reintentar="emit('reintentar')" />

    <p v-else-if="datasets.length === 0" class="lista__vacio">
      No hay datasets todavía.
    </p>

    <div v-else class="lista__tarjetas">
      <DatasetCard
        v-for="dataset in datasets"
        :key="dataset.id"
        :dataset="dataset"
        @editar="emit('editar', $event)"
        @eliminar="emit('eliminar', $event)"
      />
    </div>
  </div>
</template>

<style scoped>
.lista__vacio {
  color: var(--color-texto-tenue);
  font-style: italic;
}

.lista__tarjetas {
  display: grid;
  gap: 1rem;
}
</style>
