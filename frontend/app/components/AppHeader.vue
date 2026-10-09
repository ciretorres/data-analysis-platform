<template>
  <!-- RF-02: menú horizontal sticky con 4 elementos en orden fijo -->
  <header class="cabecera">
    <nav class="cabecera__contenido contenedor" aria-label="Secciones de la página">
      <a class="cabecera__marca" href="#bienvenida">Data Analysis Platform</a>
      <ul class="cabecera__menu">
        <li><a href="#bienvenida">Bienvenida</a></li>
        <li><a href="#metricas">Métricas</a></li>
        <li><a href="#carga-archivo">Carga de archivo</a></li>
        <li><a href="#graficos">Gráficos</a></li>
        <li><a href="#estado-api">Estado de la API</a></li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
.cabecera {
  /* sticky: el menú permanece visible al hacer scroll (RF-02) */
  position: sticky;
  top: 0;
  z-index: 10;
  background-color: rgba(2, 4, 32, 0.92);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid var(--color-borde);
}

.cabecera__contenido {
  min-height: var(--cabecera-alta);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
}

.cabecera__marca {
  color: var(--color-acento);
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
}

.cabecera__menu {
  /* en móvil (<768px) los enlaces se apilan en varias líneas (CL-04) */
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem 1.25rem;
  margin: 0;
  padding: 0.5rem 0;
  list-style: none;
}

.cabecera__menu a {
  color: var(--color-texto);
  text-decoration: none;
  font-size: 0.9375rem;
}

.cabecera__menu a:hover {
  color: var(--color-acento);
}
</style>
