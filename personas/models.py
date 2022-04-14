from django.db import models

# Create your models here.

class Personajes (models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    sexo= models.CharField(max_length=20)
    club_futbol= models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre}- Apellido: {self.apellido} - Sexo: {self.sexo}"

class Mascotas(models.Model):
    animal: models.CharField(max_length=100)
    tamaño: models.CharField(max_length=25)
    color: models.CharField(max_length=20)


    def __str__(self):
        return f"Animal: {self.animal} -Tamaño: {self.tamaño} - Color: {self.color}"


class Viajes (models.Model):
    destino= models.CharField(max_length=40)
    transporte= models.CharField(max_length=40)
    duracion= models.CharField(max_length=30)

    def __str__(self):
        return f"Destino: {self.destino}- Transporte: {self.transporte} - Duración: {self.duracion}"