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

extensions = [
    'numpydoc',
    'sphinx_copybutton',
    'nbsphinx',
    # 'sphinx_panels',
    'sphinx_toggleprompt',
    'sphinx_design',
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

intersphinx_disabled_domains = ['std']

autodoc_typehints = 'signature'
autodoc_default_options = {
    # 'member-order': 'bysource',
    # 'undoc-members': True,
    'exclude-members': (
        'append, clear, copy, count, pop, remove, reverse, sort, extend, index, insert, '
        'from_bytes, to_bytes, conjugate, bit_length, bit_count, sibling_type, elem_type, '
        'as_integer_ratio, border, shape, header, id, height, width, __weakref__, denominator, '
        'imag, numerator, real'
    )
}

numpydoc_xref_param_type = True
numpydoc_attributes_as_param_list = True
numpydoc_class_members_toctree = False
numpydoc_xref_aliases = {
    'pd.DataFrame': 'pandas.DataFrame',
    'pd.Series': 'pandas.Series',
    'np.ndarray': 'numpy.ndarray',
    'bool': 'bool',
    'str': 'str',
    'int': 'int',
    'float': 'float',
    'dict': 'dict',
    # 'tuple': 'tuple',
    'list': 'list',
    # 'set': 'set',
    # values
    'None': 'None',
    # 'True': 'True',
    # 'False': 'False',
}
numpydoc_xref_ignore = {
    'bool', 
    'str', 
    'int', 
    'float', 
    'dict', 
    'tuple', 
    'list', 
    'set', 
    'None', 
    'True', 
    'False',
}

intersphinx_mapping = {
    'pd': ('https://pandas.pydata.org/pandas-docs/stable', None),
    "dateutil": ("https://dateutil.readthedocs.io/en/latest/", None),
    "np": ("https://numpy.org/doc/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "pyarrow": ("https://arrow.apache.org/docs/", None),
}
# numpydoc_show_class_members = True
#
# numpydoc_show_inherited_class_members = False

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
    # "css/getting_started.css",
    # "css/pandas.css",
    # "css/numpy.css",
    "css/test.css",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

# If false, no module index is generated.
html_title = "excelbird"
html_use_modindex = True
html_context = dict(
    default_mode = "light",
    github_user = "ryayoung",
    github_repo = "excelbird",
    github_version = "main",
    doc_path = "docs/source/"
)

# If false, no index is generated.
# html_use_index = True

html_theme_options = dict(
    # navigation_depth = 3,
    # show_nav_level = 3,
    github_url = "https://github.com/ryayoung/excelbird",
    # collapse_navigation = True,
    use_edit_page_button = True,
    show_toc_level = 2,
    # Add light/dark mode and documentation version switcher:
    # "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
)





nbsphinx_prolog = """
.. raw:: html

    <style>

        #notebook-container{
            box-shadow: none !important;
        }

        .container {
            width: 80% !important;
        }

        .notebook_app {
            background: #fff !important;
        }

        body > #header {
            background:  #f57b00;
        }

        .navbar-default {
            background: none;
            border: none;
        }

        .navbar-default .navbar-nav > li > a, #kernel_indicator {
            color: rgba(255, 255, 255, 0.25);
            border-bottom: 2px solid #f57b00;
            transition: all 0.25s;
        }

        .navbar-default .navbar-nav > li > a:hover, #kernel_indicator:hover {
            border-bottom: 2px solid #fff;
            color: rgba(255, 255, 255, 1);
        }

        div.input_area {
            border: none;
            border-radius: 0;
            background: #f7f7f7;
            line-height: 1.5em;
            margin: 0.5em 0;
            padding: 0;
        }

        div.cell {
            transition: all 0.25s;
            border: none;
            position: relative;
            top: 0;
        }

        div.cell.selected, div.cell.selected.jupyter-soft-selected {
            border: none;
            background: transparent;
            box-shadow: 0 6px 18px #aaa;
            z-index: 10;
            top: -10px;
        }


        div#pager {
            opacity: 0.85;
            z-index: 9999;
        }

        .navbar-default .navbar-nav > .open > a, .navbar-default .navbar-nav > .open > a:hover, .navbar-default .navbar-nav > .open > a:focus {
            color: #fff;
            background-color: transparent;
            border-bottom: 2px solid #fff;
        }

        .dropdown-menu {
            z-index: 999999 !important;
            background-color: #f57b00;
            opacity: 0.95;
        }

        .dropdown-menu > li > a {
            color: #fff;
        }

        .dropdown-menu > .disabled > a, .dropdown-menu > .disabled > a:hover, .dropdown-menu > .disabled > a:focus {
            color: rgba(255, 255, 255, 0.25);
        }

        .navbar-nav > li > .dropdown-menu {
            border: none;
            box-shadow: none;
        }

        div.output_wrapper {
            background: #eee;
        }

        div.cell.unselected div.output_area{
            box-shadow: inset 0 0 25px #aaa;
            padding: 1em 0;
            overflow-x: auto;
            transition: all 0.25s;
        }

        div.cell.selected .output_area {
            box-shadow: inset 0 0 5px #aaa;
            padding: 0.5em 0;
            overflow-x: auto;
        }

        div.cell.selected .div.output_scroll {
            box-shadow: none;
        }

        div.output_wrapper {
            margin: 0 0 1em;
            transition: all 0.25s;
        }

        div.cell.selected .output_wrapper {
            margin: 0;
        }

        .dataframe {
            background: #fff;
            box-shadow: 0px 1px 2px #bbb;
        }

        .dataframe thead th, .dataframe tbody td {
            text-align: right;
            padding: 1em;
        }

        .output, div.output_scroll {
            box-shadow: none;
        }

        .rendered_html pre code {
            background: #f4f4f4;
            border: 1px solid #ddd;
            border-left: 3px solid #2a7bbd;
            color: #444;
            page-break-inside: avoid;
            font-family: monospace;
            font-size: 15px;
            line-height: 1.6;
            margin-bottom: 1.6em;
            max-width: 100%;
            overflow: auto;
            padding: 1em 1.5em;
            display: block;
            word-wrap: break-word;
        }

        h1, .h1 {
            font-size: 33px;
            font-family: "Trebuchet MS";
            font-size: 2.5em !important;
            color: #2a7bbd;
        }

    </style>
"""






