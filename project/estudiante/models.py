from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
