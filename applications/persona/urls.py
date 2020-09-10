from django.contrib import admin
from django.urls import path

from . import views
app_name = "persona_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(), 
        name='Inicio'
    ),

    path(
        'listar-todo-empleados/',
        views.LsitAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'listar-by-area/<shortname>/', 
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),
    path(
        'lista-empleados-admin/', 
        views.LsitaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('buscar-empleado/', views.ListEpleadosByKword.as_view()),
    path('lista-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'success/',
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
    ),
]