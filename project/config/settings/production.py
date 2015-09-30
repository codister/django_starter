from __future__ import absolute_import

from .base import *  # noqa

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'u%##f(g^-6t$40_gf)z2ic$!7q)lt^!v5jg6h##($n%hr!o@(k'
ALLOWED_HOSTS = ['djangostarter.com']

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

STATIC_ROOT = normpath(join(DJANGO_ROOT, '../../static'))
MEDIA_ROOT = normpath(join(DJANGO_ROOT, '../../media'))

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'my_mandrill_config@gmail.com'
EMAIL_HOST_PASSWORD = 'my_mandrill_password'

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True  # disable if using Markitup
X_FRAME_OPTIONS = 'DENY'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': normpath(join(DJANGO_ROOT, '../../logs', 'django.log')),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s [%(name)s:%(lineno)s] %(message)s',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
