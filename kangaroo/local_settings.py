from kangaroo.settings import *

ALLOWED_HOSTS = ['*']
DEBUG = False
INSTALLED_APPS
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'test',
            'USER': 'postgres',
            'PASSWORD': 'q319546',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }