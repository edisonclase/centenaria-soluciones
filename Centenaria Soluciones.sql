CREATE DATABASE CentenariaSolucionesDB;
GO

USE CentenariaSolucionesDB;

-- =============================================
-- Seleccionar base de datos o crear si no existe
-- =============================================
IF DB_ID('CentenariaSolucionesDB') IS NULL
BEGIN
    CREATE DATABASE CentenariaSolucionesDB;
END
GO

USE CentenariaSolucionesDB;
GO

-- =============================================
-- Borrar tablas si ya existen para limpiar el proyecto
-- =============================================
IF OBJECT_ID('Detalle_Ventas', 'U') IS NOT NULL DROP TABLE Detalle_Ventas;
IF OBJECT_ID('Ventas', 'U') IS NOT NULL DROP TABLE Ventas;
IF OBJECT_ID('Detalle_Compras', 'U') IS NOT NULL DROP TABLE Detalle_Compras;
IF OBJECT_ID('Compras', 'U') IS NOT NULL DROP TABLE Compras;
IF OBJECT_ID('Maquinas_Categorias', 'U') IS NOT NULL DROP TABLE Maquinas_Categorias;
IF OBJECT_ID('Categorias', 'U') IS NOT NULL DROP TABLE Categorias;
IF OBJECT_ID('Maquinas', 'U') IS NOT NULL DROP TABLE Maquinas;
IF OBJECT_ID('Proveedores', 'U') IS NOT NULL DROP TABLE Proveedores;
IF OBJECT_ID('Clientes', 'U') IS NOT NULL DROP TABLE Clientes;
IF OBJECT_ID('Empleados', 'U') IS NOT NULL DROP TABLE Empleados;
GO

-- =============================================
-- Tablas principales
-- =============================================

-- Empleados
CREATE TABLE Empleados (
    id_empleado INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    puesto VARCHAR(50),
    telefono VARCHAR(15)
);

-- Clientes
CREATE TABLE Clientes (
    id_cliente INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo VARCHAR(100),
    telefono VARCHAR(15),
    direccion VARCHAR(100)
);

-- Proveedores
CREATE TABLE Proveedores (
    id_proveedor INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50),
    telefono VARCHAR(15),
    correo VARCHAR(100)
);

-- Máquinas
CREATE TABLE Maquinas (
    id_maquina INT IDENTITY(1,1) PRIMARY KEY,
    modelo VARCHAR(50),
    marca VARCHAR(50),
    precio DECIMAL(10,2),
    stock INT
);

-- Categorías
CREATE TABLE Categorias (
    id_categoria INT IDENTITY(1,1) PRIMARY KEY,
    nombre_categoria VARCHAR(50)
);

-- Relación Máquinas – Categorías
CREATE TABLE Maquinas_Categorias (
    id_maquina INT,
    id_categoria INT,
    PRIMARY KEY (id_maquina, id_categoria),
    FOREIGN KEY (id_maquina) REFERENCES Maquinas(id_maquina),
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

-- Ventas
CREATE TABLE Ventas (
    id_venta INT IDENTITY(1,1) PRIMARY KEY,
    id_cliente INT,
    id_empleado INT,
    fecha DATE,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado)
);

-- Detalle Ventas
CREATE TABLE Detalle_Ventas (
    id_detalle INT IDENTITY(1,1) PRIMARY KEY,
    id_venta INT,
    id_maquina INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta),
    FOREIGN KEY (id_maquina) REFERENCES Maquinas(id_maquina)
);

-- Compras
CREATE TABLE Compras (
    id_compra INT IDENTITY(1,1) PRIMARY KEY,
    id_proveedor INT,
    fecha DATE,
    total DECIMAL(10,2),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);

-- Detalle Compras
CREATE TABLE Detalle_Compras (
    id_detalle_compra INT IDENTITY(1,1) PRIMARY KEY,
    id_compra INT,
    id_maquina INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_compra) REFERENCES Compras(id_compra),
    FOREIGN KEY (id_maquina) REFERENCES Maquinas(id_maquina)
);

-- =============================================
-- Insertar datos de prueba
-- =============================================

