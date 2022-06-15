# Data Engineer Pipeline

[Aqui](https://github.com/Sembofer/Data_Engineer/blob/master/Prueba%20data%20pipeline%20(Data%20Engineer)%20.pdf) los requerimientos del proyecto.


## Requisitos
Instale las siguientes dependencias del proyecto:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
## Preparar la Base de Datos

Before executing the queries, you need to set up the database with docker
```
docker run -d --name arkon_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -e POSTGRES_DB=arkon_db postgres
```
Para tener la base de datos actualizada, ejecuta el siguiente comando
```
python main.py
```

Ejecute el siguiente comando para obtener la API Rest
```
python app.py
```

### Consulta de la información almacenada
Para responder a los requerimientos (1,2,3,4) consuma el servicio mediante un método POST y con la URL generada. A continuación se describe la estructura del json para el consumo.

Para los requerimientos 2 y 4:
```
{
    "requirement" : number,
    "id" : number
}
```
Por ejemplo, para consultar la ubicación de una unidad dado su ID
```
{
    "requirement" : 2,
    "id" : 4
}
```

Para los requerimientos 1 y 3:
```
{
    "requirement" : number,
    "id" : ""
}
```
si bien, para los requerimientos 1 y 3, en la llave "id" puede poner cualquier cosa sin afectar la consulta.