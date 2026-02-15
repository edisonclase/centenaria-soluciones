from datetime import date
from typing import List, Tuple
from db import get_connection

ItemCompra = Tuple[int, int, float]  # (id_maquina, cantidad, precio_unitario)


def registrar_compra(id_proveedor: int, items: List[ItemCompra], fecha: date | None = None) -> tuple[int, float]:
    """
    Registra una compra:
    - inserta Compras + Detalle_Compras
    - aumenta stock
    Retorna: (id_compra, total)
    """
    if not items:
        raise ValueError("La compra debe tener al menos 1 item.")
    if fecha is None:
        fecha = date.today()

    conn = get_connection()
    try:
        cur = conn.cursor()

        for (id_maquina, cantidad, precio_unitario) in items:
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que 0.")
            if float(precio_unitario) <= 0:
                raise ValueError("El precio unitario debe ser mayor que 0.")

            cur.execute("SELECT 1 FROM Maquinas WHERE id_maquina = ?;", (id_maquina,))
            if cur.fetchone() is None:
                raise ValueError(f"Máquina no existe: id_maquina={id_maquina}")

        total = sum(cant * float(precio) for (_id, cant, precio) in items)

        cur.execute(
            """
            INSERT INTO Compras (id_proveedor, fecha, total)
            OUTPUT INSERTED.id_compra
            VALUES (?, ?, ?);
            """,
            (id_proveedor, fecha, total)
        )
        row = cur.fetchone()
        if row is None or row[0] is None:
            raise RuntimeError("No se pudo obtener id_compra (OUTPUT INSERTED devolvió NULL).")
        id_compra = int(row[0])

        for (id_maquina, cantidad, precio_unitario) in items:
            cur.execute(
                """
                INSERT INTO Detalle_Compras (id_compra, id_maquina, cantidad, precio_unitario)
                VALUES (?, ?, ?, ?);
                """,
                (id_compra, id_maquina, cantidad, precio_unitario)
            )
            cur.execute(
                "UPDATE Maquinas SET stock = stock + ? WHERE id_maquina = ?;",
                (cantidad, id_maquina)
            )

        conn.commit()
        return id_compra, float(total)

    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()