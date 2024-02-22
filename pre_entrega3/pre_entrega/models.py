from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Profesores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

class Property(models.Model):
    m2 = models.IntegerField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()

class Image(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')