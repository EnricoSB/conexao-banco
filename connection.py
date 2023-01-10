import sqlalchemy
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL
import os
from dotenv import find_dotenv,load_dotenv
load_dotenv(find_dotenv())
class Db():
    def __init__(self):
        connection_string = (
            f'DRIVER={os.getenv("DRIVER")};'
            f'SERVER={os.getenv("HOST")};'
            f'DATABASE={os.getenv("DATABASE")};'
            f'UID={os.getenv("USERDB")};'
            f'PWD={os.getenv("PASSWORD")}'
        )
        connection_url=URL.create(
            'mssql+pyodbc', query={'odbc_connect':connection_string}
        )

        self.__engine = create_engine(connection_url,echo=True,future=True)

    def execute(self,query):
        with self.__engine.begin() as conn:
            return conn.execute(text(query)).all()

db=Db()
db.execute('select * from ...')