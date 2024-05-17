from django.urls import path
from . import views

app_name = "curso"

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.CursoList.as_view(), name="list"),
    path("detail/<int:pk>", views.CursoDetail.as_view(), name="detail"),
    path("create/", views.CursoCreate.as_view(), name="create"),
    path("update/<int:pk>", views.CursoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.CursoDelete.as_view(), name="delete"),
]
