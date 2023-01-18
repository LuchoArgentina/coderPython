from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posteos(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to="posteos", null=True, blank=True)
    cuerpo=models.CharField(max_length=500)
    nombreAutor=models.CharField(max_length=50)
    apellidoAutor=models.CharField(max_length=50)
    fechaCreacion=models.DateField(null=True)

    def __str__(self):
        return f"{self.titulo} | {self.subtitulo} | {self.nombreAutor} , {self.apellidoAutor} " 

class Perfil(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE )
    ocupacion=models.CharField(max_length=50)
    intereses=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.user} | {self.ocupacion} "               

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE )
    imagen=models.ImageField(upload_to="avatars", null=True, blank=True)

    def __str__(self):
       return f"{self.user} | {self.imagen} "  