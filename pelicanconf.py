"""
Pelican settings for Carolina Analytics Team (CAT).

Most of the things you'll want to change live in the "BUSINESS DETAILS",
"PRICING" and "TEAM" sections below. Long-form page text lives in
content/pages/*.md.

Build locally:   pelican content
Live preview:    pelican --autoreload --listen   (then open http://localhost:8000)
"""

import datetime as _dt

import markdown as _md

CURRENT_YEAR = _dt.date.today().year

# ---------------------------------------------------------------------------
# BUSINESS DETAILS  (edit these)
# ---------------------------------------------------------------------------
AUTHOR = "Carolina Analytics Team"
SITENAME = "Carolina Analytics Team"
SITE_SHORTNAME = "CAT"
SITE_TAGLINE = "Data help for small businesses, minus the jargon."
SITE_DESCRIPTION = (
    "Carolina Analytics Team helps small businesses automate busywork, "
    "understand their numbers, and get their data into one trustworthy place."
)
SITEURL = ""  # leave blank for local dev; set the real URL in publishconf.py

SERVICE_AREA = "Serving the Carolinas in person and clients anywhere remotely"

# TODO: replace with your real contact details
CONTACT_EMAIL = "bigcat@carolinaanalyticsteam.com"
CONTACT_PHONE = ""  # e.g. "(803) 555-0123" — leave blank to hide
LINKEDIN_URL = ""   # e.g. "https://www.linkedin.com/in/your-name" — blank hides it
GITHUB_URL = ""     # blank hides it
SCHEDULING_URL = "https://calendar.app.google/jKHmUT9Gaeufr1Qn8"  # e.g. a Calendly / Cal.com link for booking the free call

# Contact form: create a free form at https://formspree.io, then paste the
# form ID (the part after /f/ in the endpoint, e.g. "xyzabcde").
# If left blank, the form falls back to opening the visitor's email app.
FORMSPREE_ID = ""

# ---------------------------------------------------------------------------
# HOME PAGE SERVICE CARDS  (short versions; full write-ups are in services.md)
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "automation",
        "icon": "automation",
        "name": "Automation",
        "headline": "Stop doing the same task every Monday.",
        "blurb": (
            "We turn repetitive copy-paste work, recurring reports, and manual "
            "data entry into things that just happen on their own."
        ),
    },
    {
        "slug": "analytics",
        "icon": "analytics",
        "name": "Analytics",
        "headline": "Know your numbers at a glance.",
        "blurb": (
            "Clear dashboards and plain-English reports that answer the "
            "questions you actually ask: what's selling, who's coming back, "
            "and where the money goes."
        ),
    },
    {
        "slug": "data-integration",
        "icon": "integration",
        "name": "Data Integration",
        "headline": "All your data in one place you can trust.",
        "blurb": (
            "We connect your point-of-sale, online store, spreadsheets, and "
            "other tools into one organized database that stays up to date."
        ),
    },
]

HOW_WE_WORK = [
    ("Free discovery call",
     "A 30-minute chat about what's eating your time or what you wish you knew. No pitch, no obligation."),
    ("Clear written quote",
     "You get a fixed price or a capped estimate in plain English before any work starts."),
    ("Build with check-ins",
     "We build in small pieces and show you progress, so there are no surprises at the end."),
    ("Handoff you can live with",
     "You own everything we build, with simple docs and a walkthrough so your team can use it."),
]

# ---------------------------------------------------------------------------
# PRICING  (ballpark ranges shown on the Pricing page — edit freely)
# ---------------------------------------------------------------------------
HOURLY_RATE = 95
DISCOVERY_CALL = "Free, 30 minutes"

