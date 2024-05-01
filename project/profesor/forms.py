from django import forms
from . import models


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "especializacion": forms.TextInput(attrs={"class": "form-control"}),
            "correo_electronico": forms.EmailInput(attrs={"class": "form-control", "type": "email"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }
