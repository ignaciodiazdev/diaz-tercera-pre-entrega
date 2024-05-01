from django.shortcuts import render, redirect
from django.db.models import Q
from . import models, forms
# Create your views here.


def home(request):
    return render(request, "estudiante/index.html")


def estudiante_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Estudiante.objects.filter(
            Q(nombre__icontains=consulta) | Q(apellido__icontains=consulta))
    else:
        query = models.Estudiante.objects.all()

    context = {"estudiantes": query}
    return render(request, "estudiante/estudiante_list.html", context)


def estudiante_create(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("estudiante:home")
    else:
        form = forms.EstudianteForm()
    return render(request, "estudiante/estudiante_create.html", context={"form": form})
