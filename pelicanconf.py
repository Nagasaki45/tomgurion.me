#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

from theme_specific_texts import *

AUTHOR = 'Tom Gurion'
SITENAME = 'Tom Gurion'
DESCRIPTION = 'Musician, coder, and researcher of head nods. <br />Collecting hobbies in my spare time'

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

# Don't generate anything but index and articles
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

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

SOCIAL = (
    ('fas fa-blog', 'https://blog.tomgurion.me'),
    ('fab fa-github', 'https://github.com/Nagasaki45'),
    ('fab fa-twitter', 'https://twitter.com/nagasaki45'),
    ('fa fa-envelope', 'mailto:nagasaki45@gmail.com'),
)

HOBBIES = [
    {
        'title': 'Music',
        'content': '''
        I play an instrument since... forever!
        Started with sax and piano as a kid. Picked up bass guitar at 14 and played in a few rock bands since then.
        Got into electronic music in 2017 and shortly after started performing improvised modular jams under the alias <a href="https://nagasaki45.com"><i>nagasaki45</i></a>.
        Recently teamed up with <a href="https://www.residentadvisor.net/dj/digitalselves"><i>digital selves</i></a> to perform together as <i>IDMT?</i>
        '''.strip(),
    },
    {
        'title': 'Code',
        'content': '''
        My main language is python. I use it regularly for web development, data analysis, and other bits and pieces.
        Prefer elixir for highly conccurent webapps though.
        Can do some js and frontend with vue.js and bulma.
        Familiar with way too many creative coding languages: max/MSP and Pd, arduino and processing, some unity3d, blender and a bit more.
        '''.strip(),
    },
    {
        'title': 'Board games',
        'content': '''
        Enjoy playing board games for many years, and got deeper into the hobby ~2018.
        Favourite game at the moment is <a href="https://boardgamegeek.com/boardgame/155821/inis">Inis</a>.
        If you're from Queen Mary University of London, we play regularly. Drop me a line!
        '''.strip(),
    },
    {
        'title': 'Boldering',
        'content': '''
        My home wall is <a href="https://www.mileendwall.org.uk/">Mile End Climbing Wall</a>. On a good day I might even manage a V5.
        '''.strip(),
    },
    {
        'title': 'Cycling',
        'content': '''
        Into bikepacking recently. Not competitive, at all. Haven't done much yet <a>#covid19</a>
        '''.strip(),
    },
    {
        'title': 'Sewing',
        'content': '''
        Started from making bags for my bike.
        Now developing some ambition for larger projects.
        There's no such thing as too many hobbies, right?
        '''.strip(),
    },
]
