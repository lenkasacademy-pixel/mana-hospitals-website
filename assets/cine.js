/* ═══════════════════════════════════════════════════════════
   Mana Hospitals — cinematic scroll hero
   Scrolling through .cine plays the building fly-in frame by frame on a
   <canvas>; the text panels (.cine-step) fade in at their stage.
   Frames: assets/cine/{d|m}/f_001.webp …  (desktop 1280w / mobile 405×720)

   Performance (phones):
   • frames are pre-decoded to ImageBitmaps off the main thread, so drawing is a cheap blit
   • canvas resolution matches the frame resolution (no 2× upscaling work)
   • the canvas is only redrawn when the frame number changes; zoom is a CSS transform
   • the darkening layer and scroll hint use opacity (compositor-only), never repaint
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var sec = document.querySelector('.cine');
  if (!sec) return;
  var canvas = sec.querySelector('canvas');
  var ctx = canvas.getContext('2d', { alpha: false });
  var steps = Array.prototype.slice.call(sec.querySelectorAll('.cine-step'));
  var bar = sec.querySelector('.cine-bar i');
  var dim = sec.querySelector('.cine-dim');
  var hint = sec.querySelector('.cine-hint');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var mobile = window.matchMedia('(max-width: 720px)').matches;

  var COUNT = +sec.dataset.frames || 96;
  /* phones: stop before the camera gets so close the rooftop sign leaves the upright crop */
  var LAST = mobile ? Math.round((COUNT - 1) * 0.8) : COUNT - 1;
  var dir = 'assets/cine/' + (mobile ? 'm' : 'd') + '/f_';
  var bmp = new Array(COUNT);      // decoded frames (ImageBitmap or decoded <img>)
  var shown = 0, target = 0, progress = 0, zoomNow = 1;
  var drawnSrc = null, running = false;
  var canBitmap = 'createImageBitmap' in window;

  function src(i) { return dir + String(i + 1).padStart(3, '0') + '.webp'; }

  function nearest(i) {
    if (bmp[i]) return bmp[i];
    for (var d = 1; d < COUNT; d++) {
      if (bmp[i - d]) return bmp[i - d];
      if (bmp[i + d]) return bmp[i + d];
    }
    return null;
  }

  function size() {
    /* match the frame resolution: phones draw at 1× (frames are 405px wide), desktop ≤1.5× */
    var dpr = mobile ? 1 : Math.min(window.devicePixelRatio || 1, 1.5);
    var w = Math.round(canvas.clientWidth * dpr), h = Math.round(canvas.clientHeight * dpr);
    if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; drawnSrc = null; }
    paint(true);
  }

  function paint(force) {
    var i = Math.min(COUNT - 1, Math.max(0, Math.round(shown)));
    var img = nearest(i);
    if (!img || (!force && img === drawnSrc)) return;
    var iw = img.width, ih = img.height, cw = canvas.width, ch = canvas.height;
    var s = Math.max(cw / iw, ch / ih), w = iw * s, h = ih * s;
    ctx.drawImage(img, (cw - w) / 2, (ch - h) * 0.4, w, h);
    drawnSrc = img;
  }

  /* ease toward the scroll position; zoom is a GPU transform, not a redraw */
  function tick() {
    var zoomTarget = 1 + progress * (mobile ? 0.07 : 0.04);
    var df = target - shown, dz = zoomTarget - zoomNow;
    shown += df * 0.22;
    zoomNow += dz * 0.22;
    if (Math.abs(df) < 0.05) shown = target;
    if (Math.abs(dz) < 0.0005) zoomNow = zoomTarget;
    paint(false);
    canvas.style.transform = 'scale(' + zoomNow.toFixed(4) + ')';
    if (shown !== target || zoomNow !== zoomTarget) requestAnimationFrame(tick);
    else running = false;
  }
  function kick() { if (!running) { running = true; requestAnimationFrame(tick); } }

  function store(i, decoded, cb) {
    bmp[i] = decoded;
    if (Math.abs(i - Math.round(shown)) < 6) paint(true);
    if (cb) cb();
  }

  function load(i, cb) {
    var im = new Image();
    im.decoding = 'async';
    im.onload = function () {
      if (canBitmap) {
        createImageBitmap(im).then(function (b) { store(i, b, cb); }, function () { store(i, im, cb); });
      } else if (im.decode) {
        im.decode().then(function () { store(i, im, cb); }, function () { store(i, im, cb); });
      } else store(i, im, cb);
    };
    im.onerror = function () { if (cb) cb(); };
    im.src = src(i);
  }

  load(0, function () { paint(true); sec.classList.add('ready'); });

  if (reduce) {
    steps.forEach(function (s) { s.classList.add('on'); });
    window.addEventListener('resize', size);
    size();
    return;
  }

  /* every 4th frame first so scrubbing works early, then fill in */
  var order = [];
  for (var k = 4; k <= LAST; k += 4) order.push(k);
  order.push(LAST);
  for (var j = 1; j < COUNT; j++) if (j % 4 && order.indexOf(j) < 0) order.push(j);
  (function next() {
    var batch = order.splice(0, mobile ? 3 : 6);
    if (!batch.length) return;
    var left = batch.length;
    batch.forEach(function (n) { load(n, function () { if (--left === 0) setTimeout(next, 16); }); });
  })();

  var lastOn = null, queued = false;
  function update() {
    queued = false;
    var r = sec.getBoundingClientRect();
    var total = sec.offsetHeight - window.innerHeight;
    progress = Math.min(Math.max(-r.top / total, 0), 1);
    target = progress * LAST;
    if (bar) bar.style.transform = 'scaleY(' + progress.toFixed(3) + ')';
    if (dim) dim.style.opacity = (progress * 0.5).toFixed(3);
    if (hint) hint.style.opacity = Math.max(0, 1 - progress * 12).toFixed(2);
    var on = null;
    for (var n = 0; n < steps.length; n++) {
      if (progress >= +steps[n].dataset.from && progress < +steps[n].dataset.to) { on = steps[n]; break; }
    }
    if (on !== lastOn) {                       // only touch classes when the panel actually changes
      if (lastOn) lastOn.classList.remove('on');
      if (on) on.classList.add('on');
      lastOn = on;
    }
    kick();
  }
  window.addEventListener('scroll', function () {
    if (!queued) { queued = true; requestAnimationFrame(update); }
  }, { passive: true });
  var rz;
  window.addEventListener('resize', function () {   // phone toolbars resize the viewport while scrolling
    clearTimeout(rz); rz = setTimeout(function () { size(); update(); }, 120);
  });
  size();
  update();
})();
