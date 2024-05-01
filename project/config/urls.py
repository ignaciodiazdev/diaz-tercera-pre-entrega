from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('estudiante/', include('estudiante.urls')),
    path('curso/', include('curso.urls')),
    path('profesor/', include('profesor.urls')),
]
