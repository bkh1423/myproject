from django.db import models
from django.contrib.auth.models import AbstractUser

# مبدئيًا نستخدم نظام المستخدم الافتراضي
# وإذا احتجت مستقبلاً توسّع البروفايل ممكن تعمل موديل منفصل
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
