"""
Settings used ONLY on development environment
"""

# SECURITY WARNING: don't run with debug turned on in production!
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books_db',
        'USER': 'root',
        'PASSWORD': '1amhated',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
        'connect_timeout': 500
    }
}

SITE_DOMAIN = 'http://localhost:8000'

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = os.path.realpath(here(".."))
root = lambda *x: os.path.realpath(os.path.join(os.path.abspath(PROJECT_ROOT), *x))

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
