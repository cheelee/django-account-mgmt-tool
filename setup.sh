#!/bin/bash

# Set up Python environment
if [ ! -d env ] ; then
    virtualenv env;
    source env/bin/activate
    pip install -r requirements.txt
else
    source env/bin/activate
fi

# Use the test database as the default demo database
# The reason we make a copy instead of link is that usage of the database changes
#   its timestamp, and this makes the repository mark it as a change.
cp db.sqlite3.test db.sqlite3

# Download and set up app static environment
export appRoot=$PWD/account_tool
mkdir -p externals;
cd externals;

echo "Installing Bootstrap 4 javascript and CSS files."
if [ ! -d bootstrap-4.3.1-dist ] ; then
    if [ ! -f bootstrap-4.3.1-dist.zip ] ; then
	echo "Downloading Bootstrap 4."
	wget https://github.com/twbs/bootstrap/releases/download/v4.3.1/bootstrap-4.3.1-dist.zip
    fi
    echo "Expanding Bootstrap 4 package."
    unzip bootstrap-4.3.1-dist.zip
fi
ln -sfn $PWD/bootstrap-4.3.1-dist $appRoot/static/bootstrap4
echo "*****"

echo "Installing jQuery 3.3.1."
if [ ! -f jquery-3.3.1.min.js ] ; then
    wget https://code.jquery.com/jquery-3.3.1.min.js; 
fi
mkdir -p $appRoot/static/js
ln -sfn $PWD/jquery-3.3.1.min.js $appRoot/static/js/jquery.min.js
echo "*****"

echo "Installing Assets."
ln -sfn $PWD/stubAssets/images $appRoot/static/images
echo "*****"
