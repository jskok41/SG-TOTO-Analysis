// Matrix Screensaver Service Worker
// Optimized for iPhone 15 Pro Max iOS 26

const CACHE_NAME = 'matrix-screensaver-v1.0.0';
const urlsToCache = [
  '/matrix-screensaver.html',
  '/manifest.json',
  '/',
  'https://fonts.googleapis.com/css2?family=Courier+New:wght@400;700&display=swap'
];

// Install event - cache resources
self.addEventListener('install', (event) => {
  console.log('Matrix Screensaver SW: Installing...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Matrix Screensaver SW: Caching files');
        return cache.addAll(urlsToCache);
      })
      .catch((error) => {
        console.log('Matrix Screensaver SW: Cache failed', error);
      })
  );
  self.skipWaiting();
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  console.log('Matrix Screensaver SW: Activating...');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Matrix Screensaver SW: Deleting old cache', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  // Skip non-GET requests
  if (event.request.method !== 'GET') {
    return;
  }

  // Skip chrome-extension and other non-http requests
  if (!event.request.url.startsWith('http')) {
    return;
  }

  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Return cached version or fetch from network
        if (response) {
          console.log('Matrix Screensaver SW: Serving from cache', event.request.url);
          return response;
        }

        console.log('Matrix Screensaver SW: Fetching from network', event.request.url);
        return fetch(event.request).then((response) => {
          // Don't cache if not a valid response
          if (!response || response.status !== 200 || response.type !== 'basic') {
            return response;
          }

          // Clone the response
          const responseToCache = response.clone();

          caches.open(CACHE_NAME)
            .then((cache) => {
              cache.put(event.request, responseToCache);
            });

          return response;
        });
      })
      .catch(() => {
        // Return offline page or fallback
        if (event.request.destination === 'document') {
          return caches.match('/matrix-screensaver.html');
        }
      })
  );
});

// Background sync for offline functionality
self.addEventListener('sync', (event) => {
  if (event.tag === 'matrix-screensaver-sync') {
    console.log('Matrix Screensaver SW: Background sync triggered');
    event.waitUntil(
      // Perform background tasks here
      Promise.resolve()
    );
  }
});

// Push notifications (for future enhancements)
self.addEventListener('push', (event) => {
  if (event.data) {
    const data = event.data.json();
    const options = {
      body: data.body,
      icon: '/icon-192x192.png',
      badge: '/icon-96x96.png',
      vibrate: [100, 50, 100],
      data: {
        dateOfArrival: Date.now(),
        primaryKey: 1
      },
      actions: [
        {
          action: 'explore',
          title: 'Open Screensaver',
          icon: '/icon-96x96.png'
        },
        {
          action: 'close',
          title: 'Close',
          icon: '/icon-96x96.png'
        }
      ]
    };

    event.waitUntil(
      self.registration.showNotification(data.title, options)
    );
  }
});

// Notification click handler
self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/matrix-screensaver.html')
    );
  }
});

// Message handler for communication with main thread
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// Periodic background sync (if supported)
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'matrix-screensaver-update') {
    console.log('Matrix Screensaver SW: Periodic sync triggered');
    event.waitUntil(
      // Perform periodic updates here
      Promise.resolve()
    );
  }
});

console.log('Matrix Screensaver SW: Service Worker loaded');