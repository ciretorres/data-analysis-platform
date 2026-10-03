# Endpoints CRUD de la entidad Dataset (RF-03, RF-04, RF-05).
# La lista vive en memoria: se vacía al reiniciar el servidor (RNF-04).

from datetime import date
from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

from app.models.dataset import Dataset, DatasetCreate, DatasetUpdate

# Lista en memoria: aquí se guardan los datasets creados (RF-03).
datasets: list[Dataset] = []

router = APIRouter(
    prefix="/api/datasets",
    tags=["datasets"],
)


@router.get("/")
def listar_datasets() -> list[Dataset]:
    """Obtener todos los conjuntos de datos.

    Devuelve la lista completa de datasets. Si no hay ninguno, devuelve una
    lista vacía.
    """
    return datasets


@router.get("/{id}")
def obtener_dataset(id: Annotated[int, Path(ge=1, description="ID del dataset")]) -> Dataset:
    """Obtener un conjunto de datos por su id.

    Devuelve el dataset con el id indicado. Si no existe, devuelve 404.
    """
    for dataset in datasets:
        if dataset.id == id:
            return dataset
    raise HTTPException(status_code=404, detail="Dataset no encontrado")


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_dataset(datos: DatasetCreate) -> Dataset:
    """Crear un conjunto de datos.

    El servidor genera el `id` (el mayor actual + 1, sin reutilizar ids
    eliminados) y el `created_at` (fecha de hoy).
    """
    nuevo_id = max((d.id for d in datasets), default=0) + 1
    dataset = Dataset(
        id=nuevo_id,
        name=datos.name,
        description=datos.description,
        file_name=datos.file_name,
        created_at=date.today(),
    )
    datasets.append(dataset)
    return dataset


@router.put("/{id}")
def actualizar_dataset(
    id: Annotated[int, Path(ge=1, description="ID del dataset")],
    datos: DatasetUpdate,
) -> Dataset:
    """Actualizar un conjunto de datos (reemplazo completo).

    Hay que enviar todos los campos. Si se omite `description`, queda a nulo.
    Si el id no existe, devuelve 404.
    """
    for indice, dataset in enumerate(datasets):
        if dataset.id == id:
            actualizado = Dataset(
                id=id,
                name=datos.name,
                description=datos.description,
                file_name=datos.file_name,
                created_at=datos.created_at,
            )
            datasets[indice] = actualizado
            return actualizado
    raise HTTPException(status_code=404, detail="Dataset no encontrado")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_dataset(id: Annotated[int, Path(ge=1, description="ID del dataset")]) -> None:
    """Eliminar un conjunto de datos.

    Si el id no existe, devuelve 404.
    """
    for indice, dataset in enumerate(datasets):
        if dataset.id == id:
            datasets.pop(indice)
            return
    raise HTTPException(status_code=404, detail="Dataset no encontrado")
