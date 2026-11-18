/* ═══════════════════════════════════════════════════════════
   Mana Hospitals — cinematic scroll hero
   Scrolling through .cine plays the building fly-in frame by frame on a
   <canvas>; the text panels (.cine-step) fade in at their stage.
   Frames: assets/cine/{d|m}/f_001.webp …  (desktop 1280w / mobile 405×720)

   Smoothness: the drawn frame eases toward the scroll position every
   animation frame (instead of jumping), and a gentle zoom tied to scroll
   keeps the picture moving even while later frames are still loading.
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var sec = document.querySelector('.cine');
  if (!sec) return;
  var canvas = sec.querySelector('canvas');
  var ctx = canvas.getContext('2d');
  var steps = Array.prototype.slice.call(sec.querySelectorAll('.cine-step'));
  var bar = sec.querySelector('.cine-bar i');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var mobile = window.matchMedia('(max-width: 720px)').matches;

  var COUNT = +sec.dataset.frames || 96;
  /* phones: stop before the camera gets so close the rooftop sign leaves the upright crop */
  var LAST = mobile ? Math.round((COUNT - 1) * 0.8) : COUNT - 1;
  var dir = 'assets/cine/' + (mobile ? 'm' : 'd') + '/f_';
  var frames = new Array(COUNT);
  var shown = 0;          // eased (fractional) frame position
  var target = 0;         // frame the scroll position asks for
  var progress = 0;       // 0..1 through the section
  var zoomNow = 1;
  var drawnKey = '';
  var running = false;

  function src(i) { return dir + String(i + 1).padStart(3, '0') + '.webp'; }
  function ok(im) { return im && im.complete && im.naturalWidth; }

  /* nearest loaded frame to i */
  function nearest(i) {
    if (ok(frames[i])) return frames[i];
    for (var d = 1; d < COUNT; d++) {
      if (ok(frames[i - d])) return frames[i - d];
      if (ok(frames[i + d])) return frames[i + d];
    }
    return null;
  }

  function size() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = Math.round(canvas.clientWidth * dpr), h = Math.round(canvas.clientHeight * dpr);
    if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; drawnKey = ''; }
    paint();
  }

  function paint() {
    var i = Math.min(COUNT - 1, Math.max(0, Math.round(shown)));
    var img = nearest(i);
    if (!img) return;
    var key = img.src + '|' + zoomNow.toFixed(4) + '|' + canvas.width;
    if (key === drawnKey) return;
    var cw = canvas.width, ch = canvas.height;
    var s = Math.max(cw / img.naturalWidth, ch / img.naturalHeight) * zoomNow;   // cover + zoom
    var w = img.naturalWidth * s, h = img.naturalHeight * s;
    ctx.drawImage(img, (cw - w) / 2, (ch - h) * (mobile ? 0 : 0.25), w, h);   // zoom grows downward on phones so the rooftop sign is never cropped
    drawnKey = key;
  }

  /* ease the shown frame + zoom toward the scroll position */
  function tick() {
    var zoomTarget = 1 + progress * (mobile ? 0.07 : 0.04);
    var df = target - shown, dz = zoomTarget - zoomNow;
    shown += df * 0.18;
    zoomNow += dz * 0.18;
    if (Math.abs(df) < 0.05) shown = target;
    if (Math.abs(dz) < 0.0005) zoomNow = zoomTarget;
    paint();
    if (shown !== target || zoomNow !== zoomTarget) requestAnimationFrame(tick);
    else running = false;
  }
  function kick() { if (!running) { running = true; requestAnimationFrame(tick); } }

  function load(i, cb) {
    var im = new Image();
    im.decoding = 'async';
    im.onload = function () {
      if (cb) cb();
      if (Math.abs(i - Math.round(shown)) < 6) { drawnKey = ''; paint(); }
    };
    im.onerror = function () { if (cb) cb(); };
    im.src = src(i);
    frames[i] = im;
  }

  /* first frame now (fades the poster out), then every 4th so scrubbing works early, then the rest */
  load(0, function () { paint(); sec.classList.add('ready'); });

  if (reduce) {
    steps.forEach(function (s) { s.classList.add('on'); });
    window.addEventListener('resize', size);
    size();
    return;
  }

  var order = [];
  for (var k = 4; k < COUNT; k += 4) order.push(k);
  order.push(COUNT - 1);
  for (var j = 1; j < COUNT; j++) if (j % 4) order.push(j);
  (function next() {
    var batch = order.splice(0, mobile ? 4 : 6);
    if (!batch.length) return;
    var left = batch.length;
    batch.forEach(function (n) { load(n, function () { if (--left === 0) setTimeout(next, 0); }); });
  })();

  /* scroll → progress → target frame + panels */
  var queued = false;
  function update() {
    queued = false;
    var r = sec.getBoundingClientRect();
    var total = sec.offsetHeight - window.innerHeight;
    progress = Math.min(Math.max(-r.top / total, 0), 1);
    target = progress * LAST;
    if (bar) bar.style.transform = 'scaleY(' + progress + ')';
    sec.style.setProperty('--p', progress.toFixed(4));
    steps.forEach(function (s) {
      s.classList.toggle('on', progress >= +s.dataset.from && progress < +s.dataset.to);
    });
    kick();
  }
  window.addEventListener('scroll', function () {
    if (!queued) { queued = true; requestAnimationFrame(update); }
  }, { passive: true });
  /* iOS resizes the viewport as the address bar hides — only redraw, never jump */
  window.addEventListener('resize', function () { size(); update(); });
  size();
  update();
})();
