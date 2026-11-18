/* ═══════════════════════════════════════════════════════════
   Mana Hospitals — motion layer
   Loaded BEFORE app.js (both deferred) so the classes it adds
   are picked up by app.js's reveal observer.
   Everything here is skipped when the visitor prefers reduced motion.
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  document.documentElement.classList.add('js-motion');
  if (reduce) return;

  /* 1 ── headline words rise in one after another */
  $$('.hero h1, .phero h1').forEach(function (h) {
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3 && n.textContent.trim()) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var w = document.createElement('span');
            w.className = 'w';
            w.style.setProperty('--wd', (120 + i++ * 70) + 'ms');
            w.textContent = part;
            frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') {
          walk(n);
        }
      });
    })(h);
    h.classList.add('words');
  });

  /* 2 ── grids reveal card by card */
  $$('.sgrid, .dgrid, .fgrid3, .cgrid, .rel, .srow, .facs, .mdocs, .chips-all, .tl, .faqw').forEach(function (g) {
    Array.prototype.slice.call(g.children).forEach(function (c, i) {
      if (!c.classList.contains('rise')) c.classList.add('rise');
      c.style.setProperty('--d', Math.min(i, 8) * 60 + 'ms');
    });
  });

  /* 3 ── facility strip becomes an endless ticker */
  $$('.strip-row').forEach(function (row) {
    var items = row.innerHTML;
    row.innerHTML = '<div class="tick">' + items + '<span class="tick-gap"></span>' + items + '<span class="tick-gap"></span></div>';
    row.classList.add('ticking');
  });

  /* 4 ── gentle parallax on the hero photo and its floating cards */
  var photo = document.querySelector('.hero .photo img');
  var cards = $$('.hero .fc, .dp-photo .fc');
  if (photo || cards.length) {
    var ticking = false;
    var onScroll = function () {
      var y = Math.min(window.scrollY, 900);
      if (photo) photo.style.transform = 'translate3d(0,' + (y * 0.06) + 'px,0) scale(1.06)';
      cards.forEach(function (c, i) { c.style.translate = '0 ' + (-y * (0.05 + i * 0.03)) + 'px'; });
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
    }, { passive: true });
    onScroll();
  }

  /* 5 ── cards: soft spotlight + slight tilt under the mouse (desktop only) */
  if (fine) {
    $$('.sp, .doc, .fcard, .rel a, .ci, .mdoc').forEach(function (el) {
      el.classList.add('spot');
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        el.style.setProperty('--mx', (x * 100) + '%');
        el.style.setProperty('--my', (y * 100) + '%');
        el.style.setProperty('--rx', ((0.5 - y) * 5) + 'deg');
        el.style.setProperty('--ry', ((x - 0.5) * 6) + 'deg');
      });
      el.addEventListener('pointerleave', function () {
        el.style.setProperty('--rx', '0deg');
        el.style.setProperty('--ry', '0deg');
      });
    });

    /* magnetic primary buttons */
    $$('.btn.b-dark, .btn.b-green').forEach(function (b) {
      b.addEventListener('pointermove', function (e) {
        var r = b.getBoundingClientRect();
        b.style.translate = ((e.clientX - r.left - r.width / 2) * 0.12) + 'px ' + ((e.clientY - r.top - r.height / 2) * 0.2) + 'px';
      });
      b.addEventListener('pointerleave', function () { b.style.translate = ''; });
    });
  }

  /* 6 ── ripple on tap (works on phones) */
  document.addEventListener('pointerdown', function (e) {
    var b = e.target.closest('.btn, .chip, .doc-b');
    if (!b) return;
    var r = b.getBoundingClientRect(), s = Math.max(r.width, r.height) * 1.4;
    var dot = document.createElement('span');
    dot.className = 'ripple';
    dot.style.cssText = 'width:' + s + 'px;height:' + s + 'px;left:' + (e.clientX - r.left - s / 2) + 'px;top:' + (e.clientY - r.top - s / 2) + 'px';
    b.appendChild(dot);
    setTimeout(function () { dot.remove(); }, 650);
  }, { passive: true });
})();
