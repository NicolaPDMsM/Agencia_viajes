"""
URL configuration for agencia_viajes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from viajes.views import forms, adds, delete, read, update


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Inicio
    path('', forms.all_tables, name="inicio"),
    path('exito/', forms.exito, name="exito"),

    # Usuario
    path('usuario', forms.form_usuario, name="usuario"),
    path('exito/adds-usuario/', adds.add_usuario, name="add_usuario"),
    path('exito/delete-usuario/', delete.delete_usuario, name="delete_usuario"),
    path('exito/read-usuario/', read.read_usuario, name="read_usuario"),
    path('exito/update-usuario/', update.update_usuario, name="update_usuario"),

    # Estado
    path('estado', forms.form_estado, name="estado"),
    path('exito/estado/', adds.add_estado, name="add_estado"),

    # FechaHora
    path('fecha_hora', forms.form_fecha_hora, name="fecha_hora"),
    path('exito/adds-fecha_hora/', adds.add_fecha_hora, name="add_fecha_hora"),
    path('exito/delete-fecha_hora/', delete.delete_fecha_hora, name="delete_fecha_hora"),
    path('exito/read-fecha_hora/', read.read_fecha_hora, name="read_fecha_hora"),
    path('exito/update-fecha_hora/', update.update_fecha_hora, name="update_fecha_hora"),

    # Aeropuerto
    path('aeropuerto', forms.form_aeropuerto, name="aeropuerto"),
    path('exito/adds-aeropuerto/', adds.add_aeropuerto, name="add_aeropuerto"),
    path('exito/delete-aeropuerto/', delete.delete_aeropuerto, name="delete_aeropuerto"),
    path('exito/read-aeropuerto/', read.read_aeropuerto, name="read_aeropuerto"),
    path('exito/update-aeropuerto/', update.update_aeropuerto, name="update_aeropuerto"),

    # Modelos Avión
    path('modelos-avion', forms.form_modeloAvion, name="modeloAvion"),
    path('exito/adds-modelos-avion/', adds.add_modeloAvion, name="add_modeloAvion"),
    path('exito/delete-modelo-avion/', delete.delete_modeloAvion, name="delete_modeloAvion"),
    path('exito/read-modelo-avion/', read.read_modeloAvion, name="read_modeloAvion"),
    path('exito/update-modelo-avion/', update.update_modeloAvion, name="update_modeloAvion"),

    # Avión
    path('avion', forms.form_avion, name="avion"),
    path('exito/adds-avion/', adds.add_avion, name="add_avion"),
    path('exito/delete-avion/', delete.delete_avion, name="delete_avion"),
    path('exito/read-avion/', read.read_avion, name="read_avion"),
    path('exito/update-avion/', update.update_avion, name="update_avion"),

    # Asiento
    path('asiento', forms.form_asiento, name="asiento"),
    path('exito/adds-asiento/', adds.add_asiento, name="add_asiento"),
    path('exito/delete-asiento/', delete.delete_asiento, name="delete_asiento"),
    path('exito/read-asiento/', read.read_asiento, name="read_asiento"),
    path('exito/update-asiento/', update.update_asiento, name="update_asiento"),

    # Pasajero
    path('pasajero', forms.form_pasajero, name="pasajero"),
    path('exito/adds-pasajero/', adds.add_pasajero, name="add_pasajero"),
    path('exito/delete-pasajero/', delete.delete_pasajero, name="delete_pasajero"),
    path('exito/read-pasajero/', read.read_pasajero, name="read_pasajero"),
    path('exito/update-pasajero/', update.update_pasajero, name="update_pasajero"),

    # Equipaje
    path('equipaje', forms.form_equipaje, name="equipaje"),
    path('exito/adds-equipaje/', adds.add_equipaje, name="add_equipaje"),
    path('exito/delete-equipaje/', delete.delete_equipaje, name="delete_equipaje"),
    path('exito/read-equipaje/', read.read_equipaje, name="read_equipaje"),
    path('exito/update-equipaje/', update.update_equipaje, name="update_equipaje"),

    # Vuelo
    path('vuelo', forms.form_vuelo, name="vuelo"),
    path('exito/adds-vuelo/', adds.add_vuelo, name="add_vuelo"),
    path('exito/delete-vuelo/', delete.delete_vuelo, name="delete_vuelo"),
    path('exito/read-vuelo/', read.read_vuelo, name="read_vuelo"),
    path('exito/update-vuelo/', update.update_vuelo, name="update_vuelo"),

    # Checkin
    path('checkin', forms.form_checkin, name="checkin"),
    path('exito/adds-checkin/', adds.add_checkin, name="add_checkin"),
    path('exito/delete-checkin/', delete.delete_checkin, name="delete_checkin"),
    path('exito/read-checkin/', read.read_checkin, name="read_checkin"),
    path('exito/update-checkin/', update.update_checkin, name="update_checkin"),

    # Pasaje
    path('pasaje', forms.form_pasaje, name="pasaje"),
    path('exito/adds-pasaje/', adds.add_pasaje, name="add_pasaje"),
    path('exito/delete-pasaje/', delete.delete_pasaje, name="delete_pasaje"),
    path('exito/read-pasaje/', read.read_pasaje, name="read_pasaje"),
    path('exito/update-pasaje/', update.update_pasaje, name="update_pasaje"),

    # Tarjeta embarque
    path('tarjeta-embarque', forms.form_tarjetaEmbarque, name="tarjeta_embarque"),
    path('exito/adds-tarjeta-embarque/', adds.add_tarjetaEmbarque, name="add_tarjeta_embarque"),
    path('exito/delete-tarjeta-embarque/', delete.delete_tarjetaEmbarque, name="delete_tarjetaEmbarque"),
    path('exito/read-tarjeta-embarque/', read.read_tarjetaEmbarque, name="read_tarjetaEmbarque"),
    path('exito/update-tarjeta-embarque/', update.update_tarjetaEmbarque, name="update_tarjetaEmbarque"),

    # Transfer
    path('transfer', forms.form_transfer, name="transfer"),
    path('exito/adds-transfer/', adds.add_transfer, name="add_transfer"),
    path('exito/delete-transfer/', delete.delete_transfer, name="delete_transfer"),
    path('exito/read-transfer/', read.read_transfer, name="read_transfer"),
    path('exito/update-transfer/', update.update_transfer, name="update_transfer"),
]
