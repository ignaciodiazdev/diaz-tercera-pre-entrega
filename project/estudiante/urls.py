from django.urls import path
from . import views

app_name = "estudiante"

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.EstudianteList.as_view(), name="list"),
    path("detail/<int:pk>", views.EstudianteDetail.as_view(), name="detail"),
    path("create/", views.EstudianteCreate.as_view(), name="create"),
    path("update/<int:pk>", views.EstudianteUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.EstudianteDelete.as_view(), name="delete"),
]
