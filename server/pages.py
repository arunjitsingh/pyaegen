# Copyright 2013 Arunjit Singh. All Rights Reserved.

"""The application's HTML pages."""

__author__ = 'arunjitsingh'

from server import wsgi


class IndexPage(wsgi.RequestHandler):

  def get(self):
    self.response.write(self.RenderTemplate('index.html'))
