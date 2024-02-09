from django.contrib import admin
from pre_entrega.models import Profesores, Estudiantes, Cursos, Entregables

# Register your models here.

admin.site.register(Profesores)

admin.site.register(Estudiantes)

admin.site.register(Cursos)

admin.site.register(Entregables)