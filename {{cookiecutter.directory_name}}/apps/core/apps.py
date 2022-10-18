from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'apps.core'
    label = "core"
    
    def ready(self):
        from apps.core.signals import create_or_update_user_profile
