from reportes_graficos import (
    ventas_por_cliente,
    ventas_por_empleado,
    inventario_maquinas,
    compras_por_proveedor,
    ventas_por_categoria,
)

def main():
    ventas_por_cliente()
    ventas_por_empleado()
    inventario_maquinas()
    compras_por_proveedor()
    ventas_por_categoria()

if __name__ == "__main__":
    main()