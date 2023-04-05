# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_material',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = "sphinx_material"

html_theme_options = {
    # 'logo_only': True,
    'globaltoc_depth': 2,
    'html_minify': False,
    'css_minify': True,
    'globaltoc_collapse': False,
    'globaltoc_includehidden': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
