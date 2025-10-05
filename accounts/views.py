# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import NoValidationUserCreationForm, CustomAuthenticationForm

def register_view(request):
    if request.method == "POST":
        form = NoValidationUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "✅ تم إنشاء الحساب بنجاح 🎉")
            return redirect("/")
    else:
        form = NoValidationUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 أهلاً بك يا {user.username}")
            return redirect("/")
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "🚪 تم تسجيل الخروج بنجاح")
    return redirect("/")


