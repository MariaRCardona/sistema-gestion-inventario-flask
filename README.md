📦 Sistema de Gestión de Inventario Web con Flask y MySQL
Proyecto desarrollado como parte del programa Backend Dianjo impulsado por IBM SkillsBuild & BeJob.
Esta aplicación web permite gestionar un inventario de productos, aplicando conceptos de desarrollo backend con Python (Flask) y MySQL.

Características
✅ Interfaz web amigable
🔄 Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
🔍 Búsqueda de productos por nombre
✔️ Validación de datos
⚠️ Manejo de errores
💬 Mensajes de retroalimentación al usuario

🧰 Tecnologías
Python 3.8+
Flask
MySQL 5.7+
HTML (Jinja2 Templates)

📦 Requisitos
Asegúrate de tener instalado:
Python 3.8 o superior
MySQL 5.7 o superior
pip (gestor de paquetes de Python)

▶️ Ejecución de la Aplicación
Asegúrate de tener tu base de datos creada con el script crear_bd.sql

Ejecuta la aplicación:
Abre tu navegador en: http://127.0.0.1:5000

🧪 Funcionalidades
Página principal: Lista de productos registrados
Agregar producto: Formulario para añadir nuevos artículos
Buscar producto: Por nombre
Editar producto: Modificar información existente
Eliminar producto: Borrar registros del inventario

📁 Estructura del Proyecto
sistema-gestion-inventario/
│
├── app.py                  # Aplicación principal Flask
├── crear_bd.sql            # Script SQL para la base de datos
├── .env                    # Variables de entorno (excluir del repo)
├── requirements.txt        # Lista de dependencias
├── README.md               # Este archivo
│
└── templates/              # Plantillas HTML (Jinja2)
    ├── base.html
    ├── index.html
    ├── agregar.html
    ├── editar.html
    ├── buscar.html
    └── resultados_busqueda.html

📜 Licencia
Este proyecto está bajo la licencia MIT.

👨‍💻 Autor
María José Rivas Cardona
Proyecto de Formación Backend Dianjo (IBM SkillsBuild & BeJob)

