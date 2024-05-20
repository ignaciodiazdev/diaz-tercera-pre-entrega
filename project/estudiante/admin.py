from django.contrib import admin
from . import models
# Register your models here.


class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "email",
        "telefono",
        "fecha_registro",
    )
    list_display_links = ("nombre", "apellido")
    search_fields = ("nombre", "apellido")
    ordering = ("nombre", "apellido")
    date_hierarchy = "fecha_registro"


admin.site.register(models.Estudiante, EstudianteAdmin)
