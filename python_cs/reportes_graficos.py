import pandas as pd
import matplotlib.pyplot as plt
from db import get_connection

def _leer_df(query: str) -> pd.DataFrame:
    conn = get_connection()
    try:
        return pd.read_sql(query, conn)
    finally:
        conn.close()

def _plot_bar(df: pd.DataFrame, x_col: str, y_col: str, titulo: str):
    if df is None or df.empty:
        print("No hay datos para graficar.")
        return
    plt.figure()
    plt.bar(df[x_col], df[y_col])
    plt.title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def ventas_por_cliente():
    query = """
    SELECT c.nombre,
           SUM(dv.cantidad * dv.precio_unitario) AS total_ventas
    FROM dbo.Ventas v
    JOIN dbo.Detalle_Ventas dv ON v.id_venta = dv.id_venta
    JOIN dbo.Clientes c ON v.id_cliente = c.id_cliente
    GROUP BY c.nombre
    ORDER BY total_ventas DESC;
    """
    df = _leer_df(query)
    _plot_bar(df, "nombre", "total_ventas", "Ventas por Cliente")

def ventas_por_empleado():
    query = """
    SELECT e.nombre,
           SUM(dv.cantidad * dv.precio_unitario) AS total_ventas
    FROM dbo.Ventas v
    JOIN dbo.Empleados e ON v.id_empleado = e.id_empleado
    JOIN dbo.Detalle_Ventas dv ON v.id_venta = dv.id_venta
    GROUP BY e.nombre
    ORDER BY total_ventas DESC;
    """
    df = _leer_df(query)
    _plot_bar(df, "nombre", "total_ventas", "Ventas por Empleado")

def inventario_maquinas():
    query = """
    SELECT modelo,
           stock
    FROM dbo.Maquinas
    ORDER BY stock DESC;
    """
    df = _leer_df(query)
    _plot_bar(df, "modelo", "stock", "Inventario de Máquinas (Stock)")

def compras_por_proveedor():
    query = """
    SELECT p.nombre,
           SUM(dc.cantidad * dc.precio_unitario) AS total_compras
    FROM dbo.Compras co
    JOIN dbo.Proveedores p ON co.id_proveedor = p.id_proveedor
    JOIN dbo.Detalle_Compras dc ON co.id_compra = dc.id_compra
    GROUP BY p.nombre
    ORDER BY total_compras DESC;
    """
    df = _leer_df(query)
    _plot_bar(df, "nombre", "total_compras", "Compras por Proveedor")

def ventas_por_categoria():
    query = """
    SELECT cat.nombre_categoria,
           SUM(dv.cantidad * dv.precio_unitario) AS total_ventas
    FROM dbo.Ventas v
    JOIN dbo.Detalle_Ventas dv ON v.id_venta = dv.id_venta
    JOIN dbo.Maquinas m ON dv.id_maquina = m.id_maquina
    JOIN dbo.Maquinas_Categorias mc ON m.id_maquina = mc.id_maquina
    JOIN dbo.Categorias cat ON mc.id_categoria = cat.id_categoria
    GROUP BY cat.nombre_categoria
    ORDER BY total_ventas DESC;
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