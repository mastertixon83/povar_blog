import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-efa^y&0hs28#d4nxhiwees@p@5vqp9^z^!r(x6rcq=n!*hln&c'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'povar_db',
        'USER': 'tixon',
        'PASSWORD': 'gft654gfhgf',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [STATIC_DIR]