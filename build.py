#!/usr/bin/env python3
"""Static site generator for 556678.com.
Run: python3 build.py  — regenerates every HTML page, sitemap and feed.
The weekly GitHub Action runs this to rotate the tip of the week, contest round and dates."""
import datetime, html, json, os
from content_tools import TOOLS
from content_guides import GUIDES

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://556678.com"
NAME = "556678.com"
TAGLINE = "Count In Your Growth"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
INQUIRY_URL = "https://web.works/contact"
TODAY = datetime.date.today()
WEEK = TODAY.isocalendar()[1]

TIPS = [
    "Invoice the same day you deliver. Every day you wait is a day of free credit you give your customer.",
    "Review your prices every 12 months. Costs rise quietly; prices should keep up on purpose.",
    "Keep a cash floor of at least one month of fixed costs that you never touch.",
    "Ask for a referral right after a customer says thank you — that's when it lands best.",
    "Pick one repetitive task this week and test whether an AI assistant can draft it for you.",
    "Track one leading metric (conversations booked) alongside revenue. It tells you what next month looks like.",
    "Move annual software subscriptions to monthly until revenue is predictable.",
    "Write down your break-even number and put it where you'll see it every day.",
    "Offer three packages. The middle one usually wins and lifts your average sale.",
    "Open a line of credit while the business looks strong — not when you need it.",
    "Calculate CAC by channel. One channel is usually carrying the rest.",
    "Take a 30–50% deposit on custom work. It funds the job and filters serious buyers.",
]
VIDEOS = [
    ("CBYhVcO4WgI", "How to Start a Startup — Lecture 1", "Y Combinator lecture series: ideas, product, team and execution.", "Launch"),
    ("ii1jcLg-eIQ", "Before the Startup — Paul Graham", "Counterintuitive truths about starting a company.", "Launch"),
    ("Th8JoIan4dg", "How to Get and Evaluate Startup Ideas", "A framework for judging which ideas are worth pursuing.", "Ideas"),
    ("hyYCn_kAngI", "How to Get Your First Customers", "Practical tactics for early traction.", "Growth"),
    ("C27RVio2rOs", "Building Product — Michael Seibel", "How to build what customers actually want.", "Product"),
    ("17XZGUX_9iM", "How to Pitch Your Startup — Kevin Hale", "Make a pitch that is clear, concise and memorable.", "Funding"),
]
VIDEO_TITLES = {v[0]: v[1] for v in VIDEOS}

NAV = [("index.html", "Home"), ("tools/index.html", "Tools"), ("guides/index.html", "Guides"), ("videos.html", "Videos"),
       ("contests.html", "Contests"), ("careers.html", "Careers"), ("support.html", "Support")]

def esc(s): return html.escape(s, quote=True)

def layout(path, title, desc, body, extra_head="", schema=None, scripts=("site.js",)):
    depth = path.count("/")
    p = "../" * depth
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    nav = "".join(
        f'<li><a href="{p}{href}"{" aria-current=\"page\"" if href == path or (href != "index.html" and path.startswith(href.split("/")[0] + "/") and "/" in href) else ""}>{label}</a></li>'
        for href, label in NAV)
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE + "/",
           "description": "Free business calculators, guides and growth programs for founders and small businesses."}]
    if schema: ld.append(schema)
    full_title = title if NAME in title else f"{title} | {NAME}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ff5a36">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/site.css">
{ADSENSE}
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0])}</script>
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="{INQUIRY_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership</a></div>
<header class="site-header"><div class="wrap nav">
<a class="brand" href="{p}index.html" aria-label="{NAME} home"><span class="mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>556678</a>
<ul class="menu" id="menu">{nav}<li><a class="cta" href="{p}growth-plan.html">Free Growth Plan</a></li></ul>
<div class="nav-tools"><button class="icon-btn" id="themeBtn" aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button><button class="icon-btn burger" id="burger" aria-label="Open menu" aria-expanded="false">☰</button></div>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{p}index.html" style="color:#fff"><span class="mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>556678</a>
<p style="margin-top:12px">{TAGLINE}. Free calculators, plain-English guides and growth programs that help founders launch on the beat and grow with confidence.</p>
<p><a href="{p}growth-plan.html">→ Get a free growth plan</a></p></div>
<div><h4>Toolkit</h4><ul><li><a href="{p}tools/index.html">All calculators</a></li><li><a href="{p}tools/cash-runway.html">Cash runway</a></li><li><a href="{p}tools/break-even.html">Break-even</a></li><li><a href="{p}tools/ai-roi.html">AI ROI</a></li><li><a href="{p}guides/index.html">Guides</a></li><li><a href="{p}videos.html">Video library</a></li></ul></div>
<div><h4>Community</h4><ul><li><a href="{p}contests.html">8-Count Challenge</a></li><li><a href="{p}careers.html">Careers & talent</a></li><li><a href="{p}support.html">Support the project</a></li><li><a href="{p}advertise.html">Advertise & partner</a></li><li><a href="{p}meaning-of-556678.html">Why "556678"?</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{p}about.html">About</a></li><li><a href="{p}contact.html">Contact</a></li><li><a href="{p}privacy.html">Privacy policy</a></li><li><a href="{p}terms.html">Terms of use</a></li><li><a href="{p}disclaimer.html">Disclaimer</a></li><li><a href="{p}cookies.html">Cookie policy</a></li><li><a href="{p}legal.html">Trademark & copyright</a></li></ul></div>
</div>
<div class="fineprint">© <span data-year>{TODAY.year}</span> {NAME}. All rights reserved. Content is general information, not financial, legal or tax advice. "556678" is used solely as this website's domain name; no trademark rights in the number are claimed and no affiliation with any other organization using these digits is implied. See our <a href="{p}legal.html">trademark & copyright disclosure</a>. Last updated {TODAY.strftime('%B %d, %Y')}.</div>
</div></footer>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie notice"><strong>Cookies & ads.</strong> We use cookies to remember your preferences and, with Google AdSense, to show and measure ads. See our <a href="{p}privacy.html">privacy</a> and <a href="{p}cookies.html">cookie policy</a>.<div class="btns"><button class="btn btn-primary" data-ck="all">Accept</button><button class="btn btn-ghost" data-ck="essential">Essential only</button></div></div>
{''.join(f'<script src="{p}assets/js/{s}" defer></script>' for s in scripts)}
</body></html>"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(content)

HP = '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
CONSENT = '<label class="check"><input type="checkbox" required> I agree to be contacted about my request and accept the <a href="{p}privacy.html">privacy policy</a>.</label>'

def video_card(vid, title, desc="", tag=""):
    return f'''<div class="card" data-find="{esc(title + ' ' + desc + ' ' + tag)}"><div class="video" data-id="{vid}" data-title="{esc(title)}" role="button" tabindex="0" aria-label="Play video: {esc(title)}">
<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360"><span class="play"><b>▶</b></span></div>
<div style="margin-top:12px">{f'<span class="tag">{tag}</span>' if tag else ''}<h3 style="font-size:1.05rem">{esc(title)}</h3><p>{esc(desc)}</p></div></div>'''

def newsletter(p):
    return f'''<section><div class="wrap"><div class="band reveal"><h2>One sharp growth tip, every week.</h2><p>Cash, pricing, AI and customer tactics in a 3-minute read. No spam, unsubscribe anytime.</p>
<form data-form="Newsletter signup" data-ok="You're in! Watch your inbox for this week's tip.">{HP}<input type="email" name="email" placeholder="you@business.com" required aria-label="Email address"><button class="btn btn-dark" type="submit">Subscribe</button><div class="form-msg" style="width:100%"></div></form></div></div></section>'''

