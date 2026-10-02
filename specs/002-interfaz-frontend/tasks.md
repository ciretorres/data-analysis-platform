# Tareas — Spec 002 (Nivel 1)

**Plan**: `plan.md` · **Formato**: skill spec-driven-development · **Total**: 10 tareas (sin tests automatizados: verificación manual)

- [ ] **1. Base del nivel 1** — `assets/css/main.css`, `nuxt.config.ts`, `app/app.vue`
  - RF: RF-07, RNF-02, RNF-03
  - Hecho cuando: `npm run dev` carga http://localhost:3000 sin errores de consola, `app/app.vue` renderiza `<NuxtLayout>` + `<NuxtPage>` (sustituye la bienvenida de nivel 0), el CSS global se aplica y la pestaña Red no tiene ninguna petición a :8000.

- [ ] **2. Sección de bienvenida** — `pages/index.vue`
  - RF: RF-01, RNF-02
  - Hecho cuando: la página muestra sin interacción el nombre de la aplicación, un título (elemento visual distinto del nombre), la descripción y un párrafo de bienvenida para quien empieza a programar.

- [ ] **3. Menú de navegación sticky** — `components/AppHeader.vue`, `layouts/default.vue`
  - RF: RF-02, RF-06, RF-08
  - Hecho cuando: hay 4 enlaces en orden (Bienvenida, Métricas, Carga de archivo, Gráficos) apuntando a sus `#anclas`, el menú permanece visible arriba al hacer scroll y el contenido no supera 1200px.

- [ ] **4. Tarjeta de métrica reutilizable** — `components/MetricCard.vue`
  - RF: RF-03, RF-08, RNF-04
  - Hecho cuando: con props de título y valor, la tarjeta muestra el valor numérico y la etiqueta visible "datos de ejemplo"; no hay ningún dato real.

- [ ] **5. Lógica de validación pura** — `utils/validacion.js`
  - RF: RF-04, CL-08, CL-10, CL-11
  - Hecho cuando: `validarExtension`, `formatearTamano` y `truncarNombre` existen y, probadas desde la consola del navegador, devuelven `true` para `datos.CSV`, `false` para `datos.csv.txt` y truncan un nombre de 120 caracteres con puntos suspensivos.

- [ ] **6. Botón de carga con validación** — `components/FileUploader.vue`
  - RF: RF-04, CL-01, CL-02, CL-03, CL-07, CL-09, CL-14, CL-15
  - Hecho cuando: un .csv muestra nombre y tamaño en KB/MB; un .txt o un .csv de 0 bytes muestra error en español y no aparece como cargado; abrir el selector y cancelar no cambia nada; y en la pestaña Red el archivo no sale del navegador.

- [ ] **7. Área de gráficos (placeholder)** — `components/ChartPlaceholder.vue`
  - RF: RF-05
  - Hecho cuando: el área mide ≥300px de alto y muestra "Los gráficos aparecerán aquí en un nivel futuro", sin gráficos reales.

- [ ] **8. Ensamblaje responsive de la página** — `pages/index.vue`
  - RF: RF-01, RF-02, RF-03, RF-06, RF-07, RF-08, CL-04
  - Hecho cuando: están las 4 secciones, cada elemento del menú desplaza a su sección, el grid pasa de 1 a 2 a 4 columnas (móvil/tablet/escritorio) y a 375px, 800px y 1280px no hay scroll horizontal.

- [ ] **9. Documentación de conceptos** — `docs/conceptos-nivel-1.md`
  - RF: RF-09, RNF-01
  - Hecho cuando: los 11 conceptos (componentes, props, eventos, estado reactivo, estado local, directivas, renderizado condicional y de listados, rutas, layouts, responsive) tienen explicación breve en español y la diferencia página/componente aparece con un ejemplo del propio proyecto (`pages/index.vue` vs `components/MetricCard.vue`).

- [ ] **10. Revisión final de criterios de finalización** — verificación manual en el navegador
  - RF: RF-01 … RF-09 (los 9), CL-05, CL-06, CL-12, CL-13
  - Hecho cuando: los 9 criterios de finalización de la spec se cumplen a mano, incluidos backend detenido (idéntico comportamiento), recarga pierde el archivo y zoom al 200% usable.
