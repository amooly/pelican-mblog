#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mooly'
SITENAME = 'Mooly\'s Home'
SITETITLE = 'Mooly'
SITESUBTITLE = '一只崇洋媚外的代码狗'
SITEURL = ''
COPYRIGHT_NAME = 'amooly'

USE_LESS = True
MAIN_MENU =True

PATH = 'content'

DEFAULT_LANG = 'zh_CN'
TIMEZONE = 'Asia/Chongqing'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = (('首页', '/'),
         ('列表', '/arhives.html'),
         ('归档', 'http://jinja.pocoo.org/'),
         ('关于', '/author/amooly.html'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/whbfcc'),
          ('github', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme
THEME = '../pelican-mblog-theme'
THEME_STATIC_DIR = 'static'
