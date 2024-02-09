from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

class Profesores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()


