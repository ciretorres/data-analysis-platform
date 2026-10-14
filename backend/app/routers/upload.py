# Endpoint de subida de archivos (RF-02, RF-03, RF-04, RF-05, RF-06).
# Recibe archivos CSV o JSON, los valida, los lee con Pandas y devuelve un
# resumen con estadísticas y vista previa.

from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io
import json
import math

router = APIRouter(
    prefix="/api",
    tags=["upload"],
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {'.csv', '.json'}


def _limpiar_nan(valor):
    """Convertir NaN a None para que sea serializable en JSON."""
    if isinstance(valor, float) and math.isnan(valor):
        return None
    return valor


def _json_es_tabular(contenido_bytes: bytes) -> bool:
    """Verificar si un JSON tiene formato tabular.

    Un JSON es tabular si es:
    - Una lista de objetos (ej. [{"a": 1}, {"a": 2}])
    - Una lista vacía (ej. []) — caso especial válido (CL-18)
    - Un objeto con valores que son listas (ej. {"a": [1, 2], "b": [3, 4]})

    No es tabular si es:
    - Un objeto anidado (ej. {"datos": {"a": 1}})
    - Un objeto plano sin listas (ej. {"a": 1, "b": 2})
    """
    try:
        datos = json.loads(contenido_bytes)
    except Exception:
        return False

    #print('datos:', datos)

    # Lista vacía: válido (CL-18)
    if isinstance(datos, list) and len(datos) == 0:
        return True

    # Lista de objetos: tabular
    if isinstance(datos, list) and all(isinstance(item, dict) for item in datos):
        return True

    # Objeto con valores que son listas: tabular
    if isinstance(datos, dict):
        # Si todos los valores son listas, es tabular
        if all(isinstance(v, list) for v in datos.values()):
            return True
        # Si algún valor es un diccionario, no es tabular
        if any(isinstance(v, dict) for v in datos.values()):
            return False

    return False


@router.post("/datasets/upload")
async def subir_archivo(archivo: UploadFile = File(...)):
    """Subir un archivo CSV o JSON y obtener un resumen de sus datos.

    Valida la extensión, el tamaño y el formato del archivo. Si es válido,
    lo lee con Pandas y devuelve estadísticas descriptivas y una vista previa.
    """
    # Validar extensión
    #print('archivo:', archivo)
    nombre = archivo.filename or ""
    extension = "." + nombre.split(".")[-1].lower() if "." in nombre else ""
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Formato no válido. Solo se permiten archivos .csv y .json."
        )

    # Leer contenido
    contenido = await archivo.read()
    #print('contenido:', contenido)

    # Validar tamaño
    if len(contenido) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="El archivo es demasiado grande. El máximo es 10 MB."
        )

    # Validar que no esté vacío
    if len(contenido) == 0:
        raise HTTPException(
            status_code=400,
            detail="El archivo está vacío."
        )

    # Validar JSON tabular antes de leer con Pandas (CL-19)
    if extension == ".json" and not _json_es_tabular(contenido):
        raise HTTPException(
            status_code=400,
            detail="El JSON no tiene un formato tabular válido."
        )

    # Leer con Pandas
    try:
        if extension == ".csv":
            df = pd.read_csv(io.BytesIO(contenido))
        else:
            df = pd.read_json(io.BytesIO(contenido))
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="No se pudo leer el archivo. Verifica que esté bien formado."
        )

    #print('df:', df)

    # Calcular estadísticas SOLO para COLUMNAS "NUMÉRICAS"
    estadisticas = {}
    for columna in df.select_dtypes(include="number").columns:
        # crea un dataframe con las propiedades del describe
        desc = df[columna].describe()
        #print('df[columna].describe():', desc)
        estadisticas[columna] = {
            "count": int(desc["count"]),
            "mean": _limpiar_nan(float(desc["mean"])),
            "std": _limpiar_nan(float(desc["std"])),
            "min": _limpiar_nan(float(desc["min"])),
            "25%": _limpiar_nan(float(desc["25%"])),
            "50%": _limpiar_nan(float(desc["50%"])),
            "75%": _limpiar_nan(float(desc["75%"])),
            "max": _limpiar_nan(float(desc["max"])),
        }
    #print('estadisticas:', estadisticas)

    # Valores nulos por columna
    valores_nulos = {col: int(df[col].isnull().sum()) for col in df.columns}

    # Preview (primeras 5 filas) — limpiar NaN para JSON
    preview_crudo = df.head(5).to_dict(orient="records")
    #print('preview_crudo:', preview_crudo)
    preview = [
        {k: _limpiar_nan(v) for k, v in fila.items()}
        for fila in preview_crudo
    ]
    print('preview:', preview)
    print('df.columns.tolist():', df.columns.tolist())

    return {
        "file_name": nombre,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist(),
        "missing_values": valores_nulos,
        "statistics": estadisticas,
        "preview": preview,
    }
