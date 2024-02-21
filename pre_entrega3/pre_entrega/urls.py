from django.urls import path
from pre_entrega.views import buscar, curso_form , estudiantes_form , profesores_form , entregables_form 


app_name = 'pre_entrega'

urlpatterns = [path('index/', buscar, name="index"),
               path('cursos/', curso_form, name="cursos"),
               path('profesores/', profesores_form, name="profesores"),
               path('estudiantes/', estudiantes_form, name="estudiantes"),
               path('entregables/', entregables_form , name="entregables"),
               ]