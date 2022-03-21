from django.shortcuts import render
from personas.models import Mujeres, Hombres
from personas.forms import BusquedaNombre, Formulario


# Create your views here.

def formulario_nombres(request):
    form= None
    return render(request, 'personas/formulario.html', {'form': form })

    # if request.method== 'POST': 
    #     form = Formulario()

    # if form.is_valid():
    #     data = form.cleaned_data
    #     nombre = Mujeres(nombre=data['nombre'], apellido=data['apellido'])
    #     formulario.save()
    # return render(request, 'indice/index.html', {'formulario': formulario})

    # formulario = Formulario()
    # return render(request, 'personas/formulario.html', {'formulario': formulario})

def busqueda_nombre(request):
    
    nombres_buscados = []
    dato = request.GET.get('partial_nombre', None)

    if dato is not None:
        nombres_buscados = Mujeres.objects.filter(nombre__icontains=dato)
        nombres_buscados = Hombres.objects.filter(nombre__icontains=dato)
   
    buscador = BusquedaNombre
    ()
    return render(
        request, "personas/busqueda.html",
        {'buscador': buscador, 'nombres_buscados': nombres_buscados, 'dato': dato})