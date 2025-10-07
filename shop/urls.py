from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # 🏠 الصفحة الرئيسية
    path("products/", views.product_list, name="product_list"),  # 🛍️ صفحة عرض المنتجات
]


