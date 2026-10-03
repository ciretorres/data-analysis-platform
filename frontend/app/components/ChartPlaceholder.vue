<template>
  <!-- RF-05: área reservada para gráficos, sin gráficos reales -->
  <div class="placeholder">
    <p class="placeholder__texto">
      Los gráficos aparecerán aquí en un nivel futuro
    </p>
    <p class="placeholder__nota">
      Este nivel reserva el espacio; todavía no hay datos procesados que dibujar.
    </p>
  </div>
</template>

<style scoped>
.placeholder {
  /* Altura mínima exigida por RF-05 */
  min-height: 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 1.5rem;
  text-align: center;
  border: 1px dashed var(--color-borde);
  border-radius: 12px;
  background-color: var(--color-superficie);
}

.placeholder__texto {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
}

.placeholder__nota {
  margin: 0;
  color: var(--color-texto-tenue);
  max-width: 50ch;
}
</style>
