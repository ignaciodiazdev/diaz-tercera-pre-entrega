from django.urls import path
from . import views

app_name = 'profesor'

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.ProfesorList.as_view(), name="list"),
    path("detail/<int:pk>", views.ProfesorDetail.as_view(), name="detail"),
    path("create/", views.ProfesorCreate.as_view(), name="create"),
    path("update/<int:pk>", views.ProfesorUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.ProfesorDelete.as_view(), name="delete"),
]
