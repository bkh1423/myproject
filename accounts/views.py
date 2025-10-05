from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm, LoginForm


# Register
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # ✉️ إرسال رسالة إلى البريد المدخل
            subject = "Welcome to Rose Store 🌸"
            message = f"Hello {user.username},\n\nYour account has been created successfully at Rose Store!"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]

            # fail_silently=False يخليك تشوف الغلط لو ما انرسل
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # ✅ رسالة نجاح على الموقع
            messages.success(request, f"🎉 Account created successfully! Welcome {user.username}")
            return redirect("home")  # 👈 يوديه للهوم
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


# Login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 Welcome back, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "❌ Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


# Logout
def logout_view(request):
    logout(request)
    messages.info(request, "🚪 Logged out successfully.")
    return redirect("home")

