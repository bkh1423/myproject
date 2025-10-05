from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import RegisterForm, LoginForm


# ✅ Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "✅ Account created successfully 🎉")

            # Send welcome email
            if user.email:
                subject = "🌸 Welcome to Rose Store"
                text_content = f"Hello {user.username}, welcome to Rose Store!"
                html_content = f"""
                <html>
                    <body style="font-family: Arial; background:#fdf2f8; padding:20px;">
                        <h2 style="color:#e75480;">🌸 Welcome, {user.username}!</h2>
                        <p>Thank you for creating an account with <b>Rose Store</b>.</p>
                        <p>We hope you enjoy shopping with us!</p>
                        <p style="color:#888;">This is an automated message.</p>
                    </body>
                </html>
                """
                msg = EmailMultiAlternatives(subject, text_content, None, [user.email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


# ✅ Login View
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 Welcome back, {user.username}!")
            return redirect("/")
        else:
            messages.error(request, "❌ Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


# ✅ Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "🚪 You have been logged out successfully")
    return redirect("/")

