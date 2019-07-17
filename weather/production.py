from .settings import *

# STATIC_URL = "https://rawgit.com/balakumarane/weather/v2.0/weather_app/static/" 

STATIC_URL = "https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/"

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
