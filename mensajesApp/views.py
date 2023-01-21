from django.shortcuts import render
from .models import Mensajes
from django.contrib.auth.decorators import login_required
from mensajesApp.forms import crearMensajeForm



# Create your views here.

@login_required
def listaMensajes(request):
    user_id=request.user.pk #25
    mensajes = Mensajes.objects.filter(receptor_id=user_id)
    return render(request, "mensajesApp/listaMensajes.html", {"mensajes":mensajes})

    
@login_required
def enviarMensaje(request):
    user_id=request.user.pk
    if request.method=="POST":
        form= crearMensajeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            fecha=info["fecha"]
            cuerpo=info["cuerpo"]
            emisor_id=user_id
            receptor_id=info["receptor"]
        
            mensaje= Mensajes(fecha=fecha,cuerpo=cuerpo,receptor_id=receptor_id,emisor_id=emisor_id)
            mensaje.save()
            return render(request, "blogApp/index.html", {"mensaje":"Mensaje enviado exitosamente"})
        else:
                return render(request, "blogApp/enviarMensaje.html", {"form":form, "mensaje": "No se pudo crear el posteo"})
    else:
        form= crearMensajeForm()
        return render(request, "mensajesApp/enviarMensaje.html", {"form":form})



#  user_id=request.user.pk 
#     mensajes = Mensajes.objects.filter(receptor_id=user_id)
#     return render(request, "mensajesApp/enviarMensaje.html", {"mensajes":mensajes})
