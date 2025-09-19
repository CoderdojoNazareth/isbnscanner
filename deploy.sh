#!/bin/bash

# Navigate to your project directory
cd /home/cdjnazareth/isbnscanner/ || exit

# Pull the latest changes from the main branch
git pull origin main

# Install/update dependencies (optional, but good practice)
# Make sure you have a virtualenv set up for your project
source /home/cdjnazareth/.virtualenvs/venv-isbnscanner/bin/activate
pip install -r requirements.txt

# "Touch" the WSGI file to reload the web app
# The path is found in your PythonAnywhere "Web" tab
touch /var/www/cdjnazareth_eu_pythonanywhere_com_wsgi.py
