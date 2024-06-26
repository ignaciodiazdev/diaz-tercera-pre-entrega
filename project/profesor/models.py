from django.db import models

# Create your models here.


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    especializacion = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='profesores/', null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
