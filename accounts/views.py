from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegisterForm, LoginForm


# ✅ Register View (تسجيل مستخدم جديد)
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # ✉️ إرسال رسالة ترحيب عبر البريد الإلكتروني
            subject = "Welcome to Rose Store 🌸"
            message = f"Hello {user.username},\n\nYour account has been created successfully at Rose Store! We're happy to have you with us 🌷"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            # 💬 رسالة نجاح داخل الموقع
            messages.success(request, f"🎉 Account created successfully! Welcome, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "❌ Please correct the errors below and try again.")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


# ✅ Login View (تسجيل الدخول)
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # ✉️ إرسال رسالة تأكيد تسجيل الدخول
            subject = "تم تسجيل الدخول إلى Rose Store 🌼"
            message = f"Hello {user.username},\n\nYou have successfully logged in to your Rose Store account. Enjoy shopping with us 🌸"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            # 💬 رسالة نجاح داخل الموقع
            messages.success(request, f"👋 Welcome back, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "❌ Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


# ✅ Logout View (تسجيل الخروج)
def logout_view(request):
    logout(request)
    messages.info(request, "🚪 You have logged out successfully.")
    return redirect("home")
