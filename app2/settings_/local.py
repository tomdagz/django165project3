# -*- encoding: utf-8 -*-
from .base import *
from django.utils.translation import ugettext_lazy as _

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app2', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'app2user',
        'PASSWORD': '123456',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child('media')
STATIC_ROOT = BASE_DIR.child('content')
