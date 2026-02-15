from db import run_execute, run_query_df

# =========================
# CREAR
# =========================
def crear_proveedor(nombre, telefono, correo):
    sql = """
    INSERT INTO Proveedores (nombre, telefono, correo)
    VALUES (?, ?, ?);
    """
    run_execute(sql, [nombre, telefono, correo])

# =========================
# LEER
# =========================
def listar_proveedores():
    return run_query_df("SELECT * FROM Proveedores ORDER BY id_proveedor;")

def buscar_proveedor_por_nombre(nombre):
    return run_query_df("SELECT * FROM Proveedores WHERE nombre LIKE ?;", [f"%{nombre}%"])

def buscar_proveedor_por_telefono(telefono):
    return run_query_df("SELECT * FROM Proveedores WHERE telefono = ?;", [telefono])

# =========================
# ACTUALIZAR
# =========================
def actualizar_telefono_proveedor(id_proveedor, nuevo_telefono):
    run_execute("UPDATE Proveedores SET telefono = ? WHERE id_proveedor = ?;", [nuevo_telefono, id_proveedor])

def actualizar_proveedor_completo(id_proveedor, nombre, telefono, correo):
    sql = """
    UPDATE Proveedores
    SET nombre = ?, telefono = ?, correo = ?
    WHERE id_proveedor = ?;
    """
    run_execute(sql, [nombre, telefono, correo, id_proveedor])

# =========================
# ELIMINAR
# =========================
def eliminar_proveedor(id_proveedor):
    run_execute("DELETE FROM Proveedores WHERE id_proveedor = ?;", [id_proveedor])