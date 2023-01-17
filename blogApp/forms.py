from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]
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