# ---------------- HOME ----------------
def home():
    tip = TIPS[WEEK % len(TIPS)]
    qs = [("cash", "How many months of expenses could you cover if sales paused?"), ("price", "Do you know your exact price floor after fees and costs?"),
          ("breakeven", "Do you know how many sales you need each month to break even?"), ("customers", "Can you name the specific customer you serve best?"),
          ("unit", "Do you know what it costs to win one customer?"), ("ai", "Are you using AI or automation to save time each week?"),
          ("funding", "If you needed capital in 30 days, do you know where you'd get it?"), ("plan", "Do you review 3 core numbers every week?")]
    opts = [("Yes — confidently", 3), ("Partly / roughly", 1), ("Not yet", 0)]
    qhtml = ""
    for i, (area, q) in enumerate(qs):
        qhtml += f'<div class="q" data-area="{area}"><div class="q-num">Count {i+1} of 8</div><h3>{q}</h3><div class="opts">' + "".join(f'<button class="opt" type="button" data-p="{pt}">{t}</button>' for t, pt in opts) + '</div></div>'
    qhtml += '''<div class="q"><div class="center"><div class="q-num">Your Launch Readiness Score</div><div class="score-ring"><span id="scoreVal">0</span>%</div><p id="scoreVerdict" style="font-weight:600"></p></div>
<p class="muted">Start with these:</p><ul id="scoreFix"></ul><div class="pill-row"><a href="#lead">Get my free growth plan →</a><a href="#quiz" id="quizAgain">Retake</a></div></div>'''
    tools_cards = "".join(f'<a class="card reveal" href="tools/{t["slug"]}.html"><span class="ico">{t["icon"]}</span><span class="tag">{t["cat"]}</span><h3>{t["title"]}</h3><p>{t["short"]}</p></a>' for t in TOOLS[:8])
    guide_cards = "".join(f'<a class="card reveal" href="guides/{g["slug"]}.html"><span class="tag coral">{g["cat"]} · {g["mins"]} min</span><h3>{g["title"]}</h3><p>{g["desc"]}</p></a>' for g in GUIDES[:6])
    vids = "".join(video_card(v[0], v[1], v[2], v[3]) for v in VIDEOS[:3])
    body = f'''
<section class="hero"><div class="wrap hero-grid">
<div><span class="eyebrow">Five · Six · Seven · Eight — Go</span>
<h1>Count in your launch. Then grow on the beat.</h1>
<p class="lead">Free business calculators, plain-English playbooks and hands-on growth programs for founders, freelancers and small-business owners. Know your numbers before you move — then move fast.</p>
<div class="count" id="countIn" aria-hidden="true"><span>5</span><span>6</span><span>7</span><span>8</span><span class="go">GO</span></div>
<div class="pill-row" style="gap:12px"><a class="btn btn-primary" href="#quiz">Take the 2-minute readiness test</a><a class="btn btn-ghost" href="tools/index.html">Open the free toolkit</a></div></div>
<div class="hero-card reveal"><span class="tag">Why it matters</span><h3>Most businesses don't fail on ideas. They fail on timing and cash.</h3>
<div class="stat-row"><div class="stat"><b>~1 in 5</b><small>new U.S. businesses close in year one (BLS)</small></div><div class="stat"><b>~50%</b><small>are gone within five years (BLS)</small></div><div class="stat"><b>#1</b><small>cited reason: cash-flow problems</small></div></div>
<p class="muted" style="margin-top:14px;font-size:.9rem">Our toolkit attacks the controllable causes — runway, pricing, break-even and customer economics.</p></div>
</div></section>

<section class="alt" id="quiz-sec"><div class="wrap grid g2" style="align-items:center">
<div class="reveal"><span class="eyebrow">Interactive</span><h2>Launch Readiness Score</h2><p class="muted">Eight quick questions — one for every count. You'll get a score and the exact tools and guides that close your biggest gaps.</p>
<div class="tip-box card mt"><span class="n">#{WEEK}</span><div><strong>Tip of the week</strong><p>{tip}</p></div></div></div>
<div class="quiz" id="quiz"><div class="progress"><i></i></div>{qhtml}</div>
</div></section>

<section><div class="wrap"><div class="section-head reveal"><span class="eyebrow">Free toolkit</span><h2>Calculators that answer the questions that keep owners up at night</h2><p>No sign-up. Your numbers never leave your browser.</p></div>
<div class="grid g4">{tools_cards}</div><p class="mt"><a class="btn btn-dark" href="tools/index.html">See all {len(TOOLS)} tools →</a></p></div></section>

<section class="alt" id="lead"><div class="wrap grid g2" style="align-items:start">
<div class="reveal"><span class="eyebrow">Free · 48-hour turnaround</span><h2>Get your personal 8-step growth plan</h2>
<p class="muted">Tell us where you are and what's blocking you. We'll send back a focused plan: the numbers to fix first, the funding routes that fit, and the next eight moves — in order.</p>
<ul><li>✔ Cash, pricing and break-even review</li><li>✔ Funding and grant options matched to your stage</li><li>✔ AI and automation quick wins for your team</li><li>✔ Optional intro to vetted partners and mentors</li></ul>
<p class="muted" style="font-size:.88rem">Need deeper help? The <a href="growth-plan.html">full growth plan request</a> takes 90 seconds.</p></div>
<div class="card"><form data-form="Home growth plan lead" data-ok="Got it! Your growth plan request is in — expect a reply within 2 business days.">{HP}
<input type="hidden" name="readiness_score" value="not taken">
<div class="row"><div class="field"><label for="hn">Your name</label><input id="hn" name="name" required autocomplete="name"></div><div class="field"><label for="he">Email</label><input id="he" type="email" name="email" required autocomplete="email"></div></div>
<div class="field"><label for="hs">Stage</label><select id="hs" name="stage" required><option value="">Choose…</option><option>Idea / pre-launch</option><option>Launched, under 1 year</option><option>1–3 years</option><option>3+ years, scaling</option></select></div>
<div class="field"><label for="hc">Biggest challenge right now</label><select id="hc" name="challenge" required><option value="">Choose…</option><option>Cash flow / runway</option><option>Getting customers</option><option>Pricing & margins</option><option>Funding / loans / grants</option><option>Using AI & automation</option><option>Hiring & team</option></select></div>
<div class="field"><label for="hm">Anything else? (optional)</label><textarea id="hm" name="message" rows="3"></textarea></div>
<div class="field">{CONSENT.format(p="")}</div>
<button class="btn btn-primary btn-block" type="submit">Send me my free plan</button><div class="form-msg"></div></form></div>
</div></section>

<section><div class="wrap"><div class="section-head reveal"><span class="eyebrow">Playbooks</span><h2>Plain-English guides</h2><p>Written for owners, not accountants. Each one ends with a tool you can use today.</p></div>
<div class="grid g3">{guide_cards}</div></div></section>

<section class="alt"><div class="wrap"><div class="section-head reveal"><span class="eyebrow">Watch & learn</span><h2>Founder video library</h2><p>Hand-picked talks from experienced builders. Click to play — videos load only when you ask.</p></div>
<div class="grid g3">{vids}</div><p class="mt"><a class="btn btn-dark" href="videos.html">Full video library →</a></p></div></section>

<section><div class="wrap grid g4">
<a class="card reveal" href="contests.html"><span class="ico">🏆</span><h3>8-Count Challenge</h3><p>Launch something in eight days. Win sponsor-funded prizes and a featured spotlight.</p></a>
<a class="card reveal" href="careers.html"><span class="ico">🤝</span><h3>Join the team</h3><p>Writers, growth marketers, developers and creators — paid and project-based roles.</p></a>
<a class="card reveal" href="support.html"><span class="ico">💛</span><h3>Support the project</h3><p>Help keep every tool free and fund contests, prizes and new resources.</p></a>
<a class="card reveal" href="advertise.html"><span class="ico">📣</span><h3>Partner with us</h3><p>Reach founders at the exact moment they're planning, pricing and funding.</p></a>
</div></section>
{newsletter("")}
<section><div class="wrap"><div class="section-head"><h2>Frequently asked questions</h2></div>
<details><summary>Are the tools really free?</summary><p>Yes. Every calculator is free and runs in your browser. We are supported by advertising, sponsors and community contributions.</p></details>
<details><summary>Do you store the numbers I enter?</summary><p>No. Calculator inputs are processed locally on your device and are not sent to us.</p></details>
<details><summary>Is this financial advice?</summary><p>No. Our content is general education. For decisions about loans, taxes or investments, consult a qualified professional in your jurisdiction.</p></details>
<details><summary>Why is the site called 556678?</summary><p>It reads like a rising count-in — 5, 6, 7, 8 — the beat dancers use to start together. <a href="meaning-of-556678.html">Read the story.</a></p></details>
</div></section>'''
    write("index.html", layout("index.html", f"556678 — {TAGLINE}: Free Business Calculators, Guides & Growth Plans",
          "Free small-business calculators (cash runway, break-even, pricing, AI ROI), plain-English guides, founder videos and a free personal growth plan.", body))

