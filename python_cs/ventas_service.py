from datetime import date
from typing import List, Tuple
from db import get_connection

ItemVenta = Tuple[int, int]  # (id_maquina, cantidad)


def registrar_venta(id_cliente: int, id_empleado: int, items: List[ItemVenta], fecha: date | None = None) -> tuple[int, float]:
    """
    Registra una venta:
    - precio_unitario se toma desde Maquinas.precio (BD)
    - inserta Ventas + Detalle_Ventas
    - descuenta stock
    Retorna: (id_venta, total)
    """
    if not items:
        raise ValueError("La venta debe tener al menos 1 item.")
    if fecha is None:
        fecha = date.today()

    conn = get_connection()
    try:
        cur = conn.cursor()

        # Validar stock y obtener precios desde BD
        precios = {}
        for (id_maquina, cantidad) in items:
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que 0.")

            cur.execute("SELECT precio, stock FROM Maquinas WHERE id_maquina = ?;", (id_maquina,))
            row = cur.fetchone()
            if row is None:
                raise ValueError(f"Máquina no existe: id_maquina={id_maquina}")

            precio_bd = float(row[0])
            stock = int(row[1])

            if stock < cantidad:
                raise ValueError(f"Stock insuficiente para id_maquina={id_maquina}. Stock={stock}, solicitado={cantidad}")

            precios[id_maquina] = precio_bd

        total = sum(cant * precios[idm] for (idm, cant) in items)

        # Insertar cabecera y devolver id_venta con OUTPUT (más robusto que SCOPE_IDENTITY)
        cur.execute(
            """
            INSERT INTO Ventas (id_cliente, id_empleado, fecha, total)
            OUTPUT INSERTED.id_venta
            VALUES (?, ?, ?, ?);
            """,
            (id_cliente, id_empleado, fecha, total)
        )
        row = cur.fetchone()
        if row is None or row[0] is None:
            raise RuntimeError("No se pudo obtener id_venta (OUTPUT INSERTED devolvió NULL).")
        id_venta = int(row[0])

        # Detalle + descuento de stock
        for (id_maquina, cantidad) in items:
            precio_unitario = precios[id_maquina]

            cur.execute(
                """
                INSERT INTO Detalle_Ventas (id_venta, id_maquina, cantidad, precio_unitario)
                VALUES (?, ?, ?, ?);
                """,
                (id_venta, id_maquina, cantidad, precio_unitario)
            )

            cur.execute(
                "UPDATE Maquinas SET stock = stock - ? WHERE id_maquina = ?;",
                (cantidad, id_maquina)
            )

        conn.commit()
        return id_venta, float(total)

    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()