-- Empleados
INSERT INTO Empleados (nombre, apellido, puesto, telefono) VALUES
('Ana','Martínez','Vendedora','8091000001'),
('Carlos','Gómez','Gerente','8091000002'),
('Luis','Pérez','Vendedor','8091000003'),
('María','López','Contadora','8091000004'),
('José','Ramírez','Vendedor','8091000005'),
('Sofía','Fernández','Administrativa','8091000006'),
('Pedro','Santos','Vendedor','8091000007'),
('Lucía','García','Gerente de Ventas','8091000008'),
('Andrés','Vásquez','Vendedor','8091000009'),
('Clara','Rodríguez','Vendedora','8091000010'),
('Miguel','Díaz','Vendedor','8091000011'),
('Isabel','Morales','Administrativa','8091000012'),
('Diego','Torres','Vendedor','8091000013'),
('Valeria','Suárez','Vendedora','8091000014'),
('Juan','Hernández','Vendedor','8091000015');

-- Clientes
INSERT INTO Clientes (nombre, apellido, correo, telefono, direccion) VALUES
('Luis','Gómez','luis@gmail.com','8092000001','Av. Libertad 123'),
('María','Pérez','maria@gmail.com','8092000002','Calle Central 45'),
('Carlos','Ramírez','carlos@gmail.com','8092000003','Av. Duarte 67'),
('Ana','López','ana@gmail.com','8092000004','Calle 5 de Julio 12'),
('José','Fernández','jose@gmail.com','8092000005','Av. Independencia 99');

-- Proveedores
INSERT INTO Proveedores (nombre, telefono, correo) VALUES
('TextilPro','8093000001','contacto@textilpro.com'),
('CoserPlus','8093000002','ventas@coserplus.com'),
('MaquinasRápidas','8093000003','info@maquinasrapidas.com');

-- Máquinas
INSERT INTO Maquinas (modelo, marca, precio, stock) VALUES
('MC-101','Singer',250.00,10),
('MC-102','Brother',270.00,8),
('MC-103','Janome',300.00,12);

-- Categorías
INSERT INTO Categorias (nombre_categoria) VALUES
('Doméstica'), ('Industrial'), ('Portátil');

-- Relación máquinas – categorías
INSERT INTO Maquinas_Categorias (id_maquina, id_categoria) VALUES
(1,1), (2,2), (3,3);

-- Compras
INSERT INTO Compras (id_proveedor, fecha, total) VALUES
(1,'2026-02-01',2500.00),
(2,'2026-02-03',3200.00);

-- Detalle Compras
INSERT INTO Detalle_Compras (id_compra, id_maquina, cantidad, precio_unitario) VALUES
(1,1,10,250.00),
(2,2,5,270.00);

-- Ventas
INSERT INTO Ventas (id_cliente, id_empleado, fecha, total) VALUES
(1,1,'2026-02-05',250.00),
(2,2,'2026-02-06',270.00);

-- Detalle Ventas
INSERT INTO Detalle_Ventas (id_venta, id_maquina, cantidad, precio_unitario) VALUES
(1,1,1,250.00),
(2,2,1,270.00);
SELECT 
    v.id_venta,
    c.nombre AS NombreCliente,
    m.modelo,
    cat.nombre_categoria,
    dv.cantidad,
    dv.precio_unitario
FROM Ventas v
INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
INNER JOIN Maquinas m ON dv.id_maquina = m.id_maquina
INNER JOIN Maquinas_Categorias mc ON m.id_maquina = mc.id_maquina
INNER JOIN Categorias cat ON mc.id_categoria = cat.id_categoria
INNER JOIN Clientes c ON v.id_cliente = c.id_cliente;
SELECT 
    v.id_venta,
    c.nombre AS NombreCliente,
    m.modelo,
    cat.nombre_categoria,
    dv.cantidad,
    dv.precio_unitario
FROM Ventas v
INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
INNER JOIN Maquinas m ON dv.id_maquina = m.id_maquina
INNER JOIN Maquinas_Categorias mc ON m.id_maquina = mc.id_maquina
INNER JOIN Categorias cat ON mc.id_categoria = cat.id_categoria
INNER JOIN Clientes c ON v.id_cliente = c.id_cliente;
SELECT 
    v.id_venta,
    c.nombre AS NombreCliente,
    e.nombre AS NombreEmpleado,
    m.modelo,
    dv.cantidad,
    dv.precio_unitario,
    dv.cantidad * dv.precio_unitario AS Subtotal
FROM Ventas v
INNER JOIN Clientes c ON v.id_cliente = c.id_cliente
INNER JOIN Empleados e ON v.id_empleado = e.id_empleado
INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
INNER JOIN Maquinas m ON dv.id_maquina = m.id_maquina;
