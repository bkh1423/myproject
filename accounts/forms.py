from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class SimpleUserCreationForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=True)  # ✅ إضافة الإيميل
    password = forms.CharField(widget=forms.PasswordInput, label="الرمز")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")  # ✅ صار يشمل الإيميل

    def save(self, commit=True):
        user = super().save(commit=False)
        # تخزين كلمة المرور بشكل مشفر باستخدام set_password
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class SimpleAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = CustomUser
        fields = ("username", "password")
