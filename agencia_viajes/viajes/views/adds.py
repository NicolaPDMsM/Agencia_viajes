from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from viajes.models import Usuario, Estado, FechaHora, Aeropuerto, ModelosAviones, Aviones, Asientos, Pasajeros, Checkin, Equipaje, Vuelos, Pasajes, TarjetaEmbarque, Transfer

def add_usuario(request):
    if request.method == "POST":
        id_usuario = request.POST.get("idUsuario")
        user_name = request.POST.get("username")
        password = request.POST.get("passwords")
        estado = request.POST.get("fk_idEstado")
        fecha_hora = request.POST.get("fk_idFechaHora")

        estado = get_object_or_404(Estado, id_estado=estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=fecha_hora)

        nuevo_usuario = Usuario.objects.create(
            id_usuario=id_usuario,
            user_name=user_name,
            password=password,
            id_estado=estado,
            id_fecha_hora=fecha_hora
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_estado(request):
    if request.method == "POST":
        id_estado = request.POST["idEstado"]

        nuevo_estado = Estado.objects.create(
            id_estado=id_estado
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_fecha_hora(request):
    if request.method == "POST":
        id_fecha_hora = request.POST["idFecha_hora"]
        fecha_hora = request.POST["fecha_hora"]

        nuevo_fecha_hora = FechaHora.objects.create(
            id_fecha_hora = id_fecha_hora,
            fecha_hora = fecha_hora
	    )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_aeropuerto(request):
    if request.method == "POST":
        id_aeropuerto = request.POST.get("idAeropuerto")
        aviones_disponibles = request.POST.get("avionesDisponibles")
        empleados = request.POST.get("empleados")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")

        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_aeropuerto = Aeropuerto.objects.create(
            id_aeropuerto = id_aeropuerto,
            aviones_disponibles = aviones_disponibles,
            empleados = empleados,
            id_estado = estado,
            id_usuario = usuario,
            id_fecha_hora = fecha_hora
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_modeloAvion(request):
    if request.method == "POST":
        id_modelo = request.POST["idModeloAvion"]
        modelos = request.POST["modelos"]
        id_estado = request.POST["fk_idEstado"]
        id_usuario = request.POST["fk_idUsuario"]
        id_fecha_hora = request.POST["fk_idFecha_hora"]

        estado = get_object_or_404(Estado, id_estado=id_estado)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)

        nuevo_modeloAvion = ModelosAviones.objects.create(
            id_modelo = id_modelo,
            modelos = modelos,
            id_estado = estado,
            id_usuario = usuario,
            id_fecha_hora = fecha_hora
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_avion(request):
    if request.method == "POST":
        id_avion = request.POST["idAvion"]
        capacidad = request.POST["capacidad"]
        id_aeropuerto = request.POST["idAeropuerto"]
        id_modelo = request.POST["idModelo"]
        id_estado = request.POST["fk_idEstado"]
        id_fecha_hora = request.POST["fk_idFecha_hora"]
        id_usuario = request.POST["fk_idUsuario"]

        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        modelo = get_object_or_404(ModelosAviones, id_modelo=id_modelo)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_avion = Aviones.objects.create(
            id_avion = id_avion,
            capacidad = capacidad,
            id_aeropuerto = aeropuerto,
            id_modelo = modelo,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_asiento(request):
    if request.method == "POST":
        id_asiento = request.POST["idAsiento"]
        clase = request.POST["clase"]
        id_avion = request.POST["idAvion"]
        id_estado = request.POST["fk_idEstado"]
        id_fecha_hora = request.POST["fk_idFecha_hora"]
        id_usuario = request.POST["fk_idUsuario"]

        avion = get_object_or_404(Aviones, id_avion=id_avion)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_avion = Asientos.objects.create(
            id_asiento = id_asiento,
            clase = clase,
            id_avion = avion,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_pasajero(request):
    if request.method == "POST":
        rut_pasajero = request.POST.get("rutPasajero")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        id_aeropuerto = request.POST.get("idAeropuerto")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")

        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_pasajero = Pasajeros.objects.create(
            rut_pasajero = rut_pasajero,
            nombre = nombre,
            apellido = apellido,
            id_aeropuerto = aeropuerto,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_equipaje(request):
    if request.method == "POST":
        id_equipaje = request.POST.get("idEquipaje")
        peso_equipaje = request.POST.get("equipaje")
        rut_pasajero = request.POST.get("rutPasajero")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")

        pasajero = get_object_or_404(Pasajeros, rut_pasajero=rut_pasajero)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_equipaje = Equipaje.objects.create(
            id_equipaje = id_equipaje,
            peso_equipaje = peso_equipaje,
            rut_pasajero = pasajero,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_vuelo(request):
    if request.method == "POST":
        id_vuelo = request.POST.get("idVuelos")
        hora_vuelo = request.POST.get("horaVuelo")
        id_avion = request.POST.get("idAvion")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")

        avion = get_object_or_404(Aviones, id_avion=id_avion)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_vuelo = Vuelos.objects.create(
            id_vuelo = id_vuelo,
            hora_vuelo = hora_vuelo,
            id_avion = avion,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_checkin(request):
    if request.method == "POST":
        id_checkin = request.POST.get("idCheckin")
        id_vuelo = request.POST.get("idVuelo")
        rut_pasajero = request.POST.get("rutPasajero")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")
        
        vuelo = get_object_or_404(Vuelos, id_vuelo=id_vuelo)
        pasajero = get_object_or_404(Pasajeros, rut_pasajero=rut_pasajero)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_checkin = Checkin.objects.create(
            id_checkin = id_checkin,
            id_vuelo = vuelo,
            rut_pasajero = pasajero,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_pasaje(request):
    if request.method == "POST":
        id_pasaje = request.POST.get("idPasajes")
        codigo_verificacion = request.POST.get("codigoVerificador")
        id_asiento = request.POST.get("idAsiento")
        id_vuelo = request.POST.get("idVuelos")
        rut_pasajero = request.POST.get("rutPasajero")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")
        id_avion = request.POST.get("idAvion")

        asiento = get_object_or_404(Asientos, id_asiento=id_asiento)
        vuelo = get_object_or_404(Vuelos, id_vuelo=id_vuelo)
        pasajero = get_object_or_404(Pasajeros, rut_pasajero=rut_pasajero)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
        avion = get_object_or_404(Aviones, id_avion=id_avion)

        nuevo_pasaje = Pasajes.objects.create(
            id_pasaje = id_pasaje,
            codigo_verificacion = codigo_verificacion,
            id_asiento = asiento,
            id_vuelo = vuelo,
            rut_pasajero = pasajero,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario,
            id_avion = avion
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_tarjetaEmbarque(request):
    if request.method == "POST":
        id_tarjeta_embarque = request.POST.get("idTarjeta")
        puerta_embarque = request.POST.get("puertaEmbarque")
        id_checkin = request.POST.get("idCheckin")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")

        checkin = get_object_or_404(Checkin, id_checkin=id_checkin)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_tarjetaEmbarque = TarjetaEmbarque.objects.create(
            id_tarjeta_embarque = id_tarjeta_embarque,
            puerta_embarque = puerta_embarque,
            id_checkin = checkin,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)

def add_transfer(request):
    if request.method == "POST":
        id_transfer = request.POST.get("idTransfer")
        destino = request.POST.get("destino")
        id_aeropuerto = request.POST.get("idAeropuerto")
        id_estado = request.POST.get("fk_idEstado")
        id_fecha_hora = request.POST.get("fk_idFecha_hora")
        id_usuario = request.POST.get("fk_idUsuario")

        aeropuerto = get_object_or_404(Aeropuerto, id_aeropuerto=id_aeropuerto)
        estado = get_object_or_404(Estado, id_estado=id_estado)
        fecha_hora = get_object_or_404(FechaHora, id_fecha_hora=id_fecha_hora)
        usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

        nuevo_transfer = Transfer.objects.create(
            id_transfer = id_transfer,
            destino = destino,
            id_aeropuerto = aeropuerto,
            id_estado = estado,
            id_fecha_hora = fecha_hora,
            id_usuario = usuario
        )
        return redirect("exito")
    return HttpResponse("Método no permitido", status=405)