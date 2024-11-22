from django.db import models

class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)

class FechaHora(models.Model):
    id_fecha_hora = models.IntegerField(primary_key=True)
    fecha_hora = models.DateTimeField(null=True, blank=True)

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=60, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)

class Aeropuerto(models.Model):
    id_aeropuerto = models.IntegerField(primary_key=True)
    aviones_disponibles = models.IntegerField(null=True, blank=True)
    empleados = models.IntegerField(null=True, blank=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class ModelosAviones(models.Model):
    id_modelo = models.IntegerField(primary_key=True)
    modelos = models.CharField(max_length=60, null=True, blank=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Aviones(models.Model):
    id_avion = models.IntegerField(primary_key=True)
    capacidad = models.IntegerField(null=True, blank=True)
    id_aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)
    id_modelo = models.ForeignKey(ModelosAviones, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Asientos(models.Model):
    id_asiento = models.IntegerField(primary_key=True)
    clase = models.CharField(max_length=20, null=True, blank=True)
    id_avion = models.ForeignKey(Aviones, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pasajeros(models.Model):
    rut_pasajero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, null=True, blank=True)
    apellido = models.CharField(max_length=30, null=True, blank=True)
    id_aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Equipaje(models.Model):
    id_equipaje = models.IntegerField(primary_key=True)
    peso_equipaje = models.IntegerField(null=True, blank=True)
    rut_pasajero = models.ForeignKey(Pasajeros, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Vuelos(models.Model):
    id_vuelo = models.IntegerField(primary_key=True)
    hora_vuelo = models.DateTimeField(null=True, blank=True)
    id_avion = models.ForeignKey(Aviones, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Checkin(models.Model):
    id_checkin = models.IntegerField(primary_key=True)
    id_vuelo = models.ForeignKey(Vuelos, on_delete=models.CASCADE, null=True)
    rut_pasajero = models.ForeignKey(Pasajeros, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pasajes(models.Model):
    id_pasaje = models.IntegerField(primary_key=True)
    codigo_verificacion = models.CharField(max_length=40, null=True, blank=True)
    id_asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)
    id_vuelo = models.ForeignKey(Vuelos, on_delete=models.CASCADE)
    rut_pasajero = models.ForeignKey(Pasajeros, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_avion = models.ForeignKey(Aviones, on_delete=models.CASCADE)
    
class TarjetaEmbarque(models.Model):
    id_tarjeta_embarque = models.IntegerField(primary_key=True)
    puerta_embarque = models.CharField(max_length=5, null=True, blank=True)
    id_checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Transfer(models.Model):
    id_transfer = models.IntegerField(primary_key=True)
    destino = models.CharField(max_length=60, null=True, blank=True)
    id_aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_fecha_hora = models.ForeignKey(FechaHora, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
