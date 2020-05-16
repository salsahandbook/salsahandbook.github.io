#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marisol Enchufa'
SITENAME = 'Salsa Handbook'
SITEURL = ''
#SITEURL = 'https://github.com/salsahandbook/' # todo: experiment after first push

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
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# GITHUB_URL = 'https://github.com/salsahandbook' # is this for the Fork Me badge?

GOOGLE_ANALYTICS = "UA-123156804-1" 

STATIC_PATHS = ['images']
