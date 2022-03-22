from unittest.util import _MAX_LENGTH
from django import forms

class Formulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=30)
    club_futbol= forms.BooleanField(required=False)

class BusquedaNombre(forms.Form):
    partial_nombre =forms.CharField(label='Buscador',max_length=30)
