from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from core.mixins import RoleRequiredMixin
from django.contrib import messages
from canchas.models import Cancha
from .models import Reserva
from django.core.exceptions import ValidationError

class CrearReservaView(RoleRequiredMixin, View):
    allowed_roles = ['DEPORTISTA']
    
    def get(self, request, cancha_id):
        cancha = get_object_or_404(Cancha, id=cancha_id)
        return render(request, 'crear_reserva.html', {'cancha': cancha})

    def post(self, request, cancha_id):
        cancha = get_object_or_404(Cancha, id=cancha_id)
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        if not fecha or not hora:
            messages.error(request, 'Debe proporcionar una fecha y hora.')
            return render(request, 'crear_reserva.html', {'cancha': cancha})

        reserva = Reserva(
            usuario=request.user,
            cancha=cancha,
            fecha=fecha,
            hora=hora
        )

        try:
            reserva.full_clean() # Will trigger our overlapping validation
            reserva.save()
            messages.success(request, '¡Reserva creada con éxito!')
            return redirect('dashboard')
        except ValidationError as e:
            # e.messages contains the list of error strings
            for msg in e.messages:
                messages.error(request, msg)
            return render(request, 'crear_reserva.html', {'cancha': cancha})
