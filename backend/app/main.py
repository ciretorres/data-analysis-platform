# Aplicación principal de la API (RF-01, RF-02).
# Crea la app FastAPI, define los endpoints base, configura CORS y monta el
# router de datasets.

from datetime import date

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.datasets import router as datasets_router

app = FastAPI(
    title="Data Analysis Platform API",
    description="API para la plataforma de análisis de datos",
    version="1.0.0",
)

# CORS: permite que el frontend (http://localhost:3000) haga peticiones a la
# API desde el navegador (RF-02).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
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


@app.get("/api/health", summary="Estado de la API")
def api_health():
    """Estado de la API con información adicional.

    Devuelve el nombre de la aplicación, el estado, la versión y la fecha de
    respuesta. Lo consume el frontend para mostrar el estado de la conexión.
    """
    return {
        "app_name": "Data Analysis Platform",
        "status": "ok",
        "version": "1.0.0",
        "response_date": date.today().isoformat(),
    }


# Monta los endpoints Create, Read, Update and Delete o CRUD de datasets bajo /api/datasets.
app.include_router(datasets_router)
