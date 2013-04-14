# Copyright 2013 Arunjit Singh. All Rights Reserved.

"""The main script."""

__author__ = 'arunjitsingh'

import webapp2

from server import config
from server import router


app = webapp2.WSGIApplication(
  routes=router.ROUTES,
  debug=config.DEBUGGING,
  config=config.WEBAPP2_CONFIG)
