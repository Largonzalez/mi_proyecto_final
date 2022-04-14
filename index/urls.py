from operator import index
from django.urls import path 
from .views import index, plantilla, login, registrar, editar

# from django.urls import path
# from .views import inicio, otro_vista, numero_random, numero_del_usuario, mi_plantilla, 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name= "index"),
    path('plantilla/', plantilla, name='plantilla'),
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('editar/', editar, name='editar'),
    path('logout/', LogoutView.as_view(template_name='indice/logout.html'), name='logout')
]



# from django.urls import path
# from .views import index, plantilla, login, registrar, editar
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('', index, name="inicio"),
#     path('plantilla/', plantilla, name="plantilla"),
#     path('login/', login, name='login'),
#     path('registrar/', registrar, name='registrar'),
#     path('editar/', editar, name='editar'),
#     path('logout/', LogoutView.as_view(template_name='indice/logout.html'), name='logout'),
# ]