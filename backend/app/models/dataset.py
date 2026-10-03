# Modelos de datos de la entidad Dataset (RF-02, RF-05).
# Viven separados de las rutas para que la definición de datos no se
# mezcle con la lógica de los endpoints (RF-08).

from datetime import date
from typing import Annotated

from pydantic import BaseModel, Field, field_validator

# Tipos reutilizables con sus reglas de validación y documentación.
Nombre = Annotated[str, Field(min_length=1, max_length=100, description="Nombre del dataset")]
Descripcion = Annotated[str | None, Field(default=None, max_length=500, description="Descripción del dataset (opcional)")]
NombreArchivo = Annotated[str, Field(min_length=1, max_length=255, description="Nombre del fichero del dataset")]


class DatasetCreate(BaseModel):
    """Datos que envía el cliente para crear un dataset (POST).

    `id` y `created_at` no se piden aquí: los genera el servidor.
    """

    name: Nombre
    description: Descripcion
    file_name: NombreArchivo

    @field_validator("name", "file_name")
    @classmethod
    def no_solo_espacios(cls, valor: str) -> str:
        """Rechaza cadenas vacías o compuestas solo por espacios."""
        if not valor.strip():
            raise ValueError("no puede estar vacío o solo con espacios")
        return valor


class DatasetUpdate(BaseModel):
    """Datos que envía el cliente para actualizar un dataset (PUT).

    Reemplazo completo: hay que enviar todos los campos, incluido
    `created_at` (a diferencia de POST, donde lo genera el servidor).
    """

    name: Nombre
    description: Descripcion
    file_name: NombreArchivo
    created_at: date = Field(description="Fecha de creación en formato AAAA-MM-DD")

    @field_validator("name", "file_name")
    @classmethod
    def no_solo_espacios(cls, valor: str) -> str:
        """Rechaza cadenas vacías o compuestas solo por espacios."""
        if not valor.strip():
            raise ValueError("no puede estar vacío o solo con espacios")
        return valor


class Dataset(BaseModel):
    """Dataset completo que devuelve la API."""

    id: int = Field(description="ID único del dataset (generado por el servidor)")
    name: str = Field(description="Nombre del dataset")
    description: str | None = Field(default=None, description="Descripción del dataset")
    file_name: str = Field(description="Nombre del fichero del dataset")
    created_at: date = Field(description="Fecha de creación en formato AAAA-MM-DD")
