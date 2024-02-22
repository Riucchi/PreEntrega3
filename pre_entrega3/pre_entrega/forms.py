from django import forms 
from pre_entrega.models import Estudiantes, Cursos, Entregables, Profesores, Property, Image

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



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['m2', 'rooms', 'bathrooms']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ['image']