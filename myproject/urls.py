from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('accounts/', include('accounts.urls')),   # تسجيل ودخول وبروفايل
    path('shop/', include('shop.urls')),           # المنتجات والعربة
    path('orders/', include('orders.urls')),       # الطلبات والدفع
]

# 📌 إضافة دعم عرض ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
