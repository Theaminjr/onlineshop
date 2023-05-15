from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Sale

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'full_name', 'phone_number', 'is_active', 'is_staff', 'is_superuser','is_productmanager','is_staff','is_operator']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Sale)