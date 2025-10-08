from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # الحقول اللي تبين في قائمة المستخدمين
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active")

    # صفحة تعديل المستخدم
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # صفحة إضافة مستخدم جديد من الـ admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    # ✉️ نرسل إيميل بعد إنشاء المستخدم من الـ admin
    def save_model(self, request, obj, form, change):
        is_new = obj.pk is None  # إذا كان المستخدم جديد
        super().save_model(request, obj, form, change)

        if is_new:  # فقط عند الإنشاء لأول مرة
            subject = "Welcome to Rose Store 🌸"
            message = f"Hello {obj.username},\n\nYour account has been successfully created at Rose Store! 🌷"
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [obj.email],
                fail_silently=True,
            )
