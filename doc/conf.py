#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinxcontrib.seqdiag',
]
autodoc_default_flags = ['members']
autoclass_content = 'both'
autosummary_generate = True

source_suffix = '.rst'
master_doc = 'index'

project = 'Deep thought'
copyright = '2015, Mice'
author = 'Mice'

version = release = '0.7.5'

html_static_path = ['_static']
exclude_patterns = ['_build']
locale_dirs = ['locale']
# language='ja'

intersphinx_mapping = {'python': ('https://docs.python.org/3.4', None)}


def setup(app):
    app.add_stylesheet('custom.css')

