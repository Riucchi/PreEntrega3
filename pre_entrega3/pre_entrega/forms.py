from django import forms 
from pre_entrega.models import Estudiantes, Cursos, Entregables, Profesores

class FormEstudiantes(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = "__all__"

class FormCursos(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = "__all__"

class FormEntregables(forms.ModelForm):
    class Meta:
        model = Entregables
        fields = "__all__"

class FormProfesores(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = "__all__"

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)