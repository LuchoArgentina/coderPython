from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil, Avatar, Posteos

class RegistroUsuarioForm(UserCreationForm):
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        help_texts={k:"" for k in fields}



class ModificacionPerfilForm(forms.Form):
    
    ocupacion= forms.CharField(label="Ocupacion", max_length=50)
    intereses= forms.CharField(label="Tema de interes", max_length=200)

    class Meta:
        model=Perfil
        fields=["ocupacion","intereses"]
        help_texts={k:"" for k in fields}

class CrearPerfilForm(forms.Form):
    
    ocupacion= forms.CharField(label="Ocupacion", max_length=50)
    intereses= forms.CharField(label="Tema de interes", max_length=200)

    class Meta:
        model=User
        fields=["username","ocupacion","intereses"]
        help_texts={k:"" for k in fields}
        

class crearPosteoForm(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=30)
    cuerpo=forms.CharField(max_length=500)
    nombreAutor=forms.CharField(label="Nombre Autor",max_length=50)
    apellidoAutor=forms.CharField(label="Apellido Autor",max_length=50)
    fechaCreacion=forms.DateField(label="Fecha creacion")
    imagen=forms.ImageField(label="Imagen")

    class Meta:
        model=Posteos
        fields=["titulo","subtitulo","cuerpo","nombreAutor","apellidoAutor","fechaCreacion","imagen"]
        help_texts={k:"" for k in fields}


class avatarForm(forms.Form):
    imagen=forms.ImageField(label="Agregar avatar")