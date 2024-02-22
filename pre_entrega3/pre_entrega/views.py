from django.shortcuts import render, redirect
from pre_entrega.models import Cursos, Property, Image
from pre_entrega.forms import FormCursos, FormEntregables, FormEstudiantes, FormProfesores, Buscar, PropertyForm, ImageForm
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
    
    
def ver_propiedad(request, property_id):
    property_instance = Image.objects.get(pk=property_id)
    print(property_instance)
    return render(request, 'pre_entrega/propiedad.html', {'property': property_instance})




def subir_propiedad(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if property_form.is_valid() and image_form.is_valid():
            property_instance = property_form.save()
            for image in request.FILES.getlist('image'):
                Image.objects.create(property=property_instance, image=image)
                return redirect('propiedad.html', property_id=property_instance.id)
    else:
        property_form = PropertyForm()
        image_form = ImageForm()
    return render(request, 'pre_entrega/subirpropiedad.html', {'property_form': property_form, 'image_form': image_form})