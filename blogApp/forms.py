from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username","nombre","apellido","email","password1","password2"]
        help_texts={k:"" for k in fields}


class ModificacionUsuarioForm(UserCreationForm):
    email= forms.EmailField(label="Modificar Email")
    password1= forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    nombre= forms.CharField(label="Modificar Nombre", max_length=50)
    apellido= forms.CharField(label="Modificar Apellido", max_length=50)

    class Meta:
        model=User
        fields=["nombre","apellido","email","password1","password2"]
        help_texts={k:"" for k in fields}