import os
import random
import urllib.request
from django.core.management.base import BaseCommand
from django.core.files import File
from usuarios.models import CustomUser
from canchas.models import Deporte, Cancha
from django.conf import settings

class Command(BaseCommand):
    help = 'Poblar la base de datos con categorías de deportes, dueño de prueba y 6 canchas.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Iniciando carga de datos..."))

        # 1. Crear Dueño de Prueba si no existe
        owner, created = CustomUser.objects.get_or_create(
            username='dueno_prueba',
            defaults={
                'email': 'dueno@gosport.com',
                'rol': 'DUEÑO',
            }
        )
        if created:
            owner.set_password('admin123')
            owner.save()
            self.stdout.write(self.style.SUCCESS('Dueño de prueba creado.'))
        else:
            self.stdout.write('Dueño de prueba ya existía.')

        # 2. Crear Categorías de Deportes
        deportes_nombres = ['Fútbol', 'Tenis', 'Basket']
        deportes = {}
        for nombre in deportes_nombres:
            deporte, created = Deporte.objects.get_or_create(nombre=nombre)
            deportes[nombre] = deporte
            if created:
                self.stdout.write(self.style.SUCCESS(f'Deporte "{nombre}" creado.'))

        # 3. Crear Canchas de Prueba
        canchas_data = [
            {'nombre': 'La Bombonera 5v5', 'desc': 'Excelente cancha de fútbol sintética.', 'precio': 80.00, 'ubic': 'Centro Norte', 'deporte': deportes['Fútbol']},
            {'nombre': 'El Monumental F7', 'desc': 'Cancha de fútbol 7 techada.', 'precio': 120.00, 'ubic': 'Sur Ciudad', 'deporte': deportes['Fútbol']},
            {'nombre': 'Roland Garros Red', 'desc': 'Cancha de polvo de ladrillo impecable.', 'precio': 100.00, 'ubic': 'Club de Tenis Este', 'deporte': deportes['Tenis']},
            {'nombre': 'Wimbledon Green', 'desc': 'Cancha de césped para profesionales.', 'precio': 150.00, 'ubic': 'Club de Tenis Este', 'deporte': deportes['Tenis']},
            {'nombre': 'Staples Center Mini', 'desc': 'Cancha de basket de madera.', 'precio': 90.00, 'ubic': 'Polideportivo Central', 'deporte': deportes['Basket']},
            {'nombre': 'Street Hoops', 'desc': 'Cancha de basket al aire libre de asfalto liso.', 'precio': 50.00, 'ubic': 'Parque Bicentenario', 'deporte': deportes['Basket']},
        ]

        if Cancha.objects.count() >= 6:
            self.stdout.write(self.style.WARNING("Ya existen 6 o más canchas, omitiendo creación de canchas."))
        else:
            for data in canchas_data:
                cancha, created = Cancha.objects.get_or_create(
                    nombre=data['nombre'],
                    defaults={
                        'descripcion': data['desc'],
                        'precio': data['precio'],
                        'ubicacion': data['ubic'],
                        'dueño': owner,
                        'deporte': data['deporte'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Cancha "{cancha.nombre}" creada, descargando imagen...'))
                    try:
                        from django.core.files.base import ContentFile
                        response = urllib.request.urlopen('https://picsum.photos/800/600')
                        img_temp = ContentFile(response.read())
                        cancha.imagen.save(f"cancha_{cancha.id}.jpg", img_temp)
                        self.stdout.write(self.style.SUCCESS(f'Imagen asignada a "{cancha.nombre}".'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error al descargar imagen para "{cancha.nombre}": {e}'))

        self.stdout.write(self.style.SUCCESS("Carga de datos finalizada exitosamente!"))
