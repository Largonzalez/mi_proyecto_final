from django.db import models

# Create your models here.

class Mujeres (models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    club_futbol= models.BooleanField()


class Hombres(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    club_futbol= models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre}- Apellido: {self.apellido}"

class Hobbies(models.Model):
    hobbie: models.CharField(max_length=100)

    def __str__(self):
        return f"Hobbie: {self.hobbie}"