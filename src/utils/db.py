import sqlalchemy as sa
import urllib.parse
from src.utils.settings import Config

def get_engine():
    odbc_str = (
        f"DRIVER=ODBC Driver 18 for SQL Server;"
        f"SERVER={Config.SQL_HOST},{Config.SQL_PORT};"
        f"DATABASE={Config.SQL_DB};"
        f"UID={Config.SQL_USER};"
        f"PWD={Config.SQL_PASSWORD};"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
    )

    params = urllib.parse.quote_plus(odbc_str)
    conn = f"mssql+pyodbc:///?odbc_connect={params}"

    return sa.create_engine(conn)
