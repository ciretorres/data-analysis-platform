<template>
  <!-- Layout por defecto: menú sticky arriba + contenido centrado (máx. 1200px) -->
  <div class="layout">
    <AppHeader />
    <main class="layout__contenido contenedor">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.layout {
  min-height: 100vh;
}

.layout__contenido {
  padding-top: 1rem;
  padding-bottom: 3rem;
}
</style>
