#importamos un paquete de django
from django import forms

class NewDepartamentoForm(forms.Form):
    """Declarar formulario"""
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)



