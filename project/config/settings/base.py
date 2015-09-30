# -*- coding: utf-8 -*-

from os.path import abspath, dirname, join, normpath
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

DJANGO_ROOT = dirname(dirname(dirname(abspath(__file__))))

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'my_email_address@gmail.com'

ADMINS = (
    ('My Name', DEFAULT_FROM_EMAIL),
)

MANAGERS = ADMINS

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)

PROJECT_APPS = ('starter_app',)

INSTALLED_APPS += PROJECT_APPS

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

ROOT_URLCONF = 'config.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

WSGI_APPLICATION = 'config.wsgi.application'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', ('English'))
)

STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'static')),
)

TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

