from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # 🏠 الصفحة الرئيسية والمنتجات من تطبيق shop
    path("", include("shop.urls")),

    # 👤 تسجيل الدخول/الخروج/التسجيل من تطبيق accounts
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
