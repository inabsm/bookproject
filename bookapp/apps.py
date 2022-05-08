from django.apps import AppConfig


class BookappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookapp'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


    def ready(self):
        import users.signals # noqa