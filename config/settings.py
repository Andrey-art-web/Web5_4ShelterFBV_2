"""
Django settings for config project.
"""

import os
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-h3juwn^%y@-jiwjtib&1y7&_8ba$%tqr043s&q%v@0lg*a_duv'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'dogs',
    # Сторонние приложения
    # 'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# ========== НАСТРОЙКА БАЗЫ ДАННЫХ ДЛЯ SQL SERVER 2022 ==========
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'WEB524ShelterFBV',  # ← Это имя базы
        'USER': 'Andre',
        'PASSWORD': 'se101da0',
        'HOST': r'DESKTOP-F448OPL\SQLEXPRESS02',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'extra_params': "TrustServerCertificate=yes",
        },
    }
}
USE_TZ = False  # ← ОБЯЗАТЕЛЬНО!

# ========== ВАЖНЫЕ НАСТРОЙКИ ДЛЯ SQL SERVER ==========
TIME_ZONE = 'Europe/Moscow'

# DATABASES = {
#    'default': {
#    'ENGINE': 'django.db.backends.sqlite3',
#    'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

# Password validation
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

LANGUAGE_CODE = 'ru-ru'
USE_I18N = True

STATIC_URL = 'static/'
STATIC_DIRS = (
    BASE_DIR / 'static',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = (
    BASE_DIR / 'media'
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'