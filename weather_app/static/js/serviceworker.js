const VERSION = 'v3';

self.addEventListener('install', event => event.waitUntil(installServiceWorker()));


async function installServiceWorker() {

    log("Service Worker installation started ");

    const cache = await caches.open(VERSION);

    return cache.addAll([
      'https://use.fontawesome.com/releases/v5.0.13/css/all.css',
      'https://bk.sytes.net/weather-static/css/bootstrap.min.css',
      'https://bk.sytes.net/weather-static/css/main.css',
      'https://bk.sytes.net/weather-static/images/bk_640.svg',
      'https://www.gstatic.com/firebasejs/3.9.0/firebase.js',
      'https://bk.sytes.net/weather-static/js/jquery-3.3.1.slim.min.js',
      'https://bk.sytes.net/weather-static/js/popper.min.js',
      'https://bk.sytes.net/weather-static/js/bootstrap.min.js',
      'https://use.fontawesome.com/releases/v5.0.13/webfonts/fa-solid-900.woff2',
      'https://weather.zapto.org/manifest.json',
      'https://bk.sytes.net/weather-static/images/bk_160.png',
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


// [START initialize_firebase_in_sw]
// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here, other Firebase libraries
// are not available in the service worker.
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.
firebase.initializeApp({
  'messagingSenderId': '945096546130'
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
// [END initialize_firebase_in_sw]

// If you would like to customize notifications that are received in the
// background (Web app is closed or not in browser focus) then you should
// implement this optional method.
// [START background_handler]
messaging.setBackgroundMessageHandler(function(payload) {
  console.log('[serviceworker.js] Received background message ', payload);
  // Customize notification here
  const notificationTitle = 'Background Message Title';
  const notificationOptions = {
    body: 'Background Message body.',
    icon: '/static/images/bk_160.png'
  };

  return self.registration.showNotification(notificationTitle,
      notificationOptions);
});
// [END background_handler]