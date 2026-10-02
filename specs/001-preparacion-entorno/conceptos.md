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

### FastAPI
Framework de Python para construir APIs de forma rápida y sencilla. Genera
documentación automática de los endpoints.

### Uvicorn
Servidor web que ejecuta la aplicación FastAPI. Es el que hace que el backend
pueda recibir peticiones.

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
