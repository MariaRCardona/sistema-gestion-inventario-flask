from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave_secreta_predeterminada")


# Configuración de la base de datos
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "inventario_db"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "")
        )
        if connection.is_connected():
            return connection
    except Error as e:
        flash(f"Error al conectar a MySQL: {e}", "danger")
        return None


# Clase Producto
class Producto:
    def __init__(self, id=None, nombre="", cantidad=0, precio=0.0, categoria=""):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria


# Clase GestionInventario
class GestionInventario:
    @staticmethod
    def agregar_producto(producto):
        try:
            connection = get_db_connection()
            if connection is None:
                return False, "Error de conexión a la base de datos"

            cursor = connection.cursor()

            # Verificar si ya existe un producto con el mismo nombre
            cursor.execute("SELECT id FROM productos WHERE nombre = %s", (producto.nombre,))
            if cursor.fetchone():
                return False, f"Ya existe un producto con el nombre '{producto.nombre}'"

            # Insertar el producto
            query = """INSERT INTO productos (nombre, cantidad, precio, categoria) 
                       VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (producto.nombre, producto.cantidad, producto.precio, producto.categoria))
            connection.commit()

            return True, "Producto agregado con éxito"
        except Error as e:
            return False, f"Error al agregar producto: {e}"
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def obtener_productos():
        try:
            connection = get_db_connection()
            if connection is None:
                return [], "Error de conexión a la base de datos"

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos ORDER BY nombre")
            productos_data = cursor.fetchall()

            productos = []
            for p in productos_data:
                producto = Producto(
                    id=p['id'],
                    nombre=p['nombre'],
                    cantidad=p['cantidad'],
                    precio=p['precio'],
                    categoria=p['categoria']
                )
                productos.append(producto)

            return productos, None
        except Error as e:
            return [], f"Error al obtener productos: {e}"
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def buscar_producto(nombre):
        try:
            connection = get_db_connection()
            if connection is None:
                return None, "Error de conexión a la base de datos"

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE %s", (f"%{nombre}%",))
            productos_data = cursor.fetchall()

            if not productos_data:
                return [], "No se encontraron productos con ese nombre"

            productos = []
            for p in productos_data:
                producto = Producto(
                    id=p['id'],
                    nombre=p['nombre'],
                    cantidad=p['cantidad'],
                    precio=p['precio'],
                    categoria=p['categoria']
                )
                productos.append(producto)

            return productos, None
        except Error as e:
            return None, f"Error al buscar producto: {e}"
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def obtener_producto_por_id(id):
        try:
            connection = get_db_connection()
            if connection is None:
                return None, "Error de conexión a la base de datos"

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
            p = cursor.fetchone()

            if not p:
                return None, "Producto no encontrado"

            producto = Producto(
                id=p['id'],
                nombre=p['nombre'],
                cantidad=p['cantidad'],
                precio=p['precio'],
                categoria=p['categoria']
            )

            return producto, None
        except Error as e:
            return None, f"Error al obtener producto: {e}"
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def actualizar_producto(producto):
        try:
            connection = get_db_connection()
            if connection is None:
                return False, "Error de conexión a la base de datos"

            cursor = connection.cursor()

            # Verificar si existe el producto
            cursor.execute("SELECT id FROM productos WHERE id = %s", (producto.id,))
            if not cursor.fetchone():
                return False, "El producto no existe"

            # Verificar que no haya otro producto con el mismo nombre
            cursor.execute("SELECT id FROM productos WHERE nombre = %s AND id != %s",
                           (producto.nombre, producto.id))
            if cursor.fetchone():
                return False, f"Ya existe otro producto con el nombre '{producto.nombre}'"

            # Actualizar el producto
            query = """UPDATE productos 
                       SET nombre = %s, cantidad = %s, precio = %s, categoria = %s 
                       WHERE id = %s"""
            cursor.execute(query, (producto.nombre, producto.cantidad, producto.precio,
                                   producto.categoria, producto.id))
            connection.commit()

            return True, "Producto actualizado con éxito"
        except Error as e:
            return False, f"Error al actualizar producto: {e}"
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def eliminar_producto(id):
        try:
            connection = get_db_connection()
            if connection is None:
                return False, "Error de conexión a la base de datos"

            cursor = connection.cursor()

            # Verificar si existe el producto
            cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))
            if not cursor.fetchone():
                return False, "El producto no existe"

            # Eliminar el producto
            cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
            connection.commit()

            return True, "Producto eliminado con éxito"
        except Error as e:
            return False, f"Error al eliminar producto: {e}"
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()


# Rutas para la aplicación web
@app.route('/')
def index():
    productos, error = GestionInventario.obtener_productos()
    if error:
        flash(error, "danger")
    return render_template('index.html', productos=productos)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        try:
            nombre = request.form.get('nombre')
            cantidad = int(request.form.get('cantidad'))
            precio = float(request.form.get('precio'))
            categoria = request.form.get('categoria')

            if not nombre:
                flash("El nombre del producto es obligatorio", "warning")
                return redirect(url_for('agregar'))

            producto = Producto(nombre=nombre, cantidad=cantidad, precio=precio, categoria=categoria)
            success, message = GestionInventario.agregar_producto(producto)

            if success:
                flash(message, "success")
                return redirect(url_for('index'))
            else:
                flash(message, "danger")
                return redirect(url_for('agregar'))
        except ValueError:
            flash("Por favor ingrese valores numéricos válidos para cantidad y precio", "warning")
            return redirect(url_for('agregar'))

    return render_template('agregar.html')


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        productos, error = GestionInventario.buscar_producto(nombre)

        if error:
            flash(error, "warning")

        return render_template('resultados_busqueda.html', productos=productos, termino=nombre)

    return render_template('buscar.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        try:
            nombre = request.form.get('nombre')
            cantidad = int(request.form.get('cantidad'))
            precio = float(request.form.get('precio'))
            categoria = request.form.get('categoria')

            if not nombre:
                flash("El nombre del producto es obligatorio", "warning")
                return redirect(url_for('editar', id=id))

            producto = Producto(id=id, nombre=nombre, cantidad=cantidad, precio=precio, categoria=categoria)
            success, message = GestionInventario.actualizar_producto(producto)

            if success:
                flash(message, "success")
                return redirect(url_for('index'))
            else:
                flash(message, "danger")
                return redirect(url_for('editar', id=id))
        except ValueError:
            flash("Por favor ingrese valores numéricos válidos para cantidad y precio", "warning")
            return redirect(url_for('editar', id=id))

    producto, error = GestionInventario.obtener_producto_por_id(id)
    if error:
        flash(error, "danger")
        return redirect(url_for('index'))

    return render_template('editar.html', producto=producto)


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    success, message = GestionInventario.eliminar_producto(id)

    if success:
        flash(message, "success")
    else:
        flash(message, "danger")

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
