from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class SimpleUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2")  # فقط يوزر وباسوورد

    def _post_clean(self):
        """
        نتجاوز التحقق من الـ password validators
        عشان أي كلمة مرور تنقبل (حتى لو ضعيفة).
        """
        return


class SimpleAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
