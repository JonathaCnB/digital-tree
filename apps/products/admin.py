from django.contrib import admin

from apps.products.models import Group, Product, SubGroup


@admin.register(SubGroup)
class SubGroupAdmin(admin.ModelAdmin):
    model = SubGroup
    list_display = ["id", "name", "is_active"]
    list_display_links = "id", "name"
    list_editable = ("is_active",)
    search_fields = ["id", "name"]
    list_per_page = 10


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ["pk", "name", "is_active"]
    list_display_links = "pk", "name"
    list_editable = ("is_active",)
    search_fields = ["pk", "name"]
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["pk", "product", "price", "is_active", "group"]
    list_display_links = "pk", "product", "price"
    list_editable = ("is_active",)
    search_fields = ["pk", "product", "group"]
    list_per_page = 10
