from django.apps import AppConfig


class ReaderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reader'

   # def ready(self):
    #    from articleUpdater import updater
     #   updater.start()
