# -*- encoding: utf-8 -*-
from .base import *
from django.utils.translation import ugettext_lazy as _

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),#os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child('media')
STATIC_ROOT = BASE_DIR.child('content')
