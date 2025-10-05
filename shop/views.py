from django.shortcuts import render
from .models import Product


# الصفحة الرئيسية (موجودة عندك سابقاً)
def home(request):
    return render(request, 'home.html')


# عرض كل المنتجات
def product_list(request):
    products = Product.objects.all().select_related('category')
    return render(request, 'shop/product_list.html', {'products': products})
