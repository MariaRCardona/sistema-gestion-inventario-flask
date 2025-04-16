-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS inventario_db;

-- Usar la base de datos
USE inventario_db;

-- Crear la tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    precio DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    categoria VARCHAR(50),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para búsquedas por nombre
CREATE INDEX idx_nombre ON productos(nombre);

-- Datos de ejemplo (opcional)
INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES
('Laptop HP Pavilion', 10, 799.99, 'Electrónicos'),
('Smartphone Samsung Galaxy', 15, 499.99, 'Electrónicos'),
('Silla de Oficina Ergonómica', 5, 149.99, 'Muebles'),
('Impresora Canon Pixma', 8, 129.99, 'Electrónicos'),
('Mesa de Centro', 3, 89.99, 'Muebles');