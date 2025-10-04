from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # الحقول اللي تظهر في لوحة التحكم
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    search_fields = ("username", "email", "phone_number")
    list_filter = ("is_staff", "is_active")

