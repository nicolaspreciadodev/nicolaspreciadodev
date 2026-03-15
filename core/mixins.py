from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

class RoleRequiredMixin(AccessMixin):
    """
    Mixin para validar que el usuario pertenece a uno de los roles permitidos.
    """
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
            
        if request.user.rol not in self.allowed_roles:
            raise PermissionDenied("No tienes permisos suficientes para acceder a esta página.")
            
        return super().dispatch(request, *args, **kwargs)
