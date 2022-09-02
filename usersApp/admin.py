from django.contrib import admin
from usersApp.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ["id", "username", "email", "is_active", "is_seller","cart"]


admin.site.register(User, UserAdmin)

# Register your models here.
