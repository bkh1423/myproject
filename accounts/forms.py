from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ✅ بدل User بـ get_user_model
User = get_user_model()

# Register Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = ("username", "password")
