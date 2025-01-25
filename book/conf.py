# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
sys.path.insert(0, os.path.abspath('.'))  # Ensure current directory is in path
sys.path.insert(0, os.path.abspath('./utils'))  # Add subfolder to the path

from sphinx.highlighting import lexers
from pseudocode_lexer import PseudocodeLexer

project = 'PyGame Course to learn Python'
copyright = '2025, Daniel Estrada'
author = 'Daniel Estrada'
# 
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.githubpages','myst_parser', "sphinx.ext.viewcode", "sphinx_togglebutton", "sphinx_design", "sphinx_copybutton", "sphinx.ext.autosectionlabel"]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

lexers['pseudocode'] = PseudocodeLexer()
highlight_language = 'pseudocode'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'#'alabaster'
html_static_path = ['_static']
html_css_files = ['./_static/styles.css']
html_title = 'PyGame para aprender Python'


