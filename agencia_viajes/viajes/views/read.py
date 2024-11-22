from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from viajes.models import Usuario, Estado, FechaHora, Aeropuerto, ModelosAviones, Aviones, Asientos, Pasajeros, Checkin, Equipaje, Vuelos, Pasajes, TarjetaEmbarque, Transfer

def read_usuario(request):
    if request.method == "POST":
        read_id_usuario = request.POST.get("buscarIdUsuario")
        objeto = get_object_or_404(Usuario, id_usuario=read_id_usuario)

        ctx = {
            "idUsuario": objeto.id_usuario,
            "username": objeto.user_name,
            "password": objeto.password,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
        }
        return render(request, "usuario.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_fecha_hora(request):
    if request.method == "POST":
        read_id_fecha_hora = request.POST.get("buscarIdFechaHora")
        objeto = get_object_or_404(FechaHora, id_fecha_hora=read_id_fecha_hora)

        ctx = {
            "idFechaHora": objeto.id_fecha_hora,
            "fechaHora": objeto.fecha_hora
        }
        return render(request, "fecha_hora.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_aeropuerto(request):
    if request.method == "POST":
        read_id_aeropuerto = request.POST.get("buscarIdAeropuerto")
        objeto = get_object_or_404(Aeropuerto, id_aeropuerto=read_id_aeropuerto)

        ctx = {
            "idAeropuerto": objeto.id_aeropuerto,
            "avionesDisponibles": objeto.aviones_disponibles,
            "empleados": objeto.empleados,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "aeropuerto.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_modeloAvion(request):
    if request.method == "POST":
        read_id_modelo = request.POST.get("buscarIdModeloAvion")
        objeto = get_object_or_404(ModelosAviones, id_modelo=read_id_modelo)
        
        ctx = {
            "idModelo": objeto.id_modelo,
            "modelos": objeto.modelos,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "modelosAviones.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_avion(request):
    if request.method == "POST":
        read_id_avion = request.POST.get("buscarIdAvion")

        objeto = get_object_or_404(Aviones, id_avion=read_id_avion)

        ctx = {
            "idAvion": objeto.id_avion,
            "capacidad": objeto.capacidad,
            "idAeropuerto": objeto.id_aeropuerto.id_aeropuerto,
            "modelo": objeto.id_modelo.modelos,
            "idModelo": objeto.id_modelo.id_modelo,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "avion.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_asiento(request):
    if request.method == "POST":
        read_id_asiento = request.POST.get("buscarIdAsiento")
        objeto = get_object_or_404(Asientos, id_asiento=read_id_asiento)

        ctx = {
            "idAsiento": objeto.id_asiento,
            "clase": objeto.clase,
            "idAvion": objeto.id_avion.id_avion,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "asientos.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_pasajero(request):
    if request.method == "POST":
        read_rut_pasajero = request.POST.get("buscarRutPasajero")
        objeto = get_object_or_404(Pasajeros, rut_pasajero=read_rut_pasajero)

        ctx = {
            "rut": objeto.rut_pasajero,
            "nombre": objeto.nombre,
            "apellido": objeto.apellido,
            "idAeropuerto": objeto.id_aeropuerto.id_aeropuerto,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "pasajeros.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_equipaje(request):
    if request.method == "POST":
        read_id_equipaje = request.POST.get("buscarIdEquipaje")
        objeto = get_object_or_404(Equipaje, id_equipaje=read_id_equipaje)

        ctx = {
            "idEquipaje": objeto.id_equipaje,
            "pesoEquipaje": objeto.peso_equipaje,
            "rutPasajero": objeto.rut_pasajero.rut_pasajero,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "equipaje.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_vuelo(request):
    if request.method == "POST":
        read_id_vuelo = request.POST.get("buscarIdVuelo")
        objeto = get_object_or_404(Vuelos, id_vuelo=read_id_vuelo)

        ctx = {
            "idVuelo": objeto.id_vuelo,
            "horaVuelo": objeto.hora_vuelo,
            "idAvion": objeto.id_avion.id_avion,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "vuelos.html", ctx)
    return HttpResponse("Método no permitido", status=405)

def read_checkin(request):
    if request.method == "POST":
        read_id_checkin = request.POST.get("buscarIdCheckin")
        objeto = get_object_or_404(Checkin, id_checkin=read_id_checkin)

        ctx = {
            "idCheckin": objeto.id_checkin,
            "idVuelo": objeto.id_vuelo.id_vuelo,
            "rutPasajero": objeto.rut_pasajero.rut_pasajero,
            "idEstado": objeto.id_estado.id_estado,
            "fechaHora": objeto.id_fecha_hora.fecha_hora,
            "idFechaHora": objeto.id_fecha_hora.id_fecha_hora,
            "usuario": objeto.id_usuario.user_name,
            "idUsuario": objeto.id_usuario.id_usuario
        }
        return render(request, "checkin.html", ctx)
    return HttpResponse("Método no permitido", status=405)