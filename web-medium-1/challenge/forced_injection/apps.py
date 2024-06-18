from django.apps import AppConfig


class ForcedInjectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forced_injection'
