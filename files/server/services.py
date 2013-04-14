# Copyright 2013 Arunjit Singh. All Rights Reserved.
"""The API."""

__author__ = 'Arunjit Singh <arunjit@me.com>'

from google.appengine.ext import endpoints
from protorpc import remote


@endpoints.api(
    name='API_NAME',
    version='API_VERSION',
    description='API_DESC',
    allowed_client_ids=[endpoints.API_EXPLORER_CLIENT_ID],
)
class API_NAMEApi(remote.Service):
  # Add `@endpoint.method`s here.
  pass


app = endpoints.api_server([API_NAMEApi], restricted=False)
