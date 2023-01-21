from django.urls import path
from .views import *



urlpatterns = [
    path("listaMensajes/", listaMensajes, name="listaMensajes"),
    path("enviarMensaje/", enviarMensaje, name="enviarMensaje"),
    

]