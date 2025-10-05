from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔹 لوحة التحكم
    path("admin/", admin.site.urls),

    # 🔹 الصفحة الرئيسية (تجي من تطبيق shop)
    path("", include("shop.urls")),       

    # 🔹 حسابات المستخدمين (Register / Login / Logout)
    path("accounts/", include("accounts.urls")),

    # 🔹 الطلبات
    path("orders/", include("orders.urls")),
]

# 🔹 إعدادات رفع وعرض الملفات (مثلاً صور المنتجات)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


