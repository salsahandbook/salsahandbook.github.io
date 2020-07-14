#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marisol Enchufa'
SITENAME = 'Salsa Handbook'
SITEURL = 'https://salsahandbook.github.io'

PATH = 'content'

TIMEZONE = 'Mexico/BajaNorte'

DEFAULT_LANG = 'en'

THEME = '/Users/markp/code/pelican-themes/blueidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Follow Marisol Enchufa on Amazon', 'https://www.amazon.com/kindle-dbs/entity/author/B086CFNC3B')
	    ,)

# Social widget
SOCIAL = (("Marisol's Author Page", 'https://www.amazon.com/kindle-dbs/entity/author/B086CFNC3B'),)

DEFAULT_PAGINATION = False

# Set True to get document-relative URLs for viewing in localhost but only when developing
RELATIVE_URLS = False

# GITHUB_URL = 'https://github.com/salsahandbook' # is this for the Fork Me badge?

GOOGLE_ANALYTICS = "UA-123156804-1" 

STATIC_PATHS = ['images', 'images/Positions']
