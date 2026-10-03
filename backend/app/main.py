# Aplicación principal de la API (RF-01).
# Crea la app FastAPI, define los endpoints base y monta el router de datasets.

from fastapi import FastAPI

from app.routers.datasets import router as datasets_router

app = FastAPI(
    title="Data Analysis Platform API",
    description="API para la plataforma de análisis de datos",
    version="1.0.0",
)


@app.get("/", summary="Bienvenida")
def root():
    """Bienvenida de la plataforma (se conserva del nivel 0)."""
    return {"message": "¡Bienvenido a Data Analysis Platform!"}


@app.get("/health", summary="Estado del servidor")
def health_check():
    """Estado del servidor.

    Devuelve un JSON con el estado, un mensaje y la versión de la API.
    """
    return {
        "status": "ok",
        "message": "API funcionando correctamente",
        "version": "1.0.0",
    }


# Monta los endpoints CRUD de datasets bajo /api/datasets.
app.include_router(datasets_router)
