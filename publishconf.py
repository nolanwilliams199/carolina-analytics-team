"""
Production settings. Used when deploying:

    pelican content -s publishconf.py
"""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: E402,F401,F403

# TODO: set this to your real address once you have a domain,
# e.g. "https://carolinaanalytics.team"
SITEURL = os.environ.get("SITEURL", "")
RELATIVE_URLS = SITEURL == ""

DELETE_OUTPUT_DIRECTORY = True
