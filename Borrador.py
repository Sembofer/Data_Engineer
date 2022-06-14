import requests
import pandas as pd
from numpy import int64

def api_requests_response(url):
    """Realiza el request y devuelve un DataFrame

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

def unidades_dispon():
    """Función de devuelve una lista del id ("id") de las unidades disponibles,
    de acuerdo al campo "vehicle_currenten_status": 1 = Activa, 2 = Inactiva

    Returns:
        list: lista de unidades activas
    """
    unid_disp = ubicacion_metrobus[ubicacion_metrobus['vehicle_current_status']==1]
    return list(unid_disp['id'])

def ubic_por_ID(id):
    """Función que devuelve el nombre de la alcaldia según el id ("id") ingresado

    Args:
        id (int): Argumento que corresponde al campo "id"

    Returns:
        str: nombre de la alcaldía
    """
    return ubicacion_metrobus[ubicacion_metrobus['id']==id]['nomgeo']

def alcaldias_dispon():
    """Función que devuelve una lista de las alcaldías
    en las que se encuentra al menos una ubicación del metrobus

    Returns:
        list: lista de los nombres de las alcaldías (campo "nomgeo")
    """
    return list(ubicacion_metrobus['nomgeo'].unique())

def unidades_por_alcaldia(alcaldia_id):
    """_summary_

    Args:
        alcaldia_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    ubicacion_metrobus_por_alcaldia = ubicacion_metrobus[ubicacion_metrobus['alcaldia_id']==alcaldia_id]
    return ubicacion_metrobus_por_alcaldia['id'].count()

# url de las api's
api_alcaldia_url = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=e4a9b05f-c480-45fb-a62c-6d4e39c5180e&limit=16'
api_ubicacion_unidades_metrobus = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=207'

#Llamada a la función para obtener la información en un dataframe
alcaldias = api_requests_response(api_alcaldia_url)
ubicacion_metrobus = api_requests_response(api_ubicacion_unidades_metrobus)

#Se ordenan de forma ascendente los DataFrames "alcaldias" y "ubicacion_metrobus"
#por los campos "id" en ambos
alcaldias = alcaldias.sort_values('id')
ubicacion_metrobus = ubicacion_metrobus.sort_values('id')

#Lista de las columnas a las que se les cambiará el tipo de dato
positions=['position_latitude', 'position_longitude']

#Cambio de tipo de dato de str a float
alcaldias[positions] = alcaldias.geo_point_2d.str.split(',', expand=True)
alcaldias[positions] = alcaldias[positions].astype('float64')

#Loop para rellenar una lista que contiene el nombre de la alcaldia
#considerando la distancia mínima de la ubicacion de metrobus con la alcaldia
nomgeo_list = []
alcaldia_id_list =[]
alcaldia_cve_mun = []
for lab, row in ubicacion_metrobus.iterrows():
    dist = []
    distancias(row.position_latitude, row.position_longitude,alcaldias,0)
    nomgeo_list.append(alcaldias.iloc[dist.index(min(dist)), 2])
    alcaldia_id_list.append(alcaldias.iloc[dist.index(min(dist)), 1])
    alcaldia_cve_mun.append(alcaldias.iloc[dist.index(min(dist)), 3])

#Se agregan nuevas columnas "nomgeo", con el nombre de la alcaldía al que pertenece cada registro
ubicacion_metrobus = ubicacion_metrobus.assign(nomgeo = nomgeo_list)
ubicacion_metrobus = ubicacion_metrobus.assign(alcaldia_id = alcaldia_id_list)
ubicacion_metrobus = ubicacion_metrobus.assign(cve_num = alcaldia_cve_mun)

#Muestra la lista de las unidades activas
print(unidades_dispon())

#Muestra la alcaldia correspondiente al "id" = 1
print(ubic_por_ID(1))
#print(ubicacion_metrobus.loc[ubicacion_metrobus['id']==1,['id','alcaldia_id', 'nomgeo']])

#Muestra una lista de los nombres en los que se encuentra al menos una ubicación del metrobus
print(alcaldias_dispon())

#Muestra un conteo de las unididades por alcaldia de acuerdo al "id" de la alcaldia
print(unidades_por_alcaldia(3))