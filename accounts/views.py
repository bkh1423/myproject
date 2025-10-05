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
            messages.success(request, "✅ Account has been created successfully 🎉")
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
            messages.success(request, f"👋 Welcome back, {user.username}!")
            return redirect("/")
        else:
            messages.error(request, "❌ Invalid username or password")
    else:
        form = SimpleAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "🚪 You have been logged out successfully")
    return redirect("/")
