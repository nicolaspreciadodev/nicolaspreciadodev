🚀 GoSport: Fase 2 - Lógica y Datos (Continuación)
1. Activación de Modelos y Datos
[x] Modelado de Roles: Completar usuarios/models.py usando AbstractUser. Definir roles: DUEÑO y DEPORTISTA.

[x] Poblado de Canchas (Seeding): Crear canchas/management/commands/seed_data.py para llenar el diseño actual con 10 canchas reales y fotos de prueba.

[x] Relación de Negocio: Asegurar que el modelo Reserva en negocio/models.py esté vinculado correctamente a los usuarios y las canchas ya creadas.

2. Motor de Reservas (Funcionalidad Crítica)
[x] Validación de Horarios (Overlap): Implementar lógica en Reserva.clean() para evitar que se reserve la misma cancha en el mismo bloque horario.

[x] Formulario de Reserva: Crear la vista en negocio/views.py para que el botón "Reservar" de la interfaz verde neón funcione de verdad.

3. Control de Acceso (Permisos)
[x] Redirección de Dashboard: Configurar que al loguearse, el DUEÑO vaya a su gestión y el DEPORTISTA a la vista de grid de canchas.

[x] Protección de Rutas: Aplicar los roles para que un Deportista no pueda borrar canchas ni un Dueño hacer reservas para otros.

4. Automatización de Facturas
[x] Signals de Django: Configurar que cada vez que se cree una Reserva, se genere automáticamente una Factura en la app negocio.