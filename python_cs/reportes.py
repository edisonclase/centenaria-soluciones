from db import run_query_df

def reporte_ventas_con_categoria():
    sql = """
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
    INNER JOIN Clientes c ON v.id_cliente = c.id_cliente
    ORDER BY v.id_venta;
    """
    return run_query_df(sql)

def reporte_ventas_subtotales():
    sql = """
    SELECT 
        v.id_venta,
        v.fecha,
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
    INNER JOIN Maquinas m ON dv.id_maquina = m.id_maquina
    ORDER BY v.id_venta;
    """
    return run_query_df(sql)

# =========================
# VENTAS (ya tienes 2)
# =========================
def reporte_ventas_con_categoria():
    sql = """
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
    INNER JOIN Clientes c ON v.id_cliente = c.id_cliente
    ORDER BY v.id_venta;
    """
    return run_query_df(sql)


def reporte_ventas_subtotales():
    sql = """
    SELECT 
        v.id_venta,
        v.fecha,
        c.nombre AS NombreCliente,
        e.nombre AS NombreEmpleado,
        m.modelo,
        dv.cantidad,
        dv.precio_unitario,
        dv.cantidad * dv.precio_unitario AS Subtotal,
        v.total AS TotalVenta
    FROM Ventas v
    INNER JOIN Clientes c ON v.id_cliente = c.id_cliente
    INNER JOIN Empleados e ON v.id_empleado = e.id_empleado
    INNER JOIN Detalle_Ventas dv ON v.id_venta = dv.id_venta
    INNER JOIN Maquinas m ON dv.id_maquina = m.id_maquina
    ORDER BY v.id_venta;
    """
    return run_query_df(sql)

# =========================
# COMPRAS (nuevo)
# =========================
def reporte_compras_detalle():
    sql = """
    SELECT
        co.id_compra,
        co.fecha,
        p.nombre AS NombreProveedor,
        m.modelo,
        dc.cantidad,
        dc.precio_unitario,
        dc.cantidad * dc.precio_unitario AS Subtotal,
        co.total AS TotalCompra
    FROM Compras co
    INNER JOIN Proveedores p ON co.id_proveedor = p.id_proveedor
    INNER JOIN Detalle_Compras dc ON co.id_compra = dc.id_compra
    INNER JOIN Maquinas m ON dc.id_maquina = m.id_maquina
    ORDER BY co.id_compra;
    """
    return run_query_df(sql)

# =========================
# INVENTARIO (nuevo)
# =========================
def reporte_inventario_maquinas():
    sql = """
    SELECT
        id_maquina,
        modelo,
        marca,
        precio,
        stock
    FROM Maquinas
    ORDER BY id_maquina;
    """
    return run_query_df(sql)

def reporte_stock_bajo(umbral=5):
    sql = """
    SELECT
        id_maquina,
        modelo,
        marca,
        precio,
        stock
    FROM Maquinas
    WHERE stock <= ?
    ORDER BY stock ASC;
    """
    return run_query_df(sql, [umbral])