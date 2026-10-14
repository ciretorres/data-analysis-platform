<script setup lang="ts">
import type { DataSummary } from '~/composables/useUpload'

const props = defineProps<{ summary: DataSummary }>()

function formatearNumero(n: number | null): string {
  if (n === null || n === undefined) return 'null'
  return new Intl.NumberFormat('es-ES', { maximumFractionDigits: 2 }).format(n)
}
</script>

<template>
  <section class="resumen">
    <h3>Resumen: {{ summary.file_name }}</h3>

    <div class="resumen__grid">
      <div class="resumen__item">
        <span class="resumen__label">Filas:</span>
        <span class="resumen__valor">{{ summary.rows }}</span>
      </div>
      <div class="resumen__item">
        <span class="resumen__label">Columnas:</span>
        <span class="resumen__valor">{{ summary.columns }}</span>
      </div>
    </div>

    <div class="resumen__seccion">
      <h4>Columnas</h4>
      <ul>
        <li v-for="col in summary.column_names" :key="col">{{ col }}</li>
      </ul>
    </div>

    <div class="resumen__seccion">
      <h4>Valores nulos por columna</h4>
      <ul>
        <li v-for="(valor, col) in summary.missing_values" :key="col">
          {{ col }}: {{ valor }}
        </li>
      </ul>
    </div>

    <div v-if="Object.keys(summary.statistics).length > 0" class="resumen__seccion">
      <h4>Estadísticas descriptivas</h4>
      <div v-for="(stats, col) in summary.statistics" :key="col" class="resumen__stats">
        <h5>{{ col }}</h5>
        <ul>
          <li>Count: {{ stats.count }}</li>
          <li>Mean: {{ formatearNumero(stats.mean) }}</li>
          <li>Std: {{ formatearNumero(stats.std) }}</li>
          <li>Min: {{ formatearNumero(stats.min) }}</li>
          <li>25%: {{ formatearNumero(stats['25%']) }}</li>
          <li>50%: {{ formatearNumero(stats['50%']) }}</li>
          <li>75%: {{ formatearNumero(stats['75%']) }}</li>
          <li>Max: {{ formatearNumero(stats.max) }}</li>
        </ul>
      </div>
    </div>

    <div class="resumen__seccion">
      <h4>Vista previa (primeras 5 filas)</h4>
      <table class="resumen__tabla">
        <thead>
          <tr>
            <th v-for="col in summary.column_names" :key="col">{{ col }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(fila, i) in summary.preview" :key="i">
            <td v-for="col in summary.column_names" :key="col">
              {{ fila[col] ?? 'null' }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<style scoped>
.resumen {
  margin-top: 1.5rem;
  padding: 1.25rem;
  border: 1px solid var(--color-borde);
  border-radius: 0.5rem;
  background-color: var(--color-fondo);
}

.resumen__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 0.75rem;
  margin: 1rem 0;
}

.resumen__item {
  display: flex;
  flex-direction: column;
  padding: 0.75rem;
  border: 1px solid var(--color-borde);
  border-radius: 0.375rem;
}

.resumen__label {
  color: var(--color-texto-tenue);
  font-size: 0.875rem;
}

.resumen__valor {
  font-size: 1.25rem;
  font-weight: 600;
}

.resumen__seccion {
  margin-top: 1.25rem;
}

.resumen__seccion h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
}

.resumen__seccion ul {
  margin: 0;
  padding-left: 1.25rem;
}

.resumen__stats {
  margin-bottom: 0.75rem;
}

.resumen__stats h5 {
  margin: 0 0 0.25rem 0;
  color: var(--color-acento);
}

.resumen__tabla {
  width: 100%;
  border-collapse: collapse;
  margin-top: 0.5rem;
  font-size: 0.875rem;
}

.resumen__tabla th,
.resumen__tabla td {
  padding: 0.5rem;
  border: 1px solid var(--color-borde);
  text-align: left;
}

.resumen__tabla th {
  background-color: var(--color-fondo-elevado, rgba(255, 255, 255, 0.03));
  font-weight: 600;
}
</style>
