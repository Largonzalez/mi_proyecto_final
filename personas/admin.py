from django.contrib import admin

from personas.models import  Mascotas, Personajes, Vacaciones

# Register your models here.

admin.site.register(Personajes)
admin.site.register(Vacaciones)
admin.site.register(Mascotas)

