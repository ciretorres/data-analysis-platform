<script setup lang="ts">
defineProps<{ mensaje: string }>()

const emit = defineEmits<{ reintentar: [] }>()
</script>

<template>
  <div class="error" role="alert">
    <p>{{ mensaje }}</p>
    <button @click="emit('reintentar')">Reintentar</button>
  </div>
</template>

<style scoped>
.error {
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid rgba(248, 113, 113, 0.3);
  background-color: rgba(248, 113, 113, 0.05);
  color: #f87171;
}

.error button {
  margin-top: 0.5rem;
}
</style>
