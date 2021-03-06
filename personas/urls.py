from django.urls import path

from . import views



urlpatterns = [
    path('mascotas/', views.lista_mascotas, name="mascotas"),
    path('mascotas/crear/', views.crear_mascotas, name="crear_mascotas"),
    path('mascotas/<int:pk>', views.DetalleMascotas.as_view(), name="detalle_mascotas"),
    path('mascotas/<int:pk>/editar', views.EditarMascotas.as_view(), name="editar_mascotas"),
    path('mascotas/<int:pk>/borrar', views.BorrarMascotas.as_view(), name="borrar_mascotas"),
    
    path('personajes/', views.lista_personajes, name="personajes"),
    path('personajes/crear/', views.crear_personajes, name="crear_personajes"),
    path('personajes/<int:pk>', views.DetallePersonajes.as_view(), name="detalle_personajes"),
    path('personajes/<int:pk>/editar', views.EditarPersonajes.as_view(), name="editar_personajes"),
    path('personajes/<int:pk>/borrar', views.BorrarPesonajes.as_view(), name="borrar_personajes"),

    path('vacaciones/', views.lista_vacaciones, name="vacaciones"),
    path('vacaciones/crear/', views.crear_vacaciones, name="crear_vacaciones"),
    path('vacaciones/<int:pk>', views.DetalleVacaciones.as_view(), name="detalle_vacaciones"),
    path('vacaciones/<int:pk>/editar', views.EditarVacaciones.as_view(), name="editar_vacaciones"),
    path('vacaciones/<int:pk>/borrar', views.BorrarVacaciones.as_view(), name="borrar_vacaciones"),
]
