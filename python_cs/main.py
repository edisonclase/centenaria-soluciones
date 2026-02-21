import pandas as pd

from crud_clientes import (
    crear_cliente, listar_clientes, buscar_cliente_por_telefono,
    actualizar_telefono_cliente, eliminar_cliente,
    buscar_cliente_por_nombre, actualizar_cliente_completo
)

from crud_maquinas import (
    crear_maquina, listar_maquinas,
    actualizar_precio_maquina, eliminar_maquina,
    actualizar_maquina_completa, buscar_maquina_por_modelo
)

from crud_empleados import (
    crear_empleado, listar_empleados, buscar_empleado_por_telefono,
    buscar_empleado_por_nombre, actualizar_telefono_empleado,
    actualizar_empleado_completo, eliminar_empleado
)

from crud_proveedores import (
    crear_proveedor, listar_proveedores, buscar_proveedor_por_nombre,
    buscar_proveedor_por_telefono, actualizar_telefono_proveedor,
    actualizar_proveedor_completo, eliminar_proveedor
)

from reportes import (
    reporte_ventas_subtotales,
    reporte_ventas_con_categoria,
    reporte_compras_detalle,
    reporte_inventario_maquinas,
    reporte_stock_bajo
)

from reportes_graficos import (
    ventas_por_cliente,
    ventas_por_empleado,
    inventario_maquinas,
    compras_por_proveedor,
    ventas_por_categoria,
)

from exportar import exportar_csv, exportar_excel, exportar_pdf_simple

from ventas_service import registrar_venta
from compras_service import registrar_compra


# =========================
# Estructura Visual de Pandas
# =========================
pd.set_option("display.max_rows", 200)
pd.set_option("display.max_columns", 80)
pd.set_option("display.width", 160)


# Guardamos el último reporte que el usuario vio para exportarlo luego
ULTIMO_DF = None
ULTIMO_TITULO = None


def pause():
    input("\nPresiona ENTER para continuar...")


def set_ultimo_reporte(df, titulo):
    global ULTIMO_DF, ULTIMO_TITULO
    ULTIMO_DF = df
    ULTIMO_TITULO = titulo


def mostrar_df(df, titulo=None, guardar_como_ultimo=False):
    if titulo:
        print(f"\n=== {titulo} ===")

    if df is None or df.empty:
        print("No hay registros para mostrar.")
        return

    print(df.to_string(index=False))

    if guardar_como_ultimo:
        set_ultimo_reporte(df, titulo or "REPORTE")


def pedir_int(mensaje: str) -> int:
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("❌ Debes escribir un número entero. Intenta de nuevo.")


def pedir_float(mensaje: str) -> float:
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("❌ Debes escribir un número (ej: 250 o 250.50). Intenta de nuevo.")


def pedir_items_venta():
    """
    Captura items de venta:
    (id_maquina, cantidad)
    Termina cuando id_maquina = 0
    """
    items = []
    print("\nAgrega máquinas a la venta (0 para terminar):")
    while True:
        id_maquina = pedir_int("ID Máquina (0 terminar): ")
        if id_maquina == 0:
            break
        cantidad = pedir_int("Cantidad: ")
        items.append((id_maquina, cantidad))
    return items


def pedir_items_compra():
    """
    Captura items de compra:
    (id_maquina, cantidad, precio_unitario)
    Termina cuando id_maquina = 0
    """
    items = []
    print("\nAgrega máquinas a la compra (0 para terminar):")
    while True:
        id_maquina = pedir_int("ID Máquina (0 terminar): ")
        if id_maquina == 0:
            break
        cantidad = pedir_int("Cantidad: ")
        precio = pedir_float("Precio unitario de compra: ")
        items.append((id_maquina, cantidad, precio))
    return items


