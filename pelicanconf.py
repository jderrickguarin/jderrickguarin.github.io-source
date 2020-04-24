#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Derrick'
SITENAME = 'Tinkering Theodoric'
SITESUBTITLE = u'Contains musings on data science, economics, econometrics, computer science and beyond'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Asia/Manila'
DEFAULT_LANG = 'en'

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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']

PLUGINS = ['ipynb.liquid',  'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

IGNORE_FILES = ['.ipynb_checkpoints']

# Theme settings
THEME = './theme/'

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'JDerrickG'
GITHUB_USERNAME = 'jderrickguarin'
AUTHOR_BLOG = 'http://jderrickguarin.github.io'
AUTHOR_CV = '' 
SHOW_ARCHIVES = False
SHOW_FEED = False 

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'downloads']
