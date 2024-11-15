from django.http import HttpResponse
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def inicio(request):

    temas_del_curso = ["Plantilla", "Modelos", "Formulario", "Vistas", "Despliegue"]

    p1 = Persona("Nicolas MPDM", "Mollo MPDM")

    return render(request, 'index.html', {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "temas": temas_del_curso})

def FormAeropuerto (request):
    return render(request, "aeropuerto.html")