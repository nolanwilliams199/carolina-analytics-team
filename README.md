# Carolina Analytics Team website

A static marketing site built with [Pelican](https://getpelican.com) (Python) and a custom theme.

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pelican --autoreload --listen      # open http://localhost:8000
```

Edits to content, settings, or the theme rebuild automatically while that's running.

## Where to edit things

| What | Where |
|---|---|
| Email, phone, LinkedIn, booking link, contact form ID | `pelicanconf.py` → BUSINESS DETAILS |
| Home page service cards and "how it works" steps | `pelicanconf.py` → `SERVICES`, `HOW_WE_WORK` |
| Prices, packages, hourly rate | `pelicanconf.py` → PRICING |
| Team members (name, credentials, bio, photo) | `pelicanconf.py` → `TEAM` |
| Team photos | `content/images/team/` (square images look best, ~600×600) |
| Full services write-up | `content/pages/services.md` |
| Pricing FAQ | `content/pages/pricing.md` |
| Contact page text | `content/pages/contact.md` |
| Colors and fonts | top of `themes/cat/static/css/style.css` |
| Home page layout and headline | `themes/cat/templates/index.html` |
| Logo | `themes/cat/templates/partials/logo.html` and `themes/cat/static/img/favicon.svg` |

To add a team member, copy the dict inside `TEAM` and fill it in.

## Contact form

1. Create a free form at [formspree.io](https://formspree.io).
2. Copy the form ID (the bit after `/f/` in its endpoint) into `FORMSPREE_ID` in `pelicanconf.py`.

Until you do, the form opens the visitor's email app instead, which works but is clunky.

## Deploy (free)

**GitHub Pages:** push this folder to a GitHub repo, then go to Settings → Pages → Source → "GitHub Actions". The workflow in `.github/workflows/deploy.yml` builds and publishes on every push to `main`.

For a custom domain: add it under Settings → Pages, create a repo variable `SITEURL` (Settings → Secrets and variables → Actions → Variables) set to `https://yourdomain.com`, then add a file `content/extra/CNAME` containing just your domain and uncomment the CNAME line in `EXTRA_PATH_METADATA`.

**Cloudflare Pages or Netlify:** connect the repo and use

- Build command: `pip install -r requirements.txt && pelican content -s publishconf.py`
- Output directory: `output`
- Environment variable: `SITEURL=https://yourdomain.com`

## Adding a blog later

Create `content/blog/` and drop Markdown posts in it (with `Title:` and `Date:` lines at the top). Posts use `themes/cat/templates/article.html`. You'd also want a blog listing page, which is a good next step to add when you need it.
