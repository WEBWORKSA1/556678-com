/* 556678.com — site interactions (no external dependencies) */
(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Theme ---------- */
  var root = document.documentElement;
  try { var saved = localStorage.getItem('theme'); if (saved) root.setAttribute('data-theme', saved); } catch (e) {}
  var tbtn = $('#themeBtn');
  if (tbtn) tbtn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  /* ---------- Mobile menu ---------- */
  var burger = $('#burger'), menu = $('#menu');
  if (burger && menu) burger.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* ---------- Reveal on scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else { $$('.reveal').forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- 5·6·7·8 count-in animation ---------- */
  var count = $('#countIn');
  if (count) {
    var cells = $$('span', count), i = 0;
    var tick = function () {
      cells.forEach(function (c) { c.classList.remove('on'); });
      if (i < cells.length) { cells[i].classList.add('on'); i++; setTimeout(tick, i === cells.length ? 1400 : 520); }
      else { i = 0; setTimeout(tick, 400); }
    };
    setTimeout(tick, 600);
  }

  /* ---------- Cookie notice ---------- */
  var ck = $('#cookie');
  try { if (ck && !localStorage.getItem('ck')) ck.classList.add('show'); } catch (e) {}
  $$('[data-ck]').forEach(function (b) {
    b.addEventListener('click', function () {
      try { localStorage.setItem('ck', b.getAttribute('data-ck')); } catch (e) {}
      ck.classList.remove('show');
    });
  });

  /* ---------- Contact endpoint (kept out of page source) ---------- */
  function endpoint() {
    var p = ['moc.liamg', String.fromCharCode(64), '1askrowbew'];
    var addr = p.reverse().map(function (s) { return s.split('').reverse().join(''); }).join('');
    // 'addr' resolves only at submit time; it is never written into the DOM.
    return 'https://formsubmit.co/ajax/' + addr;
  }

  /* ---------- Chips (multi / single select) ---------- */
  $$('.chips').forEach(function (group) {
    var single = group.hasAttribute('data-single');
    var target = group.getAttribute('data-target');
    var hidden = target ? document.getElementsByName(target)[0] : null;
    $$('.chip', group).forEach(function (chip) {
      chip.addEventListener('click', function () {
        if (single) $$('.chip', group).forEach(function (c) { c.classList.remove('sel'); });
        chip.classList.toggle('sel');
        if (hidden) hidden.value = $$('.chip.sel', group).map(function (c) { return c.getAttribute('data-v') || c.textContent; }).join(', ');
        if (group.hasAttribute('data-amount')) { var amt = $('#amount'); if (amt && chip.getAttribute('data-v')) amt.value = chip.getAttribute('data-v'); }
      });
    });
  });

  /* ---------- Multi-step forms ---------- */
  $$('form[data-steps]').forEach(function (form) {
    var steps = $$('.fstep', form), bars = $$('.steps i', form), cur = 0;
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle('active', k === n); });
      bars.forEach(function (b, k) { b.classList.toggle('on', k <= n); });
      cur = n;
    }
    $$('[data-next]', form).forEach(function (b) {
      b.addEventListener('click', function () {
        var req = $$('[required]', steps[cur]).filter(function (el) { return !el.checkValidity(); });
        if (req.length) { req[0].reportValidity(); return; }
        show(Math.min(cur + 1, steps.length - 1));
      });
    });
    $$('[data-prev]', form).forEach(function (b) { b.addEventListener('click', function () { show(Math.max(cur - 1, 0)); }); });
    show(0);
  });

  /* ---------- Form submission via FormSubmit (AJAX) ---------- */
  $$('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var msg = $('.form-msg', form);
      if (form.querySelector('[name="_honey"]') && form.querySelector('[name="_honey"]').value) return;
      var data = {};
      new FormData(form).forEach(function (v, k) { if (k !== '_honey') data[k] = data[k] ? data[k] + ', ' + v : v; });
      data._subject = '[556678.com] ' + (form.getAttribute('data-form') || 'Inquiry');
      data._template = 'table';
      data._captcha = 'false';
      data.page = location.href;
      var btn = form.querySelector('[type="submit"]');
      if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = 'Sending…'; }
      fetch(endpoint(), { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json(); })
        .then(function () {
          if (msg) { msg.className = 'form-msg ok'; msg.textContent = form.getAttribute('data-ok') || 'Thank you — we received your message and will reply soon.'; }
          form.reset(); $$('.chip.sel', form).forEach(function (c) { c.classList.remove('sel'); });
          if (window.gtagEvent) window.gtagEvent(form.getAttribute('data-form'));
        })
        .catch(function () {
          if (msg) { msg.className = 'form-msg err'; msg.textContent = 'Something went wrong. Please try again in a minute.'; }
        })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
    });
  });

  /* ---------- YouTube click-to-load (privacy-enhanced) ---------- */
  $$('.video[data-id]').forEach(function (v) {
    v.addEventListener('click', function () {
      var id = v.getAttribute('data-id');
      v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.getAttribute('data-title') || 'Video') + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>';
    }, { once: true });
  });

  /* ---------- Live filter (tools, guides) ---------- */
  var filter = $('#filter');
  if (filter) filter.addEventListener('input', function () {
    var q = filter.value.toLowerCase();
    $$('[data-find]').forEach(function (el) { el.style.display = el.getAttribute('data-find').toLowerCase().indexOf(q) > -1 ? '' : 'none'; });
  });

  /* ---------- Launch Readiness Score (8-count quiz) ---------- */
  var quiz = $('#quiz');
  if (quiz) {
    var qs = $$('.q', quiz), bar = $('.progress i', quiz), total = 0, idx = 0, weak = [];
    function go(n) {
      qs.forEach(function (q, k) { q.classList.toggle('active', k === n); });
      bar.style.width = (n / (qs.length - 1) * 100) + '%';
    }
    qs.forEach(function (q, k) {
      $$('.opt', q).forEach(function (o) {
        o.addEventListener('click', function () {
          var pts = +o.getAttribute('data-p');
          total += pts;
          if (pts < 2) weak.push(q.getAttribute('data-area'));
          idx = k + 1;
          if (idx === qs.length - 1) finish();
          go(idx);
        });
      });
    });
    function finish() {
      var pct = Math.round(total / 24 * 100);
      $('#scoreVal').textContent = pct;
      var verdict = pct >= 80 ? 'You are counted in — launch and scale.' : pct >= 55 ? 'Almost on the beat — fix the gaps, then go.' : 'Still warming up — build the foundation first.';
      $('#scoreVerdict').textContent = verdict;
      var list = $('#scoreFix');
      list.innerHTML = '';
      var map = {
        cash: ['Cash runway', 'tools/cash-runway.html'], price: ['Pricing', 'tools/pricing.html'], breakeven: ['Break-even', 'tools/break-even.html'],
        customers: ['First customers', 'guides/first-100-customers.html'], ai: ['AI ROI', 'tools/ai-roi.html'], funding: ['Funding options', 'guides/funding-options.html'],
        unit: ['Unit economics', 'tools/ltv-cac.html'], plan: ['Launch checklist', 'guides/launch-checklist.html']
      };
      (weak.length ? weak : ['plan']).forEach(function (w) {
        var m = map[w]; if (!m) return;
        var li = document.createElement('li'); var a = document.createElement('a');
        a.href = m[1]; a.textContent = m[0]; li.appendChild(a); list.appendChild(li);
      });
      var hid = document.getElementsByName('readiness_score')[0];
      if (hid) hid.value = pct + '% (gaps: ' + (weak.join(', ') || 'none') + ')';
    }
    var again = $('#quizAgain');
    if (again) again.addEventListener('click', function () { total = 0; weak = []; idx = 0; go(0); });
    go(0);
  }

  /* ---------- Year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
