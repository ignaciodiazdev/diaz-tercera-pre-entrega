from django.contrib import admin
from . import models
# Register your models here.


class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "especializacion",
        "correo_electronico",
    )
    list_display_links = ("nombre", "apellido")
    search_fields = ("nombre", "apellido")
    ordering = ("nombre", "apellido")


admin.site.register(models.Profesor, ProfesorAdmin)
