from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from canchas.models import Cancha, Deporte
from negocio.models import Reserva, Torneo

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        if user.role == 'DUEÑO_CANCHA':
            context['mis_canchas'] = Cancha.objects.filter(dueño=user)
            context['mis_torneos'] = Torneo.objects.filter(organizador=user)
        elif user.role == 'DEPORTISTA':
            context['canchas_disponibles'] = Cancha.objects.all()
            context['mis_reservas'] = Reserva.objects.filter(usuario=user)
        
        return context
