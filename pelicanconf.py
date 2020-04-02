#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

from theme_specific_texts import *

AUTHOR = 'Tom Gurion'
SITENAME = 'Tom Gurion | Music / Tech / Interaction'
DESCRIPTION = 'I explore new ideas to facilitate interactive music creation and consumption.'

SITEURL = ''

PATH = 'content'

THEME = 'theme'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

ARTICLE_ORDER_BY = 'order'

DEFAULT_DATE = 'fs'  # Get date from file creation time if missing

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sidebar links
SOCIAL = (
    ('home', 'http://tomgurion.me'),
    ('github', 'https://github.com/Nagasaki45'),
    ('twitter', 'https://twitter.com/nagasaki45'),
    ('envelope', 'mailto:nagasaki45@gmail.com'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'pdfs',
    'extra/favicon.ico',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

PLUGINS = ['pelican_youtube']
