from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # نخلي الإيميل مطلوب وفريد
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
