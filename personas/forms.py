from unittest.util import _MAX_LENGTH
from django import forms
from ckeditor.fields import RichTextFormField


#Personajes

class CrearPersonajes(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    sexo = forms.CharField(max_length=30)
    club_futbol = forms.BooleanField(required=False)
    
class BusquedaPersonajes(forms.Form):
    nombre = forms.CharField(max_length=20)

#Mascotas

class CrearMascotas(forms.Form):
    animal = forms.CharField(max_length=20)
    tamaño = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    
class BusquedaMascotas(forms.Form):
    animal = forms.CharField(max_length=20)

#Viajes

class CrearViajes(forms.Form):
    destino = forms.CharField(max_length=20)
    transporte = forms.CharField(max_length=30)
    duracion = forms.CharField(max_length=30)
    descripcion_viaje= RichTextFormField (required=False)

class BusquedaViajes(forms.Form):
    destino = forms.CharField(max_length=20)