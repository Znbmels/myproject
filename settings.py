import os
from pathlib import Path
from datetime import timedelta
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# Базовый путь проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'app',  # Наше приложение
]

# Добавление sslserver только в режиме DEBUG
if DEBUG:
    INSTALLED_APPS.append('sslserver')
# Настройки безопасности
SECRET_KEY = 'your-secret-key-here'  # Замените на реальный секретный ключ

if DEBUG:
    # Настройки для локальной разработки
    ALLOWED_HOSTS = [
        'localhost',       # Для локального тестирования
        '127.0.0.1',       # Для локального тестирования
        '0.0.0.0',         # Для Docker (если используется)
    ]
else:
    # Настройки для продакшена
    ALLOWED_HOSTS = [
        'tahfiz.halalguide.me',  # Ваш домен
        '37.27.216.212',         # Ваш IPv4-адрес
        'django_app',            # Имя контейнера (если используется внутри Docker)
    ]

# Дополнительные настройки безопасности для продакшена
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        "https://tahfiz.halalguide.me",
        "http://tahfiz.halalguide.me",  # Если сайт доступен по HTTP
    ]
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Для работы через Cloudflare
    SECURE_SSL_REDIRECT = True  # Перенаправление HTTP -> HTTPS
    SESSION_COOKIE_SECURE = True  # Cookies только через HTTPS
    CSRF_COOKIE_SECURE = True  # CSRF-токены только через HTTPS

# Промежуточные слои (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основной URL-конфиг
ROOT_URLCONF = 'my_project.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение
WSGI_APPLICATION = 'my_project.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Проверка паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Международизация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Настройки REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Настройки JWT

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=35),
}

AUTH_USER_MODEL = 'app.User'
