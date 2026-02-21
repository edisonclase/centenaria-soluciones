import pandas as pd
import matplotlib.pyplot as plt
from db import get_connection

def ventas_por_cliente():
    query = """
    SELECT c.nombre,
           SUM(dv.cantidad * dv.precio_unitario) AS total_ventas
    FROM dbo.Ventas v
    JOIN dbo.Detalle_Ventas dv ON v.id_venta = dv.id_venta
    JOIN dbo.Clientes c ON v.id_cliente = c.id_cliente
    GROUP BY c.nombre
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    plt.figure()
    plt.bar(df["nombre"], df["total_ventas"])
    plt.title("Ventas por Cliente")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def ventas_por_empleado():
    query = """
    SELECT e.nombre,
           SUM(dv.cantidad * dv.precio_unitario) AS total_ventas
    FROM dbo.Ventas v
    JOIN dbo.Empleados e ON v.id_empleado = e.id_empleado
    JOIN dbo.Detalle_Ventas dv ON v.id_venta = dv.id_venta
    GROUP BY e.nombre
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    plt.figure()
    plt.bar(df["nombre"], df["total_ventas"])
    plt.title("Ventas por Empleado")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def inventario_maquinas():
    query = "SELECT nombre, stock FROM dbo.Maquinas"
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    plt.figure()
    plt.bar(df["nombre"], df["stock"])
    plt.title("Inventario de Máquinas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def compras_por_proveedor():
    query = """
    SELECT p.nombre,
           SUM(dc.cantidad * dc.precio_unitario) AS total_compras
    FROM dbo.Compras c
    JOIN dbo.Proveedores p ON c.id_proveedor = p.id_proveedor
    JOIN dbo.Detalle_Compras dc ON c.id_compra = dc.id_compra
    GROUP BY p.nombre
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    plt.figure()
    plt.bar(df["nombre"], df["total_compras"])
    plt.title("Compras por Proveedor")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def ventas_por_categoria():
    query = """
    SELECT mc.nombre_categoria,
           SUM(dv.cantidad * dv.precio_unitario) AS total_ventas
    FROM dbo.Ventas v
    JOIN dbo.Detalle_Ventas dv ON v.id_venta = dv.id_venta
    JOIN dbo.Maquinas m ON dv.id_maquina = m.id_maquina
    JOIN dbo.Maquinas_Categorias mc ON m.id_categoria = mc.id_categoria
    GROUP BY mc.nombre_categoria
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    plt.figure()
    plt.bar(df["nombre_categoria"], df["total_ventas"])
    plt.title("Ventas por Categoría")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()