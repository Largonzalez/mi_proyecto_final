from django.contrib import admin

from personas.models import  Mascotas, Personajes, Viajes

# Register your models here.

admin.site.register(Personajes)
admin.site.register(Viajes)
admin.site.register(Mascotas)

