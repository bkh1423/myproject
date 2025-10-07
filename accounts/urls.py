from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # 🏠 الصفحة الرئيسية والمنتجات (داخل تطبيق shop)
    path("", include("shop.urls")),

    # 👤 التسجيل وتسجيل الدخول والخروج (داخل تطبيق accounts)
    path("accounts/", include("accounts.urls")),
]

# ⚙️ دعم ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

