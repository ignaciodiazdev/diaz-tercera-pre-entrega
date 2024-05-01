from django.urls import path
from . import views

app_name = "curso"

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.curso_list, name="list"),
    path("create/", views.curso_create, name="create"),
]
