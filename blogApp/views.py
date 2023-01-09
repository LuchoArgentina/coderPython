from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, "blogApp/index.html")

def acercaDeMi(request):
    return render(request, "blogApp/acercaDeMi.html")

def contacto(request):
    return render(request, "blogApp/contacto.html")

def posteos(request):
    return render(request, "blogApp/posteos.html")

def microblading(request):
    return render(request, "blogApp/microblading.html")

def perfilado(request):
    return render(request, "blogApp/perfilado.html")