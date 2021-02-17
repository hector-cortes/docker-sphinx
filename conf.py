# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

# -- Project information -----------------------------------------------------
project = os.getenv("PROJECT_NAME")
author = os.getenv("PROJECT_AUTHOR")

# The full version, including alpha/beta/rc tags
release = os.getenv("PROJECT_RELEASE_VERSION")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinxcontrib.confluencebuilder',
]

# Sphinx Confluence configuration
confluence_publish = os.getenv("CONFLUENCE_PUBLISH")
confluence_space_name = os.getenv("CONFLUENCE_SPACE_NAME")
confluence_server_url = os.getenv("CONFLUENCE_SERVER_URL")
confluence_server_user = os.getenv("CONFLUENCE_SERVER_USERNAME")
confluence_server_pass = os.getenv("CONFLUENCE_SERVER_PASSWORD")