# Configuration file for the Sphinx documentation builder.
# Tuguldur T. Odbadrakh
# 6/8/2025

import os
import sys
from datetime import datetime

# Add project directory to sys.path
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Next Generation Pathways Computational Chemistry Documentation'
author = 'Tuguldur T. Odbadrakh'
copyright = f'{datetime.now().year}, {author}'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',                # Enable Markdown support
    'sphinx.ext.autodoc',         # Autodoc if needed
    'sphinx.ext.napoleon',        # Google-style docstring support
    'sphinx.ext.viewcode',        # Add links to source code
]

# Allow both .rst and .md source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
