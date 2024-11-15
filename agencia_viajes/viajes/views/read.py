from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from viajes.models import Usuario, Estado, FechaHora, Aeropuerto, ModelosAviones, Aviones, Asientos

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