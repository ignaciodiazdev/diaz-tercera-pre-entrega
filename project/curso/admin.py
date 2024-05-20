from django.contrib import admin
from . import models
# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "fecha_inicio",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("id",)
    date_hierarchy = "fecha_inicio"


admin.site.register(models.Curso, CursoAdmin)
