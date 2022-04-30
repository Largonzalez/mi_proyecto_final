
from django.shortcuts import render, redirect

from .models import Personajes, Mascotas, Viajes

from . import forms
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


# Create your views here.

#Class Personajes

@login_required
def crear_personajes(request):
    if request.method== 'POST':
        form= forms.CrearPersonajes(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_personaje = Personajes(nombre=data['nombre'], apellido= data['apellido'], sexo= data['sexo'], club_futbol=data['club_futbol'])
            nuevo_personaje.save()
           
    form= forms.CrearPersonajes()
    return render(request, 'personajes/crear_personajes.html', {'form': form })

def lista_personajes(request):
    
    personaje_a_buscar = request.GET.get('personaje', None)
    
    if personaje_a_buscar is not None:
        personajes = Personajes.objects.filter(personajes__icontains=personaje_a_buscar)
    else:
        personajes = Personajes.objects.all()
        
    form = forms.BusquedaPersonajes()
    return render(request, "personajes/lista_personajes.html", {'form': form, 'personajes': personajes})

# class ListaPersonajes (ListView):
#     model= Personajes
#     template_name= 'personajes/lista_personajes.html'

class DetallePersonajes(LoginRequiredMixin, DetailView):
    model = Personajes
    template_name = "personajes/detalle_personajes.html"

class EditarPersonajes(LoginRequiredMixin, UpdateView):
    model = Personajes
    template_name= 'personajes/personajes_confirm_delete.html'
    success_url = '/personas/personajes/'
    fields = ['nombre', 'apellido', 'sexo', 'club_futbol']


class BorrarPesonajes(LoginRequiredMixin, DeleteView):
    model = Personajes
    template_name= 'personajes/personajes_form.html'
    success_url = '/personas/personajes/'


#Class Mascotas

def crear_mascotas(request):
    if request.method== 'POST':
        form= forms.CrearMascotas(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_mascota = Mascotas(
                animal= data['animal'],
                tamaño= data ['tamaño'], 
                color= data ['color']
            )
            nuevo_mascota.save()
            return redirect('mascotas/lista_mascotas.html')
           
    form= forms.CrearMascotas()
    return render(request, 'mascotas/crear_mascotas.html', {'form': form })


def lista_mascotas(request):
    
    mascota_a_buscar = []
    dato = request.GET.get('partial_animal', None)
    
    if dato is not None:
        mascotas = Mascotas.objects.filter(mascota__icontains=dato)
    else:
        mascotas = Mascotas.objects.all()
    
    form = forms.BusquedaMascotas()
    return render(request, "mascotas/lista_mascotas.html", {'form': form, 'mascotas': mascotas})



class DetalleMascotas(DetailView):
    model = Mascotas
    template_name = "mascotas/detalle_mascotas.html"
    success_url = '/personas/mascotas/'



class EditarMascotas(LoginRequiredMixin, UpdateView):
    model = Mascotas
    success_url = '/personas/mascotas/'
    template_name = 'mascotas/mascotas_confirm_delete.html'
    fields = ['animal', 'tamaño', 'color']


class BorrarMascotas(LoginRequiredMixin, DeleteView):
    model = Mascotas
    template_name = '/mascotas/mascotas_form.html'
    success_url = '/personas/mascotas/'


#Class Viajes

def crear_viajes(request):
    if request.method== 'POST':
        form= forms.CrearViajes(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_viajes = Viajes(
                destino= data['destino'],
                transporte=data['transporte'],
                duracion=data['duracion'],
                descripcion_viaje=data['descripcion_viaje'],
                
            )
            nuevo_viajes.save()
           
    form= forms.CrearViajes()
    return render(request, 'viajes/lista_viajes.html', {'form': form })


def lista_viajes(request):
    
    viaje_a_buscar = request.GET.get('viajes', None)
    
    if viaje_a_buscar is not None:
        viajes = Viajes.objects.filter(viajes__icontains=viaje_a_buscar)
    else:
        viajes = Viajes.objects.all()
        
    form = forms.BusquedaViajes()
    return render(request, "viajes/lista_viajes.html", {'form': form, 'viajes': viajes})

class DetalleViajes(DetailView):
    model = Viajes
    template_name = "viajes/detalle_viajes.html"


class EditarViajes(LoginRequiredMixin, UpdateView):
    model = Viajes
    success_url = '/personas/viajes/'
    template_name= 'viajes/viajes_confirm_delete.html'
    fields = ['destino', 'transporte', 'duración', 'descripcion_viaje', 'fecha_creacion']


class BorrarViajes(LoginRequiredMixin, DeleteView):
    model = Viajes
    template_name= 'viajes/viajes_form.html'
    success_url = '/personas/viajes/'