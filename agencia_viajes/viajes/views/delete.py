from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from viajes.models import Usuario, Estado, FechaHora, Aeropuerto, ModelosAviones, Aviones, Asientos, Pasajeros, Checkin, Equipaje, Vuelos, Pasajes, TarjetaEmbarque, Transfer

def delete_usuario(request):
    if request.method == "POST":
        delete_id_usuario = request.POST.get("deleteIdUsuario")
        objetos = get_object_or_404(Usuario, id_usuario=delete_id_usuario)
        
        estado_inactivo = Estado.objects.get(id_estado=0)

        if objetos.id_estado.id_estado == 1:
            objetos.id_estado = estado_inactivo
            objetos.save()
            return redirect("exito")
        else:
            return redirect("usuario")
    return HttpResponse("Método no permitido", status=405)

def delete_fecha_hora(request):
    if request.method == "POST":
       delete_id_fecha_hora = request.POST.get("")

def delete_aeropuerto(request):
    if request.method == "POST":
        delete_id_aeropuerto = request.POST.get("deleteIdAeropuerto")
        objeto = get_object_or_404(Aeropuerto, id_aeropuerto=delete_id_aeropuerto)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            redirect("aeropuerto")
    return HttpResponse("Método no permitido", status=405)

def delete_modeloAvion(request):
    if request.method == "POST":
        delete_id_modelos = request.POST.get("deleteIdModeloAvion")
        objeto = get_object_or_404(ModelosAviones, id_modelo=delete_id_modelos)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("modeloAvion")
    return HttpResponse("Método no permitido", status=405)

def delete_avion(request):
    if request.method == "POST":
        delete_id_avion = request.POST.get("deleteIdAvion")
        objeto = get_object_or_404(Aviones, id_avion=delete_id_avion)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("avion")
    return HttpResponse("Método no permitido", status=405)

def delete_asiento(request):
    if request.method == "POST":
        delete_id_asiento = request.POST.get("deleteIdAsiento")
        objeto = get_object_or_404(Asientos, id_asiento=delete_id_asiento)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("asiento")
    return HttpResponse("Método no permitido", status=405)

def delete_pasajero(request):
    if request.method == "POST":
        delete_rut_pasajero = request.POST.get("deleteRutPasajero")
        objeto = get_object_or_404(Pasajeros, rut_pasajero=delete_rut_pasajero)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("pasajero")
    return HttpResponse("Método no permitido", status=405)

def delete_equipaje(request):
    if request.method == "POST":
        delete_id_equipaje = request.POST.get("deleteIdEquipaje")
        objeto = get_object_or_404(Equipaje, id_equipaje=delete_id_equipaje)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("equipaje")
    return HttpResponse("Método no permitido", status=405)

def delete_vuelo(request):
    if request.method == "POST":
        delete_id_vuelo = request.POST.get("deleteIdVuelo")
        objeto = get_object_or_404(Vuelos, id_vuelo=delete_id_vuelo)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("vuelo")
    return HttpResponse("Método no permitido", status=405)

def delete_checkin(request):
    if request.method == "POST":
        delete_rut_pasajero = request.POST.get("deleteIdCheckin")
        objeto = get_object_or_404(Checkin, rut_pasajero=delete_rut_pasajero)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("checkin")
    return HttpResponse("Método no permitido", status=405)

def delete_pasaje(request):
    if request.method == "POST":
        delete_id_pasaje = request.POST.get("deleteIdPasaje")
        objeto = get_object_or_404(Pasajes, id_pasaje=delete_id_pasaje)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("pasaje")
    return HttpResponse("Método no permitido", status=405)
    
def delete_tarjetaEmbarque(request):
    if request.method == "POST":
        delete_id_embarque = request.POST.get("deleteIdEmbarque")
        objeto = get_object_or_404(TarjetaEmbarque, id_tarjeta_embarque=delete_id_embarque)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("tarjeta_embarque")
    return HttpResponse("Método no permitido", status=405)

def delete_transfer(request):
    if request.method == "POST":
        delete_id_transfer = request.POST.get("deleteIdTransfer")
        objeto = get_object_or_404(Transfer, id_transfer=delete_id_transfer)

        estado_inactivo = Estado.objects.get(id_estado=0)

        if objeto.id_estado.id_estado == 1:
            objeto.id_estado = estado_inactivo
            objeto.save()
            return redirect("exito")
        else:
            return redirect("transfer")
    return HttpResponse("Método no permitido", status=405)