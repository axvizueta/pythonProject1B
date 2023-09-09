from django.shortcuts import render
import os
from dotenv import load_dotenv, find_dotenv


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def buscador(request):
    load_dotenv(find_dotenv())

    USER = os.environ.get("MONGO_USER")
    PASSWORD = os.environ.get("MONGO_PASSWORD")
    HOSTNAME = os.environ.get("MONGO_HOSTNAME")

    uri = f"mongodb+srv://{USER}:{PASSWORD}@{HOSTNAME}/?retryWrites=true&w=majority"

    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    mydb = client["proyecto"]
    carros_collection = mydb["carros"]
    dict_carros = carros_collection.find()



    return render(request, 'buscador_carros/buscador.html', {
        'carros': dict_carros
    })
