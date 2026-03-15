from django.urls import path
from .views import CrearReservaView

app_name = 'negocio'

urlpatterns = [
    path('reservar/<int:cancha_id>/', CrearReservaView.as_view(), name='crear_reserva'),
]
