from django.shortcuts import render, redirect
from django.db.models import Q
from . import models, forms
# Create your views here.


def home(request):
    return render(request, 'profesor/index.html')


def profesor_list(request):
    consulta = request.GET.get('consulta', None)
    if consulta:
        print(consulta)
        query = models.Profesor.objects.filter(
            Q(nombre__icontains=consulta) | Q(apellido__icontains=consulta))
    else:
        query = models.Profesor.objects.all()

    context = {'profesores': query}
    return render(request, 'profesor/profesor_list.html', context)


def profesor_create(request):
    if request.method == 'POST':
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor:home")
    else:
        form = forms.ProfesorForm()

    context = {'form': form}
    return render(request, 'profesor/profesor_create.html', context)