# ---------------- TOOLS ----------------
def tools():
    cards = "".join(f'<a class="card" href="{t["slug"]}.html" data-find="{esc(t["title"]+" "+t["short"]+" "+t["cat"])}"><span class="ico">{t["icon"]}</span><span class="tag">{t["cat"]}</span><h3>{t["title"]}</h3><p>{t["short"]}</p></a>' for t in TOOLS)
    body = f'''<div class="wrap"><nav class="crumbs"><a href="../index.html">Home</a> › Tools</nav></div>
<section class="page-hero"><div class="wrap"><span class="eyebrow">Free toolkit</span><h1>Business calculators</h1><p>{len(TOOLS)} fast, private calculators for cash, profit, pricing, growth, funding and AI. Bookmark the ones you use every week.</p>
<div class="search mt"><input id="filter" type="search" placeholder="Search tools…" aria-label="Search tools"></div></div></section>
<section style="padding-top:10px"><div class="wrap grid g3">{cards}</div></section>{newsletter("../")}'''
    write("tools/index.html", layout("tools/index.html", "Free Small Business Calculators", "Free calculators for break-even, profit margin, cash runway, loan payments, pricing, CAGR, startup costs, AI ROI, LTV:CAC and freelance rates.", body))
    for t in TOOLS:
        fields = "".join(f'<div class="field"><label for="f_{n}">{lbl}</label><input id="f_{n}" name="{n}" type="number" step="any" value="{val}" inputmode="decimal"></div>' for n, lbl, val in t["fields"])
        faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t["faq"])
        related = "".join(f'<a href="{o["slug"]}.html">{o["icon"]} {o["title"]}</a>' for o in TOOLS if o["slug"] != t["slug"])[:2000]
        body = f'''<div class="wrap"><nav class="crumbs"><a href="../index.html">Home</a> › <a href="index.html">Tools</a> › {t["title"]}</nav></div>
<section class="page-hero"><div class="wrap"><span class="eyebrow">{t["icon"]} {t["cat"]}</span><h1>{t["title"]}</h1><p>{t["short"]}</p></div></section>
<section style="padding-top:0"><div class="wrap tool-wrap">
<form class="card" data-tool="{t["slug"]}" autocomplete="off">{fields}<button class="btn btn-dark btn-block" type="submit">Calculate</button><p class="muted" style="font-size:.85rem;margin-top:10px">Results update as you type. Inputs stay on your device.</p></form>
<div><div class="result" id="out" aria-live="polite"></div>
<div class="card mt"><h3>Want a human to check these numbers?</h3><p>Get a free growth plan with a review of your cash, pricing and funding options.</p><p class="mt"><a class="btn btn-primary" href="../growth-plan.html">Request my free plan</a></p></div></div>
</div></section>
<section class="alt"><div class="wrap article">{t["body"]}<h2>FAQ</h2>{faq}<p class="muted mt" style="font-size:.88rem">Results are estimates for planning and education only — not financial, tax or lending advice.</p></div></section>
<section><div class="wrap"><h2>More calculators</h2><div class="pill-row">{related}</div></div></section>'''
        schema = {"@context": "https://schema.org", "@type": "WebApplication", "name": t["title"], "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
                  "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": f"{SITE}/tools/{t['slug']}.html"}
        write(f"tools/{t['slug']}.html", layout(f"tools/{t['slug']}.html", f"{t['title']} — Free", t["short"], body, schema=schema, scripts=("site.js", "tools.js")))

# ---------------- GUIDES ----------------
def guides():
    cards = "".join(f'<a class="card" href="{g["slug"]}.html" data-find="{esc(g["title"]+" "+g["desc"]+" "+g["cat"])}"><span class="tag coral">{g["cat"]} · {g["mins"]} min read</span><h3>{g["title"]}</h3><p>{g["desc"]}</p></a>' for g in GUIDES)
    body = f'''<div class="wrap"><nav class="crumbs"><a href="../index.html">Home</a> › Guides</nav></div>
<section class="page-hero"><div class="wrap"><span class="eyebrow">Playbooks</span><h1>Guides for founders & owners</h1><p>Practical, original guides on cash flow, pricing, customers, AI and funding — each linked to a calculator so you can act right away.</p>
<div class="search mt"><input id="filter" type="search" placeholder="Search guides…" aria-label="Search guides"></div></div></section>
<section style="padding-top:10px"><div class="wrap grid g2">{cards}</div></section>{newsletter("../")}'''
    write("guides/index.html", layout("guides/index.html", "Small Business Guides & Playbooks", "Original, plain-English guides on cash flow, break-even, pricing, first customers, AI for small business, funding and unit economics.", body))
    for i, g in enumerate(GUIDES):
        nxt = GUIDES[(i + 1) % len(GUIDES)]
        vid = g.get("video")
        vblock = f'<h2>Watch: related talk</h2>{video_card(vid, VIDEO_TITLES.get(vid, "Related video"), "Embedded from YouTube. All rights belong to the original creator.")}' if vid else ""
        body = f'''<div class="wrap"><nav class="crumbs"><a href="../index.html">Home</a> › <a href="index.html">Guides</a> › {g["cat"]}</nav></div>
<article class="article wrap" style="padding-bottom:30px"><span class="tag coral">{g["cat"]}</span><h1 style="font-size:clamp(1.9rem,4vw,2.8rem)">{g["title"]}</h1>
<p class="meta">By the 556678 Editorial Team · {g["mins"]} min read · Updated {TODAY.strftime('%B %Y')}</p>
<p class="lead">{g["desc"]}</p>{g["html"]}{vblock}
<div class="card mt"><h3>Turn this into a plan</h3><p>Get a free, personal growth plan built around your numbers and your stage.</p><p class="mt"><a class="btn btn-primary" href="../growth-plan.html">Get my free growth plan</a></p></div>
<p class="mt">Next guide: <a href="{nxt["slug"]}.html">{nxt["title"]} →</a></p>
<p class="muted" style="font-size:.85rem">This guide is general information, not financial, legal or tax advice. Statistics referenced come from public sources such as the U.S. Bureau of Labor Statistics and the U.S. Small Business Administration; check current figures for your own region.</p></article>'''
        schema = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "dateModified": TODAY.isoformat(),
                  "author": {"@type": "Organization", "name": "556678 Editorial Team"}, "publisher": {"@type": "Organization", "name": NAME}, "mainEntityOfPage": f"{SITE}/guides/{g['slug']}.html"}
        write(f"guides/{g['slug']}.html", layout(f"guides/{g['slug']}.html", g["title"], g["desc"], body, schema=schema))

