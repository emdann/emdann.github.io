

# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from typing import Any, Dict


# -- Project information -----------------------------------------------------
#

project = "Personal website"
copyright = "2024, Emma Dann"
author = "Emma Dann"

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
    "myst_nb",
]
templates_path = ["_templates"]

# -- Options for extlinks ----------------------------------------------------
#

extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
}

# -- Options for intersphinx -------------------------------------------------
#

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = False

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
]
myst_heading_anchors = 3

nb_output_stderr = "remove"

# -- Options for HTML output -------------------------------------------

# html_show_sourcelink = True
html_theme = "furo"

# Set link name generated in the top bar.
html_title = "Emma Dann"
html_favicon = "./_assets/favicon.ico"
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "font-stack": "acumin-pro, sans-serif",
        "color-background-primary": "#f5e9dc",
        "color-background-secondary": "#f5e9dc",
        "color-background-hover": "#F5F3ED",
        "color-brand-primary": "black",
        "color-brand-content": "#A46F0D",
        # "color-background-border": "#fffff8",
        "admonition-font-size": "var(--font-size-normal)",
        "admonition-title-font-size": "var(--font-size-normal)",
        # "code-font-size": "var(--font-size--small)",
    },
    "navigation_with_keys": True,
   "footer_icons": [
    {
        "name": "GitHub",
        "url": "https://github.com/emdann/",
        "html": """
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
            </svg>
        """,
        "class": "",
    },
    {
        "name": "Bluesky",
        "url": "https://bsky.app/profile/emmamarydann.bsky.social/",
        "html": """
            <svg xmlns="http://www.w3.org/2000/svg" stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512">
                <path d="M253.1 120.3c-27.3 1.4-54 10.4-76.7 26.2c-30.9 21.6-52.3 54.4-59.9 91.2c-2.5 12.3-3 24.8-1.5 37.3c1.3 10.5 3.8 20.8 7.5 30.6c6.5 17.1 16.7 32.6 29.9 45.1c25.1 23.7 58.9 37.2 93.7 37.2h158.6c5 0 9.8-2 13.4-5.6c3.5-3.5 5.5-8.3 5.5-13.3V273c-0.1-42.7-17.1-83.7-47.2-113.9c-30.2-30.2-71.1-47.2-113.9-47.3c-3.1-0.1-6.3-0.1-9.4 0.1v8.4zM316.5 228c10.4 0 20.5 4.1 27.9 11.5c7.4 7.4 11.5 17.5 11.5 27.9c0 10.4-4.1 20.5-11.5 27.9c-7.4 7.4-17.5 11.5-27.9 11.5c-10.4 0-20.5-4.1-27.9-11.5c-7.4-7.4-11.5-17.5-11.5-27.9c0-10.4 4.1-20.5 11.5-27.9c7.4-7.4 17.5-11.5 27.9-11.5z"/>
            </svg>
        """,
        "class": "",
    },
],
}

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_css_files = []
html_css_files = [
      "css/override.css",
]
html_css_files += ["https://use.typekit.net/ajj5weq.css"]
html_js_files = [
    'https://www.googletagmanager.com/gtag/js?id=G-WZL1ZQLZ7K',
    'google_analytics_tracker.js',
]
html_show_sphinx = False
