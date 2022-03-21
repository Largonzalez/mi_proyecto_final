from unittest.util import _MAX_LENGTH
from django import forms

class Formulario(forms.Form):
    Nombre= forms.CharField(max_length=20)
    Apellido= forms.IntegerField()

class BusquedaNombre(forms.Form):
    partial_nombre =forms.CharField(label='Buscador',max_length=30)
