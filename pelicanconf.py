#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Crosleys'
SITENAME = 'Love Licton'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'attila'
HEADER_COVER = 'images/header.jpg'
SITE_LOGO = '/images/logo.png'
CSS_OVERRIDE = ['static/main.css']
STATIC_PATHS = ['static',
                'images',
                'extra/robots.txt', 
                'extra/favicon.ico',
                'extra/CNAME'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

COLOR_SCHEME_CSS = 'monokai.css'
AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "website": "http://blog.arulraj.net",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}
SHOW_CREDITS = {'left': 'Made in Licton Springs, Seattle, WA',
                'right': 'Composed by the Crosleys'}
  
SOCIAL = (('twitter', 'https://twitter.com/lictonlove'),
          ('facebook','https://facebook.com/lovelicton'),
          ('envelope','mailto:timothy.crosley@gmail.com'))


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10
DISQUS_SITENAME = 'lovelicton'
GOOGLE_ANALYTICS = 'UA-115518273-1'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
