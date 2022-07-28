from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"

    def ready(self, *args, **kwargs) -> None:
        import apps.users.signals  # noqa

        return super().ready(*args, **kwargs)
