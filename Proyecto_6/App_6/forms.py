from django import forms
from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['fechaInicio', 'fechaTermino',
                  'nombre', 'responsable', 'prioridad']

        widgets = {
            'fechaInicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fechaTermino': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridad': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control'}),
        }

        labels = {
            'fechaInicio': 'Fecha de Inicio',
            'fechaTermino': 'Fecha de Término',
            'nombre': 'Nombre del Proyecto',
            'responsable': 'Responsable del Proyecto',
            'prioridad': 'Prioridad del Proyecto',
        }
