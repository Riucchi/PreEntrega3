from django.urls import path
from .views import *


app_name = 'pre_entrega'

urlpatterns = [path('index/', buscar, name="index"),
               path('cursos/', curso_form, name="cursos"),
               path('profesores/', profesores_form, name="profesores"),
               path('estudiantes/', estudiantes_form, name="estudiantes"),
               path('entregables/', entregables_form , name="entregables"),
               path('subir-propiedad/',subir_propiedad, name="subir-propiedad"),
               path('ver-propiedad/<int:property_id>/', ver_propiedad, name='ver-propiedad')
               ]