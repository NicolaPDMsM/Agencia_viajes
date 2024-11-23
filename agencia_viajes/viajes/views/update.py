from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from viajes.models import Usuario, Estado, FechaHora, Aeropuerto, ModelosAviones, Aviones, Asientos, Pasajeros, Checkin, Equipaje, Vuelos, Pasajes, TarjetaEmbarque, Transfer

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

def update_usuario(request):
    if request.method == "POST":
        id_usuario = request.POST.get("updateIdUsuario")
        user_name = request.POST.get("updateUsername")
        password = request.POST.get("updatePasswords")
        id_estado = request.POST.get("updateIdEstado")
        id_fecha_hora = request.POST.get("updateIdFechaHora")

        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)

        usuario.user_name = user_name
        usuario.password = password
        usuario.id_estado = estado
        usuario.id_fecha_hora = fecha_hora
        usuario.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_fecha_hora(request):
    if request.method == "POST":
        id_fecha_hora = request.POST.get("updateIdFechaHora")
        nueva_fecha_hora = request.POST.get("updateFechaHora")

        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        fecha_hora.fecha_hora = nueva_fecha_hora
        fecha_hora.save()
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

        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        aeropuerto.aviones_disponibles = aviones_disponibles
        aeropuerto.empleados = empleados
        aeropuerto.id_estado = estado
        aeropuerto.id_fecha_hora = fecha_hora
        aeropuerto.id_usuario = usuario
        aeropuerto.save()
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_modeloAvion(request):
    if request.method == "POST":
        id_modelo = request.POST.get("updateIdModeloAvion")
        modelos = request.POST.get("updateModelos")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        modelo_avion = get_object_or_404(ModelosAviones, id_modelo=id_modelo)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        modelo_avion.modelos = modelos
        modelo_avion.id_estado = estado
        modelo_avion.id_fecha_hora = fecha_hora
        modelo_avion.id_usuario = usuario
        modelo_avion.save()
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

        avion = get_object_or_404(Aviones, id_avion=id_avion)
        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        modelo = get_object_or_404(ModelosAviones, id_modelo=id_modelo)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        avion.capacidad = capacidad
        avion.id_aeropuerto = aeropuerto
        avion.id_modelo = modelo
        avion.id_estado = estado
        avion.id_fecha_hora = fecha_hora
        avion.id_usuario = usuario
        avion.save()
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

        asiento = get_object_or_404(Asientos, id_asiento=id_asiento)
        avion = get_object_or_404(Aviones, id_avion=id_avion)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        asiento.clase = clase
        asiento.id_avion = avion
        asiento.id_estado = estado
        asiento.id_fecha_hora = fecha_hora
        asiento.id_usuario = usuario
        asiento.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_pasajero(request):
    if request.method == "POST":
        rut_pasajero = request.POST.get("updateRutPasajero")
        nombre = request.POST.get("updateNombre")
        apellido = request.POST.get("updateApellido")
        id_aeropuerto = request.POST.get("updateIdAeropuerto")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        pasajero = get_object_or_404(Pasajeros, rut_pasajero=rut_pasajero)
        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        pasajero.nombre = nombre
        pasajero.apellido = apellido
        pasajero.id_aeropuerto = aeropuerto
        pasajero.id_estado = estado
        pasajero.id_fecha_hora = fecha_hora
        pasajero.id_usuario = usuario
        pasajero.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_equipaje(request):
    if request.method == "POST":
        id_equipaje = request.POST.get("updateIdEquipaje")
        peso_equipaje = request.POST.get("updateEquipaje")
        rut_pasajero = request.POST.get("updateRutPasajero")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        equipaje = get_object_or_404(Equipaje, id_equipaje=id_equipaje)
        pasajero = get_object_or_404(Pasajeros, rut_pasajero=rut_pasajero)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        equipaje.peso_equipaje = peso_equipaje
        equipaje.rut_pasajero = pasajero
        equipaje.id_estado = estado
        equipaje.id_fecha_hora = fecha_hora
        equipaje.id_usuario = usuario
        equipaje.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_vuelo(request):
    if request.method == "POST":
        id_vuelo = request.POST.get("updateIdVuelos")
        hora_vuelo = request.POST.get("updateHoraVuelo")
        id_avion = request.POST.get("updateIdAvion")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        vuelo = get_object_or_404(Vuelos, id_vuelo=id_vuelo)
        avion = get_object_or_404(Aviones, id_avion=id_avion)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        vuelo.hora_vuelo = hora_vuelo
        vuelo.id_avion = avion
        vuelo.id_estado = estado
        vuelo.id_fecha_hora = fecha_hora
        vuelo.id_usuario = usuario
        vuelo.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_checkin(request):
    if request.method == "POST":
        id_checkin = request.POST.get("updateIdCheckin")
        id_vuelo = request.POST.get("updateIdVuelo")
        rut_pasajero = request.POST.get("updateRutPasajero")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        checkin = get_object_or_404(Checkin, id_checkin=id_checkin)
        vuelo = get_object_or_404(Vuelos, id_vuelo=id_vuelo)
        pasajero = get_object_or_404(Pasajeros, rut_pasajero=rut_pasajero)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        checkin.id_vuelo = vuelo
        checkin.rut_pasajero = pasajero
        checkin.id_estado = estado
        checkin.id_fecha_hora = fecha_hora
        checkin.id_usuario = usuario
        checkin.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_pasaje(request):
    if request.method == "POST":
        id_pasaje = request.POST.get("updateIdPasajes")
        codigo_verificacion = request.POST.get("updateCodigoVerificador")
        id_asiento = request.POST.get("updateIdAsiento")
        id_vuelo = request.POST.get("updateIdVuelos")
        rut_pasajero = request.POST.get("updateRutPasajero")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")
        id_avion = request.POST.get("updateIdAvion")

        pasaje = get_object_or_404(Pasajes, id_pasaje=id_pasaje)
        asiento = get_object_or_404(Asientos, id_asiento=id_asiento)
        vuelo = get_object_or_404(Vuelos, id_vuelo=id_vuelo)
        pasajero = get_object_or_404(Pasajeros, rut_pasajero=rut_pasajero)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
        avion = get_object_or_404(Aviones, id_avion=id_avion)

        pasaje.codigo_verificacion = codigo_verificacion
        pasaje.id_asiento = asiento
        pasaje.id_vuelo = vuelo
        pasaje.rut_pasajero = pasajero
        pasaje.id_estado = estado
        pasaje.id_fecha_hora = fecha_hora
        pasaje.id_usuario = usuario
        pasaje.id_avion = avion
        pasaje.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_tarjetaEmbarque(request):
    if request.method == "POST":
        id_tarjeta_embarque = request.POST.get("updateIdTarjeta")
        puerta_embarque = request.POST.get("updatePuertaEmbarque")
        id_checkin = request.POST.get("updateIdCheckin")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")

        tarjeta_embarque = get_object_or_404(TarjetaEmbarque, id_tarjeta_embarque=id_tarjeta_embarque)
        checkin = get_object_or_404(Checkin, id_checkin=id_checkin)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        tarjeta_embarque.puerta_embarque = puerta_embarque
        tarjeta_embarque.id_checkin = checkin
        tarjeta_embarque.id_estado = estado
        tarjeta_embarque.id_fecha_hora = fecha_hora
        tarjeta_embarque.id_usuario = usuario
        tarjeta_embarque.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def update_transfer(request):
    if request.method == "POST":
        id_transfer = request.POST.get("updateIdTransfer")
        destino = request.POST.get("updateDestino")
        id_aeropuerto = request.POST.get("updateIdAeropuerto")
        id_estado = request.POST.get("updateFk_idEstado")
        id_fecha_hora = request.POST.get("updateFk_idFecha_hora")
        id_usuario = request.POST.get("updateFk_idUsuario")
        print(id_estado)
        transfer = get_object_or_404(Transfer, id_transfer=id_transfer)
        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        transfer.destino = destino
        transfer.id_aeropuerto = aeropuerto
        transfer.id_estado = estado
        transfer.id_fecha_hora = fecha_hora
        transfer.id_usuario = usuario
        transfer.save()

        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)
