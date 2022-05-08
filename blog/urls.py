from django.urls import path

from . import views


urlpatterns = [
    path("blog/", views.crear_blog ,name="blog"),
    path("editar/", views.editar_usuario, name="editar_usuario"),
    path("datos/", views.usuario_datos, name="usuario_datos"),
    path("blog/<int:pk>/", views.Detalleblog.as_view(),name="detalle_blog"),
    path("lista_blog/", views.lista_blog,name="lista_blog"),
    path("blog/editar/<int:pk>/", views.EditarBlog.as_view(),name="editar_blog"),
    path("blog/borrar/<int:pk>/", views.BorrarBlog.as_view(),name="borrar_blog"),
]