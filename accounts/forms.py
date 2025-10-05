# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class NoValidationUserCreationForm(UserCreationForm):
    """
    فورم تسجيل يتجاهل الـ password validators الافتراضية في Django.
    يتأكد فقط أن الحقلين متطابقين (password1 == password2).
    """
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number", "address", "password1", "password2")

    def _post_clean(self):
        """
        نُطفئ استدعاء التحقق الافتراضي (validate_password) الذي يستند على AUTH_PASSWORD_VALIDATORS.
        لن ندعو super()._post_clean() هنا لكي لا تُفرض قواعد كلمة المرور.
        نحتفظ بباقي تنظيف الفورم كما هو (clean_*).
        """
        # intentionally skip calling super()._post_clean() to avoid password validators
        return

    def clean_password2(self):
        # نتحقق فقط من تطابق الحقلين
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("كلمتا المرور غير متطابقتين.")
        return password2


class CustomAuthenticationForm(AuthenticationForm):
    """
    فورم تسجيل الدخول القياسي (لا حاجة لتعديل هنا، لكن نحتفظ به جاهزًا).
    """
    class Meta:
        model = CustomUser
        fields = ("username", "password")