# ---------------- VIDEOS ----------------
def videos():
    cards = "".join(video_card(*v) for v in VIDEOS)
    topics = ["small business cash flow", "how to price your product", "business break even analysis", "AI tools for small business", "how to get small business loan", "pitch competition tips", "first customers startup", "bookkeeping basics small business"]
    search = "".join(f'<a href="https://www.youtube.com/results?search_query={t.replace(" ", "+")}" target="_blank" rel="noopener">▶ {t.title()}</a>' for t in topics)
    body = f'''<section class="page-hero"><div class="wrap"><span class="eyebrow">Watch & learn</span><h1>Founder video library</h1><p>Hand-picked talks on ideas, product, customers and fundraising. Videos use YouTube's privacy-enhanced mode and load only when you click play.</p>
<div class="search mt"><input id="filter" type="search" placeholder="Filter videos…" aria-label="Filter videos"></div></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="grid g3">{cards}</div>
<h2 class="mt">Explore more topics on YouTube</h2><div class="pill-row">{search}</div>
<p class="muted" style="font-size:.88rem">All videos are embedded using YouTube's standard embed player. Copyright and trademarks belong to their respective creators and channels; 556678.com is not affiliated with them. Creators who want a video removed or added can <a href="contact.html">contact us</a>.</p></div></section>
<section class="alt"><div class="wrap center"><h2>Create founder content?</h2><p class="muted">We feature practical videos from independent creators. Pitch your channel for our library and newsletter.</p><a class="btn btn-primary" href="advertise.html#partner">Submit your channel</a></div></section>'''
    write("videos.html", layout("videos.html", "Founder & Small Business Video Library", "Curated startup and small-business videos on ideas, product, first customers and pitching.", body))

# ---------------- GROWTH PLAN (LEAD GEN) ----------------
def growth_plan():
    body = f'''<section class="page-hero"><div class="wrap grid g2" style="align-items:start">
<div><span class="eyebrow">Free · No obligation · 90 seconds</span><h1>Get your free growth & funding plan</h1>
<p>Three short steps. A real person reviews every request and replies within two business days with a focused plan — and, if you want, introductions to vetted lenders, accountants, mentors and service partners.</p>
<div class="grid g2 mt"><div class="card"><span class="ico">🧭</span><h3>Clear next moves</h3><p>Your eight priorities, in order, for the next 90 days.</p></div>
<div class="card"><span class="ico">💵</span><h3>Funding match</h3><p>Loans, grants, competitions and programs that fit your stage.</p></div>
<div class="card"><span class="ico">⚙️</span><h3>AI quick wins</h3><p>Two or three automations to free hours this month.</p></div>
<div class="card"><span class="ico">🔒</span><h3>Private</h3><p>We never sell your details. Partner intros only with your permission.</p></div></div>
<details class="mt"><summary>Who is this for?</summary><p>Founders with an idea, new businesses in their first year and established small businesses planning their next stage of growth — anywhere in the world.</p></details>
<details><summary>What does it cost?</summary><p>The plan is free. If we suggest a paid partner, we'll tell you upfront, and you're never obliged to use them.</p></details>
<details><summary>How do you make money then?</summary><p>Through advertising, sponsorships and, where disclosed, referral fees from partners. These never change the advice in your plan.</p></details></div>
<div class="card"><form data-form="Growth plan request (full)" data-steps data-ok="Thank you! Your request is in. Expect your personal plan within 2 business days.">{HP}
<div class="steps"><i></i><i></i><i></i></div>
<div class="fstep"><h3>1 · What do you need?</h3><label>Pick all that apply</label>
<input type="hidden" name="needs"><div class="chips" data-target="needs"><button type="button" class="chip">Growth plan</button><button type="button" class="chip">Funding / loan</button><button type="button" class="chip">Grants & competitions</button><button type="button" class="chip">Pricing review</button><button type="button" class="chip">Cash-flow help</button><button type="button" class="chip">AI & automation</button><button type="button" class="chip">Website & marketing</button><button type="button" class="chip">Mentor intro</button></div>
<label class="mt" style="margin-top:16px">Your stage</label><input type="hidden" name="stage"><div class="chips" data-single data-target="stage"><button type="button" class="chip">Idea</button><button type="button" class="chip">Launching</button><button type="button" class="chip">Under 1 year</button><button type="button" class="chip">1–3 years</button><button type="button" class="chip">3+ years</button></div>
<div class="field" style="margin-top:16px"><label for="g_amt">Capital needed (if any)</label><select id="g_amt" name="capital_needed"><option>Not needed</option><option>Under $10k</option><option>$10k–$50k</option><option>$50k–$250k</option><option>$250k+</option></select></div>
<button class="btn btn-dark btn-block" type="button" data-next>Next →</button></div>
<div class="fstep"><h3>2 · About the business</h3>
<div class="field"><label for="g_bn">Business name (or idea)</label><input id="g_bn" name="business" required></div>
<div class="row"><div class="field"><label for="g_ind">Industry</label><select id="g_ind" name="industry" required><option value="">Choose…</option><option>Retail / e-commerce</option><option>Food & hospitality</option><option>Professional services</option><option>Health & wellness</option><option>Construction & trades</option><option>Tech / software</option><option>Creative & media</option><option>Other</option></select></div>
<div class="field"><label for="g_c">Country</label><input id="g_c" name="country" required autocomplete="country-name"></div></div>
<div class="row"><div class="field"><label for="g_rev">Monthly revenue</label><select id="g_rev" name="monthly_revenue"><option>Pre-revenue</option><option>Under $5k</option><option>$5k–$25k</option><option>$25k–$100k</option><option>$100k+</option></select></div>
<div class="field"><label for="g_team">Team size</label><select id="g_team" name="team_size"><option>Just me</option><option>2–5</option><option>6–20</option><option>21+</option></select></div></div>
<div class="row"><button class="btn btn-ghost" type="button" data-prev>← Back</button><button class="btn btn-dark" type="button" data-next>Next →</button></div></div>
<div class="fstep"><h3>3 · Where should we send it?</h3>
<div class="row"><div class="field"><label for="g_n">Full name</label><input id="g_n" name="name" required autocomplete="name"></div><div class="field"><label for="g_e">Email</label><input id="g_e" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="g_p">Phone (optional)</label><input id="g_p" type="tel" name="phone" autocomplete="tel"></div><div class="field"><label for="g_t">Best time to reach you</label><select id="g_t" name="best_time"><option>Any time</option><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div></div>
<div class="field"><label for="g_m">Your biggest challenge, in one or two sentences</label><textarea id="g_m" name="message" rows="3" required></textarea></div>
<div class="field"><label class="check"><input type="checkbox" name="partner_intros" value="yes"> Yes, introduce me to vetted partners who can help.</label></div>
<div class="field">{CONSENT.format(p="")}</div>
<div class="row"><button class="btn btn-ghost" type="button" data-prev>← Back</button><button class="btn btn-primary" type="submit">Get my free plan</button></div><div class="form-msg"></div></div>
</form></div></div></section>
<section class="alt"><div class="wrap"><div class="section-head"><h2>How it works</h2></div><div class="grid g4">
<div class="card"><span class="tip-box"><span class="n">5</span></span><h3>Tell us</h3><p>Three short steps about your goals and stage.</p></div>
<div class="card"><span class="tip-box"><span class="n">6</span></span><h3>We review</h3><p>A person reads your request and runs the numbers.</p></div>
<div class="card"><span class="tip-box"><span class="n">7</span></span><h3>You get a plan</h3><p>Priorities, tools, funding routes and quick wins.</p></div>
<div class="card"><span class="tip-box"><span class="n">8</span></span><h3>Go</h3><p>Act on it — with partner support if you choose.</p></div></div></div></section>'''
    write("growth-plan.html", layout("growth-plan.html", "Free Growth & Funding Plan for Small Businesses", "Request a free personal growth and funding plan: cash, pricing, AI quick wins and matched funding options, reviewed by a person within 2 business days.", body))

