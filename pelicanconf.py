#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Hoese'
SITENAME = 'David Hoese'
SITEURL = ''
LICENSE_URL = "https://github.com/djhoese/djhoese.github.io-src/blob/master/LICENSE"
LICENSE = "MIT"
THEME = 'theme'
INDEX_SAVE_AS = 'blog_index.html'
DISQUS_SITENAME = 'https-djhoese-github-io'

PATH = 'content'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.youtube',  # embedding videos
    'liquid_tags.vimeo',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
    'liquid_tags.notebook',
    'twitter_card',
]
IGNORE_FILES = ['.ipynb_checkpoints']
LIQUID_CONFIGS = (("IPYNB_EXPORT_TEMPLATE", "notebook.tpl", ""), )

# Notebook plugin
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
EXTRA_HEADER = open('_nb_header.html').read()

TWITTER_USERNAME = 'djhoese'
GITHUB_USERNAME = 'djhoese'
STACKOVERFLOW_ADDRESS = 'https://stackexchange.com/users/192194/djhoese'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']


# Blogroll
LINKS = (('PyTroll', 'http://pytroll.github.io/'),
         ('VisPy', 'http://vispy.org/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/{}/'.format(GITHUB_USERNAME)),
         ('Twitter', 'https://twitter.com/{}'.format(TWITTER_USERNAME)),
         )

#=============
# Twitter Card
#=============
# https://dev.twitter.com/cards
TWITTER_CARD_USE = True # (False)
TWITTER_CARD_SITE = ''  # The site's Twitter handle like @my_blog
TWITTER_CARD_SITE_ID = ''  # The site's Twitter ID
TWITTER_CARD_CREATOR = '@djhoese'  # Your twitter handle like @monkmartinez
TWITTER_CARD_CREATOR_ID = ''  # The site creator's id
GRAVATAR_URL = ''

