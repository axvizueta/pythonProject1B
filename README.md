# Aplicacion en Django con MongoDB
Esta aplicacion web en django utiliza la arquitectura de software modelo-vista-controlador (MVC), para crear un sistema que muestra informacion en el explorador de forma local. 

## PreRequisitos
1. Descargar el repositorio local con el comando : `git clone https://github.com/axvizueta/pythonProject1B.git`
2. Ingresar a la carpeta del proyecto, activar el ambiente virtual: `source .venv/bin/activate`
3. Actualiza la libreria de pip : `pip install --upgrade pip`
4. Instalar los requerimientos y librerias de python: `pip install -r requirements.txt`
5. Asegurarse que mongodb se encuentre ejecutnado en la nube

## Ejecutar el sistema
1. Dentro de la carpeta del sistema ejecutar el siguiente comando : python manage.py runserver
2. Abrir al explorador web , ir al localhost:8000


## Desafios encontrados 
- El modelo vista controlador utiliza una base de datos relacional lo cual no es compatible con mongoDb
- La estructura de datos de mongodb necesiita procesamiento para que sea compatible con django temple
- La estructura de datos de mongodb utiliza cursores que son iterables pero necesita ser compartido a diccionarios
- Existe 
