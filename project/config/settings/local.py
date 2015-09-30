from __future__ import absolute_import

from .base import *  # noqa


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = 'local_not_secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'starter',
        'USER': 'starter',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = normpath(join(DJANGO_ROOT, '../static'))  # only used for collectstatic
MEDIA_ROOT = normpath(join(DJANGO_ROOT, '../media'))

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
