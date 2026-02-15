from db import run_execute, run_query_df

# =========================
# CREAR
# =========================
def crear_empleado(nombre, apellido, puesto, telefono):
    sql = """
    INSERT INTO Empleados (nombre, apellido, puesto, telefono)
    VALUES (?, ?, ?, ?);
    """
    run_execute(sql, [nombre, apellido, puesto, telefono])

# =========================
# LEER
# =========================
def listar_empleados():
    return run_query_df("SELECT * FROM Empleados ORDER BY id_empleado;")

def buscar_empleado_por_telefono(telefono):
    return run_query_df("SELECT * FROM Empleados WHERE telefono = ?;", [telefono])

def buscar_empleado_por_nombre(nombre):
    return run_query_df("SELECT * FROM Empleados WHERE nombre LIKE ?;", [f"%{nombre}%"])

# =========================
# ACTUALIZAR
# =========================
def actualizar_telefono_empleado(id_empleado, nuevo_telefono):
    run_execute("UPDATE Empleados SET telefono = ? WHERE id_empleado = ?;", [nuevo_telefono, id_empleado])

def actualizar_empleado_completo(id_empleado, nombre, apellido, puesto, telefono):
    sql = """
    UPDATE Empleados
    SET nombre = ?, apellido = ?, puesto = ?, telefono = ?
    WHERE id_empleado = ?;
    """
    run_execute(sql, [nombre, apellido, puesto, telefono, id_empleado])

# =========================
# ELIMINAR
# =========================
def eliminar_empleado(id_empleado):
    run_execute("DELETE FROM Empleados WHERE id_empleado = ?;", [id_empleado])