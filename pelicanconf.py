#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Licton Springs Community Council'
SITENAME = 'Licton Springs Community Council'
SITEURL = 'https://lictonsprings.org'

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

INDEX_SAVE_AS = 'latest.html'
THEME = 'attila'
SITESUBTITLE = 'Building Community Since 1990'
SITE_DESCRIPTION = ('The official website for the Licton Springs Community Council.')
SHOW_SITESUBTITLE_IN_HTML = True
HEADER_COVER = 'images/header.jpg'
HEADER_COVERS_BY_CATEGORY = {}
SITE_LOGO = '/images/logo.png'
CSS_OVERRIDE = ['static/main.css']
STATIC_PATHS = ['static',
                'images',
                'images/spring',
                'extra/robots.txt',
                'extra/favicon.ico',
                'extra/work_party.pdf',
                'extra/historical_minutes.docx',
                'extra/LSCC_Bylaws_2022-02-16.pdf',
                'extra/CNAME',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/work_party.pdf': {'path': 'work_party.pdf'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/historical_minutes.docx': {'path': 'historical_minutes.docx'},
    'extra/LSCC_Bylaws_2022-02-16.pdf': {'path': 'LSCC_Bylaws_2022-02-16.pdf'},
}

COLOR_SCHEME_CSS = 'monokai.css'
AUTHORS_BIO = {
  "timothycrosley": {
    "name": "Timothy Crosley",
    "cover": "images/spring/trees.jpg",
    "image": "https://avatars1.githubusercontent.com/u/2090154?s=400&u=4f46538354444ce0a0d4d89cd676f769d7d846d3&v=4",
    "location": "Licton Springs, Seattle, WA",
    "bio": "During the day, I work at DomainTools, where I’m helping to develop predictive security solutions on top of truly large data sets. I can’t resist a good craft beer, a new board game, an arcade, or any food that contains peanut butter."
  },
  "amandacrosley": {
      "name": "Amanda Crosley",
      "cover": "images/spring/bird.jpg",
      "image": "images/amandacrosley.jpg",
      "location": "Licton Springs, Seattle, WA",
      "bio": "When I'm not mentoring the next generation of STEM leaders, urban hiking through Seattle or playing arcade/board games, you can find me @ Microsoft driving analytics for Bing Ads search advertising."
  }
}
SHOW_CREDITS = {'left': 'Made in Licton Springs, Seattle, WA',
                'right': 'Follow: <a href="https://twitter.com/LictonSprings" style="color: #1da1f3; font-weight: bold;">'
                         'Twitter</a> '
                         '<a href="https://www.facebook.com/LictonSpringsNeighborhood/" style="color: #4267b2; font-weight: bold;">'
                         'Facebook</a> '
                         '<a href="https://www.instagram.com/lictonsprings/" style="color: black; font-weight: bold;">'
                         'Instagram</a>'
                         '<br />'
                         '<div style="margin: .5em">'
                         'Contact: <a href="mailto: lictonsprings@hotmail.com" style="color: #e04c40; font-weight: bold">'
                         ' lictonsprings@hotmail.com</a></div>'
                         '<br />'
                         'Feed: <a href="/feeds/all.rss.xml" style="color: #ee802f; font-weight: '
                         'bold;">RSS</a> <a href="/feeds/all.atom.xml" style="color: #07b392; '
                         'font-weight: bold;">Atom</a><br /><br />'
                         '<a href="https://www.paypal.com/donate/?token=NE1anuglqCz3JeajqvU-yxgiic3qyD912FQtG11H_ROYYde_Dw8dJwwzxZKa2TsbDVxygm&country.x=US&locale.x=US&Z3JncnB0=" style="color: green; font-weight: bold">Donate</a>'}

SOCIAL = (('twitter', 'https://twitter.com/lictonlove'),
          ('facebook','https://facebook.com/lovelicton'),
          ('envelope','mailto:lovelicton@gmail.com'))


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('About Licton Springs', '/pages/about-licton-springs.html'),
    ('Map of the Neighborhood', '/pages/neighborhood-map.html'),
    ('Community Calendar', '/pages/community-calendar.html'),
    ('Latest from the Council', '/latest.html'),
    ('Neighborhood Blog', 'https://lovelicton.com'),
    ('History of Licton Springs', '/pages/history-of-licton-springs.html'),
    ('Old Website', 'https://licton.github.io/lictonsprings_org_legacy/index.html'),
    ('Historical Minutes', '/historical_minutes.docx'),
    ('Council Bylaws', '/LSCC_Bylaws_2022-02-16.pdf'),
)

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

DEFAULT_PAGINATION = 5
DISQUS_SITENAME = 'lictonsprings'
GOOGLE_ANALYTICS = 'UA-115518273-2'
SHOW_FULL_ARTICLE = True
EXTRA_TEMPLATES_PATHS = ['templates', ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
