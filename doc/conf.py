# -*- coding: utf-8 -*-
#
# pypiv documentation build configuration file, created by
# sphinx-quickstart on Thu Feb 23 13:45:33 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import distutils.command.build
import sphinx_bootstrap_theme

from distutils.dist import Distribution

bdir = distutils.command.build.build(Distribution())
bdir.initialize_options()
bdir.finalize_options()

#sys.path.append(os.path.abspath('../'+bdir.build_lib+'/pypiv/'))
sys.path.append(os.path.abspath('../pypiv/'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosummary',
    'numpydoc']

numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pypiv'
copyright = u'2016-2017, PyPIV Development Team'
author = u'Jonas Ruebsam, Axel Rosenthal, Kevin Luedemann'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.1'
# The full version, including alpha/beta/rc tags.
release = u'a1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinxdoc'
html_theme = 'bootstrap'

html_theme_options = {
    'navbar_title': "PyPIV",
    'navbar_site_name': "",
    'source_link_position' : '',

    'globaltoc_depth': -1,
    'globaltoc_includehidden': "true",

    'navbar_links': [
        ("Examples", "examples"),
        ("Documentation", "api_doc"),
    ],


    'globaltoc_depth': 2,

    'navbar_sidebarrel': False,
    'navbar_pagenav': True,
    'navbar_pagenav_name': "",

    'navbar_fixed_top': False,

    # Bootswatch (http://bootswatch.com/) theme.
    'bootswatch_theme': "flatly",
    'bootstrap_version': "3",
}

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pypivdoc'


# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pypiv.tex', u'pypiv Documentation',
     u'Jonas Ruebsam, Axel Rosenthal, Kevin Luedemann', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pypiv', u'pypiv Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pypiv', u'pypiv Documentation',
     author, 'pypiv', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for autodoc---------------------------------------------------

autoclass_content = "both"

def setup(app):
    app.add_stylesheet("my-styles.css")
