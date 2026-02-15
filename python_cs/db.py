import pyodbc
import pandas as pd

SERVER = "localhost"
DATABASE = "CentenariaSolucionesDB"
DRIVER = "ODBC Driver 17 for SQL Server"

def get_connection():
    return pyodbc.connect(
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

def run_execute(sql: str, params=None):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql, params or [])
        conn.commit()
    finally:
        conn.close()

def run_query_df(sql: str, params=None) -> pd.DataFrame:
    conn = get_connection()
    try:
        return pd.read_sql(sql, conn, params=params)
    finally:
        conn.close()