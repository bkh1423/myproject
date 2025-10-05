from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# تسجيل مستخدم جديد
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل الدخول مباشرة بعد إنشاء الحساب
            return redirect("/")  # رجّعه للصفحة الرئيسية أو أي مسار آخر
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# تسجيل دخول
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# تسجيل خروج (إضافة اختيارية)
def logout_view(request):
    logout(request)
    return redirect("/")
