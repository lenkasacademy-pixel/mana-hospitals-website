/* ═══════════════════════════════════════════════════════════
   Mana Hospitals — cinematic scroll hero
   Scrolling through .cine plays the building fly-in frame by frame on a
   <canvas>, and the text panels (.cine-step) fade in at their stage.
   Frames: assets/cine/{d|m}/f_001.webp …  (desktop 1280w / mobile 720w)
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
  var dir = 'assets/cine/' + (mobile ? 'm' : 'd') + '/f_';
  var frames = new Array(COUNT);
  var current = -1, target = 0;

  function src(i) { return dir + String(i + 1).padStart(3, '0') + '.webp'; }

  function size() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(canvas.clientWidth * dpr);
    canvas.height = Math.round(canvas.clientHeight * dpr);
    current = -1;
    draw(target);
  }

  /* nearest frame that has finished loading */
  function nearest(i) {
    for (var d = 0; d < COUNT; d++) {
      if (frames[i - d] && frames[i - d].complete && frames[i - d].naturalWidth) return frames[i - d];
      if (frames[i + d] && frames[i + d].complete && frames[i + d].naturalWidth) return frames[i + d];
    }
    return null;
  }

  function draw(i) {
    var img = nearest(i);
    if (!img) return;
    var cw = canvas.width, ch = canvas.height;
    var s = Math.max(cw / img.naturalWidth, ch / img.naturalHeight);   // cover
    var w = img.naturalWidth * s, h = img.naturalHeight * s;
    ctx.drawImage(img, (cw - w) / 2, (ch - h) / 2, w, h);
    current = i;
  }

  function load(i, cb) {
    var im = new Image();
    im.decoding = 'async';
    im.onload = function () { if (cb) cb(); if (Math.abs(i - target) < 3) draw(target); };
    im.src = src(i);
    frames[i] = im;
  }

  /* first frame now, then every 8th (so scrubbing works early), then the rest */
  load(0, function () { draw(0); sec.classList.add('ready'); });
  if (reduce) {
    steps.forEach(function (s) { s.classList.add('on'); });
    window.addEventListener('resize', size);
    size();
    return;
  }
  var order = [];
  for (var k = 8; k < COUNT; k += 8) order.push(k);
  for (var j = 1; j < COUNT; j++) if (j % 8) order.push(j);
  (function next() {
    var batch = order.splice(0, 6);
    if (!batch.length) return;
    var left = batch.length;
    batch.forEach(function (n) { load(n, function () { if (--left === 0) setTimeout(next, 0); }); });
  })();

  /* scroll → progress → frame + panels */
  var ticking = false;
  function update() {
    ticking = false;
    var r = sec.getBoundingClientRect();
    var total = sec.offsetHeight - window.innerHeight;
    var p = Math.min(Math.max(-r.top / total, 0), 1);
    target = Math.min(COUNT - 1, Math.round(p * (COUNT - 1)));
    if (target !== current) draw(target);
    if (bar) bar.style.transform = 'scaleY(' + p + ')';
    sec.style.setProperty('--p', p.toFixed(4));
    steps.forEach(function (s) {
      var a = +s.dataset.from, b = +s.dataset.to;
      s.classList.toggle('on', p >= a && p < b);
    });
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
  window.addEventListener('resize', function () { size(); update(); });
  size();
  update();
})();
