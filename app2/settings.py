# -*- encoding: utf-8 -*
"""
Django settings for app2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from unipath import Path

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = Path(__file__).ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vuzv4*2-ccd4z=lkc81*$ajok_4*jw!e53_+_ida2e=&8r81$@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.multi',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app2.urls'

WSGI_APPLICATION = 'app2.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _(u'Inglés')),
    ('es', _(u'Español')),
)
# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# )
LOCALE_PATHS = (BASE_DIR.child('locale'),)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
)

STATIC_URL = '/static/'

# from django.conf import settings
# settings.BASE_DIR
# '/home/thom/django16yeo/app2'
# settings.LOCALE_PATHS
# ('/home/thom/django16yeo/app2/locale',)
