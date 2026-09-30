from fastapi import FastAPI

app = FastAPI(
    title="Data Analysis Platform API",
    description="API para la plataforma de análisis de datos",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "¡Bienvenido a Data Analysis Platform!"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
