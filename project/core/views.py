from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import CustomAuthenticationForm, CustomUserCreationForm
# Create your views here.


def home(request):
    return render(request, 'core/index.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})
