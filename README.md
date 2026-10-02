# Data Analysis Platform

Plataforma web para cargar, procesar y visualizar archivos de datos CSV.

## Estructura del proyecto

```
data-analysis-platform/
├── frontend/          # Aplicación Nuxt (cliente)
├── backend/           # API FastAPI (servidor)
├── docker-compose.yml # Configuración Docker (futura)
├── .env.example       # Variables de entorno de ejemplo
└── README.md          # Este archivo
```

## Requisitos

- Python 3.11+
- Node.js 20+

## Configuración inicial

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/data-analysis-platform.git
cd data-analysis-platform
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

### 3. Backend

En Ubuntu/Debian instala primero el paquete `python3.12-venv` (si no, `python3 -m venv` falla por falta de `ensurepip`):

```bash
sudo apt install python3.12-venv
```

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

### 5. Atajos desde la raíz

```bash
bun run install:all   # instala frontend y crea backend/venv con sus dependencias
bun run dev:backend   # levanta FastAPI en http://localhost:8000
bun run dev:frontend  # levanta Nuxt en http://localhost:3000
```

## Acceso

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Documentación API: http://localhost:8000/docs
