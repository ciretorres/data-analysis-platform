<template>
  <div class="page">
    <div class="content">
      <div class="logo">
        <span class="logo-icon">DA</span>
        <span class="logo-text">Data Analysis Platform</span>
        <span class="badge">Nivel 0</span>
      </div>

      <div class="grid">
        <div class="card">
          <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="w-6 h-6">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
            </svg>
          </div>
          <h2>Frontend</h2>
          <p>La parte de la aplicación que se ve en el navegador. Construido con Vue y Nuxt.</p>
          <a href="http://localhost:3000" target="_blank" class="link">http://localhost:3000</a>
        </div>

        <div class="card">
          <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="w-6 h-6">
              <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
              <line x1="8" y1="21" x2="16" y2="21"/>
              <line x1="12" y1="17" x2="12" y2="21"/>
            </svg>
          </div>
          <h2>Backend</h2>
          <p>El servidor que recibe peticiones y responde. Construido con FastAPI y Uvicorn.</p>
          <a href="http://localhost:8000" target="_blank" class="link">http://localhost:8000</a>
        </div>

        <div class="card">
          <div class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="w-6 h-6">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14 2 14 8 20 8"/>
              <line x1="16" y1="13" x2="8" y2="13"/>
              <line x1="16" y1="17" x2="8" y2="17"/>
              <polyline points="10 9 9 9 8 9"/>
            </svg>
          </div>
          <h2>Documentación API</h2>
          <p>Documentación interactiva generada automáticamente por FastAPI.</p>
          <a href="http://localhost:8000/docs" target="_blank" class="link">http://localhost:8000/docs</a>
        </div>
      </div>

      <footer class="footer">
        <p>Proyecto educativo · Nivel 0 — Preparación del entorno</p>
      </footer>
    </div>
  </div>
</template>

<style scoped>
.page {
  min-height: 100vh;
  background-color: #020420;
  color: #fff;
  font-family: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.content {
  max-width: 980px;
  width: 100%;
  text-align: center;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 3rem;
}

.logo-icon {
  width: 48px;
  height: 48px;
  background-color: #00DC82;
  color: #020420;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.25rem;
}

.logo-text {
  font-size: 2rem;
  font-weight: 700;
  color: #fff;
}

.badge {
  background-color: rgba(0, 220, 130, 0.1);
  color: #00DC82;
  border: 1px solid rgba(0, 220, 130, 0.3);
  border-radius: 999px;
  padding: 0.25rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.grid {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  gap: 1rem;
  margin-bottom: 3rem;
}

@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.card {
  background-color: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 0.75rem;
  padding: 1.5rem;
  text-align: left;
  transition: border-color 0.2s;
}

.card:hover {
  border-color: rgba(0, 220, 130, 0.5);
}

.icon {
  width: 40px;
  height: 40px;
  background-color: rgba(0, 220, 130, 0.1);
  border: 1px solid rgba(0, 220, 130, 0.2);
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #00DC82;
  margin-bottom: 1rem;
}

.card h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #fff;
  margin: 0 0 0.5rem;
}

.card p {
  color: #94a3b8;
  font-size: 0.875rem;
  line-height: 1.5;
  margin: 0 0 1rem;
}

.link {
  color: #00DC82;
  font-size: 0.875rem;
  font-family: ui-monospace, monospace;
  text-decoration: none;
}

.link:hover {
  text-decoration: underline;
}

.footer {
  color: #64748b;
  font-size: 0.875rem;
}
</style>
