from django.urls import path
from . import views

app_name = "estudiante"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.estudiante_create, name="create"),
    path("list/", views.estudiante_list, name="list"),
]
