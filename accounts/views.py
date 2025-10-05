from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SimpleUserCreationForm, SimpleAuthenticationForm


def register_view(request):
    if request.method == "POST":
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "✅ تم إنشاء الحساب بنجاح 🎉")
            return redirect("/")
    else:
        form = SimpleUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = SimpleAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 أهلاً {user.username}")
            return redirect("/")
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة")
    else:
        form = SimpleAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "🚪 تم تسجيل الخروج")
    return redirect("/")
