# Sistema de Recomendación de Videojuegos

El Sistema de Recomendación de Videojuegos es una plataforma que recomienda videojuegos a los usuarios en función de su comportamiento de juego pasado. Utiliza surprise framework para predecir qué juegos podría gustarle a un usuario en base a los percentiles de tiempo que este pasa jugando cada juego en particular. De esta manera, se busca poder aumentar la probabilidad de que cada juego recomendado sea de los más jugados para cada usuario.

## Primeros pasos
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para fines de desarrollo y prueba.

### Prerrequisitos
El proyecto se basa en Python y requiere las siguientes librerías de Python:

- pandas
- scikit-surprise
- pickle
- FastAPI
- magnum
- uvicorn

Puedes instalar estos usando pip:

pip install -r requirements.txt

### Correr el codigo

El codigo puede ser interactuado a traves de fastapi. Este tiene un metodo get */predictvideogames* que recibe como parametro el user_id de una de las personas y n_recommendations como la cantidad de items a recomendar.

Finalmente, si se desea conocoer los user_ids que estan habilidad se puede hacer un get request a /users y este devolvera la lista de todos los ids activos para el modelo. En este orden de ideas, solo se hacen recomendacions a usuarios ya existentes y no a nuevos.

Para correr el modelo en fastapi:

1. Ir a la carpeta en donde se guardó el repositorio.

2. Correr lo siguiente:
`uvicorn main:app --reload`