from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product


# 🏠 الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')


# 🛍️ عرض كل المنتجات
def product_list(request):
    products = Product.objects.all().select_related('category')
    return render(request, 'shop/product_list.html', {'products': products})


# ➕ إضافة المنتج إلى السلة ثم الانتقال مباشرة إلى السلة
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get("cart", {})

    # إذا المنتج موجود مسبقًا، زيد الكمية
    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1
    else:
        cart[str(product_id)] = {
            "name": product.name,
            "price": float(product.price),
            "quantity": 1,
            "image": str(product.image.url) if product.image else "",
        }

    request.session["cart"] = cart
    messages.success(request, f"✅ {product.name} added to your cart.")
    return redirect("cart_view")  # ✅ ينتقل مباشرة إلى صفحة السلة


# 🧾 عرض السلة
def cart_view(request):
    cart = request.session.get("cart", {})
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    return render(request, "shop/cart.html", {"cart": cart, "total": total})


# ❌ حذف منتج من السلة
def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session["cart"] = cart
        messages.info(request, "🗑️ Item removed from cart.")
    return redirect("cart_view")
