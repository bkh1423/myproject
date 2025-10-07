from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # 🏠 الصفحة الرئيسية
    path("products/", views.product_list, name="product_list"),  # 🛍️ قائمة المنتجات

    # 🛒 روابط السلة
    path("cart/", views.cart_view, name="cart"),  # عرض السلة
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),  # إضافة للسلة
    path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),  # حذف من السلة
]
