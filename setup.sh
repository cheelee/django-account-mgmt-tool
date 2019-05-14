#!/bin/bash

# Set up Python environment
virtualenv env;
source env/bin/activate
pip install -r requirements.txt

# Use the test database as the default demo database
cp db.sqlite3.test db.sqlite3

# Download and set up app static environment
export appRoot=$PWD/account_tool
cd externals;
if [ ! -d bootstrap-4.3.1-dist ] ; then
    if [ ! -f bootstrap-4.3.1-dist.zip ] ; then
	echo "Downloading Bootstrap 4."
	wget https://github.com/twbs/bootstrap/releases/download/v4.3.1/bootstrap-4.3.1-dist.zip
    fi
    echo "Expanding Bootstrap 4 package."
    unzip bootstrap-4.3.1-dist.zip
fi
echo "Installing Bootstrap 4 javascript and CSS files."
cp bootstrap-4.3.1-dist/js/* $appRoot/static/js
cp bootstrap-4.3.1-dist/css/* $appRoot/static/css
if [ ! -f jquery-3.3.1.min.js ] ; then
    wget https://code.jquery.com/jquery-3.3.1.min.js; 
fi
echo "Installing jQuery 3.3.1."
cp jquery-3.3.1.min.js $appRoot/static/js
