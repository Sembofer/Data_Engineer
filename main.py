from cfg import DB_CONNSTR, URL
from etl_process import Stackoverflow

def extract_data():
    Stackoverflow(URL, DB_CONNSTR)

def load_data():
    Stackoverflow(URL, DB_CONNSTR).load()

def setup_all():
    extract_data()
    load_data()

if __name__ == "__main__":
    setup_all()