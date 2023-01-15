from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posteos(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30)
    imagen=models.ImageField()
    cuerpo=models.CharField(max_length=500)
    nombreAutor=models.CharField(max_length=50)
    apellidoAutor=models.CharField(max_length=50)
    fechaCreacion=models.DateField()

    def __str__(self):
        return f"{self.titulo} | {self.subtitulo} | {self.nombreAutor} , {self.apellidoAutor} " 

class Perfil(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE )
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=500)
    ocupacion=models.CharField(max_length=500)

    def __str__(self):
        return f"{self.nombre} | {self.apellido} | {self.ocupacion} "               

