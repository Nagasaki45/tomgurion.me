#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

from theme_specific_texts import *

AUTHOR = 'Tom Gurion'
SITENAME = 'Tom Gurion | Music / Tech / Interaction'
DESCRIPTION = 'lorem desc'  # TODO

SITEURL = ''

PATH = 'content'

THEME = 'theme'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

ARTICLE_ORDER_BY = 'order'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
DEFAULT_DATE = 'fs'  # Get date from file creation time if missing

STATIC_PATHS = ['images', 'pdfs']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'pelican_youtube']

SITEMAP = {'format': 'xml'}
