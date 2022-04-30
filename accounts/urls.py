from operator import index
from django.urls import path 
from .views import index, login, registrar, editar, about
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('', index, name= "index"),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('editar/', editar, name='editar'),
    path('logout/', LogoutView.as_view(template_name='index/logout.html'), name='logout')
]


