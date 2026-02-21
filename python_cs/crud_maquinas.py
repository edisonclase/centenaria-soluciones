from db import run_execute, run_query_df

# ==========================================================================
# CRUD MAQUINAS
# - CREAR: crear_maquinas
# - LECTURA:   listar_maquinas, buscar_maquina_por_modelo,
# - ACTUALIZAR: actualizar_precio_maquina, actualizar_maquina_completa
# - ELIMINAR: eliminar_maquina
# =========================================================================


# =========================
# CREAR
# =========================
def crear_maquina(modelo, marca, precio, stock):
    sql = """
    INSERT INTO Maquinas (modelo, marca, precio, stock)
    VALUES (?, ?, ?, ?);
    """
    run_execute(sql, [modelo, marca, precio, stock])


# =========================
# LECTURA
# =========================
def listar_maquinas():
    return run_query_df("SELECT * FROM Maquinas ORDER BY id_maquina;")

def buscar_maquina_por_modelo(modelo):
    return run_query_df("SELECT * FROM Maquinas WHERE modelo LIKE ?;", [f"%{modelo}%"])


# =========================
# ACTUALIZAR
# =========================
def actualizar_precio_maquina(id_maquina, nuevo_precio):
    run_execute("UPDATE Maquinas SET precio = ? WHERE id_maquina = ?;", [nuevo_precio, id_maquina])

def actualizar_maquina_completa(id_maquina, modelo, marca, precio, stock):
    sql = """
    UPDATE Maquinas
    SET modelo = ?, marca = ?, precio = ?, stock = ?
    WHERE id_maquina = ?;
    """
    run_execute(sql, [modelo, marca, precio, stock, id_maquina])


# =========================
# ELIMINAR
# =========================
def eliminar_maquina(id_maquina):
    run_execute("DELETE FROM Maquinas WHERE id_maquina = ?;", [id_maquina])