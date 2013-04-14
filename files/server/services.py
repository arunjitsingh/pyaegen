# Copyright 2013 Arunjit Singh. All Rights Reserved.
"""The API."""

__author__ = 'arunjitsingh'

from google.appengine.ext import endpoints
from protorpc import remote


@endpoints.api(
    name='%(AE_API_NAME)s',
    version='%(AE_API_VERSION)s',
    description='%(AE_API_DESC)s',
    allowed_client_ids=[endpoints.API_EXPLORER_CLIENT_ID],
)
class %(AE_API_CLASS_NAME)sApi(remote.Service):
  # Add `@endpoint.method`s here.
  pass


app = endpoints.api_server([%(AE_API_CLASS_NAME)sApi], restricted=False)
