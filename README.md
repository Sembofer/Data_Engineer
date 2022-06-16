# Data Engineer Pipeline

[Aquí](https://github.com/Sembofer/Data_Engineer/blob/master/Prueba%20data%20pipeline%20(Data%20Engineer)%20.pdf) los requerimientos del proyecto.

[Aquí](https://github.com/Sembofer/Data_Engineer_Pipeline/blob/master/Diagrama_Solucion.pdf) el diagrama de la solución.

[Aquí](https://github.com/Sembofer/Data_Engineer_Pipeline/blob/master/summary.ipynb) un resumen del análisis de los datos.


## Requisitos
Instale las siguientes dependencias del proyecto:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### Preparar la Base de Datos
Antes de ejecutar el servicio necesita levantar una base de datos con docker
```
docker run -d --name arkon_data -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -e POSTGRES_DB=arkon_db postgres
```

## Servicio pipeline
A continuación, con los siguientes comandos se extrae la información directamente de los datos abiertos de la Ciudad de México y se obtiene el recurso API:
```
cd pipeline
python main.py
```

### Consulta de la información almacenada
Para responder a los requerimientos (1,2,3,4) consuma el servicio mediante un método POST y con la URL generada, el servidor espera recibir un formato json. A continuación se describe la estructura del json para el consumo.

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
Si bien, para los requerimientos 1 y 3, la clave "id" puede poner cualquier cosa sin afectar la consulta.

#### Acceso a la base de datos
Puede acceder a la base de datos ejecutando
```
docker exec -it arkon_data psql -U postgres
```

## Extras
- [ ] Implementar el API usando GraphQL.
- [ ] Las configuraciones necesarias para desplegar el servicio en kubernetes.