# 556678.com — Phase-wise Build Prompts

Concept: **556678 — Count In Your Growth.** "55 66 78" reads as the dancer's count-in *5, 6, 7, 8 — go*. The site is a free small-business launch and growth toolkit: calculators, plain-English guides, a founder video library, a free growth and funding plan (lead generation), a monthly contest, a careers page, sponsorships and contributions. It is monetized with Google AdSense.

Constants for every phase:
- AdSense publisher ID: `ca-pub-6620975821265271`. Put the script in every page `<head>`: `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>`
- Top bar on every page, linked to `https://web.works/contact`: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership". The visible text never shows the URL.
- All forms go to one inbox through FormSubmit AJAX. Assemble the address in JavaScript at submit time. It must never appear in HTML, visible text or plain JS strings.
- Hosting: GitHub Pages free plan, repo `WEBWORKSA1/556678-com`, branch `main`, root folder. Static only, with `.nojekyll`.

---

## Phase 1: Foundation and design system
> Build a static site skeleton for 556678.com with no frameworks: semantic HTML5, one CSS file and vanilla JS. Use this design system: Inter for body text, Space Grotesk for display text, and the colours ink #0d1117, coral #ff5a36, sun #ffc531, teal #00a58c and violet #5b4bff. Use rounded cards, soft shadows and a light/dark theme toggle saved in localStorage. The logo is four rising bars. Include a sticky header with a mobile burger menu, a skip link, a footer with four columns and a fine-print disclosure. Add the inquiry top bar on every page. Write a Python generator (`build.py`) that renders every page from one shared layout, using relative links so the site works on both `*.github.io/556678-com/` and `556678.com`. Add Open Graph and Twitter tags, a canonical URL, WebSite JSON-LD, a favicon SVG, an OG image, a web manifest, `robots.txt` (allow Mediapartners-Google), `ads.txt` and `sitemap.xml`.

## Phase 2: Home page and interactive hook
> Build a hero headlined "Count in your launch. Then grow on the beat." with an animated 5-6-7-8-GO count-in. Add a stats card citing BLS survival data: about 1 in 5 businesses close in year 1 and about 50% by year 5, and cash flow is the most cited cause. Build an 8-question "Launch Readiness Score" quiz with a progress bar. Each answer scores 3/1/0. The result screen shows a percentage, a verdict, and links to the tools and guides for each weak area. Store the score in a hidden lead-form field. Add a tip-of-the-week box that rotates by ISO week. Add sections for the tool grid, guide cards, a 3-video strip, community tiles (contests, careers, support, advertise), a newsletter band and an FAQ.

## Phase 3: Calculator suite (core traffic engine)
> Build 10 calculators with live results as the user types. Each one gets a dark result panel, a mini bar chart where useful, a 250–400-word explainer, an FAQ, WebApplication JSON-LD, and a "want a human to check?" call to action that links to the growth plan. The calculators are: break-even (with profit target), profit margin vs markup, cash runway/burn with 24-month projection, loan payment with yearly balance, product pricing (margin + % fees + fixed fee), revenue growth/CAGR with doubling time, startup cost + operating reserve, AI ROI (hours saved × loaded rate − tool cost, payback), LTV:CAC with payback, and freelance rate. All maths runs client-side and the page states that "inputs stay on your device". Add a tools index with live search.

## Phase 4: Original content (AdSense approval depth)
> Write 8 original guides of 600–900 words each in plain English. Each one links to the relevant calculators, embeds one related YouTube video and carries Article JSON-LD, a byline, an updated date, a "next guide" link and a disclaimer. The guides cover: cash flow survival (with a 13-week forecast method), break-even explained, pricing for profit, the first 100 customers, AI for small business, funding options compared, the 8-Count Launch Checklist, and unit economics. Add a guides index with search and a "Why 556678?" brand-story page (dance count-in, rising sequence, cross-cultural number meanings, and a no-affiliation note). Don't use copied text or thin pages.

## Phase 5: Lead generation (dedicated, high-converting)
> Build `growth-plan.html` as a 3-step form with a progress bar. Step 1 covers needs (multi-select chips), stage (single chip) and capital needed. Step 2 covers business, industry, country, revenue band and team size. Step 3 covers name, email, optional phone, best time, challenge, a partner-intro opt-in and a consent checkbox linked to the privacy policy. Add trust copy ("a real person replies in 2 business days", "never sold"), a "how it works" 5-6-7-8 strip, and an FAQ that discloses how the site earns money. Also add a short lead form on the home page and a growth-plan call to action on every tool and guide. All forms submit by AJAX, show inline success and error messages, include a honeypot, and set the subject "[556678.com] <form name>".

## Phase 6: Community and revenue pages
> Build these pages:
> 1. **Support**: contribution tiers of $8, $25, $78 and $556, with purpose routing (operations, promotion and marketing, hiring talent, contests and prizes), a frequency option, a supporters-wall opt-in and a transparency note. The form requests a secure payment link.
> 2. **Contests**: the monthly "8-Count Challenge". The theme and deadline are generated automatically from the current month. Include a prize ladder, a weighted judging table, official rules (skill contest, no purchase necessary, 18+, void where prohibited) and an entry form.
> 3. **Careers**: 6 remote roles plus a talent-pool application form.
> 4. **Advertise**: sponsorship packages, a partner program, a domain/site acquisition note and a media-kit form.
> 5. **Videos**: verified YouTube IDs with click-to-load embeds in privacy-enhanced mode (youtube-nocookie), a filter, YouTube topic search links and a creator-rights note.

## Phase 7: Compliance and trust (AdSense-ready)
> Write these pages: About (editorial standards and how the site is funded), Contact (FormSubmit form plus the inquiry page link), a Privacy Policy that includes Google's required third-party cookie language with opt-out links to Google Ads Settings and aboutads.info and EEA consent notes, Terms, Disclaimer (not financial advice, calculator limits, ad and referral disclosure), a Cookie Policy table, a Trademark & Copyright disclosure, and a 404 page. Add a cookie notice with Accept and Essential-only buttons. Before applying to AdSense, check that there are no empty ad slots, no misleading buttons near ads, that the site works on mobile, that there are no broken links, and that every page is reachable from navigation or the footer.

## Phase 8: Deploy, refresh and verify
> Commit to `main` and push to `WEBWORKSA1/556678-com`. Enable GitHub Pages under Settings → Pages: deploy from branch `main` / root. Add `.github/workflows/auto-refresh.yml`. It runs `python3 build.py` every Monday and on the 1st of each month, and on manual dispatch. It rotates the tip, the contest round, the dates, the sitemap lastmod and the RSS feed, then commits any changes so Pages republishes. QA in a headless browser: check for JS errors, crawl internal links, test the quiz flow, test every calculator, and take mobile screenshots. Grep the source to confirm the email never appears. For the custom domain, add a `CNAME` file containing `556678.com`, point DNS A records to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153 (and `www` CNAME to `webworksa1.github.io`), enable HTTPS, then submit the sitemap to Search Console and apply to AdSense.

## Phase 9: Expansion roadmap (after approval)
> - Add 2 guides a week: industry startup-cost estimators, grants by country, and AI workflow recipes.
> - Add CSV/PDF export and shareable result URLs to the calculators.
> - Build an embeddable-calculator program for backlinks.
> - Add sponsor slots on the tool pages.
> - Launch the supporters wall and contest winners gallery.
> - Add a localized edition (FR/ES/HI).
> - Track form conversion and offer qualified leads to lender and accounting partners.