# ---------------- SUPPORT / DONATE ----------------
def support():
    tiers = [("$8", "Count-in", ["Keeps one calculator online for a month", "Supporter newsletter shout-out"]),
             ("$25", "On the beat", ["Funds a new guide or tool update", "Name on the supporters wall (optional)"]),
             ("$78", "Full eight", ["Sponsors a contest prize", "Early access to new tools", "Supporters wall + badge"]),
             ("$556", "Headliner", ["Funds a month of promotion & hiring", "Featured thank-you on homepage", "Strategy call with the team"])]
    tcards = "".join(f'<div class="card tier{" featured" if i == 2 else ""}"><span class="tag">{n}</span><div class="amt">{a}</div><ul>{"".join(f"<li>{x}</li>" for x in perks)}</ul></div>' for i, (a, n, perks) in enumerate(tiers))
    body = f'''<section class="page-hero"><div class="wrap"><span class="eyebrow">Support the project</span><h1>Help keep every tool free</h1><p>556678.com is independent. Contributions fund hosting and operations, promotion and marketing, hiring talented writers and developers, and the prizes in our community contests.</p></div></section>
<section style="padding-top:0"><div class="wrap"><div class="grid g4">{tcards}</div>
<div class="grid g4 mt"><div class="card"><span class="ico">🖥️</span><h3>Operations</h3><p>Hosting, tools, security and maintenance.</p></div><div class="card"><span class="ico">📣</span><h3>Promotion & marketing</h3><p>Reaching founders who need these tools most.</p></div><div class="card"><span class="ico">🧑‍💻</span><h3>Hiring talent</h3><p>Paying writers, developers, designers and editors.</p></div><div class="card"><span class="ico">🏆</span><h3>Contests & prizes</h3><p>Funding the 8-Count Challenge prize pool.</p></div></div></div></section>
<section class="alt" id="pledge"><div class="wrap grid g2" style="align-items:start">
<div><h2>Make a contribution</h2><p class="muted">Choose an amount and where you'd like it to go. We'll reply with a secure payment link (card, PayPal or bank transfer) and a receipt. One-time or monthly — your choice.</p>
<div class="callout">Transparency: contributions support an independent project and are not tax-deductible charitable donations. We publish a short summary of how support was used each quarter.</div>
<details><summary>Can my company sponsor instead?</summary><p>Yes — see <a href="advertise.html">sponsorships & partnerships</a> for branded packages and contest title sponsorship.</p></details>
<details><summary>Can I contribute anonymously?</summary><p>Of course. Leave the supporters-wall box unticked.</p></details></div>
<div class="card"><form data-form="Support contribution pledge" data-ok="Thank you for your support! We'll email you a secure payment link shortly.">{HP}
<label>Amount (USD)</label><div class="chips" data-single data-amount><button type="button" class="chip" data-v="8">$8</button><button type="button" class="chip" data-v="25">$25</button><button type="button" class="chip" data-v="78">$78</button><button type="button" class="chip" data-v="556">$556</button></div>
<div class="row" style="margin-top:14px"><div class="field"><label for="amount">Or custom amount</label><input id="amount" name="amount" type="number" min="1" required></div>
<div class="field"><label for="freq">Frequency</label><select id="freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="field"><label for="purp">Direct my support to</label><select id="purp" name="purpose"><option>Where it's needed most</option><option>Ongoing operations</option><option>Promotion & marketing</option><option>Hiring talent</option><option>Contests & prizes</option></select></div>
<div class="row"><div class="field"><label for="sn">Name</label><input id="sn" name="name" required></div><div class="field"><label for="se">Email</label><input id="se" type="email" name="email" required></div></div>
<div class="field"><label for="sm">Message (optional)</label><textarea id="sm" name="message" rows="2"></textarea></div>
<div class="field"><label class="check"><input type="checkbox" name="supporters_wall" value="yes"> List my name on the supporters wall</label></div>
<button class="btn btn-primary btn-block" type="submit">Send contribution request</button><div class="form-msg"></div></form></div>
</div></section>
<section><div class="wrap center"><h2>Other ways to help</h2><div class="pill-row" style="justify-content:center"><a href="tools/index.html">Share a calculator with a founder</a><a href="careers.html">Volunteer your skills</a><a href="contests.html">Enter or judge a contest</a><a href="contact.html">Suggest a new tool</a></div></div></section>'''
    write("support.html", layout("support.html", "Support the Project — Donate & Sponsor", "Support 556678.com: contributions fund operations, promotion, hiring talent and prizes for community contests.", body))

# ---------------- CONTESTS ----------------
def contests():
    m = TODAY.replace(day=1)
    nm = (m + datetime.timedelta(days=32)).replace(day=1)
    round_name = m.strftime("%B %Y")
    deadline = (nm - datetime.timedelta(days=1)).strftime("%B %d, %Y")
    themes = ["Launch a micro-offer", "Automate one workflow with AI", "Win your first 10 customers", "Raise your prices", "Build a free tool", "Cut your break-even", "Pitch in 88 seconds", "Ship a landing page",
              "Collect every overdue invoice", "Start a referral loop", "Package your service", "Plan next year in 8 counts"]
    theme = themes[(TODAY.month - 1) % len(themes)]
    body = f'''<section class="page-hero"><div class="wrap"><span class="eyebrow">Monthly community contest</span><h1>The 8-Count Challenge</h1><p>Eight days. One focused business move. Share what you did and what happened — the most useful, inventive and measurable entries win sponsor-funded prizes and a featured spotlight.</p>
<div class="grid g3 mt"><div class="card"><span class="tag coral">Current round</span><h3>{round_name}</h3><p>Theme: <strong>{theme}</strong></p></div><div class="card"><span class="tag">Entries close</span><h3>{deadline}</h3><p>11:59 pm Eastern Time</p></div><div class="card"><span class="tag">Entry fee</span><h3>Free</h3><p>No purchase necessary.</p></div></div></div></section>
<section class="alt"><div class="wrap"><h2>Prizes</h2><div class="grid g4">
<div class="card tier featured"><span class="ico">🥇</span><h3>Grand winner</h3><p>Top sponsor prize, homepage feature, newsletter spotlight and a strategy session.</p></div>
<div class="card tier"><span class="ico">🥈</span><h3>Runner-up</h3><p>Sponsor prize package and a featured case study.</p></div>
<div class="card tier"><span class="ico">🥉</span><h3>Third place</h3><p>Tools and software credits from partners.</p></div>
<div class="card tier"><span class="ico">⭐</span><h3>Community pick</h3><p>Voted by readers — newsletter feature and badge.</p></div></div>
<p class="muted mt">Prize details for each round are announced on this page and in the newsletter. Want to put your brand on a prize? <a href="advertise.html">Become a contest sponsor</a>.</p></div></section>
<section><div class="wrap grid g2" style="align-items:start"><div><h2>How judging works</h2>
<table><tr><th>Criterion</th><th>Weight</th></tr><tr><td>Measurable result (numbers, before & after)</td><td>35%</td></tr><tr><td>Usefulness to other founders</td><td>25%</td></tr><tr><td>Creativity & originality</td><td>20%</td></tr><tr><td>Clarity of the write-up</td><td>20%</td></tr></table>
<h3 class="mt">Official rules (summary)</h3><ul class="muted"><li>Open to individuals 18+ where contests of skill are permitted; void where prohibited.</li><li>No purchase or payment is necessary to enter or win. Winners are selected by judges on the criteria above — this is a contest of skill, not a lottery.</li><li>One entry per person per round. Entries must be your own original work and truthful.</li><li>By entering you allow us to publish your name, business name and entry summary. You keep ownership of your work.</li><li>Winners are contacted by email and must reply within 14 days. Prizes are non-transferable; taxes, if any, are the winner's responsibility.</li><li>We may adjust or cancel a round for reasons beyond our control; any change will be posted here.</li></ul></div>
<div class="card"><h3>Enter this round</h3><form data-form="8-Count Challenge entry" data-ok="Entry received! Good luck — winners are announced in the first week of next month.">{HP}
<input type="hidden" name="round" value="{round_name} — {theme}">
<div class="row"><div class="field"><label for="c_n">Name</label><input id="c_n" name="name" required></div><div class="field"><label for="c_e">Email</label><input id="c_e" type="email" name="email" required></div></div>
<div class="field"><label for="c_b">Business / project</label><input id="c_b" name="business" required></div>
<div class="field"><label for="c_w">What did you do in 8 days?</label><textarea id="c_w" name="what_you_did" rows="4" required></textarea></div>
<div class="field"><label for="c_r">Result (numbers welcome)</label><textarea id="c_r" name="result" rows="2" required></textarea></div>
<div class="field"><label for="c_l">Link to proof (optional)</label><input id="c_l" name="link" type="url" placeholder="https://"></div>
<div class="field"><label class="check"><input type="checkbox" required> I am 18+ and agree to the official rules.</label></div>
<button class="btn btn-primary btn-block" type="submit">Submit my entry</button><div class="form-msg"></div></form></div></div></section>
<section class="alt"><div class="wrap center"><h2>Upcoming themes</h2><div class="pill-row" style="justify-content:center">{"".join(f"<a>{themes[(TODAY.month - 1 + k) % len(themes)]}</a>" for k in range(1, 5))}</div></div></section>'''
    write("contests.html", layout("contests.html", "The 8-Count Challenge — Monthly Founder Contest", "Enter the free monthly 8-Count Challenge: make one focused business move in eight days and win sponsor-funded prizes and a featured spotlight.", body))

