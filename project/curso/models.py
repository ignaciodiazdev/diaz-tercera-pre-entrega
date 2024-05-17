from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
