from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from viajes.models import Usuario, Estado, FechaHora, Aeropuerto, ModelosAviones, Aviones, Asientos, Pasajeros, Checkin, Equipaje, Vuelos, Pasajes, TarjetaEmbarque, Transfer

def update_usuario(request):
    if request.method == "POST":
        id_usuario = request.POST.get("updateIdUsuario")
        user_name = request.POST.get("updateUsername")
        password = request.POST.get("updatePasswords")
        id_estado = request.POST.get("updateIdEstado")
        id_fecha_hora = request.POST.get("updateIdFechaHora")

        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)

        actualizar_usuario = Usuario(
            id_usuario=id_usuario,
            user_name=user_name,
            password=password,
            id_estado=estado,
            id_fecha_hora=fecha_hora
        )

        actualizar_usuario.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_fecha_hora(request):
    if request.method == "POST":
        id_fecha_hora = request.POST.get("updateIdFechaHora")
        fecha_hora = request.POST.get("updateFechaHora")

        actualizar_fecha_hora = FechaHora(
            id_fecha_hora = id_fecha_hora,
            fecha_hora = fecha_hora
        )
        actualizar_fecha_hora.save()
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_aeropuerto(request):
    if request.method == "POST":
        id_aeropuerto = request.POST.get("updateIdAeropuerto")
        aviones_disponibles = request.POST.get("updateAvionesDisponibles")
        empleados = request.POST.get("updateEmpleados")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        actualizar_aeropuerto = Aeropuerto(
            id_aeropuerto = id_aeropuerto,
            aviones_disponibles = aviones_disponibles,
            empleados = empleados,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        actualizar_aeropuerto.save()
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_modeloAvion(request):
    if request.method == "POST":

        id_modelo = request.POST.get("updateIdModeloAvion")
        modelos = request.POST.get("updateModelos")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
        
        actualizar_modelo = ModelosAviones(
            id_modelo = id_modelo,
            modelos = modelos,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )

        actualizar_modelo.save()
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_avion(request):
    if request.method == "POST":
        id_avion = request.POST.get("updateIdAvion")
        capacidad = request.POST.get("updateCapacidad")
        id_aeropuerto = request.POST.get("updateIdAeropuerto")
        id_modelo = request.POST.get("updateIdModelo")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        modelo = get_object_or_404(ModelosAviones, id_modelo=id_modelo)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        actualizar_avion = Aviones(
            id_avion = id_avion,
            capacidad = capacidad,
            id_aeropuerto = aeropuerto,
            id_modelo = modelo,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        actualizar_avion.save()
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_asiento(request):
    if request.method == "POST":
        id_asiento = request.POST.get("updateIdAsiento")
        clase = request.POST.get("updateClase")
        id_avion = request.POST.get("updateIdAvion")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        avion = get_object_or_404(Aviones, id_avion=id_avion)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        actualizar_asiento = Asientos(
            id_asiento = id_asiento,
            clase = clase,
            id_avion = avion,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        actualizar_asiento.save()
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

