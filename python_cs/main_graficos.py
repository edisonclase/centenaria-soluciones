# main_graficos.py
from reportes_graficos import (
    crear_conexion,
    ventas_por_cliente,
    ventas_por_empleado,
    inventario_maquinas,
    compras_por_proveedor,
    ventas_por_categoria,
)

def main():
    server = r"localhost"
    database = "CentenariaSolucionesDB"

    conexion = crear_conexion(server=server, database=database)

    ventas_por_cliente(conexion)
    ventas_por_empleado(conexion)
    inventario_maquinas(conexion)
    compras_por_proveedor(conexion)
    ventas_por_categoria(conexion)

    conexion.close()

if __name__ == "__main__":
    main()