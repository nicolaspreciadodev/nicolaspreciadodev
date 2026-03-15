from django.db import models
from django.conf import settings

class Deporte(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='canchas/', blank=True, null=True)
    dueño = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='canchas')
    deporte = models.ForeignKey(Deporte, on_delete=models.SET_NULL, null=True, related_name='canchas')
    
    def __str__(self):
        return self.nombre

class Disponibilidad(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='disponibilidades')
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    def __str__(self):
        return f"{self.cancha.nombre} - {self.dia} ({self.hora_inicio} a {self.hora_fin})"
