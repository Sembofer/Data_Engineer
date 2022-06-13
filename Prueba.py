import json
from numpy import int64
import requests
import pandas as pd


def api_requests_response(url):
    """_summary_

    Args:
        url (string): url de la api para extraer información

    Returns:
        DataFrame: devuelve un dataframe con la información
    """
    response = requests.get(str(url))
    data = response.json()
    return pd.DataFrame(data['result']['records'])

def distancias(x, y, alcaldia, indice):
    if indice <16:
        dist.append((x-alcaldia.position_latitude[indice])**2 + (y - alcaldia.position_longitude[indice])**2)
        distancias(x, y, alcaldia, indice +1)


# url de las api's
api_alcaldia_url = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=e4a9b05f-c480-45fb-a62c-6d4e39c5180e&limit=16'
api_ubicacion_unidades_metrobus = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=207'

#Llamada a la función para obtener la información en un dataframe
alcaldias = api_requests_response(api_alcaldia_url)
ubicacion_metrobus = api_requests_response(api_ubicacion_unidades_metrobus)

#Se ordenan de forma ascendente los DataFrames "alcaldias" y "ubicacion_metrobus"
#por los campos "cve_mun" y "vehicle_id", respectivamente
alcaldias = alcaldias.sort_values('cve_mun')
ubicacion_metrobus = ubicacion_metrobus.sort_values('vehicle_id')

#Lista de las columnas a las que se les cambiará el tipo de dato
positions=['position_latitude', 'position_longitude']

#Cambio de tipo de dato de str a float
alcaldias[positions] = alcaldias.geo_point_2d.str.split(',', expand=True)
alcaldias[positions] = alcaldias[positions].astype('float64')

#DataFrame que relaciona la alcaldia con cada "vehicle_id"
ubicacion_por_alcaldia= pd.DataFrame()

nomgeo_list = []
for lab, row in ubicacion_metrobus.iterrows():
    dist = []
    distancias(row.position_latitude, row.position_longitude,alcaldias,0)
    nomgeo_list.append(alcaldias.iloc[dist.index(min(dist)), 2])

ubicacion_por_alcaldia = ubicacion_por_alcaldia.assign(nomgeo = nomgeo_list)
ubicacion_por_alcaldia = ubicacion_por_alcaldia.assign(vehicle_id = ubicacion_metrobus.vehicle_id)

ubicacion_por_alcaldia = ubicacion_por_alcaldia.sort_values('vehicle_id')
print(ubicacion_por_alcaldia.iloc[2,:])
