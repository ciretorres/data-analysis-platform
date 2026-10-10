<script setup lang="ts">
defineProps<{ mensaje?: string }>()
</script>

<template>
  <div class="cargando" role="status">
    <p>{{ mensaje ?? 'Cargando...' }}</p>
  </div>
</template>

<style scoped>
.cargando {
  padding: 1rem;
  color: var(--color-texto-tenue);
  font-style: italic;
}
</style>