# ---------------- CAREERS ----------------
def careers():
    roles = [("Business & finance writer", "Freelance · Remote", "Write original, well-researched guides for small-business owners."),
             ("Growth & SEO marketer", "Part-time · Remote", "Grow organic traffic, partnerships and the newsletter."),
             ("Front-end developer", "Contract · Remote", "Build new calculators and interactive tools in vanilla JS."),
             ("Video editor & creator", "Project-based · Remote", "Turn guides into short explainers and tutorials."),
             ("AI automation specialist", "Project-based · Remote", "Design practical AI workflows for small businesses."),
             ("Community & contest manager", "Part-time · Remote", "Run the 8-Count Challenge and supporter community.")]
    rc = "".join(f'<div class="card"><span class="tag">{t}</span><h3>{r}</h3><p>{d}</p><p class="mt"><a href="#apply" data-role="{esc(r)}">Apply →</a></p></div>' for r, t, d in roles)
    opts = "".join(f"<option>{r[0]}</option>" for r in roles)
    body = f'''<section class="page-hero"><div class="wrap"><span class="eyebrow">Careers & talent network</span><h1>Help founders grow — and get paid to do it</h1><p>We work with independent writers, marketers, developers and creators around the world. Remote, flexible, outcome-focused.</p></div></section>
<section style="padding-top:0"><div class="wrap"><div class="grid g3">{rc}</div></div></section>
<section class="alt" id="apply"><div class="wrap grid g2" style="align-items:start"><div><h2>Apply or join the talent pool</h2><p class="muted">Not seeing your role? Join the talent pool and we'll reach out when a project fits. We review every application.</p>
<ul><li>✔ Remote-first, async-friendly</li><li>✔ Paid project and part-time work</li><li>✔ Your bylines and portfolio credit</li><li>✔ Equal opportunity — we welcome applicants of every background</li></ul></div>
<div class="card"><form data-form="Careers application" data-ok="Application received — thank you! We'll be in touch if there's a fit.">{HP}
<div class="row"><div class="field"><label for="a_n">Full name</label><input id="a_n" name="name" required></div><div class="field"><label for="a_e">Email</label><input id="a_e" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="a_r">Role</label><select id="a_r" name="role">{opts}<option>Talent pool (other)</option></select></div><div class="field"><label for="a_l">Location / time zone</label><input id="a_l" name="location" required></div></div>
<div class="field"><label for="a_p">Portfolio or LinkedIn URL</label><input id="a_p" name="portfolio" type="url" placeholder="https://" required></div>
<div class="row"><div class="field"><label for="a_a">Availability</label><select id="a_a" name="availability"><option>Project-based</option><option>Up to 10 hrs/week</option><option>10–20 hrs/week</option><option>20+ hrs/week</option></select></div><div class="field"><label for="a_rate">Rate expectation (optional)</label><input id="a_rate" name="rate"></div></div>
<div class="field"><label for="a_m">Why you, in a few lines</label><textarea id="a_m" name="message" rows="4" required></textarea></div>
<div class="field">{CONSENT.format(p="")}</div>
<button class="btn btn-primary btn-block" type="submit">Submit application</button><div class="form-msg"></div></form></div></div></section>'''
    write("careers.html", layout("careers.html", "Careers & Talent Network", "Remote, paid roles for business writers, growth marketers, developers, video creators and AI automation specialists.", body))

# ---------------- ADVERTISE ----------------
def advertise():
    pk = [("Tool sponsor", "Your brand on a high-intent calculator page (cash runway, loans, pricing) with a native call to action."),
          ("Guide sponsor", "Sponsored placement inside a relevant guide, clearly labelled, reaching readers mid-decision."),
          ("Contest title sponsor", "Name the monthly 8-Count Challenge, provide prizes and get featured in announcements."),
          ("Newsletter feature", "A dedicated slot in the weekly growth tip email."),
          ("Partner program", "Lenders, accountants, software and service providers who want qualified growth-plan referrals."),
          ("Domain & site acquisition", "Interested in this website or the 556678.com domain itself? Reach out via the link at the top of every page.")]
    pc = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in pk)
    body = f'''<section class="page-hero"><div class="wrap"><span class="eyebrow">Advertise · Sponsor · Partner</span><h1>Reach founders at the moment they decide</h1><p>Our audience comes to plan cash, set prices, compare funding and adopt AI — high-intent moments for financial, software and service brands.</p>
<p class="mt"><a class="btn btn-primary" href="{INQUIRY_URL}" target="_blank" rel="noopener">Inquire about sponsorship & partnership</a></p></div></section>
<section style="padding-top:0"><div class="wrap grid g3">{pc}</div></section>
<section class="alt" id="partner"><div class="wrap grid g2" style="align-items:start"><div><h2>Request the media kit</h2><p class="muted">Tell us about your brand and goals. We'll send audience details, available placements and rates. All sponsored content is clearly labelled and must meet our editorial standards and Google publisher policies.</p></div>
<div class="card"><form data-form="Advertising / partnership inquiry" data-ok="Thanks! We'll send the media kit and next steps shortly.">{HP}
<div class="row"><div class="field"><label for="ad_n">Name</label><input id="ad_n" name="name" required></div><div class="field"><label for="ad_e">Work email</label><input id="ad_e" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="ad_c">Company</label><input id="ad_c" name="company" required></div><div class="field"><label for="ad_w">Website</label><input id="ad_w" name="website" type="url" placeholder="https://"></div></div>
<div class="row"><div class="field"><label for="ad_i">Interested in</label><select id="ad_i" name="interest"><option>Tool sponsorship</option><option>Guide sponsorship</option><option>Contest title sponsor</option><option>Newsletter feature</option><option>Partner / referral program</option><option>Creator / channel feature</option><option>Website or domain acquisition</option></select></div>
<div class="field"><label for="ad_b">Monthly budget</label><select id="ad_b" name="budget"><option>To be discussed</option><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div></div>
<div class="field"><label for="ad_m">Goals</label><textarea id="ad_m" name="message" rows="3" required></textarea></div>
<button class="btn btn-primary btn-block" type="submit">Request media kit</button><div class="form-msg"></div></form></div></div></section>'''
    write("advertise.html", layout("advertise.html", "Advertise, Sponsor & Partner", "Sponsorship, advertising and partnership opportunities reaching founders and small-business owners at high-intent moments.", body))

