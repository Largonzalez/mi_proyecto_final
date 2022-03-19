from django.db import models

# Create your models here.

class Mujeres(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    mascota= models.BooleanField()
    club_futbol= models.CharField(max_length=50)


class Hombres(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    mascota= models.BooleanField()
    club_futbol= models.CharField(max_length=50)
