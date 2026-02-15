from db import run_execute, run_query_df

# ============================================================
# CRUD CLIENTES
# - CREAR: crear_cliente
# - LECTURA:   listar_clientes, buscar_cliente_por_telefono, buscar_cliente_por_nombre
# - ACTUALIZAR: actualizar_telefono_cliente, actualizar_cliente_completo
# - ELIMINAR: eliminar_cliente
# ============================================================

# =========================
# CREAR
# =========================
def crear_cliente(nombre, apellido, correo, telefono, direccion):
    sql = """
    INSERT INTO Clientes (nombre, apellido, correo, telefono, direccion)
    VALUES (?, ?, ?, ?, ?);
    """
    run_execute(sql, [nombre, apellido, correo, telefono, direccion])


# =========================
# LECTURA
# =========================
def listar_clientes():
    return run_query_df("SELECT * FROM Clientes ORDER BY id_cliente;")

def buscar_cliente_por_telefono(telefono):
    sql = "SELECT * FROM Clientes WHERE telefono = ?;"
    return run_query_df(sql, [telefono])

def buscar_cliente_por_nombre(nombre):
    # LIKE para encontrar coincidencias parciales
    sql = "SELECT * FROM Clientes WHERE nombre LIKE ?;"
    return run_query_df(sql, [f"%{nombre}%"])


# =========================
# ACTUALIZAR
# =========================
def actualizar_telefono_cliente(id_cliente, nuevo_telefono):
    sql = "UPDATE Clientes SET telefono = ? WHERE id_cliente = ?;"
    run_execute(sql, [nuevo_telefono, id_cliente])

def actualizar_cliente_completo(id_cliente, nombre, apellido, correo, telefono, direccion):
    sql = """
    UPDATE Clientes
    SET nombre = ?, apellido = ?, correo = ?, telefono = ?, direccion = ?
    WHERE id_cliente = ?;
    """
    run_execute(sql, [nombre, apellido, correo, telefono, direccion, id_cliente])


# =========================
# ELIMINAR
# =========================
def eliminar_cliente(id_cliente):
    sql = "DELETE FROM Clientes WHERE id_cliente = ?;"
    run_execute(sql, [id_cliente])