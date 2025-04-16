# 📦 Sistema de Gestión de Inventario Web con Flask y MySQL

Proyecto desarrollado como parte del programa Backend Dianjo impulsado por IBM SkillsBuild & BeJob. Esta aplicación web permite gestionar un inventario de productos, aplicando conceptos de desarrollo backend con Python (Flask) y MySQL.

[![Gestión de inventarios](https://github.com/user-attachments/assets/0341122f-b756-47f1-82f8-9220594f3c52)](https://github.com/user-attachments/assets/0341122f-b756-47f1-82f8-9220594f3c52)

## ✨ Características
✅ Interfaz web amigable

🔄 Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)

🔍 Búsqueda de productos por nombre

✔️ Validación de datos

⚠️ Manejo de errores

💬 Mensajes de retroalimentación al usuario

## 🛠️ Tecnologías utilizadas
- Python 3
- Flask
- MySQL 5
- HTML
- Jinja2 (plantillas HTML)
- pip (gestor de paquetes de Python)
- python-dotenv (para la gestión de variables de entorno)
- mysql-connector-python (para la conexión a la base de datos MySQL)

---
## ▶️ Ejecución

La aplicación estará disponible en http://127.0.0.1:5000/

## 🧪 Funcionalidades
- Página principal: Lista de productos registrados.
- Agregar producto: Formulario para añadir nuevos artículos.
- Buscar producto: Búsqueda por nombre.
- Editar producto: Modificar información existente.
- Eliminar producto: Borrar registros del inventario.

## 📂 Estructura del proyecto
```
sistema-gestion-inventario/
│
├── app.py                  # Aplicación principal Flask
├── crear_bd.sql            # Script SQL para la base de datos
├── requirements.txt        # Lista de dependencias
├── .env                    # Variables de entorno (¡No subir a Git!)
├── README.md               # Este archivo
│
└── templates/              # Plantillas HTML (Jinja2)
    ├── base.html
    ├── index.html
    ├── agregar.html
    ├── editar.html
    ├── buscar.html
    └── resultados_busqueda.html


## 📜 Licencia
Este proyecto está bajo la licencia MIT.

## 🧑‍💻 Autor
**María José Rivas Cardona**
Este sistema fue desarrollado como parte de un proyecto personal para la Formación Avanzada en Desarrollo Backend (Python, Flask, Django) (En curso) IBM SkillsBuild / Bejob.