PRICING_PACKAGES = [
    {
        "name": "Data Health Check",
        "service": "Good first step",
        "group": "extra",
        "range": "$400 – $750",
        "unit": "flat fee",
        "timeline": "About 1 week",
        "description": (
            "Not sure where to start? We review your spreadsheets, tools, and "
            "reports and hand you a short, prioritized list of what to fix or "
            "automate first. Credited toward any project you book within 60 days."
        ),
        "includes": [
            "Review of up to 5 tools or files",
            "Written findings in plain English",
            "Rough price for each recommendation",
        ],
    },
    {
        "name": "Quick Automation",
        "service": "Automation",
        "range": "$500 – $2,000",
        "unit": "per project",
        "timeline": "1 – 2 weeks",
        "description": (
            "One recurring task, handled. For example: a weekly sales report "
            "that builds and emails itself, or web-form orders that land in "
            "your spreadsheet automatically."
        ),
        "includes": [
            "One workflow, start to finish",
            "Error alerts if something breaks",
            "30 days of fixes included",
        ],
    },
    {
        "name": "Dashboard Starter",
        "service": "Analytics",
        "range": "$2,000 – $5,000",
        "unit": "per project",
        "timeline": "2 – 4 weeks",
        "featured": True,
        "description": (
            "One to three dashboards built on one or two data sources, such as "
            "your point-of-sale system and a spreadsheet. Refreshes on its own."
        ),
        "includes": [
            "Data cleanup for the included sources",
            "1 – 3 dashboards, mobile friendly",
            "Training session for your team",
        ],
    },
    {
        "name": "Data Consolidation",
        "service": "Data Integration",
        "range": "$3,500 – $10,000+",
        "unit": "per project",
        "timeline": "3 – 8 weeks",
        "description": (
            "Bring scattered spreadsheets and systems together into one "
            "organized database with automatic, scheduled updates."
        ),
        "includes": [
            "Database design and setup",
            "Automated data pipelines",
            "Documentation of where every number comes from",
        ],
    },
    {
        "name": "Ongoing Support",
        "service": "After launch",
        "group": "extra",
        "range": "From $300",
        "unit": "per month",
        "timeline": "Month to month",
        "description": (
            "A small block of hours each month for tweaks, new reports, and "
            "keeping things running. Cancel any time."
        ),
        "includes": [
            "Priority response",
            "Unused hours roll over one month",
            "Discounted hourly rate for extra work",
        ],
    },
]

PRICING_FACTORS = [
    ("How many data sources", "Two clean spreadsheets is a different job from five systems that disagree with each other."),
    ("How messy the data is", "Cleanup is often the biggest share of a data project. A quick look at samples tells us a lot."),
    ("Access to your tools", "Modern apps with good export options are faster to work with than older or locked-down systems."),
    ("Ongoing vs. one-time", "A one-off report costs less than something that has to run reliably every day for years."),
]

# ---------------------------------------------------------------------------
# TEAM  (add a dict per person; photo goes in content/images/team/)
# Bio supports Markdown.
# ---------------------------------------------------------------------------
TEAM = [
    {
        "name": "Nolan Williams",
        "role": "Founder & Lead Data Engineer",
        "photo": "images/team/Nolan Headshot.jfif",#placeholder.svg",
        "credentials": [
            "M.S. in Data Science",
            "4 years in Data Engineering, Analytics Engineering & BI Development",
        ],
        "bio": (
            "I started Carolina Analytics Team to bring the kind of data "
            "tooling larger companies take for granted to the small businesses "
            "that make the Carolinas run.\n\n"
            "Over the past four years I've worked across the full data "
            "lifecycle: designing databases and pipelines as a data engineer, "
            "modeling and testing business logic as an analytics engineer, and "
            "building the dashboards and reports that leaders rely on as a BI "
            "developer. That range means I can take a problem from a messy "
            "export all the way to a decision-ready answer, without handing you "
            "off between specialists.\n\n"
            "I hold a Master's degree in Data Science, but my favorite part of "
            "the job is translating: turning a question like *\"why does it feel "
            "like we're busier but making less?\"* into numbers you can act on, "
            "and explaining them without the jargon."
        ),
        "skills": ["Python", "SQL", "Advanced Data Analysis", "Intuitive Dashboards", "Excel & Google Sheets", "APIs & Automation"],
        "linkedin": "",
        "email": "",
    },
]

# ---------------------------------------------------------------------------
# PELICAN PLUMBING  (you rarely need to touch anything below)
# ---------------------------------------------------------------------------
PATH = "content"
THEME = "themes/cat"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# This is a pages-only site for now. Add .md files to content/blog/ later
# and set ARTICLE_PATHS / DIRECT_TEMPLATES if you want a blog.
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["blog"]
DIRECT_TEMPLATES = ["index"]
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = "order"  # each page sets "Order: N" in its metadata

# Clean URLs: /services/ instead of /pages/services.html
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    # "extra/CNAME": {"path": "CNAME"},  # uncomment for a custom domain on GitHub Pages
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},   # tables, md_in_html, attr_list, etc.
        "markdown.extensions.meta": {},
        "markdown.extensions.smarty": {},
    },
    "output_format": "html5",
}

JINJA_FILTERS = {
    "md": lambda text: _md.markdown(text or "", extensions=["extra", "smarty"]),
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
RELATIVE_URLS = True