# ---------------- MEANING ----------------
def meaning():
    body = '''<article class="article wrap" style="padding:40px 20px"><span class="eyebrow">The story behind the name</span><h1>Why "556678"? The count-in behind the brand</h1>
<p class="lead">Read it aloud — "fifty-five, sixty-six, seventy-eight" — and it climbs. Break it apart and it becomes the most famous count-in in performance: <em>five, six, seven, eight.</em></p>
<h2>The dancer's count-in</h2>
<p>Choreography is usually built in phrases of eight beats. Instead of counting a whole phrase aloud, instructors call the last four beats — "five, six, seven, eight!" — to set the tempo and get everyone starting on the same downbeat. It's quick, it's rhythmic, and it means "get ready: we go now." That is exactly the moment this website is built for: the instant before a founder launches, prices, hires or borrows.</p>
<h2>A rising sequence</h2>
<p>The digits never go down: 5, 5, 6, 6, 7, 8. Two steady steps, then acceleration. It's a neat picture of healthy growth — consolidate, consolidate, then climb — and it inspired our logo of four rising bars.</p>
<h2>Numbers and commerce across cultures</h2>
<p>Numbers carry meaning in business culture around the world. In Chinese numerology, 6 and 8 are widely considered lucky: 8 is associated with prosperity and 6 with things going smoothly, which is why addresses, phone numbers and licence plates rich in these digits can command premiums. In Western numerology, 5 is often linked with change and trade, and 7 with good fortune. We don't make claims about luck — we prefer calculators — but we like that the number reads well in many cultures.</p>
<h2>What 556678 is not</h2>
<p>"556678" is not a brand we claim exclusive rights to, and this site is not affiliated with any company, product, phone number, postal code, part number or registration that happens to use the same digits. It is simply our domain name. See our <a href="legal.html">trademark & copyright disclosure</a>.</p>
<div class="callout">Five, six, seven, eight — go. Start with the <a href="index.html#quiz">Launch Readiness Score</a>.</div></article>'''
    write("meaning-of-556678.html", layout("meaning-of-556678.html", "Why 556678? The Meaning Behind the Name", "556678 reads as a rising count-in — five, six, seven, eight — the beat that starts every routine. The story behind our name.", body))

