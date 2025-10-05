from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 هذا يخلي الرابط / يفتح الصفحة
]

