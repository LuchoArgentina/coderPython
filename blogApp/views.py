from django.shortcuts import render
from django.http import HttpResponse
from .models import Posteos
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from blogApp.forms import RegistroUsuarioForm, ModificacionUsuarioForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio(request):
    posteoMicroblading = Posteos.objects.get(id=1)
    posteoPerfilado = Posteos.objects.get(id=2)
    posteoLabios = Posteos.objects.get(id=3)
    return render(request, "blogApp/index.html", {"posteoMicroblading":posteoMicroblading,"posteoPerfilado": posteoPerfilado,"posteoLabios":posteoLabios})

def acercaDeMi(request):
    return render(request, "blogApp/acercaDeMi.html")


@login_required
def admin(request):
    return render(request, "blogApp/admin")

@login_required
def listaPosteos(request):
    posteos = Posteos.objects.all()
    return render(request, "blogApp/listaPosteos.html", {"posteos":posteos})

def microblading(request):
    posteoMicroblading = Posteos.objects.get(id=1)
    return render(request, "blogApp/microblading.html", {"posteoMicroblading":posteoMicroblading})

def perfilado(request):
    posteoPerfilado = Posteos.objects.get(id=2)
    return render(request, "blogApp/perfilado.html", {"posteoPerfilado": posteoPerfilado})


def labios(request):
    posteoLabios = Posteos.objects.get(id=3)
    return render(request, "blogApp/labios.html",  {"posteoLabios":posteoLabios})


def registerUser(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "blogApp/index.html",{"mensaje":f"Felicitaciones! Usuario {username} creado correctamente"})
        else:
            return render(request, "blogApp/registerUser.html",{"form":form, "mensaje":"Error al crear el usuario. Vuelva a internarlo."})
    else:
        form= RegistroUsuarioForm()
        return render(request, "blogApp/registerUser.html",{"form":form})


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, "blogApp/index.html", {"mensaje": f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "blogApp/login.html", {"form":form, "mensaje": "Datos incorrectos"})
        else:
            return render(request, "blogApp/login.html", {"form":form,"mensaje": "Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "blogApp/login.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=ModificacionUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.nombre=info["nombre"]
            usuario.apellido=info["apellido"]
            usuario.email=info["email"]
            usuario.password1=info["password1"]            
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "blogApp/index.html",{"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "blogApp/editarPerfil.html", {"form":form, "mensaje": "No se pudo editar el perfil"})
    else:
        form= ModificacionUsuarioForm(instance=usuario)
        return render(request, "blogApp/editarPerfil.html",{"form":form})

@login_required
def leerPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=ModificacionUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data

            return render(request, "blogApp/index.html",{"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "blogApp/leerPerfil.html", {"form":form, "mensaje": "No se pudo editar el perfil"})
    else:
        form= ModificacionUsuarioForm(instance=usuario)
        return render(request, "blogApp/leerPerfil.html",{"form":form})