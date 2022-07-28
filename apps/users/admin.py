from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import Profile, User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["pkid", "user", "is_active"]
    list_display_links = "pkid", "user"
    list_editable = ("is_active",)
    search_fields = ["id", "user", "company"]
    list_per_page = 10
