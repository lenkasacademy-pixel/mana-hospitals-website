/* ═══════════════════════════════════════════════════════════
   Mana Hospitals — story-style header for phones (≤720px)
   The building clip loops on its own (hardware video), and the four
   .cine-step messages auto-advance like Instagram Stories:
   progress bars on top, tap right = next, tap left = back,
   press-and-hold = pause. The page scrolls normally — no scroll lock.
   Desktop keeps the scroll-controlled version (assets/cine.js).
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var sec = document.querySelector('.cine');
  if (!sec || !window.matchMedia('(max-width: 720px)').matches) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var stick = sec.querySelector('.cine-stick');
  var steps = Array.prototype.slice.call(sec.querySelectorAll('.cine-step'));
  var DUR = 5200;                       // ms per message
  var idx = 0, paused = false, timer = null, startedAt = 0, elapsed = 0, inView = true;

  sec.classList.add('story');

  /* video behind (only phones download it) */
  var v = document.createElement('video');
  v.className = 'story-video';
  v.muted = true; v.defaultMuted = true; v.loop = true; v.playsInline = true;
  v.setAttribute('muted', ''); v.setAttribute('playsinline', ''); v.setAttribute('aria-hidden', 'true');
  v.preload = 'auto';
  v.poster = 'assets/cine/poster-m.webp';
  v.src = 'assets/cine/hero-m.mp4';
  stick.insertBefore(v, stick.firstChild);
  v.addEventListener('playing', function () { sec.classList.add('ready', 'playing'); });

  /* progress bars */
  var bars = document.createElement('div');
  bars.className = 'story-bars';
  bars.setAttribute('aria-hidden', 'true');
  steps.forEach(function () {
    var b = document.createElement('span');
    b.innerHTML = '<i></i>';
    bars.appendChild(b);
  });
  stick.appendChild(bars);
  var fills = Array.prototype.slice.call(bars.querySelectorAll('i'));

  /* tap zones (sit under the text panels, so buttons/links still work) */
  var tap = document.createElement('div');
  tap.className = 'story-tap';
  tap.setAttribute('aria-hidden', 'true');
  stick.insertBefore(tap, sec.querySelector('.cine-step'));

  function render() {
    steps.forEach(function (s, i) { s.classList.toggle('on', i === idx); });
    fills.forEach(function (f, i) {
      f.style.transition = 'none';
      f.style.transform = 'scaleX(' + (i < idx ? 1 : 0) + ')';
    });
  }

  function run() {
    clearTimeout(timer);
    if (paused || !inView || reduce) return;
    var left = DUR - elapsed;
    var f = fills[idx];
    // force the reset to apply, then animate the remaining part of the bar
    void f.offsetWidth;
    f.style.transition = 'transform ' + left + 'ms linear';
    f.style.transform = 'scaleX(1)';
    startedAt = performance.now();
    timer = setTimeout(function () { go(idx + 1); }, left);
  }

  function freeze() {
    clearTimeout(timer);
    if (startedAt) elapsed = Math.min(DUR, elapsed + (performance.now() - startedAt));
    startedAt = 0;
    var f = fills[idx];
    f.style.transition = 'none';
    f.style.transform = 'scaleX(' + (elapsed / DUR).toFixed(3) + ')';
  }

  function go(n) {
    idx = (n + steps.length) % steps.length;
    elapsed = 0; startedAt = 0;
    render();
    if (!reduce) fills[idx].style.transform = 'scaleX(0)';
    run();
  }

  /* tap: left third = back, rest = next; press & hold = pause */
  var downAt = 0, holdTimer = null, held = false;
  tap.addEventListener('pointerdown', function () {
    downAt = performance.now(); held = false;
    holdTimer = setTimeout(function () { held = true; paused = true; freeze(); v.pause(); }, 220);
  });
  function release(e) {
    clearTimeout(holdTimer);
    if (held) { held = false; paused = false; v.play().catch(function () {}); run(); return; }
    if (!downAt) return;
    downAt = 0;
    var r = tap.getBoundingClientRect();
    go((e.clientX - r.left) < r.width / 3 ? idx - 1 : idx + 1);
  }
  tap.addEventListener('pointerup', release);
  tap.addEventListener('pointercancel', function () {   // finger started scrolling the page
    clearTimeout(holdTimer); downAt = 0;
    if (held) { held = false; paused = false; v.play().catch(function () {}); run(); }
  });

  /* pause when the header is off-screen or the tab is hidden (saves battery/data) */
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      inView = es[0].isIntersecting;
      if (inView) { v.play().catch(function () {}); run(); } else { freeze(); v.pause(); }
    }, { threshold: 0.25 }).observe(sec);
  }
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) { freeze(); v.pause(); } else if (inView) { v.play().catch(function () {}); run(); }
  });

  if (reduce) {
    v.removeAttribute('src'); v.load();       // still poster, no autoplay
    sec.classList.add('ready');
    render();
    return;
  }
  render();
  v.play().catch(function () {});             // muted inline autoplay is allowed on Chrome & Safari
  run();
})();
