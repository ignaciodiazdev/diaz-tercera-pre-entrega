from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.


def home(request):
    return render(request, 'curso/index.html')


def curso_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Curso.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Curso.objects.all()

    context = {"cursos": query}
    return render(request, "curso/curso_list.html", context)


def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("curso:home")
    else:
        form = forms.CursoForm()
    return render(request, "curso/curso_create.html", context={"form": form})