# ---------------- STATIC PAGES ----------------
def static_pages():
    upd = TODAY.strftime("%B %d, %Y")
    pages = {
     "about.html": ("About 556678.com", "Who we are and what we do: free business tools and growth programs for founders.", f'''<article class="article wrap" style="padding:40px 20px"><h1>About 556678.com</h1>
<p class="lead">We build free, practical tools that help people start and grow businesses with confidence.</p>
<p>556678.com started from a simple observation: most small-business failures are not caused by bad ideas but by controllable problems — running out of cash, under-pricing, not knowing the break-even point, or growing faster than the numbers allow. The information to avoid those mistakes exists, but it is often buried in jargon or behind paywalls.</p>
<h2>What we do</h2><ul><li><strong>Free calculators</strong> for cash runway, break-even, pricing, margins, loans, growth, unit economics and AI return on investment.</li><li><strong>Original guides</strong> written in plain English and reviewed for accuracy against public sources.</li><li><strong>A curated video library</strong> of talks from experienced builders.</li><li><strong>Free growth plans</strong> reviewed by a person, with optional introductions to vetted partners.</li><li><strong>The 8-Count Challenge</strong>, a monthly contest that rewards founders for taking action.</li></ul>
<h2>Editorial standards</h2><p>We write for owners, not accountants. We cite public data sources, label sponsored content clearly, and keep advertising separate from editorial decisions. If you spot an error, <a href="contact.html">tell us</a> and we'll fix it.</p>
<h2>How we're funded</h2><p>Advertising (including Google AdSense), sponsorships, disclosed partner referrals and contributions from supporters. This keeps every tool free.</p>
<p><a class="btn btn-primary" href="growth-plan.html">Get a free growth plan</a></p></article>'''),
     "contact.html": ("Contact Us", "Contact the 556678.com team with questions, corrections, partnership ideas or feedback.", f'''<section class="page-hero"><div class="wrap grid g2" style="align-items:start"><div><span class="eyebrow">Contact</span><h1>Get in touch</h1><p>Questions about a tool, a correction, a guide idea, press or anything else — send us a note and we'll reply within two business days.</p>
<div class="card mt"><h3>Interested in this website or domain?</h3><p>For acquisition, sponsorship, advertising or partnership inquiries, use our dedicated contact page.</p><p class="mt"><a class="btn btn-dark" href="{INQUIRY_URL}" target="_blank" rel="noopener">Open the inquiry page</a></p></div>
<div class="card mt"><h3>Looking for business help?</h3><p>The <a href="growth-plan.html">free growth plan</a> is the fastest way to get personal advice.</p></div></div>
<div class="card"><form data-form="General contact" data-ok="Message sent — thank you! We'll reply within two business days.">{HP}
<div class="row"><div class="field"><label for="ct_n">Name</label><input id="ct_n" name="name" required></div><div class="field"><label for="ct_e">Email</label><input id="ct_e" type="email" name="email" required></div></div>
<div class="field"><label for="ct_t">Topic</label><select id="ct_t" name="topic"><option>General question</option><option>Correction</option><option>Tool or guide idea</option><option>Press</option><option>Copyright / removal request</option><option>Other</option></select></div>
<div class="field"><label for="ct_m">Message</label><textarea id="ct_m" name="message" rows="6" required></textarea></div>
<div class="field">{CONSENT.format(p="")}</div><button class="btn btn-primary btn-block" type="submit">Send message</button><div class="form-msg"></div></form></div></div></section>'''),
     "privacy.html": ("Privacy Policy", "How 556678.com collects, uses and protects information, including cookies and Google AdSense advertising.", f'''<article class="article wrap" style="padding:40px 20px"><h1>Privacy Policy</h1><p class="meta">Last updated {upd}</p>
<p>This policy explains what information 556678.com ("we", "us") collects, how we use it and the choices you have.</p>
<h2>Information you give us</h2><p>When you submit a form (growth plan, contact, newsletter, contest entry, job application, contribution or partnership inquiry) we receive the details you enter, such as your name, email address and message. Forms are delivered to us using the third-party form service FormSubmit. We use this information only to respond to you and provide what you asked for. We do not sell your personal information.</p>
<h2>Calculator inputs</h2><p>Numbers you enter into our calculators are processed in your browser and are not transmitted to us.</p>
<h2>Cookies and local storage</h2><p>We use local storage to remember preferences such as dark mode and your cookie choice. Third parties described below may set cookies.</p>
<h2>Advertising — Google AdSense</h2><p>We use Google AdSense to display ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visits to this and/or other sites on the Internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a>, and you can opt out of some third-party vendors' use of cookies for personalized advertising at <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">aboutads.info</a>. Learn more about <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">how Google uses information from sites that use its services</a>.</p>
<p>Visitors in the European Economic Area, the United Kingdom and Switzerland may be shown a consent message managed through Google's consent tools, where required.</p>
<h2>Embedded content</h2><p>Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play. Once played, YouTube may collect data under Google's privacy policy. Fonts are served by Google Fonts.</p>
<h2>Hosting</h2><p>This site is hosted on GitHub Pages, which may log technical data such as IP addresses for security purposes.</p>
<h2>Your rights</h2><p>Depending on where you live (for example under GDPR, UK GDPR, PIPEDA or CCPA/CPRA), you may have the right to access, correct or delete personal information we hold about you, or object to its processing. Contact us through our <a href="contact.html">contact page</a> to make a request.</p>
<h2>Children</h2><p>This site is intended for adults and is not directed to children under 13 (or 16 where applicable). We do not knowingly collect their information.</p>
<h2>Retention & security</h2><p>We keep form submissions only as long as needed to respond and for legitimate record-keeping, and use reasonable safeguards to protect them.</p>
<h2>Changes</h2><p>We may update this policy and will revise the date above when we do.</p></article>'''),
     "terms.html": ("Terms of Use", "Terms governing use of 556678.com, its calculators, content and community programs.", f'''<article class="article wrap" style="padding:40px 20px"><h1>Terms of Use</h1><p class="meta">Last updated {upd}</p>
<p>By using 556678.com you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Use of the site</h2><p>You may use the tools and content for personal and internal business purposes. You may not copy the site wholesale, scrape it in a way that burdens our servers, misuse forms, or use the site for unlawful purposes.</p>
<h2>No professional advice</h2><p>All content and calculator results are general information for education and planning. They are not financial, investment, legal, tax or accounting advice. Always consult a qualified professional before making decisions. See our <a href="disclaimer.html">disclaimer</a>.</p>
<h2>Intellectual property</h2><p>Original text, design, code and graphics on this site are owned by 556678.com unless otherwise stated. Third-party content, including embedded videos and trademarks, belongs to its respective owners. See our <a href="legal.html">trademark & copyright disclosure</a>.</p>
<h2>User submissions</h2><p>When you submit contest entries, testimonials or other content, you confirm it is yours and truthful, and you grant us a non-exclusive licence to display it on the site and in related communications. You keep ownership.</p>
<h2>Contests</h2><p>Contests are governed by the official rules posted on the <a href="contests.html">contest page</a>.</p>
<h2>Contributions</h2><p>Contributions support an independent project and are not charitable donations unless explicitly stated. They are non-refundable except where required by law or in case of error.</p>
<h2>Third-party links and partners</h2><p>We link to and may introduce you to third parties. We are not responsible for their products, services or policies.</p>
<h2>Limitation of liability</h2><p>The site is provided "as is" without warranties. To the fullest extent permitted by law, we are not liable for any loss arising from use of the site or reliance on its content.</p>
<h2>Changes</h2><p>We may update these terms at any time by posting a new version here.</p></article>'''),
     "disclaimer.html": ("Disclaimer", "Important disclaimers about calculators, financial information, affiliate relationships and advertising on 556678.com.", f'''<article class="article wrap" style="padding:40px 20px"><h1>Disclaimer</h1><p class="meta">Last updated {upd}</p>
<h2>Educational purposes only</h2><p>Content on 556678.com — including calculators, guides, videos, growth plans and newsletters — is provided for general educational and informational purposes. It is not financial, investment, lending, legal, tax or accounting advice, and no professional-client relationship is created by using the site.</p>
<h2>Calculator results</h2><p>Calculators use simplified formulas and the inputs you provide. Results are estimates and may not reflect real offers, fees, taxes or outcomes. Verify important figures with a qualified professional.</p>
<h2>Statistics</h2><p>We cite public sources such as the U.S. Bureau of Labor Statistics and the U.S. Small Business Administration. Figures change over time and vary by country and industry.</p>
<h2>Advertising, sponsorship and referrals</h2><p>We display ads through Google AdSense and may publish clearly labelled sponsored content. Where we introduce you to partners we may receive a referral fee; we disclose this and it does not change our recommendations.</p>
<h2>External content</h2><p>Embedded videos and linked websites are the responsibility of their owners. Inclusion does not imply endorsement.</p></article>'''),
     "cookies.html": ("Cookie Policy", "How and why 556678.com and its partners use cookies and local storage.", f'''<article class="article wrap" style="padding:40px 20px"><h1>Cookie Policy</h1><p class="meta">Last updated {upd}</p>
<table><tr><th>Type</th><th>Who sets it</th><th>Purpose</th></tr>
<tr><td>Preferences (local storage)</td><td>556678.com</td><td>Remember dark mode and your cookie choice.</td></tr>
<tr><td>Advertising cookies</td><td>Google AdSense and its partners</td><td>Serve, personalise and measure ads; limit repetition; detect fraud.</td></tr>
<tr><td>Embedded media</td><td>YouTube (only after you press play)</td><td>Play videos and collect viewing statistics.</td></tr>
<tr><td>Fonts</td><td>Google Fonts</td><td>Deliver web fonts (no advertising cookies).</td></tr></table>
<h2>Your choices</h2><p>You can block or delete cookies in your browser settings, manage personalised ads at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>, and opt out of some vendors at <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">aboutads.info</a>. Blocking cookies may affect how some features work. See our <a href="privacy.html">privacy policy</a> for more.</p></article>'''),
     "legal.html": ("Trademark & Copyright Disclosure", "Trademark and copyright disclosure for 556678.com, including use of the number 556678 and third-party content.", f'''<article class="article wrap" style="padding:40px 20px"><h1>Trademark & Copyright Disclosure</h1><p class="meta">Last updated {upd}</p>
<h2>About the name "556678"</h2><p>"556678" is a numeric sequence used solely as the domain name and site identifier of this independent website. We do not claim trademark rights in the number 556678 or in any digit sequence, and we do not use it to identify or imitate any other business, product, service, phone number, postal code, part number, licence or registration.</p>
<p>556678.com is <strong>not affiliated with, endorsed by or sponsored by</strong> any company, organisation, government body or individual that uses these digits or similar numbers. Any resemblance is coincidental. If you believe our use of the name causes confusion with your rights, please <a href="contact.html">contact us</a> and we will review it promptly.</p>
<h2>Third-party trademarks</h2><p>Names such as Google, AdSense, YouTube, GitHub and any company or product names mentioned in guides are trademarks of their respective owners. They are used for identification and reference only (nominative use) and do not imply endorsement.</p>
<h2>Our copyright</h2><p>© {TODAY.year} 556678.com. Original text, calculators, source code, graphics, logo and layout are protected by copyright. You may quote short excerpts with attribution and a link. Republishing whole articles or copying the tools requires written permission.</p>
<h2>Third-party content</h2><p>Videos are embedded through YouTube's official embed player and remain the property of their creators; we do not host or redistribute copies. Statistics are cited from public sources and summarised in our own words.</p>
<h2>Copyright complaints (notice & takedown)</h2><p>If you believe content on this site infringes your copyright, send a notice through our <a href="contact.html">contact page</a> (topic: "Copyright / removal request") including: identification of the work, the URL of the material, your contact details, a statement of good-faith belief that the use is unauthorised, a statement that the information is accurate, and your physical or electronic signature. We respond to valid notices promptly and remove or disable access to infringing material.</p></article>'''),
     "404.html": ("Page Not Found", "The page you were looking for could not be found.", '''<section class="page-hero center"><div class="wrap"><div class="count" style="justify-content:center"><span>4</span><span class="on">0</span><span>4</span></div><h1>Missed a beat.</h1><p style="margin:0 auto">That page doesn't exist. Count back in from the top:</p><div class="pill-row" style="justify-content:center"><a href="/">Home</a><a href="/tools/index.html">Calculators</a><a href="/guides/index.html">Guides</a><a href="/growth-plan.html">Free growth plan</a></div></div></section>'''),
    }
    for path, (title, desc, body) in pages.items():
        write(path, layout(path, title, desc, body))

def sitemap():
    urls = ["", "tools/index.html", "guides/index.html", "videos.html", "growth-plan.html", "support.html", "contests.html", "careers.html", "advertise.html",
            "meaning-of-556678.html", "about.html", "contact.html", "privacy.html", "terms.html", "disclaimer.html", "cookies.html", "legal.html"]
    urls += [f"tools/{t['slug']}.html" for t in TOOLS] + [f"guides/{g['slug']}.html" for g in GUIDES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY.isoformat()}</lastmod><changefreq>{'weekly' if u in ('', 'contests.html') else 'monthly'}</changefreq><priority>{'1.0' if u == '' else '0.8' if u.startswith(('tools', 'guides', 'growth')) else '0.5'}</priority></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", xml)
    items = "".join(f"<item><title>{esc(g['title'])}</title><link>{SITE}/guides/{g['slug']}.html</link><description>{esc(g['desc'])}</description><guid>{SITE}/guides/{g['slug']}.html</guid></item>" for g in GUIDES)
    write("feed.xml", f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{NAME} — Guides</title><link>{SITE}/</link><description>{TAGLINE}: guides for founders and small businesses.</description><lastBuildDate>{TODAY.strftime("%a, %d %b %Y 00:00:00 GMT")}</lastBuildDate>{items}</channel></rss>\n')

if __name__ == "__main__":
    home(); tools(); guides(); videos(); growth_plan(); support(); contests(); careers(); advertise(); meaning(); static_pages(); sitemap()
    print("Built", NAME, "on", TODAY)
