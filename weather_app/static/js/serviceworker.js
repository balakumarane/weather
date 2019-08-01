const VERSION = 'v1';

self.addEventListener('install', event => event.waitUntil(installServiceWorker()));


async function installServiceWorker() {

    log("Service Worker installation started ");

    const cache = await caches.open(VERSION);

    return cache.addAll([
      'https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/images/bk_192.png',
      'https://use.fontawesome.com/releases/v5.0.13/css/all.css',
      'https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/css/bootstrap.min.css',
      'https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/css/main.css',
      'https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/images/bk_640.svg',
      'https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/js/jquery-3.3.1.slim.min.js',
      'https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/js/popper.min.js',
      'https://cdn.jsdelivr.net/gh/balakumarane/weather@vv2.0/weather_app/static/js/bootstrap.min.js',
    ]);
}


self.addEventListener('activate', () => activateSW());

async function activateSW() {

    log('Service Worker activated');

    const cacheKeys = await caches.keys();

    cacheKeys.forEach(cacheKey => {
        if (cacheKey !== VERSION ) {
            caches.delete(cacheKey);
        }
    });
}


self.addEventListener('fetch', event => event.respondWith(cacheThenNetwork(event)));

async function cacheThenNetwork(event) {

    const cache = await caches.open(VERSION);

    const cachedResponse = await cache.match(event.request);

    if (cachedResponse) {
        log('Serving From Cache: ' + event.request.url);
        return cachedResponse;
    }

    const networkResponse = await fetch(event.request);

    log('Calling network: ' + event.request.url);

    return networkResponse;
}


// each logging line will be prepended with the service worker version
function log(message) {
    console.log(VERSION, message);
}
