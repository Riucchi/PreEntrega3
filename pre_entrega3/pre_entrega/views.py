from django.shortcuts import render
from pre_entrega.models import Cursos
from pre_entrega.forms import FormCursos, FormEntregables, FormEstudiantes, FormProfesores, Buscar
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def curso_form(request):
    formulario = FormCursos(request.POST)
    if formulario.is_valid():
        formulario.save()
        formulario = FormCursos()
        
        context = {'form': formulario }
        return render(request, 'pre_entrega/Cursos.html' ,context)
    else:
        form = FormCursos()
        return render(request, 'pre_entrega/Cursos.html', {'form':form})
    
@login_required
def profesores_form(request):
    formulario = FormProfesores(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FormProfesores()
        
        context = {'form': formulario }
        return render(request, 'pre_entrega/Profesores.html' ,context)
    else:
        form = FormProfesores()
        return render(request, 'pre_entrega/Profesores.html', {'form':form})
    
@login_required
def entregables_form(request):
    formulario = FormEntregables(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FormEntregables()
        
        context = {'form': formulario }
        return render(request, 'pre_entrega/Entregables.html' ,context)
    else:
        form = FormEntregables()
        return render(request, 'pre_entrega/Entregables.html', {'form':form})
    
@login_required
def estudiantes_form(request):
    formulario = FormEstudiantes(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FormEstudiantes()
        
        context = {'form': formulario }
        return render(request, 'pre_entrega/Estudiantes.html' ,context)
    else:
        form = FormEstudiantes()
        return render(request, 'pre_entrega/Estudiantes.html', {'form': form})
    


def buscar(request):
    if request.method == 'POST':
        formulario = Buscar(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Cursos.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "pre_entrega/index.html", {"cursos": curso})
    else:
        formulario = Buscar()
        return render(request, "pre_entrega/index.html", {"formulario": formulario})