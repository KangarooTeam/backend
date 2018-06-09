from kangaroo.settings import *

ALLOWED_HOSTS = ['*']
DEBUG = True
INSTALLED_APPS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}