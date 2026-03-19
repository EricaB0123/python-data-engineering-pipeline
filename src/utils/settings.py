from pathlib import Path
import os

class Config:
    DEBUG = False
    SQL_HOST = os.getenv("SQL_SERVER_HOST", "localhost")
    SQL_PORT = int(os.getenv("SQL_SERVER_PORT", 1433))
    SQL_USER = os.getenv("SQL_SERVER_USER", "sa")
    SQL_DB = os.getenv("SQL_SERVER_DB", "TrafficDB")
    LOGS_DIR = "logs"


_password_file = os.getenv("SQL_SERVER_PASSWORD_FILE")

if _password_file and Path(_password_file).exists():
    SQL_PASSWORD = Path(_password_file).read_text().strip()

else:
    SQL_PASSWORD = os.getenv("SQL_SERVER_PASSWORD")

