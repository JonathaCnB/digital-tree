from django.contrib import admin

from apps.core.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ["id", "company", "cnpj", "is_active"]
    list_display_links = "id", "company"
    list_editable = ("is_active",)
    search_fields = ["id", "company", "cnpj"]
    list_per_page = 10
