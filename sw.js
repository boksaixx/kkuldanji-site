/* 꿀단지 service worker — 정적 파일은 캐시, 페이지는 네트워크 우선(새 호가 바로 보이게) */
const VER = 'kkuldanji-v1';
const ASSETS = ['/', '/index.html', '/style.css', '/gate.js', '/config.js', '/manifest.webmanifest',
  '/icons/icon-192.png', '/icons/icon-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(VER).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VER).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  const isPage = req.mode === 'navigate' || req.destination === 'document';
  if (isPage) {
    e.respondWith(fetch(req).then(r => { caches.open(VER).then(c => c.put(req, r.clone())); return r; })
      .catch(() => caches.match(req).then(r => r || caches.match('/index.html'))));
  } else {
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => { caches.open(VER).then(c => c.put(req, res.clone())); return res; })));
  }
});
