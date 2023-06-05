from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Sale,Address
from .forms import CustomUserChangeForm,CustomUserCreationForm

"custom admin panel for the custom user"
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    ordering = ['email']
    fieldsets = (
        (None, {"fields": ("email", "password","phone_number")}),
        ("Permissions", {"fields": ("is_staff", "is_active","is_supervisor","is_operator","is_productmanager", "groups", "user_permissions")}),
    )    
    list_display = ['email', 'full_name', 'phone_number', 'is_active', 'is_staff', 'is_superuser','is_productmanager','is_staff','is_operator']


admin.site.register(User,CustomUserAdmin)
admin.site.register(Sale)
admin.site.register(Address)