from django.urls import path
from .views import editar_usuario, usuario_datos, crear_blog
from . import views

urlpatterns = [
    path("blog/", crear_blog ,name="blog"),
    path("editar/", editar_usuario, name="editar_usuario"),
    path("datos/", usuario_datos, name="usuario_datos"),
    path("blog/<int:pk>/", views.Detalleblog.as_view(),name="detalle_blog"),
    path("lista_blog/", views.lista_blog,name="lista_blog"),
    path("blog/editar/<int:pk>/", views.EditarBlog.as_view(),name="editar_blog"),
    path("blog/borrar/<int:pk>/", views.BorrarBlog.as_view(),name="borrar_blog"),
]