import os
from .settings import BASE_DIR

#Django Progressive Web Application settings
PWA_APP_NAME = 'Weather'
PWA_APP_DESCRIPTION = "Weather Details of chennai"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
STATIC_IMAGE_URL = 'https://bk.sytes.net/weather-static/'
PWA_APP_ICONS = [
    {
        'src': STATIC_IMAGE_URL+'images/bk_160.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': STATIC_IMAGE_URL+'images/bk_640.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'weather_app/static/js/', 'serviceworker.js')
