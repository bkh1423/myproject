from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحة المتجر الرئيسية (home.html) من تطبيق shop
    path('', include('shop.urls')),       

    # روابط الحسابات (تسجيل / دخول / خروج)
    path('accounts/', include('accounts.urls')),

    # روابط الطلبات
    path('orders/', include('orders.urls')),
]

# إعدادات الملفات الإعلامية (صور المنتجات مثلاً)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

