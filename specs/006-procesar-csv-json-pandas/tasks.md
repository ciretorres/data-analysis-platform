# Tareas — Spec 006 (Nivel 5)

**Plan**: `plan.md` · **Formato**: skill spec-driven-development · **Total**: 10 tareas (sin tests automatizados: verificación manual)

- [x] **1. Instalar Pandas en el backend** — `backend/requirements.txt`
  - RF: RF-01
  - Dependencias: ninguna
  - Hecho cuando: `backend/requirements.txt` incluye `pandas`; se ejecuta `pip install pandas` en el entorno virtual sin errores; `python -c "import pandas"` funciona.

- [x] **2. Crear endpoint `POST /api/datasets/upload`** — `backend/app/routers/upload.py`
  - RF: RF-02, RF-03, RF-04, RF-05, RF-06
  - CL: CL-01, CL-02, CL-03, CL-04, CL-05, CL-06, CL-07, CL-18, CL-19
  - Dependencias: T1
  - Hecho cuando: el endpoint acepta archivos CSV y JSON válidos y devuelve JSON con `file_name`, `rows`, `columns`, `column_names`, `missing_values`, `statistics` y `preview`; rechaza extensiones no permitidas con 400 y mensaje en español; rechaza archivos > 10 MB con 400; rechaza archivos malformados con 400; rechaza archivos vacíos con 400; devuelve estadísticas solo para columnas numéricas; incluye máximo 5 filas en preview.

- [x] **3. Registrar router de upload en `main.py`** — `backend/app/main.py`
  - RF: RF-02
  - Dependencias: T2
  - Hecho cuando: el router de upload está importado e incluido con prefijo `/api` y tag `upload`; el endpoint `POST /api/datasets/upload` responde correctamente.

- [x] **4. Crear composable `useUpload`** — `frontend/app/composables/useUpload.ts`
  - RF: RF-07
  - CL: CL-08, CL-15, CL-16, CL-17
  - Dependencias: T3
  - Hecho cuando: el composable devuelve `loading` (ref booleano), `error` (ref string o null), `summary` (ref DataSummary o null) y `subirArchivo(archivo: File)`; usa `fetch` directamente con `FormData`; hace `POST /api/datasets/upload`; muestra "No se pudo conectar con el servidor. Inténtalo de nuevo." si falla la conexión.

- [x] **5. Crear componente `FileUpload`** — `frontend/app/components/FileUpload.vue`
  - RF: RF-08
  - CL: CL-14, CL-15, CL-16
  - Dependencias: T4
  - Hecho cuando: muestra input file que acepta `.csv` y `.json`; muestra el nombre del archivo seleccionado; tiene botón "Subir" que llama a `subirArchivo`; el botón está deshabilitado mientras se sube o no hay archivo seleccionado; muestra estado de carga con `LoadingState`; muestra error con `ErrorMessage` y botón de reintento.

- [x] **6. Crear componente `DataSummary`** — `frontend/app/components/DataSummary.vue`
  - RF: RF-09
  - CL: CL-09, CL-10, CL-11, CL-12, CL-13
  - Dependencias: T4
  - Hecho cuando: recibe prop `summary` (objeto con el respuesta del servidor); muestra nombre del archivo; muestra número de filas y columnas; muestra lista de nombres de columnas; muestra conteo de valores nulos por columna; muestra estadísticas descriptivas para columnas numéricas (count, mean, std, min, 25%, 50%, 75%, max); muestra tabla con vista previa de primeras 5 filas.

- [x] **7. Integrar sección "Procesar archivo" en página de inicio** — `frontend/app/pages/index.vue`
  - RF: RF-10
  - CL: CL-01, CL-02, CL-03, CL-04, CL-05, CL-06, CL-08, CL-09
  - Dependencias: T5, T6
  - Hecho cuando: la página incluye el componente `FileUpload` en una sección visible; al subir un archivo válido se muestra el resumen en la misma sección; se muestran errores cuando el backend rechaza el archivo o está detenido.

- [x] **8. Añadir enlace en el menú de navegación** — `frontend/app/components/AppHeader.vue`
  - RF: RF-10
  - Dependencias: T7
  - Hecho cuando: el menú incluye el enlace "Procesar archivo" que desplaza a la sección correspondiente.

- [x] **9. Documentar conceptos del nivel 5** — `docs/conceptos-nivel-5.md`
  - RF: RF-11, RNF-01
  - Dependencias: ninguna
  - Hecho cuando: los conceptos del nivel (subida de archivos con `UploadFile`, `FormData` y `fetch`, lectura de archivos con Pandas, DataFrames, estadística descriptiva con `df.describe()`, validación de archivos por extensión y tamaño, serialización de datos con `to_dict(orient='records')`, tratamiento de errores con `HTTPException`) tienen explicación breve en español.

- [x] **10. Verificación manual de criterios** — navegador + `curl`
  - RF: RF-01 … RF-11 (los 11), RNF-02, RNF-03
  - Dependencias: T1-T9
  - Hecho cuando: los 17 criterios de finalización de la spec se cumplen a mano, incluido: Pandas instalado y en requirements.txt; endpoint devuelve resumen correcto para CSV y JSON válidos; endpoint rechaza extensión no permitida, archivos > 10 MB y archivos malformados con 400; frontend permite subir archivos y mostrar resumen; se muestran mensajes de error cuando el backend está detenido; conceptos documentados en español.

**Estado**: 10/10 completadas.
