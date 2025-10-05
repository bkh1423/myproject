from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm


# تسجيل مستخدم جديد
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "✅ تم إنشاء الحساب بنجاح 🎉")
            return redirect("/")  # رجوع للصفحة الرئيسية
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# تسجيل دخول
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "👋 أهلاً بك من جديد يا " + user.username)
            return redirect("/")  # رجوع للصفحة الرئيسية
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# تسجيل خروج
def logout_view(request):
    logout(request)
    messages.info(request, "🚪 تم تسجيل الخروج بنجاح")
    return redirect("/")


