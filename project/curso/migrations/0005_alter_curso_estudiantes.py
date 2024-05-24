# Generated by Django 5.0.4 on 2024-05-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_curso_profesor'),
        ('estudiante', '0003_estudiante_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, null=True, related_name='cursos', to='estudiante.estudiante'),
        ),
    ]