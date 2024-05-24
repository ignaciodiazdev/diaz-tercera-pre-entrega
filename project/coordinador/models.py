from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Coordinador(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="coordinador")
    telefono = models.CharField(max_length=10)
    imagen = models.ImageField(
        upload_to='coordinadores', null=True, blank=True)

    def __str__(self):
        return self.usuario.username
