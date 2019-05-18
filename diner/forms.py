from django import forms
from .models import *


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre',
            'apellido',
            'ci',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'ci': 'Cédula de Identidad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}, ),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'ci': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la cédula de identidad'}),
        }


class SolicitudPlatoForm(forms.ModelForm):
    class Meta:
        model = SolicitudPlato
        fields = [
            'fecha_sol',
            'estudiante',
            'plato',
        ]
        labels = {
            'fecha_sol': 'Fecha de solicitud',
            'estudiante': 'Estudiante',
            'plato': 'Plato',
        }
        widgets = {
            'fecha_sol': forms.DateInput(format=('%d-%m-%Y'),
                                         attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha'}),
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'plato': forms.Select(attrs={'class': 'form-control'}),
        }


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = [
            'nombre',
            'disp',
            'fecha_disp',
            'descrip'
        ]
        labels = {
            'nombre': 'Nombre',
            'disp': 'Cantidad disponible',
            'fecha_disp': 'Fecha de disponibilidad',
            'descrip': 'Descripción'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'disp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad disponible'}),
            'fecha_disp': forms.DateTimeInput(format='%d-%m-%Y',
                                              attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha'}),
            'descrip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción.'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña'})
        }
