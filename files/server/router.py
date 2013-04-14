# Copyright 2013 Arunjit Singh. All Rights Reserved.

"""Sets up the application's request handler route mapping."""

__author__ = 'arunjitsingh'

from server import pages

ROUTES = [
    # Add more routes before IndexPage
    (r'/', pages.IndexPage),
]
