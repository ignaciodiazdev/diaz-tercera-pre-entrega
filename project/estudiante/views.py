from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from . import models, forms
# Create your views here.


def home(request):  # HOME
    return render(request, 'estudiante/index.html')


class EstudianteList(ListView):
    model = models.Estudiante

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Estudiante.objects.filter(
                Q(nombre__icontains=consulta) | Q(apellido__icontains=consulta))
        else:
            object_list = models.Estudiante.objects.all()

        return object_list


class EstudianteDetail(DetailView):
    model = models.Estudiante


class EstudianteCreate(CreateView):
    model = models.Estudiante
    form_class = forms.EstudianteForm
    success_url = reverse_lazy('estudiante:home')


class EstudianteUpdate(UpdateView):
    model = models.Estudiante
    form_class = forms.EstudianteForm
    success_url = reverse_lazy('estudiante:list')


class EstudianteDelete(DeleteView):
    model = models.Estudiante
    success_url = reverse_lazy('estudiante:list')
