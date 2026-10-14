# Conceptos del Nivel 5 — Procesar archivos CSV o JSON con Pandas

Este nivel introduce el procesamiento real de datos: subir un archivo, validarlo, leerlo con Pandas y calcular estadísticas. Aquí se explican los conceptos fundamentales.

---

## Subida de archivos con `UploadFile`

En FastAPI, para recibir archivos subidos desde el frontend se usa `UploadFile`. Es una clase que representa un archivo enviado por el cliente.

```python
from fastapi import UploadFile, File

@router.post("/upload")
async def subir(archivo: UploadFile = File(...)):
    contenido = await archivo.read()
```

`UploadFile` proporciona:
- `filename`: nombre original del archivo.
- `content_type`: tipo MIME (ej. `text/csv`).
- `file`: objeto file-like para leer el contenido.

---

## `FormData` y `fetch` en el frontend

Para enviar archivos desde el navegador se usa `FormData`, que permite enviar datos binarios (archivos) a través de HTTP.

```typescript
const formData = new FormData()
formData.append('archivo', archivo)

await fetch(url, {
  method: 'POST',
  body: formData,
})
```

`FormData` es el equivalente web de un formulario con `enctype="multipart/form-data"`. No se necesita `Content-Type` manual: el navegador lo añade automáticamente.

---

## Lectura de archivos con Pandas

Pandas es la librería principal para análisis de datos en Python. Permite leer archivos CSV y JSON y convertirlos en DataFrames.

```python
import pandas as pd
import io

# Leer CSV desde bytes en memoria
df = pd.read_csv(io.BytesIO(contenido))

# Leer JSON desde bytes en memoria
df = pd.read_json(io.BytesIO(contenido))
```

`io.BytesIO` permite tratar un `bytes` como un archivo, sin necesidad de guardarlo en disco.

---

## DataFrames

Un **DataFrame** es la estructura principal de Pandas: una tabla bidimensional con filas y columnas, similar a una hoja de cálculo.

```python
df.shape      # (filas, columnas)
df.columns    # nombres de las columnas
df.head(5)     # primeras 5 filas
df.isnull()   # máscara de valores nulos
```

---

## Estadística descriptiva con `df.describe()`

`df.describe()` calcula estadísticas descriptivas para columnas numéricas:

- `count`: número de valores no nulos.
- `mean`: media aritmética.
- `std`: desviación estándar.
- `min` / `max`: valores mínimo y máximo.
- `25%`, `50%`, `75%`: percentiles (cuartiles).

```python
desc = df['columna'].describe()
print(desc['mean'])  # media
print(desc['std'])   # desviación estándar
```

Solo se aplica a columnas numéricas. Las columnas de texto o fecha no incluyen estadísticas.

---

## Validación de archivos por extensión y tamaño

El backend debe validar los archivos antes de procesarlos:

1. **Extensión**: comprobar que el archivo tenga una extensión permitida (`.csv`, `.json`).
2. **Tamaño**: comprobar que no supere un límite (10 MB en este nivel).
3. **Contenido**: comprobar que no esté vacío y que se pueda leer correctamente.

```python
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {'.csv', '.json'}
```

---

## Serialización de datos con `to_dict(orient='records')`

Para enviar datos de Pandas al frontend como JSON, se usa `to_dict(orient='records')`:

```python
preview = df.head(5).to_dict(orient='records')
# Resultado: [{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}]
```

`orient='records'` convierte cada fila en un diccionario con claves = nombres de columnas. Es el formato más natural para APIs JSON.

---

## Tratamiento de errores con `HTTPException`

FastAPI usa `HTTPException` para devolver respuestas de error con código de estado y mensaje:

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=400,
    detail="Formato no válido. Solo se permiten archivos .csv y .json."
)
```

- `400`: error del cliente (archivo inválido).
- `500`: error del servidor (problema inesperado).

El mensaje `detail` se devuelve al frontend como `{"detail": "mensaje"}`.

---

## Resumen del flujo

1. **Frontend**: selecciona archivo → envía con `FormData` y `fetch`.
2. **Backend**: recibe con `UploadFile` → valida extensión y tamaño → lee con Pandas.
3. **Pandas**: calcula estadísticas (`describe()`), cuenta nulos (`isnull().sum()`), genera preview (`head(5)`).
4. **Backend**: devuelve JSON con el resumen.
5. **Frontend**: muestra el resumen en el componente `DataSummary`.
