import sqlalchemy as sa
from src.utils.settings import Config

conn = (
    "mssql+pyodbc://"
    + Config.SQL_USER + ":"
    + Config.SQL_PASSWORD + "@"
    + Config.SQL_HOST + ":"
    + str(Config.SQL_PORT) + "/"
    + Config.SQL_DB
    + "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = sa.create_engine(conn)
print(engine.connect())
