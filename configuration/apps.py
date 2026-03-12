from django.apps import AppConfig

class ConfigurationConfig(AppConfig):
    name = 'configuration'
    verbose_name = 'Configuration'

    def ready(self):
        import configuration.signals
        