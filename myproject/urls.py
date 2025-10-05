from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 الصفحة الرئيسية مرتبطة بتطبيق shop
    path('', include('shop.urls')),           

    # روابط التطبيقات
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

# 📌 دعم عرض ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

