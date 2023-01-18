from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("acercaDeMi/", acercaDeMi, name="acercaDeMi"),
    path("admin/", admin, name="admin"),    
    path("microblading/", microblading, name="microblading"),
    path("perfilado/", perfilado, name="perfilado"),
    path("labios/", labios, name="labios"),
    path("listaPosteos/", listaPosteos, name="listaPosteos"),
    path("registerUser/", registerUser, name="registerUser"),   
    path("login/", login_request, name="login"), 
    path("logout/", LogoutView.as_view(),name="logout"),
    path("leerPerfil/",leerPerfil,name="leerPerfil"),
    path("editarPerfil/",editarPerfil,name="editarPerfil"),
    path("crearPerfil/",crearPerfil,name="crearPerfil"),
    path("agregarAvatar/",agregarAvatar,name="agregarAvatar"),
    path("crearPosteo/",crearPosteo,name="crearPosteo"),
    

]