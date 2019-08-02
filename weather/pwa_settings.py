#Django Progressive Web Application settings
DEFAULT_FILE_STORAGE="minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE="minio_storage.storage.MinioStaticStorage"
MINIO_STORAGE_ENDPOINT="bk.sytes.net"
MINIO_STORAGE_ACCESS_KEY="balakumaran"
MINIO_STORAGE_SECRET_KEY="yajiv@92"
MINIO_STORAGE_USE_HTTPS=True
MINIO_STORAGE_MEDIA_BUCKET_NAME="weather-media"
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET=True
MINIO_STORAGE_STATIC_BUCKET_NAME = 'weather-static'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True

PWA_APP_NAME = 'Weather'
PWA_APP_DESCRIPTION = "Weather Details of chennai"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': STATIC_URL+'images/bk_160.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': STATIC_URL+'images/bk_640.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'weather_app/static/js/', 'serviceworker.js')
