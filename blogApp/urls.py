from django.urls import path
from .views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("acercaDeMi/", acercaDeMi, name="acercaDeMi"),
    path("contacto/", contacto, name="contacto"),
    path("posteos/", posteos, name="posteos"),
    

]