def exportar_ultimo(formato: str):
    """
    Exporta el último reporte visto (ULTIMO_DF) a CSV/Excel/PDF.
    """
    if ULTIMO_DF is None or ULTIMO_DF.empty:
        print("\n❌ No hay reporte cargado para exportar. Primero visualiza un reporte (menú REPORTES).")
        return

    nombre_base = (ULTIMO_TITULO or "reporte").lower().replace(" ", "_").replace("(", "").replace(")", "")
    if formato == "csv":
        ruta = exportar_csv(ULTIMO_DF, nombre_base)
        print(f"\n✅ CSV creado en: {ruta}")
    elif formato == "excel":
        ruta = exportar_excel(ULTIMO_DF, nombre_base)
        print(f"\n✅ Excel creado en: {ruta}")
    elif formato == "pdf":
        ruta = exportar_pdf_simple(ULTIMO_DF, nombre_base, titulo=ULTIMO_TITULO or "REPORTE")
        print(f"\n✅ PDF creado en: {ruta}")
    else:
        print("\n❌ Formato no soportado.")


def mostrar_menu():
    print("\n=========== CENTENARIA SOLUCIONES ===========")

    print("\n--- CLIENTES ---")
    print("1) Listar clientes")
    print("2) Crear cliente")
    print("3) Buscar cliente por teléfono")
    print("4) Buscar cliente por nombre")
    print("5) Actualizar teléfono cliente")
    print("6) Actualizar cliente completo")
    print("7) Eliminar cliente")

    print("\n--- MAQUINAS ---")
    print("8) Listar maquinas")
    print("9) Crear maquina")
    print("10) Buscar maquina por modelo")
    print("11) Actualizar precio maquina")
    print("12) Actualizar maquina completa")
    print("13) Eliminar maquina")

    print("\n--- EMPLEADOS ---")
    print("14) Listar empleados")
    print("15) Crear empleado")
    print("16) Buscar empleado por teléfono")
    print("17) Buscar empleado por nombre")
    print("18) Actualizar teléfono empleado")
    print("19) Actualizar empleado completo")
    print("20) Eliminar empleado")

    print("\n--- PROVEEDORES ---")
    print("21) Listar proveedores")
    print("22) Crear proveedor")
    print("23) Buscar proveedor por teléfono")
    print("24) Buscar proveedor por nombre")
    print("25) Actualizar teléfono proveedor")
    print("26) Actualizar proveedor completo")
    print("27) Eliminar proveedor")

    print("\n--- TRANSACCIONES ---")
    print("28) Registrar VENTA (cabecera + detalle + baja stock)")
    print("29) Registrar COMPRA (cabecera + detalle + sube stock)")

    print("\n--- REPORTES (SSMS -> Python/pandas) ---")
    print("30) Reporte ventas (JOIN con subtotal)")
    print("34) Reporte ventas con categoría (JOIN)")
    print("35) Reporte compras (JOIN con subtotal)")
    print("36) Reporte inventario de máquinas")
    print("37) Reporte stock bajo (umbral)")
    
    print("\n--- GRÁFICOS (matplotlib) ---")
    print("38) Gráfico: Ventas por cliente")
    print("39) Gráfico: Ventas por empleado")
    print("40) Gráfico: Inventario de máquinas")
    print("41) Gráfico: Compras por proveedor")
    print("42) Gráfico: Ventas por categoría")

    print("\n--- EXPORTAR ÚLTIMO REPORTE VISTO ---")
    print("31) Exportar a CSV")
    print("32) Exportar a Excel")
    print("33) Exportar a PDF")

    print("\n0) Salir")


def ejecutar_opcion(op: str) -> bool:
    # =======================
    # CLIENTES
    # =======================
    if op == "1":
        mostrar_df(listar_clientes(), "LISTADO DE CLIENTES")
        pause()

    elif op == "2":
        crear_cliente(
            input("Nombre: ").strip(),
            input("Apellido: ").strip(),
            input("Correo: ").strip(),
            input("Teléfono: ").strip(),
            input("Dirección: ").strip()
        )
        print("\n✅ Cliente creado correctamente.")
        pause()

    elif op == "3":
        tel = input("Teléfono: ").strip()
        mostrar_df(buscar_cliente_por_telefono(tel), f"CLIENTE TELÉFONO {tel}")
        pause()

    elif op == "4":
        nombre = input("Nombre a buscar: ").strip()
        mostrar_df(buscar_cliente_por_nombre(nombre), f"CLIENTES CON NOMBRE {nombre}")
        pause()

    elif op == "5":
        idc = pedir_int("ID Cliente: ")
        nuevo_tel = input("Nuevo teléfono: ").strip()
        actualizar_telefono_cliente(idc, nuevo_tel)
        print("\n✅ Teléfono actualizado.")
        pause()

    elif op == "6":
        idc = pedir_int("ID Cliente a actualizar: ")
        actualizar_cliente_completo(
            idc,
            input("Nuevo nombre: ").strip(),
            input("Nuevo apellido: ").strip(),
            input("Nuevo correo: ").strip(),
            input("Nuevo teléfono: ").strip(),
            input("Nueva dirección: ").strip()
        )
        print("\n✅ Cliente actualizado completamente.")
        pause()

    elif op == "7":
        idc = pedir_int("ID Cliente a eliminar: ")
        eliminar_cliente(idc)
        print("\n✅ Cliente eliminado.")
        pause()

    # =======================
    # MAQUINAS
    # =======================
    elif op == "8":
        mostrar_df(listar_maquinas(), "LISTADO DE MÁQUINAS")
        pause()

    elif op == "9":
        crear_maquina(
            input("Modelo: ").strip(),
            input("Marca: ").strip(),
            pedir_float("Precio: "),
            pedir_int("Stock: ")
        )
        print("\n✅ Máquina creada correctamente.")
        pause()

    elif op == "10":
        modelo = input("Modelo a buscar: ").strip()
        mostrar_df(buscar_maquina_por_modelo(modelo), f"MÁQUINAS CON MODELO {modelo}")
        pause()

    elif op == "11":
        idm = pedir_int("ID Máquina: ")
        nuevo_precio = pedir_float("Nuevo precio: ")
        actualizar_precio_maquina(idm, nuevo_precio)
        print("\n✅ Precio actualizado.")
        pause()

    elif op == "12":
        idm = pedir_int("ID Máquina a actualizar: ")
        actualizar_maquina_completa(
            idm,
            input("Nuevo modelo: ").strip(),
            input("Nueva marca: ").strip(),
            pedir_float("Nuevo precio: "),
            pedir_int("Nuevo stock: ")
        )
        print("\n✅ Máquina actualizada completamente.")
        pause()

    elif op == "13":
        idm = pedir_int("ID Máquina a eliminar: ")
        eliminar_maquina(idm)
        print("\n✅ Máquina eliminada.")
        pause()

    # =======================
    # EMPLEADOS
    # =======================
    elif op == "14":
        mostrar_df(listar_empleados(), "LISTADO DE EMPLEADOS")
        pause()

    elif op == "15":
        crear_empleado(
            input("Nombre: ").strip(),
            input("Apellido: ").strip(),
            input("Puesto: ").strip(),
            input("Teléfono: ").strip()
        )
        print("\n✅ Empleado creado correctamente.")
        pause()

    elif op == "16":
        tel = input("Teléfono: ").strip()
        mostrar_df(buscar_empleado_por_telefono(tel), f"EMPLEADO TELÉFONO {tel}")
        pause()

    elif op == "17":
        nombre = input("Nombre a buscar: ").strip()
        mostrar_df(buscar_empleado_por_nombre(nombre), f"EMPLEADOS CON NOMBRE {nombre}")
        pause()

    elif op == "18":
        ide = pedir_int("ID Empleado: ")
        nuevo_tel = input("Nuevo teléfono: ").strip()
        actualizar_telefono_empleado(ide, nuevo_tel)
        print("\n✅ Teléfono actualizado.")
        pause()

    elif op == "19":
        ide = pedir_int("ID Empleado a actualizar: ")
        actualizar_empleado_completo(
            ide,
            input("Nuevo nombre: ").strip(),
            input("Nuevo apellido: ").strip(),
            input("Nuevo puesto: ").strip(),
            input("Nuevo teléfono: ").strip()
        )
        print("\n✅ Empleado actualizado completamente.")
        pause()

    elif op == "20":
        ide = pedir_int("ID Empleado a eliminar: ")
        eliminar_empleado(ide)
        print("\n✅ Empleado eliminado.")
        pause()

    # =======================
    # PROVEEDORES
    # =======================
    elif op == "21":
        mostrar_df(listar_proveedores(), "LISTADO DE PROVEEDORES")
        pause()

    elif op == "22":
        crear_proveedor(
            input("Nombre: ").strip(),
            input("Teléfono: ").strip(),
            input("Correo: ").strip()
        )
        print("\n✅ Proveedor creado correctamente.")
        pause()

    elif op == "23":
        tel = input("Teléfono: ").strip()
        mostrar_df(buscar_proveedor_por_telefono(tel), f"PROVEEDOR TELÉFONO {tel}")
        pause()

    elif op == "24":
        nombre = input("Nombre a buscar: ").strip()
        mostrar_df(buscar_proveedor_por_nombre(nombre), f"PROVEEDORES CON NOMBRE {nombre}")
        pause()

    elif op == "25":
        idp = pedir_int("ID Proveedor: ")
        nuevo_tel = input("Nuevo teléfono: ").strip()
        actualizar_telefono_proveedor(idp, nuevo_tel)
        print("\n✅ Teléfono actualizado.")
        pause()

    elif op == "26":
        idp = pedir_int("ID Proveedor a actualizar: ")
        actualizar_proveedor_completo(
            idp,
            input("Nuevo nombre: ").strip(),
            input("Nuevo teléfono: ").strip(),
            input("Nuevo correo: ").strip()
        )
        print("\n✅ Proveedor actualizado completamente.")
        pause()

    elif op == "27":
        idp = pedir_int("ID Proveedor a eliminar: ")
        eliminar_proveedor(idp)
        print("\n✅ Proveedor eliminado.")
        pause()

    # =======================
    # TRANSACCIONES
    # =======================
    elif op == "28":
        id_cliente = pedir_int("ID Cliente: ")
        id_empleado = pedir_int("ID Empleado: ")
        items = pedir_items_venta()
        id_venta, total = registrar_venta(id_cliente, id_empleado, items)
        print(f"\n✅ Venta registrada. ID Venta: {id_venta} (precio tomado desde BD)")
        print(f"💰 Total a pagar del cliente: {total:.2f}")
        pause()

    elif op == "29":
        id_proveedor = pedir_int("ID Proveedor: ")
        items = pedir_items_compra()
        id_compra, total = registrar_compra(id_proveedor, items)
        print(f"\n✅ Compra registrada. ID Compra: {id_compra}")
        print(f"💰 Total de la compra: {total:.2f}")
        pause()

    # =======================
    # REPORTES (estos son los que se exportan)
    # =======================
    elif op == "30":
        df = reporte_ventas_subtotales()
        mostrar_df(df, "REPORTE VENTAS (JOIN con Subtotales)", guardar_como_ultimo=True)
        pause()

    elif op == "34":
        df = reporte_ventas_con_categoria()
        mostrar_df(df, "REPORTE VENTAS CON CATEGORÍA (JOIN)", guardar_como_ultimo=True)
        pause()

    elif op == "35":
        df = reporte_compras_detalle()
        mostrar_df(df, "REPORTE COMPRAS (JOIN con Subtotales)", guardar_como_ultimo=True)
        pause()

    elif op == "36":
        df = reporte_inventario_maquinas()
        mostrar_df(df, "REPORTE INVENTARIO DE MÁQUINAS", guardar_como_ultimo=True)
        pause()

    elif op == "37":
        umbral = pedir_int("Umbral de stock (ej: 5): ")
        df = reporte_stock_bajo(umbral)
        mostrar_df(df, f"REPORTE STOCK BAJO (<= {umbral})", guardar_como_ultimo=True)
        pause()
        
    elif op == "38":
        ventas_por_cliente()
        pause()

    elif op == "39":
        ventas_por_empleado()
        pause()

    elif op == "40":
        inventario_maquinas()
        pause()

    elif op == "41":
        compras_por_proveedor()
        pause()

    elif op == "42":
        ventas_por_categoria()
        pause()

    # =======================
    # EXPORTAR ÚLTIMO REPORTE VISTO
    # =======================
    elif op == "31":
        exportar_ultimo("csv")
        pause()

    elif op == "32":
        exportar_ultimo("excel")
        pause()

    elif op == "33":
        exportar_ultimo("pdf")
        pause()

    elif op == "0":
        return False

    else:
        print("\n❌ Opción inválida.")
        pause()

    return True


def main():
    while True:
        try:
            mostrar_menu()
            op = input("\nElige una opción: ").strip()
            if not ejecutar_opcion(op):
                break
        except Exception as e:
            print(f"\n❌ Ocurrió un error: {e}")
            pause()


if __name__ == "__main__":
    main()