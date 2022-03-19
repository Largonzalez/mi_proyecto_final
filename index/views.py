
from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'index/index.html', {})


def plantilla(request):
    
    nombre= 'Lara'
    apellido= 'Gonzalez'
    lista = [3,1,2,45,1,2,3]

    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista
} 

    return render (request,"index/plantilla.html", diccionario_de_datos)