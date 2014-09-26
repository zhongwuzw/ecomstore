"""
Django settings for ecomstore project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^8mn2zbg*ho&hrz8x$phs31+gt*$&b7#2-nuh2lwlzd0q4bhj='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = ('utils.context_processors.ecomStore',)
TEMPLATE_CONTEXT_PROCESSORS += global_settings.TEMPLATE_CONTEXT_PROCESSORS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'catalog',
    'utils',
    'cart',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'ecomstore.urls'

SITE_ID = 1

WSGI_APPLICATION = 'ecomstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'zhongwu',
        'PASSWORD' :'123',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}

TEMPLATE_DIRS = (os.path.join(BASE_DIR,'templates'),)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_NAME = 'Modern Musician'
META_KEYWORDS = 'Music,instruments,music accessories,musician supplies'
META_DESCRIPTION = 'Modern Musician is an online supplier of instruments,sheet music,and other accessories for musicians'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#MEDIA_URL = '/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    '/Users/frank/Documents/workspace/ecomstore/static',
                    )