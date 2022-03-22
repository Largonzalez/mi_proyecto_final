from django.shortcuts import render

from personas.models import Mujeres, Hombres

from . forms import BusquedaNombre, Formulario


# Create your views here.

def formulario_nombres(request):
    if request.method== 'POST':
        form= Formulario(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_nombre = Mujeres()
            nuevo_nombre.save()
           
    form= Formulario()
    return render(request, 'personas/formulario.html', {'form': form })



def busqueda_nombre(request):
    
    nombres_buscados = []
    dato = request.GET.get('partial_nombre', None)

    if dato is not None:
        nombres_buscados = Mujeres.objects.filter(nombre__icontains=dato)
   
    buscador = BusquedaNombre
    ()
    return render(
        request, "personas/busqueda.html",
        {'buscador': buscador, 'nombres_buscados': nombres_buscados, 'dato': dato})