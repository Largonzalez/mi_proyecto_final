from django.contrib import admin

from personas.models import  Hobbies, Hombres, Mujeres

# Register your models here.

admin.site.register(Mujeres)
admin.site.register(Hombres)
admin.site.register(Hobbies)
