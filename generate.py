#!/usr/bin/env python
# Copyright 2013 Arunjit Singh. All Rights Reserved.

"""Generates an App Engine project with some basic stuff."""

__author__ = 'arunjitsingh'

import os
import shutil
import sys

_HERE = os.path.dirname(__file__)

#_CWD = os.getcwd()

FILES_TO_MODIFY = [
    os.path.join('app', 'bower.json'),
    os.path.join('app', 'package.json'),
    os.path.join('server', 'services.py'),
    os.path.join('app.yaml'),
]

VALUES = [
    ('App Engine application name', 'AE_APP_NAME', '%(appname)s'),
    ('App Engine application version', 'AE_APP_VERSION', 'dev-0'),
    ('App Engine application description', 'AE_APP_DESC', 'Generated App Engine application'),
    ('App Engine API name', 'AE_API_NAME', '%(appname)s'),
    ('App Engine API version', 'AE_API_VERSION', 'v1'),
    ('App Engine API decription', 'AE_API_DESC', 'Generated App Engine API endpoint'),
    ('Angular application name', 'JS_APP_NAME', '%(appname)s'),
    ('Angular application version', 'JS_APP_VERSION', '0.0.0'),
    ('Angular application descrtiption', 'JS_APP_DESC', 'Generated AngularJS application'),
]


def CreateClassName(name):
  def _MakeFirstLetterUppercase(s):
    return s[0].upper() + s[1:]
  parts = name.split('_')
  if len(parts) == 1:
    return _MakeFirstLetterUppercase(parts[0])
  ret = []
  for part in parts:
    ret.append(_MakeFirstLetterUppercase(part))
  return ''.join(ret)


def RewriteFile(fname, replacements):
  with open(fname, 'r') as f:
    data = f.read()
  data = data % replacements
  with open(fname, 'w') as f:
    f.write(data)


def main(argv):
  if len(argv) < 2:
    print "Usage:\n\t%s relative/path/to/directory/to/create" % argv[0]
    sys.exit(1)

  print """
  This will generate an App Engine (Python) application that uses AngularJS
  on the client side. It will ask for a bunch of values.

  """

  src = os.path.join(_HERE, 'files')
  dst = argv[1]
  ignores = shutil.ignore_patterns('*.pyc', '.*')

  appname = os.path.basename(dst)

  replacements = {}
  for prompt, key, default in VALUES:
    default = default % ({'appname': appname})
    prompt = '>> %s [%s]: ' % (prompt, default)
    value = raw_input(prompt).strip()
    replacements[key] = value or default

  replacements['AE_API_CLASS_NAME'] = CreateClassName(
      replacements['AE_API_NAME'])

  shutil.copytree(src, dst, ignore=ignores)

  for fname in FILES_TO_MODIFY:
    fname = os.path.join(dst, fname)
    RewriteFile(fname, replacements)

  print """
  App Engine (python) application initialized.

  Dependencies:
    1. App Engine Python SDK
    2. Nosetests (for Python tests only)
    3. NodeJS + NPM

  Installing Bower (for Javascript library management):
    $ npm -g install bower

  Installing Grunt (for Javascript app build):
    $ npm -g install grunt-cli

  Next steps:
    1. Version control!
        $ git init
        $ git add .
        $ git commit -m "Initialize application"
    2. Pull in AngularJS deps
        $ cd app
        $ bower install
        $ cd ..
    3. Try out the base app
        $ path/to/appengine-python-sdk/dev_appserver.py \\
              --use_sqlite --clear_datastore --port=8888 \\
              .
    4. Run tests
        $ nosetests -v
        $ cd app
        $ npm install
        $ grunt test
        $ cd ..

  """


if __name__ == '__main__':
  main(sys.argv)
