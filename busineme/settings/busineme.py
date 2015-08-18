from settings import databases, security, static, apps

ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'

# Security
SECRET_KEY = security.SECRET_KEY
DEBUG = security.DEBUG
ALLOWED_HOSTS = security.ALLOWED_HOSTS

# Applications
INSTALLED_APPS = apps.INSTALLED_APPS
MIDDLEWARE_CLASSES = apps.MIDDLEWARE_CLASSES

# Static files
TEMPLATES = static.TEMPLATES
STATIC_URL = static.STATIC_URL
STATICFILES_DIRS = static.STATICFILES_DIRS

# Database
DATABASES = databases.DATABASES

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
