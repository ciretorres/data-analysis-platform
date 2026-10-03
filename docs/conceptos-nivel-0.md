# Conceptos del Nivel 0

Explicaciones en español para una principiante total. Los nombres propios de
tecnologías se conservan en su forma original.

---

## Arquitectura

### Frontend
La parte de la aplicación que se ve en el navegador. Es lo que la usuaria
toca y mira: botones, textos, imágenes. En este proyecto está construido con
Vue y Nuxt.

### Backend
La parte de la aplicación que no se ve. Es el servidor que recibe peticiones,
procesa datos y responde. En este proyecto está construido con FastAPI y
Uvicorn.

### API
Interfaz de Programación de Aplicaciones. Es el "puente" que permite que el
frontend y el backend hablen entre sí. Define qué peticiones se pueden hacer
y qué respuestas esperar.

### Servidor
Un programa (o computadora) que espera peticiones y responde a ellas. El
backend de este proyecto es un servidor que corre en `localhost:8000`.

### Cliente
El programa que hace peticiones al servidor. El navegador de la usuaria es el
cliente cuando abre el frontend.

### Cliente-servidor
El modelo de comunicación donde el cliente pide y el servidor responde. Es la
base de cómo funciona la web: el navegador (cliente) pide una página y el
servidor se la envía.

---

## Herramientas de código

### Git
Herramienta que guarda la historia de los cambios en tu código. Permite
volver atrás, trabajar en equipo y no perder nada. Es como un "guardado
automático" pero mucho más potente.

### GitHub
Plataforma en internet donde se guardan repositorios de Git. Permite
compartir código, colaborar con otros y tener una copia de seguridad en la
nube.

### Repositorio
Una carpeta donde Git guarda la historia de tu proyecto. Puede estar en tu
computadora (local) y en GitHub (remoto).

### Node.js
Entorno que permite ejecutar JavaScript fuera del navegador. Se usa para
construir el frontend con Nuxt y para ejecutar herramientas de desarrollo.

### Python
Lenguaje de programación usado para el backend. Es conocido por ser fácil de
leer y escribir, ideal para principiantes.

### Vue
Framework de JavaScript para construir interfaces de usuario. Permite crear
páginas web interactivas con componentes reutilizables.

### Nuxt
Framework construido sobre Vue que facilita crear aplicaciones web completas.
Añade herramientas para rutas, renderizado y más.

FastAPI y Uvicorn son herramientas de Python que suelen usarse juntas para crear y ejecutar APIs web.

### FastAPI
FastAPI es un framework de Python: te permite definir rutas, recibir parámetros, validar datos y devolver respuestas JSON. FastAPI sirve para construir APIs de forma rápida y sencilla. Usa anotaciones de tipos de Python y genera documentación interactiva automáticamente de los endpoints, normalmente en /docs. Está construido sobre Starlette y Pydantic. *(Referencia: tiangolo.com)*

Ejemplo:

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola, mundo"}
```

Instalación:

```bash
pip install "fastapi[standard]"
```

### Uvicorn
Uvicorn es un servidor web ASGI: recibe las peticiones HTTP desde el navegador o desde otra aplicación y se las entrega a tu aplicación FastAPI. Uvicorn ejecuta la aplicación FastAPI. Es el que hace que el backend pueda recibir peticiones. También devuelve la respuesta al cliente. Soporta HTTP/1.1, HTTP/2 y WebSockets. *(Referencia: uvicorn.dev)*

Ejecución con uvicorn:

```bash
uvicorn main:app --reload
```

`main:app` significa:

- `main`: el archivo `main.py`
- `app`: el objeto creado con `FastAPI()`
- `--reload`: reinicia el servidor automáticamente cuando modificas el código; es útil durante el desarrollo, pero no se recomienda en producción. *(Referencia: tiangolo.com)*

Después puedes abrir:

- `http://127.0.0.1:8000/` para probar la API
- `http://127.0.0.1:8000/docs` para ver la documentación interactiva

En resumen: **FastAPI define la API; Uvicorn la ejecuta y la expone por HTTP**.

### Editor de código
Programa donde escribes tu código. Visual Studio Code es una opción popular,
pero cualquier editor de texto funciona.

---

## Conceptos de desarrollo

### Entorno virtual
Una carpeta aislada donde se instalan las dependencias de un proyecto sin
afectar al resto de la computadora. En Python se crea con `python -m venv venv`.

### Dependencias
Paquetes de código que tu proyecto necesita para funcionar. En Python se
instalan con `pip` y se declaran en `requirements.txt`. En JavaScript se
instalan con `npm` y se declaran en `package.json`.

### Desarrollo local vs producción
Desarrollar localmente significa ejecutar la aplicación en tu computadora
para probarla. Producción es cuando la aplicación está disponible para las
usuarias finales en internet. Este proyecto solo trabaja en desarrollo local.

---

## Conceptos de niveles futuros

### Base de datos
Sistema para guardar datos de forma organizada y permanente. En niveles
futuros se usará SQLite o PostgreSQL. En el nivel 0 solo se explica el
concepto: **su uso es futuro**.
