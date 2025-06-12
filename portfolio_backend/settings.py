from pathlib import Path
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = []

# ✅ 1. Installed apps (include your app and staticfiles)
INSTALLED_APPS = [
    'contactme',  # Your custom app name
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
]

# ✅ 2. Middleware (keep default)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_backend.urls'

# ✅ 3. Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Load from /templates folder
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

WSGI_APPLICATION = 'portfolio_backend.wsgi.application'

# ✅ 4. MongoDB connection using djongo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite for development
       'NAME': BASE_DIR / 'portfolio_contacts.sqlite3',  # You can name your DB anything
    }
}

# ✅ 5. Static files setup (CSS/JS/Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# ✅ 6. Email configuration (Gmail example)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER =  config('EMAIL_HOST_USER')      # <- your Gmail
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')   # <- App Password from Gmail
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER        
print("EMAIL:", EMAIL_HOST_USER)

# ✅ 7. Optional – remove password validators if no login/signup
AUTH_PASSWORD_VALIDATORS = []

# ✅ 8. Optional
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
