
from operator import index
from django.urls import path
from . import views



urlpatterns = [
    path('', index, name= "index.urls"),
    path('formulario/', views.formulario_nombres, name='formulario'),
    path('busqueda/', views.busqueda_nombre, name="busqueda")
]
