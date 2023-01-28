# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'excelbird'
copyright = '2023, Ryan Young'
author = 'Ryan Young'
release = '0.0.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# autodoc_default_options = {
#     'members': True,
#     'undoc-members': True,
#     'member-order': 'bysource',
#     'inherited-members': 'list, int',
# }




extensions = [
    'numpydoc',
    'sphinx_copybutton',
    'sphinx_panels',
    'sphinx_toggleprompt',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.linkcode',
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.githubpages',
    # 'sphinx.ext.napoleon',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

numpydoc_attributes_as_param_list = True
numpydoc_class_members_toctree = False
numpydoc_show_class_members = True

numpydoc_show_inherited_class_members = False
# numpydoc_show_inherited_class_members = {
#     'excelbird.core.gap.Gap': False,
#     'excelbird.core.series.Col': False,
# }

# autodoc_default_options = {
#     'members': True,
#     'undoc-members': True,
#     'member-order': 'bysource',
#     'inherited-members': 'list, int',
# }

# sphinx-panels shouldn't add bootstrap css since the pydata-sphinx-theme
# already loads it
panels_add_bootstrap_css = False

# https://sphinx-toggleprompt.readthedocs.io/en/stable/#offset
toggleprompt_offset_right = 35

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

templates_path = ['_templates']
exclude_patterns = []

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "css/getting_started.css",
    "css/pandas.css",
]

# html_static_path = ['_static']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
# html_theme = 'sphinx_rtd_theme'

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
# html_use_index = True


























