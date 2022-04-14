from django.shortcuts import render

from personas.models import Personajes, Mascotas, Viajes

from . forms import BusquedaMascotas, BusquedaPersonajes, BusquedaViajes, CrearMascotas, CrearPersonajes, CrearViajes
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#Class Personajes

def crear_personajes(request):
    if request.method== 'POST':
        form= CrearPersonajes(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_personaje = Personajes()
            nuevo_personaje.save()
           
    form= CrearPersonajes()
    return render(request, 'personajes/crear_personajes.html', {'form': form })


def lista_personajes(request):
    
    personaje_a_buscar = request.GET.get('personaje', None)
    
    if personaje_a_buscar is not None:
        personajes = Personajes.objects.filter(personajes__icontains=personaje_a_buscar)
    else:
        personajes = Personajes.objects.all()
        
    form = BusquedaPersonajes()
    return render(request, "personajes/lista_personajes.html", {'form': form, 'personajes': personajes})

class DetallePersonajes(DetailView):
    model = Personajes
    template_name = "personajes/detalle_personajes.html"


class EditarPersonajes(LoginRequiredMixin, UpdateView):
    model = Personajes
    success_url = '/personas/personajes/'
    fields = ['nombre', 'apellido', 'sexo', 'club_futbol']

class BorrarPesonajes(LoginRequiredMixin, DeleteView):
    model = Personajes
    success_url = '/personas/personajes/'


#Class Mascotas

def crear_mascotas(request):
    if request.method== 'POST':
        form= CrearMascotas(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_mascota = Mascotas()
            nuevo_mascota.save()
           
    form= CrearMascotas()
    return render(request, 'mascotas/crear_mascotas.html', {'form': form })


def lista_mascotas(request):
    
    mascota_a_buscar = request.GET.get('mascotas', None)
    
    if mascota_a_buscar is not None:
        mascotas = Mascotas.objects.filter(mascotas__icontains=mascota_a_buscar)
    else:
        mascotas = Mascotas.objects.all()
        
    form = BusquedaMascotas()
    return render(request, "mascotas/lista_mascotas.html", {'form': form, 'mascotas': mascotas})

class DetalleMascotas(DetailView):
    model = Mascotas
    template_name = "mascotas/detalle_mascotas.html"


class EditarMascotas(LoginRequiredMixin, UpdateView):
    model = Mascotas
    success_url = '/personas/mascotas/'
    fields = ['animal', 'tamaño', 'color']

class BorrarMascotas(LoginRequiredMixin, DeleteView):
    model = Mascotas
    success_url = '/personas/mascotas/'

#Class Viajes

def crear_viajes(request):
    if request.method== 'POST':
        form= CrearViajes(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_viajes = Viajes()
            nuevo_viajes.save()
           
    form= CrearViajes()
    return render(request, 'viajes/crear_viajes.html', {'form': form })


def lista_viajes(request):
    
    viaje_a_buscar = request.GET.get('viajes', None)
    
    if viaje_a_buscar is not None:
        viajes = Viajes.objects.filter(viajes__icontains=viaje_a_buscar)
    else:
        viajes = Viajes.objects.all()
        
    form = BusquedaViajes()
    return render(request, "viajes/lista_viajes.html", {'form': form, 'viajes': viajes})

class DetalleViajes(DetailView):
    model = Viajes
    template_name = "viajes/detalle_viajes.html"


class EditarViajes(LoginRequiredMixin, UpdateView):
    model = Viajes
    success_url = '/personas/viajes/'
    fields = ['destino', 'transporte', 'duración']

class BorrarViajes(LoginRequiredMixin, DeleteView):
    model = Viajes
    success_url = '/personas/viajes/'