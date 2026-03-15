from django.contrib import admin
from .models import Torneo, Reserva, Factura, Equipo

@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'is_approved', 'organizador')
    list_filter = ('estado', 'is_approved')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('is_approved',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'cancha', 'fecha', 'hora', 'pagado')
    list_filter = ('fecha', 'pagado', 'cancha')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva', 'total', 'fecha_creacion')

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    filter_horizontal = ('jugadores', 'torneos')
