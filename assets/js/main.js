// Mobile navigation toggle
(function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('is-open', !open);
  });
})();

// Mapa Google ładowana dopiero po kliknięciu (bez łączenia z Google przy wejściu na stronę)
(function () {
  document.querySelectorAll('.js-map-load').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('.map-consent');
      var f = document.createElement('iframe');
      f.src = box.getAttribute('data-map-src');
      f.title = box.getAttribute('data-map-title');
      f.loading = 'lazy';
      f.referrerPolicy = 'no-referrer-when-downgrade';
      box.replaceWith(f);
      f.focus();
    });
  });
})();
