from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from . import models, forms
# Create your views here.


def home(request):  # HOME
    return render(request, 'curso/index.html')


class CursoList(ListView):
    model = models.Curso

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Curso.objects.filter(
                nombre__icontains=consulta)
        else:
            object_list = models.Curso.objects.all()

        return object_list


class CursoDetail(DetailView):
    model = models.Curso


class CursoCreate(CreateView):
    model = models.Curso
    form_class = forms.CursoForm
    success_url = reverse_lazy('curso:home')


class CursoUpdate(UpdateView):
    model = models.Curso
    form_class = forms.CursoForm
    success_url = reverse_lazy('curso:list')


class CursoDelete(DeleteView):
    model = models.Curso
    success_url = reverse_lazy('curso:list')
