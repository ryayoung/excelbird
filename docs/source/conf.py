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
    pygment_light_style="manni",
    pygment_dark_style="stata-dark",
)


nbsphinx_prolog = """
.. raw:: html

    <style>

        #notebook-container{
            box-shadow: none !important;
        }

        .input_area {
            border: none !important;
        }

        div.nbinput.container div.prompt, div.nboutput.container div.prompt {
            display: none;
        }



    </style>
"""






        # .input_area {
        #     border: none !important;
        #     border-bottom: 0.5px solid var(--pst-color-info) !important;
        # }
        #
        # .highlight-ipython3 .highlight {
        #     background-color: #f9f9f9 !important;
        # }
