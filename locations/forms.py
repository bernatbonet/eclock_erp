from django import forms
from locations.models import Via, Pais, Provincia, Datos


class ViasForm(forms.ModelForm):
    class Meta:
        model = Via


class PaisesForm(forms.ModelForm):
    class Meta:
        model = Pais


class ProvinciasForm(forms.ModelForm):
    class Meta:
        model = Provincia


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Datos
