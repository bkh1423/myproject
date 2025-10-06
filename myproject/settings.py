from pathlib import Path
import cloudinary

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = "django-insecure-69j4j_189r!vq4#999h5=*&d=x)*$t$m#v6z+mgdnix$t=tb$2"
DEBUG = True
ALLOWED_HOSTS = []

# INSTALLED APPS
INSTALLED_APPS = [
    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Project apps
    "accounts",
    "shop",
    "orders",

    # Cloudinary apps
    "cloudinary",
    "cloudinary_storage",
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLS / WSGI
ROOT_URLCONF = "myproject.urls"
WSGI_APPLICATION = "myproject.wsgi.application"

# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # مجلد القوالب العام
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

# DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# PASSWORD VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# LANGUAGE & TIMEZONE
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA FILES (⚡ سيتم تخزينها على Cloudinary)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# DEFAULT PK FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom User
AUTH_USER_MODEL = "accounts.CustomUser"

# Email Settings (console for development)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@flowerstore.com"

# 🌩 Cloudinary configuration
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dzulhzpmd",
    "API_KEY": "768324173714479",
    "API_SECRET": "YXusWMP9WuMVtP6RwlVAlrNizDA",
}

# ✅ Django 5.2+ STORAGES system
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    },
}

# ⚡ إعداد Cloudinary مباشرة (مهم لتفادي Must supply cloud_name)
cloudinary.config( 
    cloud_name = "dzulhzpmd", 
    api_key = "768324173714479", 
    api_secret = "YXusWMP9WuMVtP6RwlVAlrNizDA", 
    secure = True
)
