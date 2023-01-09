from django.urls import path
from .views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("acercaDeMi/", acercaDeMi, name="acercaDeMi"),
    path("contacto/", contacto, name="contacto"),
    path("posteos/", posteos, name="posteos"),
    path("microblading/", microblading, name="microblading"),
    path("perfilado/", perfilado, name="perfilado"),
    path("labios/", labios, name="labios"),
    

]