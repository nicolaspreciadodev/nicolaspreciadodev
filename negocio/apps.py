from django.apps import AppConfig

class NegocioConfig(AppConfig):
    name = 'negocio'

    def ready(self):
        import negocio.signals
