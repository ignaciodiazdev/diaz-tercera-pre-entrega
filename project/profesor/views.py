from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from . import models, forms
# Create your views here.


def home(request):  # HOME
    return render(request, 'profesor/index.html')


class ProfesorList(ListView):
    model = models.Profesor

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Profesor.objects.filter(
                Q(nombre__icontains=consulta) | Q(apellido__icontains=consulta))
        else:
            object_list = models.Profesor.objects.all()

        return object_list


class ProfesorDetail(DetailView):
    model = models.Profesor


class ProfesorCreate(CreateView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url = reverse_lazy('profesor:home')


class ProfesorUpdate(UpdateView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url = reverse_lazy('profesor:list')


class ProfesorDelete(DeleteView):
    model = models.Profesor
    success_url = reverse_lazy('profesor:list')
