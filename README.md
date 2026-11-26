# 556678.com — Count In Your Growth

This is a static website: free small-business calculators, guides, a founder video library, a growth and funding plan lead funnel, a monthly contest, a careers page, sponsorships and contributions. It is monetized with Google AdSense.

- `build.py` generates all HTML from `content_tools.py` and `content_guides.py`. Run `python3 build.py` after editing content.
- `assets/`: CSS, JS (`site.js` for interactions and forms, `tools.js` for the calculators) and images.
- `.github/workflows/auto-refresh.yml` rebuilds weekly and monthly and commits the changes.
- Hosting is GitHub Pages: Settings → Pages → Deploy from branch → `main` / `(root)`.
- Custom domain: add a `CNAME` file containing `556678.com` once DNS points to GitHub Pages.
- `RESEARCH.md` holds the concept research and benchmarks. `PROMPTS.md` holds the phase-wise build prompts.

© 556678.com. "556678" is used only as a domain name. See `legal.html`.
