// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  devServer: {
    port: 3000,
  },
  // CSS global compartido por todos los componentes (RF-08)
  css: ['~/assets/css/main.css'],
})
