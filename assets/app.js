/* ═══════════════════════════════════════════════════════════
   Mana Hospitals — shared behaviour
   Every block is guarded so the same file runs on every page.
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ── year ─────────────────────────────────────────────── */
  $$('#yr, .yr').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ── scroll: progress, nav hide/show, sticky bar ──────── */
  var nav = $('#nav'), prog = $('#prog'), sbar = $('#sbar'), last = 0, ticking = false;

  function onScroll() {
    var y = window.scrollY,
        h = document.documentElement.scrollHeight - window.innerHeight;
    if (prog) prog.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
    if (nav) {
      nav.classList.toggle('stuck', y > 10);
      nav.classList.toggle('hid', y > 420 && y > last);
    }
    if (sbar) sbar.classList.toggle('up', y > 400);
    last = y;
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  /* ── mobile menu ──────────────────────────────────────── */
  var burger = $('#burger'), mm = $('#mmenu');
  if (burger && mm) {
    var mmLinks = $$('a', mm);
    burger.addEventListener('click', function () {
      var open = mm.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.style.overflow = open ? 'hidden' : '';
      mmLinks.forEach(function (a, i) {
        a.style.transitionDelay = open ? (120 + i * 55) + 'ms' : '0ms';
      });
    });
    mm.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        mm.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mm.classList.contains('open')) burger.click();
    });
  }

  /* ── hero cursor glow (desktop only) ──────────────────── */
  var glow = $('#glow'), hero = $('.hero');
  if (glow && hero && window.matchMedia('(hover:hover)').matches && !reduce) {
    hero.addEventListener('mousemove', function (e) {
      var r = hero.getBoundingClientRect();
      glow.style.left = (e.clientX - r.left) + 'px';
      glow.style.top  = (e.clientY - r.top) + 'px';
    });
  }

  /* ── seamless marquees ────────────────────────────────── */
  $$('.drow').forEach(function (el) { el.innerHTML += el.innerHTML; });

  /* ── reveal on scroll ─────────────────────────────────── */
  var targets = $$('.rise,.pop,.wipe,.ln,.eyebrow,.h2,.shead,.ab-grid');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    targets.forEach(function (t) { io.observe(t); });
  } else {
    targets.forEach(function (t) { t.classList.add('in'); });
  }

  /* above-the-fold content animates straight away */
  requestAnimationFrame(function () {
    $$('#heroTxt .ln, #heroTxt .rise, .bcard, .phero .ln, .phero .rise').forEach(function (el) {
      el.classList.add('in');
    });
  });

  /* ── counters ─────────────────────────────────────────── */
  $$('[data-count]').forEach(function (group) {
    var done = false;
    function run() {
      if (done) return; done = true;
      $$('[data-to]', group).forEach(function (el) {
        var to = +el.dataset.to, suf = el.dataset.suf || '', t0 = null, dur = 1500;
        if (reduce) { el.textContent = to + suf; return; }
        (function step(t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / dur, 1);
          el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))) + suf;
          if (p < 1) requestAnimationFrame(step);
        })(performance.now());
      });
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (en) { if (en.isIntersecting) run(); });
      }, { threshold: 0.4 }).observe(group);
    } else run();
  });

  /* ── doctor / department filter ───────────────────────── */
  var grid = $('#dgrid');
  if (grid) {
    var chips = $$('.chip'), cards = $$('.doc', grid);
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var f = chip.dataset.f;
        chips.forEach(function (c) { c.setAttribute('aria-pressed', c === chip); });
        cards.forEach(function (d, i) {
          if (f === 'all' || d.dataset.c === f) {
            d.classList.remove('gone');
            requestAnimationFrame(function () {
              setTimeout(function () { d.classList.remove('out'); }, i * 26);
            });
          } else {
            d.classList.add('out');
            setTimeout(function () {
              if (d.classList.contains('out')) d.classList.add('gone');
            }, 320);
          }
        });
      });
    });
  }

  /* ── live search (doctors page) ───────────────────────── */
  var search = $('#docSearch');
  if (search && grid) {
    var all = $$('.doc', grid), empty = $('#noResults');
    search.addEventListener('input', function () {
      var q = search.value.trim().toLowerCase(), hits = 0;
      all.forEach(function (d) {
        var match = !q || d.textContent.toLowerCase().indexOf(q) > -1;
        d.classList.toggle('gone', !match);
        d.classList.toggle('out', !match);
        if (match) hits++;
      });
      if (empty) empty.style.display = hits ? 'none' : 'block';
    });
  }

  /* ── accordions ───────────────────────────────────────── */
  $$('.q').forEach(function (q) {
    var btn = $('.q-btn', q), body = $('.q-body', q);
    if (!btn || !body) return;
    btn.addEventListener('click', function () {
      var open = q.dataset.open === 'true';
      var scope = q.closest('.faqw') || document;
      $$('.q', scope).forEach(function (o) {
        if (o !== q && o.dataset.open === 'true') {
          o.dataset.open = 'false';
          $('.q-btn', o).setAttribute('aria-expanded', 'false');
          $('.q-body', o).style.height = '0px';
        }
      });
      q.dataset.open = open ? 'false' : 'true';
      btn.setAttribute('aria-expanded', String(!open));
      body.style.height = open ? '0px' : body.scrollHeight + 'px';
    });
  });
  window.addEventListener('resize', function () {
    $$('.q[data-open="true"] .q-body').forEach(function (b) { b.style.height = b.scrollHeight + 'px'; });
  });

  /* ── booking forms → WhatsApp handoff ─────────────────── */
  $$('form[data-book]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn  = $('button[type="submit"]', form),
          name = (form.querySelector('[name="name"]') || {}).value || '',
          dept = (form.querySelector('[name="dept"]') || {}).value || '',
          when = (form.querySelector('[name="when"]') || {}).value || '',
          txt  = btn.innerHTML;

      btn.innerHTML = 'Request received ✓';
      btn.style.background = '#1FA855';

      var msg = 'Hello Mana Hospitals, this is ' + name.trim() + '.'
              + (dept ? ' I would like to book an appointment for ' + dept + '.' : ' I would like to book an appointment.')
              + (when ? ' Preferred time: ' + when + '.' : '');

      setTimeout(function () {
        btn.innerHTML = txt; btn.style.background = ''; form.reset();
        window.open('https://wa.me/917995895858?text=' + encodeURIComponent(msg), '_blank');
      }, 1400);
    });
  });

  /* ── mark the current page in the nav ─────────────────── */
  var here = location.pathname.split('/').pop() || 'index.html';
  $$('.nlinks a, .mmenu a').forEach(function (a) {
    var href = (a.getAttribute('href') || '').split('#')[0];
    if (href && href === here) a.setAttribute('aria-current', 'page');
  });
})();
