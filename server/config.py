# Copyright 2013 Arunjit Singh. All Rights Reserved.

"""Application configuration and App Engine context."""

__author__ = 'Arunjit Singh <arunjit@me.com>'

import datetime
import os
import re

from google.appengine.api import app_identity

DEVELOPMENT = os.getenv('SERVER_SOFTWARE', '').startswith('Dev')
PRODUCTION = not DEVELOPMENT

AUTH_DOMAIN = os.getenv('AUTH_DOMAIN', '')

_VERSION_ID = os.getenv('CURRENT_VERSION_ID', '0.0').split('.')
VERSION = _VERSION_ID[0]
VERSION_TIMESTAMP = int(_VERSION_ID[1]) << 28
VERSION_DATETIME = datetime.datetime.fromtimestamp(VERSION_TIMESTAMP)

DEBUGGING = DEVELOPMENT
if re.match(r'(?:dev|debug|test)', VERSION):  # staging and prod are PRODUCTION
  DEBUGGING = True


# AppIdentity needs to be stubbed for tests, so this can't be defined globally.
def GetAppId():
  return app_identity.get_application_id()

WEBAPP2_CONFIG = {
    'webapp2_extras.jinja2': {
        'template_path': ['template']
    }
}
