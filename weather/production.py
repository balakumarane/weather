from .settings import *

STATIC_URL = "https://rawgit.com/balakumarane/weather/master/v2.0/static/"

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'weather',
            'USER': 'weather',
            'PASSWORD': 'weather',
            'HOST': 'postgres_db',
            'PORT': '5432',
        }
}

DEBUG=False
