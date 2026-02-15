import os
from datetime import datetime
import pandas as pd
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas


# Carpeta donde se guardarán los archivos generados
# IMPORTANTE: en tu proyecto la carpeta se llama "Salidas" (con S mayúscula)
CARPETA_SALIDAS = "salidas"


def asegurar_carpeta_salidas():
    """Crea la carpeta de salidas si no existe."""
    os.makedirs(CARPETA_SALIDAS, exist_ok=True)


def _nombre_con_fecha(nombre_archivo: str) -> str:
    """
    Agrega fecha y hora al nombre para evitar sobreescritura.
    Ej: reporte_ventas_20260215_073012.csv
    """
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(nombre_archivo)
    if ext:  # si ya viene con extensión
        return f"{base}_{stamp}{ext}"
    return f"{nombre_archivo}_{stamp}"


def exportar_csv(df: pd.DataFrame, nombre_archivo: str, usar_timestamp: bool = True):
    """
    Exporta un DataFrame a CSV en la carpeta "Salidas".
    """
    if df is None or df.empty:
        raise ValueError("El DataFrame está vacío. No hay datos para exportar.")

    asegurar_carpeta_salidas()

    if not nombre_archivo.lower().endswith(".csv"):
        nombre_archivo += ".csv"
    if usar_timestamp:
        nombre_archivo = _nombre_con_fecha(nombre_archivo)

    ruta = os.path.join(CARPETA_SALIDAS, nombre_archivo)
    df.to_csv(ruta, index=False, encoding="utf-8-sig")
    return ruta


def exportar_excel(df: pd.DataFrame, nombre_archivo: str, usar_timestamp: bool = True):
    """
    Exporta un DataFrame a Excel (.xlsx) en la carpeta "Salidas".
    """
    if df is None or df.empty:
        raise ValueError("El DataFrame está vacío. No hay datos para exportar.")

    asegurar_carpeta_salidas()

    if not nombre_archivo.lower().endswith(".xlsx"):
        nombre_archivo += ".xlsx"
    if usar_timestamp:
        nombre_archivo = _nombre_con_fecha(nombre_archivo)

    ruta = os.path.join(CARPETA_SALIDAS, nombre_archivo)
    df.to_excel(ruta, index=False)
    return ruta


def exportar_pdf_simple(df: pd.DataFrame, nombre_archivo: str, titulo="REPORTE", usar_timestamp: bool = True):
    """
    Exporta un DataFrame a un PDF sencillo (tipo tabla impresa).
    Útil para reportes pequeños/medianos.
    """
    if df is None or df.empty:
        raise ValueError("El DataFrame está vacío. No hay datos para exportar.")

    asegurar_carpeta_salidas()

    if not nombre_archivo.lower().endswith(".pdf"):
        nombre_archivo += ".pdf"
    if usar_timestamp:
        nombre_archivo = _nombre_con_fecha(nombre_archivo)

    ruta = os.path.join(CARPETA_SALIDAS, nombre_archivo)

    texto = df.to_string(index=False)

    c = canvas.Canvas(ruta, pagesize=landscape(letter))
    width, height = landscape(letter)

    # Título
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, height - 30, titulo)

    # Texto del dataframe
    c.setFont("Courier", 8)
    y = height - 60
    line_height = 10

    for line in texto.split("\n"):
        if y < 30:
            c.showPage()
            c.setFont("Helvetica-Bold", 14)
            c.drawString(30, height - 30, titulo)
            c.setFont("Courier", 8)
            y = height - 60

        c.drawString(30, y, line[:220])
        y -= line_height

    c.save()
    return ruta