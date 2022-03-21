from django.contrib import admin

from personas.models import  Hombres, Mujeres

# Register your models here.

admin.site.register(Mujeres)
admin.site.register(Hombres)