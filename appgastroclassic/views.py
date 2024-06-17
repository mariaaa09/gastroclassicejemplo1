from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola")

def adios(request):
    return HttpResponse("Adiós")

def mostrarhtml(request):
    minombre = 'Maria'
    contexto = {
        "minombre": minombre
    }
    return render(request, "prueba.html", contexto)

#Esto es un cambio.


