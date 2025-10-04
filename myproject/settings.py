from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# المفتاح السري (غير مناسب للإنتاج)
SECRET_KEY = 'django-insecure-69j4j_189r!vq4#999h5=*&d=x)*$t$m#v6z+mgdnix$t=tb$2'

# وضع التطوير
DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'accounts',
    'shop',
    'orders',
]

# الـ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف روابط المشروع
ROOT_URLCONF = 'myproject.urls'

# إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # مجلد القوالب الرئيسي
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ملف WSGI
WSGI_APPLICATION = 'myproject.wsgi.application'

# قاعدة البيانات الافتراضية SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# فحص كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# 📌 إعدادات الملفات الثابتة (Static files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",   # مسار مجلد static العام
]
STATIC_ROOT = BASE_DIR / "staticfiles"   # مكان التجميع بعد collectstatic

# 📌 إعدادات الملفات المرفوعة (Media files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# القيمة الافتراضية للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ⚠️ تعريف المستخدم المخصص
AUTH_USER_MODEL = 'accounts.CustomUser'
