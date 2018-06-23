from kangaroo.settings import *

ALLOWED_HOSTS = ['*']
DEBUG = False
INSTALLED_APPS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'qwerty123',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}