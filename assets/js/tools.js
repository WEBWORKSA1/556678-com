/* 556678.com — calculator engine. All math runs locally in the browser. */
(function () {
  'use strict';
  var form = document.querySelector('form[data-tool]');
  if (!form) return;
  var out = document.getElementById('out');
  var cur = function (n, d) { if (!isFinite(n)) return '—'; return (n < 0 ? '-' : '') + '$' + Math.abs(n).toLocaleString(undefined, { maximumFractionDigits: d == null ? 0 : d, minimumFractionDigits: d == null ? 0 : d }); };
  var pct = function (n, d) { return isFinite(n) ? n.toFixed(d == null ? 1 : d) + '%' : '—'; };
  var num = function (n, d) { return isFinite(n) ? n.toLocaleString(undefined, { maximumFractionDigits: d == null ? 1 : d }) : '—'; };
  var v = function (name) { var el = form.elements[name]; return el ? parseFloat(el.value) || 0 : 0; };
  var dl = function (rows) { return '<dl>' + rows.map(function (r) { return '<dt>' + r[0] + '</dt><dd>' + r[1] + '</dd>'; }).join('') + '</dl>'; };
  var bars = function (arr) {
    var max = Math.max.apply(null, arr.map(Math.abs)) || 1;
    return '<div class="bar-chart" aria-hidden="true">' + arr.map(function (x) { return '<i class="' + (x < 0 ? 'neg' : '') + '" style="height:' + Math.max(2, Math.abs(x) / max * 100) + '%"></i>'; }).join('') + '</div>';
  };

  var tools = {
    'break-even': function () {
      var f = v('fixed'), p = v('price'), c = v('variable'), t = v('target');
      var cm = p - c; if (cm <= 0) return '<p>Your price must be higher than your variable cost per unit — every sale currently loses money.</p>';
      var units = f / cm, unitsT = (f + t) / cm;
      return '<div class="big">' + num(Math.ceil(units), 0) + ' units / month</div><p>to break even</p>' + dl([
        ['Break-even revenue', cur(units * p)], ['Contribution margin / unit', cur(cm, 2)], ['Contribution margin ratio', pct(cm / p * 100)],
        ['Units to hit profit target', num(Math.ceil(unitsT), 0)], ['Revenue to hit profit target', cur(unitsT * p)]]);
    },
    'profit-margin': function () {
      var c = v('cost'), p = v('price');
      if (p <= 0) return '<p>Enter a selling price.</p>';
      var g = p - c;
      return '<div class="big">' + pct(g / p * 100) + '</div><p>gross margin</p>' + dl([
        ['Gross profit per sale', cur(g, 2)], ['Markup on cost', pct(c > 0 ? g / c * 100 : NaN)], ['Cost as % of price', pct(c / p * 100)],
        ['Price for 50% margin', cur(c / 0.5, 2)], ['Price for 70% margin', cur(c / 0.3, 2)]]);
    },
    'cash-runway': function () {
      var cash = v('cash'), rev = v('revenue'), exp = v('expenses'), g = v('growth') / 100, months = [], bal = cash, m = 0, out0 = null;
      for (m = 1; m <= 24; m++) { bal += rev * Math.pow(1 + g, m - 1) - exp; months.push(bal); if (bal < 0 && out0 === null) out0 = m; }
      var burn = exp - rev;
      var head = out0 ? '<div class="big">' + out0 + ' months</div><p>until cash runs out at this pace</p>' : '<div class="big">24+ months</div><p>no cash-out within two years at this pace</p>';
      return head + dl([['Current net burn / month', burn > 0 ? cur(burn) : 'Cash-positive'], ['Simple runway (no growth)', burn > 0 ? num(cash / burn) + ' mo' : '∞'],
        ['Balance after 12 months', cur(months[11])], ['Balance after 24 months', cur(months[23])]]) + bars(months);
    },
    'loan-payment': function () {
      var P = v('amount'), r = v('apr') / 100 / 12, n = v('term');
      if (n <= 0) return '<p>Enter a term in months.</p>';
      var pay = r === 0 ? P / n : P * r / (1 - Math.pow(1 + r, -n));
      var total = pay * n, bal = P, yr = [];
      for (var k = 1; k <= n; k++) { var it = bal * r; bal -= (pay - it); if (k % 12 === 0 || k === n) yr.push(Math.max(bal, 0)); }
      return '<div class="big">' + cur(pay, 2) + ' / month</div><p>estimated payment</p>' + dl([['Total repaid', cur(total)], ['Total interest', cur(total - P)],
        ['Interest as % of loan', pct((total - P) / P * 100)], ['Annual debt service', cur(pay * 12)]]) + bars(yr) + '<p class="muted" style="color:#b9c2cf;font-size:.85rem;margin-top:10px">Bars show remaining balance at the end of each year.</p>';
    },
    'pricing': function () {
      var c = v('cost'), m = v('margin') / 100, fee = v('fees') / 100, fixed = v('fixedfee');
      var denom = 1 - m - fee; if (denom <= 0) return '<p>Margin plus fees must be under 100%.</p>';
      var p = (c + fixed) / denom;
      var charm = Math.ceil(p) - 0.01;
      return '<div class="big">' + cur(p, 2) + '</div><p>minimum price for your target margin</p>' + dl([['Charm price suggestion', cur(charm, 2)], ['Payment fees per sale', cur(p * fee + fixed, 2)],
        ['Profit per sale', cur(p * m, 2)], ['Markup on cost', pct((p - c) / c * 100)]]);
    },
    'revenue-growth': function () {
      var s = v('start'), e = v('end'), y = v('years'), proj = v('projyears') || 5;
      if (s <= 0 || y <= 0) return '<p>Enter a starting revenue and number of years.</p>';
      var cagr = Math.pow(e / s, 1 / y) - 1, arr = [];
      for (var k = 0; k <= proj; k++) arr.push(e * Math.pow(1 + cagr, k));
      return '<div class="big">' + pct(cagr * 100) + '</div><p>compound annual growth rate (CAGR)</p>' + dl([['Total growth', pct((e / s - 1) * 100)], ['Doubling time', cagr > 0 ? num(Math.log(2) / Math.log(1 + cagr)) + ' years' : '—'],
        ['Projected in ' + proj + ' yrs (same CAGR)', cur(arr[proj])]]) + bars(arr);
    },
    'startup-cost': function () {
      var items = ['legal', 'equipment', 'inventory', 'website', 'marketing', 'deposits', 'other'].map(v).reduce(function (a, b) { return a + b; }, 0);
      var monthly = v('monthly'), buf = v('buffer');
      var total = items + monthly * buf;
      return '<div class="big">' + cur(total) + '</div><p>recommended launch budget</p>' + dl([['One-time startup costs', cur(items)], ['Operating reserve (' + buf + ' mo)', cur(monthly * buf)],
        ['Reserve share of budget', pct(total ? monthly * buf / total * 100 : 0)]]);
    },
    'ai-roi': function () {
      var h = v('hours'), rate = v('rate'), ppl = v('people'), tool = v('toolcost'), setup = v('setup');
      var monthlySave = h * 4.33 * rate * ppl, net = monthlySave - tool * ppl;
      var roi = (tool * ppl) > 0 ? net / (tool * ppl) * 100 : NaN, payback = net > 0 ? setup / net : NaN;
      return '<div class="big">' + cur(net) + ' / month</div><p>net value of AI time savings</p>' + dl([['Hours freed per month', num(h * 4.33 * ppl, 0)], ['Gross value of time', cur(monthlySave)],
        ['Tool cost per month', cur(tool * ppl)], ['ROI on subscription', pct(roi, 0)], ['Setup payback', isFinite(payback) ? num(payback) + ' months' : '—'], ['First-year net value', cur(net * 12 - setup)]]);
    },
    'ltv-cac': function () {
      var arpu = v('arpu'), gm = v('gm') / 100, churn = v('churn') / 100, cac = v('cac');
      if (churn <= 0) return '<p>Enter a monthly churn rate above 0%.</p>';
      var life = 1 / churn, ltv = arpu * gm * life, ratio = cac > 0 ? ltv / cac : NaN, pb = arpu * gm > 0 ? cac / (arpu * gm) : NaN;
      var verdict = ratio >= 3 ? 'Healthy — room to spend more on acquisition.' : ratio >= 1 ? 'Thin — improve retention or margin before scaling spend.' : 'Losing money on every customer acquired.';
      return '<div class="big">' + (isFinite(ratio) ? ratio.toFixed(1) + ' : 1' : '—') + '</div><p>LTV to CAC ratio — ' + verdict + '</p>' + dl([['Customer lifetime value', cur(ltv)], ['Average lifetime', num(life) + ' months'], ['CAC payback', isFinite(pb) ? num(pb) + ' months' : '—']]);
    },
    'freelance-rate': function () {
      var inc = v('income'), exp = v('expenses'), tax = v('tax') / 100, hrs = v('hours'), wks = v('weeks');
      var gross = (inc + exp) / (1 - tax), billable = hrs * wks;
      if (billable <= 0 || tax >= 1) return '<p>Check your hours and tax rate.</p>';
      var rate = gross / billable;
      return '<div class="big">' + cur(rate, 2) + ' / hour</div><p>minimum rate to hit your take-home goal</p>' + dl([['Gross revenue needed', cur(gross)], ['Billable hours / year', num(billable, 0)],
        ['Day rate (6 billable hrs)', cur(rate * 6)], ['Project buffer rate (+20%)', cur(rate * 1.2, 2)]]);
    }
  };

  var fn = tools[form.getAttribute('data-tool')];
  var run = function () { if (fn && out) out.innerHTML = fn(); };
  form.addEventListener('input', run);
  form.addEventListener('submit', function (e) { e.preventDefault(); run(); });
  run();
})();
