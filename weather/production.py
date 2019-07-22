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

#Django Progressive Web Application settings
PWA_APP_ICONS = [
    {
        'src': STATIC_URL+'images/bk_192.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': STATIC_URL+'images/bk_192.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]