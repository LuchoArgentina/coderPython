from django.shortcuts import render
from .models import Mensajes
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def listaMensajes(request):
    mensajes = Mensajes.objects.get(id=id)
    
    data = {"fecha": mensajes.fecha, "cuerpo": mensajes.cuerpo, "emisor": mensajes.emisor, "leido": mensajes.leido}
    
    # if leido==False:
    #     mensajes ['leido']= "Leido"
    
    return render(request, "mensajesApp/listaMensajes.html", {"mensajes":data})

    
