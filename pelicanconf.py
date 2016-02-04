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

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

ARTICLE_ORDER_BY = 'order'

DEFAULT_DATE = 'fs'  # Get date from file creation time if missing

STATIC_PATHS = ['images', 'pdfs', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'pelican_youtube']

SITEMAP = {'format': 'xml'}
