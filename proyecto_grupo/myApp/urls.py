from django.forms import forms
from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.EmpleadosListView.as_view(), name='empleadosListView'),
    path('empleados/<int:pk>/', views.EmpleadosDetailView.as_view(), name='empleadosDetailView'),
    path('empleados/registro/', views.showEmpleadoForm, name='registroEmpleado'),
    path('empleados/registrar/',views.postEmpleadoForm, name='registrarEmpleado'),
    path('proyectos/', views.ProyectosListView.as_view(), name='proyectosListView'),
    path('proyectos/<int:pk>/', views.ProyectosDetailView.as_view(), name='proyectosDetailView'),
    path('tareas/', views.TareasListView.as_view(), name='tareasListView'),
    path('tareas/<int:pk>/', views.TareasDetailView.as_view(), name='tareasDetailView'),
    path('clientes/', views.ClientesListView.as_view(), name='clientesListView'),
    path('clientes/<int:pk>/', views.ClientesDetailView.as_view(), name='clientesDetailView'),
    path('',views.showInicio, name='index')
]
