from pathlib import Path
import os
import cloudinary
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-fallback")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 🧱 تطبيقات المشروع
    "accounts",
    "shop",
    "orders",

    # ☁️ Cloudinary
    "cloudinary",
    "cloudinary_storage",
]

# ⚙️ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myproject.urls"
WSGI_APPLICATION = "myproject.wsgi.application"

# 🎨 القوالب
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# 🗄️ إعداد قواعد البيانات
DATABASES = {
    # 💻 قاعدة التطوير (محلية)
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },

    # ☁️ قاعدة الإنتاج (PostgreSQL)
    "production": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("PROD_DB_HOST"),
        "PORT": os.getenv("PROD_DB_PORT"),
        "NAME": os.getenv("PROD_DB_NAME"),
        "USER": os.getenv("PROD_DB_USER"),
        "PASSWORD": os.getenv("PROD_DB_PASSWORD"),
    },
}

# ✅ تبديل تلقائي بين البيئتين
if not DEBUG:
    DATABASES["default"] = DATABASES["production"]
    print(" Using PRODUCTION database")
else:
    print(" Using LOCAL database (SQLite)")

# 🔑 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 الإعدادات العامة
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 🧾 الملفات الثابتة والإعلامية
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 👤 نموذج المستخدم المخصص
AUTH_USER_MODEL = "accounts.CustomUser"

# 📧 البريد الإلكتروني
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@flowerstore.com"

# ☁️ Cloudinary
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUD_API_KEY"),
    "API_SECRET": os.getenv("CLOUD_API_SECRET"),
}

STORAGES = {
    "default": {"BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}

# ☁️ إعداد Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("CLOUD_API_KEY"),
    api_secret=os.getenv("CLOUD_API_SECRET"),
    secure=True,
)


