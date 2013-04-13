#!/bin/sh
# Files will be put in ".".

readonly SCRIPT="$0"
readonly APP_NAME="$1"
readonly APP_DESC="$2"

readonly SCRIPT_DIR="$(dirname $SCRIPT)"

if [[ $SCRIPT_DIR == "." || $SCRIPT_DIR == "" ]]; then
  echo "Bad current dir"
  exit 1
fi

if [[ ! -d ".git" ]]; then
  git init
fi

cp -r $SCRIPT_DIR/* ./
rm "$(basename $SCRIPT)"
echo "app/components" >> .gitignore
git add .
git commit -a -m "Initialized Python App Engine application"

echo "

\033[0;32mInitialized Python App Engine application\033[0m

\033[0;33mThis creates the client-side (JavaScript) app as a "separate"
application.. almost.

Update APP_NAME and APP_VERSION in app.yaml, app/component.json,
app/package.json and templates/_base.html (auto-replacement script coming soon)

Update README.md and app/README.md

Update API_NAME, API_VERSION, API_DESC in server/services.py. If not using APIs,
delete server/services.py and the /_ah/spi/.* mapping in app.yaml.

This hasn't created any JS/CSS stuff, but does set up some AngularJS.

Next steps:

# 0. Do all the things mentioned above, about replacing the name stuff.

# 1. Try the base app:
cd app
bower install
cd ..
$PYAE/dev_appserver.py --use_sqlite --port=8888 .

# 2. Set up testing:

# Write python tests, then
nosetests -v

cd app
npm install
grunt test
cd ..

# 3. Build and deploy the app
cd app
grunt
cd ..
$PYAE/appcfg.py update .

\033[0m
"
