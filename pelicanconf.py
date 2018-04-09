#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Crosleys'
SITENAME = 'Love Licton'
SITEURL = 'https://lovelicton.com'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

THEME = 'attila'
SITESUBTITLE = 'The Licton Springs Blog'
SITE_DESCRIPTION = ('The blog for the beautiful Licton Springs neighborhood in Seattle, WA. '
                    'Keep up to date on all the latest retail openings, neighborhood events, and news related to '
                    'this North Seattle neighborhood.')
SHOW_SITESUBTITLE_IN_HTML = True
HEADER_COVER = 'images/header.jpg'
SITE_LOGO = '/images/logo.png'
CSS_OVERRIDE = ['static/main.css']
STATIC_PATHS = ['static',
                'images',
                'images/spring',
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
  "timothycrosley": {
    "name": "Timothy Crosley",
    "cover": "https://avatars1.githubusercontent.com/u/2090154?s=400&u=4f46538354444ce0a0d4d89cd676f769d7d846d3&v=4",
    "image": "https://avatars1.githubusercontent.com/u/2090154?s=400&u=4f46538354444ce0a0d4d89cd676f769d7d846d3&v=4",
    "location": "Licton Springs, Seattle, WA",
    "bio": "During the day, I work at DomainTools, where I’m helping to develop predictive security solutions on top of truly large data sets. I can’t resist a good craft beer, a new board game, an arcade, or any food that contains peanut butter."
  }
}
SHOW_CREDITS = {'left': 'Made in Licton Springs, Seattle, WA',
                'right': 'Follow: <a href="https://twitter.com/LictonLove" style="color: #1da1f3; font-weight: bold;">'
                         'Twitter</a> '
                         '<a href="https://www.facebook.com/lovelicton" style="color: #4267b2; font-weight: bold;">'
                         'Facebook</a> '
                         '<a href="https://www.instagram.com/lictonsprings/" style="color: black; font-weight: bold;">'
                         'Instagram</a>'
                         '<br />'
                         '<div style="margin: .5em">'
                         'Contact: <a href="mailto:lovelicton@gmail.com" style="color: #e04c40; font-weight: bold">'
                         'lovelicton@gmail.com</a></div>'
                         '<br />'
                         'Feed: <a href="localhost:8000/feeds/all.rss.xml" style="color: #ee802f; font-weight: '
                         'bold;">RSS</a> <a href="localhost:8000/feeds/all.atom.xml" style="color: #07b392; '
                         'font-weight: bold;">Atom</a>'}
  
SOCIAL = (('twitter', 'https://twitter.com/lictonlove'),
          ('facebook','https://facebook.com/lovelicton'),
          ('envelope','mailto:lovelicton@gmail.com'))


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10
DISQUS_SITENAME = 'lovelicton'
GOOGLE_ANALYTICS = 'UA-115518273-1'
SHOW_FULL_ARTICLE = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
