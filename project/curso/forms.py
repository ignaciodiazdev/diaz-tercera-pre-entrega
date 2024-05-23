from django import forms
from . import models


class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "style": "height: 60px; resize: none;"}),
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
