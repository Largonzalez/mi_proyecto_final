
from django.shortcuts import render, redirect

from .models import Personajes, Mascotas, Vacaciones

from . import forms
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


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
    
    personaje_a_buscar = request.GET.get('partial_personaje', None)
    
    if personaje_a_buscar is not None:
        personajes = Personajes.objects.filter(personaje__icontains=personaje_a_buscar)
    else:
        personajes = Personajes.objects.all()
        
    form = forms.BusquedaPersonajes()
    return render(request, "personajes/lista_personajes.html", {'form': form, 'personajes': personajes})


class DetallePersonajes(LoginRequiredMixin, DetailView):
    model = Personajes
    template_name = "personajes/detalle_personajes.html"


class EditarPersonajes(LoginRequiredMixin, UpdateView):
    model = Personajes
    template_name=  'personajes/personajes_form.html'
    success_url = '/personas/personajes/'
    fields = ['nombre', 'apellido', 'sexo', 'club_futbol']


class BorrarPesonajes(LoginRequiredMixin, DeleteView):
    model = Personajes
    template_name='personajes/personajes_confirm_delete.html'
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
            return redirect('mascotas/crear_mascotas.html', {'form': form, 'msj': 'Se creó la mascota con éxito!'})
           
    form= forms.CrearMascotas()
    return render(request, 'mascotas/crear_mascotas.html', {'form': form, 'msj': 'Se creó la mascota con éxito!'})


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
    # template_name = '/mascotas/mascotas_form.html'
    success_url = '/personas/mascotas/'
    fields = ['animal', 'tamaño', 'color']


class BorrarMascotas(LoginRequiredMixin, DeleteView):
    model = Mascotas
    # template_name = 'mascotas/mascotas_confirm_delete.html'
    success_url = '/personas/mascotas/'


#Class Vacaciones

def crear_vacaciones(request):
    if request.method== 'POST':
        form= forms.CrearVacaciones(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            nuevo_vacaciones = Vacaciones(
                destino= data['destino'],
                transporte=data['transporte'],
                duracion=data['duracion'],
                descripcion_viaje=data['descripcion_viaje']  
            )
            
            nuevo_vacaciones.save()

            return redirect (request, 'vacacionesl/ista_vacaciones.html')
           
    form= forms.CrearVacaciones()
    return render(request, 'vacaciones/lista_vacaciones.html', {'form': form })


def lista_vacaciones(request):
    
    vacaciones_a_buscar = request.GET.get('partial_destino', None)
    
    if vacaciones_a_buscar is not None:
        vacaciones = Vacaciones.objects.filter(destino__icontains=vacaciones_a_buscar)
    else:
        vacaciones = Vacaciones.objects.all()
        
    form = forms.BusquedaVacaciones()
    return render(request, "vacaciones/lista_vacaciones.html", {'form': form, 'vacaciones': vacaciones})

class DetalleVacaciones(DetailView):
    model = Vacaciones
    template_name = "vacaciones/detalle_vacaciones.html"


class EditarVacaciones(LoginRequiredMixin, UpdateView):
    model = Vacaciones
    success_url = '/personas/vacaciones/'
    template_name= 'vacaciones/vacaciones_form.html'
    fields = ['destino', 'transporte', 'duración', 'descripcion_vacaciones', 'fecha_creacion']


class BorrarVacaciones(LoginRequiredMixin, DeleteView):
    model = Vacaciones
    template_name= 'vacaciones/vacaciones_confirm_delete.html'
    success_url = '/personas/vacaciones/'