from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    TemplateView,
    UpdateView,
    DeleteView,
)
# importamos el modelos de Bd empleados
from .models import Persona

class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


class LsitAllEmpleados(ListView):
    """Listar todos los empleados de una empresa"""
    template_name = 'persona/lista_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'persona'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Persona.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class LsitaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'persona'
    model = Persona


class ListByAreaEmpleado(ListView):
    """Lista Empleados de un area"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        """escribir mi codigo"""
        area = self.kwargs['shortname']
        lista = Persona.objects.filter(
            departamento__shor_name=area
        )
        return lista


class ListEpleadosByKword(ListView):
    """Lista de empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*******************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Persona.objects.filter(
            first_name=palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        persona = Persona.objects.get(id=5)
        return persona.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = 'persona/detail_empleado.html'
       
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del Mes'
        return context
        

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Persona
    fields = [
        'first_name', 
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        """Logica del Proceso"""
        persona = form.save(commit=False)
        persona.full_name = persona.first_name + ' ' + persona.last_name
        persona.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Persona
    fields = [
        'first_name', 
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**********METODO POST**********')
        print('====================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """Logica del Proceso"""
        print('**********METODO form valid**********')
        print('********************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = 'persona/delete.html'
    model = Persona
    success_url = reverse_lazy('persona_app:empleados_admin')

        




