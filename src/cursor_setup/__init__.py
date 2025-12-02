"""
cursor-setup: Initialize your Cursor AI context in seconds.

A CLI tool that automates the creation of .cursorrules files.
"""

__version__ = "2.0.0"
__author__ = "cursor-setup contributors"

from cursor_setup.main import app, main
from cursor_setup.templates import TEMPLATES

__all__ = ["app", "main", "TEMPLATES", "__version__"]
