<script setup>
// Métricas estáticas de ejemplo (RF-03): no vienen de ningún servidor (RF-07)
const metricas = [
  { id: 'archivos', titulo: 'Archivos cargados', valor: '3' },
  { id: 'filas', titulo: 'Filas totales', valor: '24.500' },
  { id: 'columnas', titulo: 'Columnas detectadas', valor: '12' },
  { id: 'tiempo', titulo: 'Tiempo de carga (ms)', valor: '320' },
]
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
</style>
