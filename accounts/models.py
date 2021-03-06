from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserExtension(models.Model):
    avatar = models.ImageField(upload_to='avatar',blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    more_description = models.CharField(max_length=100)