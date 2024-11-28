
nbsphinx_kernel_name = 'python3' # Notebook kernel

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Automatic Differentiation with Dual Numbers'
copyright = '2024, Fayzan Mahmood'
author = 'Fayzan Mahmood'

# The full version, including alpha/beta/rc tags
release = 'beta'

# -- General configuration ---------------------------------------------------

extensions = [ 'nbsphinx', # For Notebooks
    'sphinx.ext.autodoc', # To generate Automatic Documentation from docstrings
	'sphinx.ext.mathjax', # To render mathematical expressions
	'sphinx_rtd_theme', # Theme 
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
master_doc = 'index'

highlight_language = 'python3'

# For figures
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]