from sqlalchemy import create_engine, null
from sqlalchemy.sql import text
import pandas as pd


class DB_connection:
    def __init__(self, DB_CONNSTR, SQL_DIR):
        self.engine = create_engine(DB_CONNSTR)
        self.SQL_DIR = SQL_DIR

    def db_query(self, sql_file, data) -> pd.DataFrame:
        resp = []
        with self.engine.connect() as conn:
            with open(self.SQL_DIR / f"{sql_file}.sql") as q:
                query = text(q.read())
                if (sql_file == "query_1" or sql_file == "query_3"):
                    rs = conn.execute(query).fetchall()
                else:
                    rs = conn.execute(query, x= data).fetchall()
        for tuple in rs:
            for x in tuple:
                resp.append(x)
        return str(resp)
