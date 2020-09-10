from django.shortcuts import render
from django.views.generic import ListView
#importamos una vista generica del paquete "edit" que no esta vinculado a un modelo
from django.views.generic.edit import FormView

from applications.persona.models import Persona
from .models import Departamento
from .forms import NewDepartamentoForm



class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'
    


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        print('======estamos en el from valid======')
        """Creamos una instancia de Departamento"""
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Persona.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartamentoView, self).form_valid(form)


