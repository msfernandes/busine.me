# -*- coding: utf-8 -*-

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)

DJANGO_PLUGINS = (
    'django_gravatar',
    'django_extensions',
)

BUSINEME_APPS = (
    'defaults',
    'importer',
    'authentication',
    'home',
    'core',
    'api',
)

INSTALLED_APPS = DJANGO_APPS + DJANGO_PLUGINS + BUSINEME_APPS
