from django.shortcuts import render
from django.http import HttpResponse
from .models import Posteos, Perfil, Avatar
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from blogApp.forms import RegistroUsuarioForm, ModificacionPerfilForm, CrearPerfilForm, crearPosteoForm, avatarForm
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
    posteo = Posteos.objects.get(id=1)
    dicc_posteo={"titulo":posteo.titulo,"subtitulo":posteo.subtitulo,"cuerpo":posteo.cuerpo,"nombreAutor":posteo.nombreAutor,"apellidoAutor":posteo.apellidoAutor,"fechaCreacion": posteo.fechaCreacion, "imagen":posteo.imagen}

    
    return render(request, "blogApp/microblading.html", {"posteoMicroblading":dicc_posteo})

def perfilado(request):
    posteo = Posteos.objects.get(id=2)
    dicc_posteo={"titulo":posteo.titulo,"subtitulo":posteo.subtitulo,"cuerpo":posteo.cuerpo,"nombreAutor":posteo.nombreAutor,"apellidoAutor":posteo.apellidoAutor,"fechaCreacion": posteo.fechaCreacion, "imagen":posteo.imagen}

    return render(request, "blogApp/perfilado.html", {"posteoPerfilado": dicc_posteo})


def labios(request):
    posteo = Posteos.objects.get(id=3)
    dicc_posteo={"titulo":posteo.titulo,"subtitulo":posteo.subtitulo,"cuerpo":posteo.cuerpo,"nombreAutor":posteo.nombreAutor,"apellidoAutor":posteo.apellidoAutor,"fechaCreacion": posteo.fechaCreacion, "imagen":posteo.imagen}

    return render(request, "blogApp/labios.html",  {"posteoLabios":dicc_posteo})


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
def leerPerfil(request):

    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/avatarVacio.png"

    try:
        user_id=request.user.pk
        perfil = Perfil.objects.get(user_id=user_id)
        data = {"ocupacion": perfil.ocupacion, "intereses": perfil.intereses}
        if data==None:
            return render(request, "blogApp/crearPerfil.html")
        else:
            return render(request, "blogApp/leerPerfil.html", {"perfil":data, "avatar":avatar})
    except Perfil.DoesNotExist:
        form= CrearPerfilForm()
        return render(request, "blogApp/crearPerfil.html", {"form":form, "avatar": avatar})
        


@login_required
def editarPerfil(request):
    usuario=request.user
    user_id=request.user.pk
    perfil = Perfil.objects.get(user_id=user_id)
    data = {"ocupacion": perfil.ocupacion, "intereses": perfil.intereses}
    form= ModificacionPerfilForm(initial={"ocupacion":perfil.ocupacion,"intereses":perfil.intereses})
    

    if request.method=="POST":
        form=ModificacionPerfilForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            perfil.ocupacion=info["ocupacion"]
            perfil.intereses=info["intereses"]
            perfil.save()
            return render(request, "blogApp/index.html",{"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "blogApp/editarPerfil.html", {"form":form, "mensaje": "No se pudo editar el perfil"})
    else:
        form= ModificacionPerfilForm(initial={"ocupacion":perfil.ocupacion,"intereses":perfil.intereses})
        return render(request, "blogApp/editarPerfil.html",{"form":form})


@login_required
def crearPerfil(request):
    usuario=request.user
    user_id=request.user.pk
    if request.method=="POST":
        form=CrearPerfilForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user_id_forening=user_id
            ocupacion = info["ocupacion"]
            intereses = info["intereses"]
            perfil = Perfil(user_id=user_id_forening,ocupacion=ocupacion,intereses=intereses)
            perfil.save()
            return render(request, "blogApp/index.html",{"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "blogApp/crearPerfil.html", {"form":form, "mensaje": "No se pudo editar el perfil"})
    else:
        form= CrearPerfilForm()
        return render(request, "blogApp/crearPerfil.html",{"form":form})



@login_required
def agregarAvatar(request):
    if request.method=="POST":
        
        miFormulario=avatarForm(request.POST, request.FILES)
        
        if miFormulario.is_valid():
            
            u = User.objects.get(username=request.user)

            avatar= Avatar(user= u, imagen=miFormulario.cleaned_data["imagen"])

            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                 avatarViejo[0].delete()
            avatar.save()
            return render(request, "blogApp/index.html", {"mensaje":"Avatar modificado correctamente"})
        else:
            return render(request, "blogApp/leerPerfil.html", {"mensaje":"No es posible modificar el avatar"})
    else:
        miFormulario=avatarForm()
        return render(request, "blogApp/agregarAvatar.html", {"form":miFormulario})


@login_required
def crearPosteo(request):
    if request.method=="POST":
        form= crearPosteoForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            titulo=info["titulo"]
            subtitulo=info["subtitulo"]
            cuerpo=info["cuerpo"]
            nombreAutor=info["nombreAutor"]
            apellidoAutor=info["apellidoAutor"]
            fechaCreacion=info["fechaCreacion"]
            imagen=info["imagen"]
            posteo= Posteos(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,nombreAutor=nombreAutor,apellidoAutor=apellidoAutor,fechaCreacion=fechaCreacion, imagen=imagen)
            posteo.save()
            return render(request, "blogApp/index.html", {"mensaje":"Posteo creado exitosamente"})
        else:
                return render(request, "blogApp/crearPosteo.html", {"form":form, "mensaje": "No se pudo crear el posteo"})
    else:
        form= crearPosteoForm()
        return render(request, "blogApp/crearPosteo.html", {"form":form})

@login_required
def listaEditarPosteo(request):
    posteos = Posteos.objects.all()
    return render(request, "blogApp/listaEditarPosteo.html", {"posteos":posteos})




@login_required
def editarPosteo(request, id):
    posteo= Posteos.objects.get(id=id) 
   
    

    if request.method=="POST":
        form= crearPosteoForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            posteo.titulo=info["titulo"]
            posteo.subtitulo=info["subtitulo"]
            posteo.cuerpo=info["cuerpo"]
            posteo.nombreAutor=info["nombreAutor"]
            posteo.apellidoAutor=info["apellidoAutor"]
            posteo.fechaCreacion=info["fechaCreacion"]
            posteo.imagen=info["imagen"]
            posteo.save()
            
            return render(request, "blogApp/index.html", {"mensaje":"Posteo modificado exitosamente"})
        else:
            info=form.cleaned_data
            posteo.titulo=info["titulo"]
            posteo.subtitulo=info["subtitulo"]
            posteo.cuerpo=info["cuerpo"]
            posteo.nombreAutor=info["nombreAutor"]
            posteo.apellidoAutor=info["apellidoAutor"]
            posteo.fechaCreacion=info["fechaCreacion"]
            posteo.save()
            return render(request, "blogApp/index.html", {"form":form, "mensaje": "Posteo modificado exitosamente"})
    else:
        form= crearPosteoForm(initial={"titulo":posteo.titulo,"subtitulo":posteo.subtitulo,"cuerpo":posteo.cuerpo,"nombreAutor":posteo.nombreAutor,"apellidoAutor":posteo.apellidoAutor,"fechaCreacion": posteo.fechaCreacion, "imagen":posteo.imagen})
        return render(request, "blogApp/EditarPosteo.html", {"form":form,"posteo":posteo})


def eliminarPosteo(request, id): 
    posteo=Posteos.objects.get(id=id)
    posteo.delete()
    return render(request, "blogApp/index.html", {"mensaje":"Posteo eliminado correctamente"})



