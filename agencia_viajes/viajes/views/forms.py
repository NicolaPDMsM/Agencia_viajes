from django.shortcuts import render

def all_tables(request):
    return render(request, "index.html")

def exito(request):
    return render(request, "exito.html")

def form_usuario(request):
    return render(request, "usuario.html")

def form_estado(request):
    return render(request, "estado.html")

def form_fecha_hora(request):
    return render(request, "fecha_hora.html")

def form_aeropuerto(request):
    return render(request, "aeropuerto.html")

def form_asiento(request):
    return render(request, "asientos.html")

def form_avion(request):
    return render(request, "avion.html")

def form_checkin(request):
    return render(request, "checkin.html")

def form_equipaje(request):
    return render(request, "equipaje.html")

def form_modeloAvion(request):
    return render(request, "modelosAviones.html")

def form_pasaje(request):
    return render(request, "pasaje.html")

def form_pasajero(request):
    return render(request, "pasajeros.html")

def form_tarjetaEmbarque(request):
    return render(request, "tarjetaEmbarque.html")

def form_transfer(request):
    return render(request, "transfer.html")

def form_vuelo(request):
    return render(request, "vuelos.html")
