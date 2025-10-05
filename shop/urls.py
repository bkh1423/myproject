from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 الصفحة الرئيسية
]

