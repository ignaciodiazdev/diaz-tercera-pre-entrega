from django.urls import path
from . import views

app_name = 'profesor'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.profesor_list, name='list'),
    path('create/', views.profesor_create, name='create'),
]
