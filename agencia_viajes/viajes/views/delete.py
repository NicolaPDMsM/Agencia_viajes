from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from viajes.models import Usuario, Estado, FechaHora, Aeropuerto, ModelosAviones, Aviones, Asientos

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