from django.apps import AppConfig


class usersConfig(AppConfig):
    name = "users"

    def ready(self):
        from users import signals  # noqa: F401
