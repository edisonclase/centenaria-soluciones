Centenaria Soluciones - Sistema de Ventas y Compras (SQL Server + Python)
Español
Descripción

Proyecto final del Técnico en Base de Datos.

Sistema desarrollado en Python conectado a SQL Server para gestionar:

Clientes

Máquinas

Empleados

Proveedores

Ventas

Compras

El sistema permite realizar operaciones CRUD, registrar transacciones con actualización automática de inventario y generar reportes con JOIN exportables a CSV, Excel y PDF.

Tecnologías Utilizadas

SQL Server (SSMS)

Python 3

pyodbc

pandas

reportlab

openpyxl

Funcionalidades Principales
Gestión CRUD

Crear, listar, buscar, actualizar y eliminar:

Clientes

Máquinas

Empleados

Proveedores

Transacciones

Registrar Venta:

Inserta cabecera y detalle

Toma el precio desde la base de datos

Calcula total automáticamente

Descuenta stock

Usa transacciones para integridad de datos

Registrar Compra:

Inserta cabecera y detalle

Calcula total

Aumenta stock

Usa transacciones para integridad de datos

Reportes (JOIN con pandas)

Reporte de ventas con subtotales

Reporte de ventas con categoría

Reporte de compras con subtotales

Reporte de inventario de máquinas

Reporte de stock bajo (según umbral)

Exportación

El sistema permite exportar el último reporte visualizado a:

CSV

Excel (.xlsx)

PDF

Los archivos se guardan automáticamente en la carpeta salidas/.

Estructura del Proyecto

main.py → Menú principal (interfaz en consola)

db.py → Conexión a SQL Server

crud_clientes.py

crud_maquinas.py

crud_empleados.py

crud_proveedores.py

ventas_service.py → Lógica de ventas con transacción

compras_service.py → Lógica de compras con transacción

reportes.py → Consultas JOIN convertidas a DataFrame

exportar.py → Exportación a CSV / Excel / PDF

salidas/ → Carpeta de archivos exportados

requirements.txt → Dependencias del proyecto

Requisitos

Windows

SQL Server instalado

SQL Server Management Studio (SSMS)

Driver ODBC para SQL Server (ejemplo: ODBC Driver 17 o superior)

Python 3.x

Instalación

Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>

Crear entorno virtual:

python -m venv .venv

Activar entorno virtual:

.\.venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt

Ejecutar el sistema:

python main.py
Configuración de Base de Datos

En el archivo db.py se debe configurar:

Servidor SQL

Nombre de la base de datos

Driver ODBC

Tipo de autenticación (Trusted Connection o usuario/contraseña)

Objetivo del Proyecto

Aplicar los conocimientos de:

Diseño y uso de bases de datos relacionales

Consultas SQL avanzadas con JOIN

Integración de Python con SQL Server mediante pyodbc

Uso de pandas para manipulación y visualización de datos

Manejo de transacciones

Exportación de reportes a múltiples formatos

English
Description

Final project for the Database Technician program.

This system was developed using Python connected to SQL Server to manage:

Customers

Machines

Employees

Suppliers

Sales

Purchases

The system allows full CRUD operations, transactional sales and purchases with automatic stock updates, and generation of JOIN reports exportable to CSV, Excel and PDF.

Technologies Used

SQL Server (SSMS)

Python 3

pyodbc

pandas

reportlab

openpyxl

Main Features
CRUD Management

Create, list, search, update and delete:

Customers

Machines

Employees

Suppliers

Transactions

Register Sale:

Inserts header and detail

Takes price directly from database

Calculates total automatically

Decreases stock

Uses database transactions

Register Purchase:

Inserts header and detail

Calculates total

Increases stock

Uses database transactions

Reports (JOIN with pandas)

Sales report with subtotals

Sales report with category

Purchase report with subtotals

Machine inventory report

Low stock report (custom threshold)

Export

The system allows exporting the last viewed report to:

CSV

Excel (.xlsx)

PDF

Files are automatically saved inside the salidas/ folder.

Project Structure

main.py → Console interface

db.py → SQL Server connection

crud_*.py → CRUD modules

ventas_service.py → Sales transaction logic

compras_service.py → Purchase transaction logic

reportes.py → JOIN queries as DataFrames

exportar.py → Export to CSV / Excel / PDF

salidas/ → Exported files

requirements.txt → Project dependencies

Requirements

Windows

SQL Server

SQL Server ODBC Driver (17 or higher)

Python 3.x

Installation
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python main.py
Project Objective

To apply knowledge of:

Relational database design

SQL JOIN queries

Python and SQL Server integration

Data manipulation with pandas

Transaction handling

Multi-format report export