from django.contrib import admin

from apps.stocks.models import Iten, Moviment


@admin.register(Moviment)
class MovimentAdmin(admin.ModelAdmin):
    model = Moviment
    list_display = ["pk", "moviment", "profile", "is_active"]
    list_display_links = "pk", "moviment"
    list_editable = ("is_active",)
    search_fields = ["pk", "moviment", "profile"]
    list_per_page = 10


@admin.register(Iten)
class ItenAdmin(admin.ModelAdmin):
    model = Iten
    list_display = ["pk", "moviment", "product", "qty", "stock", "is_active"]
    list_display_links = "pk", "moviment"
    list_editable = ("is_active",)
    search_fields = ["pk", "moviment", "product"]
    list_per_page = 10
