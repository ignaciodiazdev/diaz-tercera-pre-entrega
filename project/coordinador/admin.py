from django.contrib import admin
from . import models
# Register your models here.


class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'usuario', 'telefono', 'imagen')
    search_fields = ('usuario__username', 'usuario__first_name',
                     'usuario__last_name', 'telefono')
    list_filter = ('usuario__is_active', 'usuario__date_joined')
    # list_display_links = ("usuario__first_name",)
    # search_fields = ("usuario__first_name",)
    # ordering = ("id",)

    def nombre_usuario(self, obj):
        return obj.usuario.first_name + " " + obj.usuario.last_name


admin.site.register(models.Coordinador, CoordinadorAdmin)
