from django.apps import AppConfig


class StocksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.stocks'
    verbose_name = "Estoque"
    verbose_name_plural = "Estoques"
