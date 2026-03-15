from django.db.models.signals import post_save
from django.dispatch import receiver
from negocio.models import Reserva, Factura

@receiver(post_save, sender=Reserva)
def crear_factura_reserva(sender, instance, created, **kwargs):
    if created:
        Factura.objects.create(
            reserva=instance,
            total=instance.cancha.precio
        )
