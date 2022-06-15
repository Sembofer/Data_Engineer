from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd


class DB_connection:
    def __init__(self, DB_CONNSTR, SQL_DIR):
        self.engine = create_engine(DB_CONNSTR)
        self.SQL_DIR = SQL_DIR

    def db_query(self, sql_file) -> pd.DataFrame:
        resp = []
        with self.engine.connect() as conn:
            with open(self.SQL_DIR / f"{sql_file}.sql") as q:
                query = text(q.read())
                rs = conn.execute(query).fetchall()
        for tuple in rs:
            for x in tuple:
                resp.append(x)
        return str(resp)
