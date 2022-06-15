from pathlib import Path

ROOT_DIR = Path().resolve().parent
SQL_DIR = ROOT_DIR / "Data_Engineer/pipeline/query"


USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DATABASE = 'arkon_db'


DB_CONNSTR = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


URL = {
    'URL_UBICACIONES' : 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=207',
    'URL_ALCALDIAS' : 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=e4a9b05f-c480-45fb-a62c-6d4e39c5180e&limit=16'
}