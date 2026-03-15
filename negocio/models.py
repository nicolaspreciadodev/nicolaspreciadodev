from django.db import models
from django.conf import settings
from canchas.models import Cancha

class Torneo(models.Model):
    ESTADO_CHOICES = (
        ('PENDIENTE', 'Pendiente'),
        ('PUBLICADO', 'Publicado'),
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    is_approved = models.BooleanField(default=False)
    organizador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='torneos_organizados')
    
    def __str__(self):
        return f"{self.nombre} ({self.get_estado_display()})"

from django.core.exceptions import ValidationError

class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservas')
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora = models.TimeField()
    pagado = models.BooleanField(default=False)
    
    def clean(self):
        # Check if a reservation already exists for the same court, date, and hour
        overlapping = Reserva.objects.filter(
            cancha=self.cancha,
            fecha=self.fecha,
            hora=self.hora
        )
        if self.pk:
            overlapping = overlapping.exclude(pk=self.pk)
            
        if overlapping.exists():
            raise ValidationError(f"La cancha {self.cancha.nombre} ya se encuentra reservada para la fecha {self.fecha} a las {self.hora}.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva {self.id} - {self.cancha.nombre} ({self.fecha})"

class Factura(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='factura')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Factura {self.id} - {self.total}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='equipos/', blank=True, null=True)
    jugadores = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='equipos')
    torneos = models.ManyToManyField(Torneo, related_name='equipos', blank=True)
    
    def __str__(self):
        return self.nombre
