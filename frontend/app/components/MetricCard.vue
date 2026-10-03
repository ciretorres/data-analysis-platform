<script setup>
// Tarjeta de métrica reutilizable (RF-03, RF-08).
// La página le pasa los datos por props; aquí solo se pintan.
defineProps({
  titulo: { type: String, required: true },
  valor: { type: String, required: true },
})
</script>

<template>
  <article class="metrica">
    <p class="metrica__valor">{{ valor }}</p>
    <h3 class="metrica__titulo">{{ titulo }}</h3>
    <!-- Etiqueta visible obligatoria: nunca se presentan como datos reales -->
    <p class="metrica__etiqueta">datos de ejemplo</p>
  </article>
</template>

<style scoped>
.metrica {
  background-color: var(--color-superficie);
  border: 1px solid var(--color-borde);
  border-radius: 12px;
  padding: 1.25rem;
}

.metrica__valor {
  margin: 0 0 0.25rem;
  color: var(--color-acento);
  font-size: 2rem;
  font-weight: 700;
}

.metrica__titulo {
  margin: 0 0 0.75rem;
  font-size: 1rem;
  font-weight: 600;
}

.metrica__etiqueta {
  display: inline-block;
  margin: 0;
  padding: 0.15rem 0.5rem;
  border: 1px solid var(--color-borde);
  border-radius: 999px;
  color: var(--color-texto-tenue);
  font-size: 0.75rem;
}
</style>
