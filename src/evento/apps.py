from django.apps import AppConfig


class EventoConfig(AppConfig):
    name = 'evento'

    def ready(self):
        from . import signals