#!/bin/sh

set -e

python3 manage.py collectstatic --no-input
gunicorn KNFK_website.wsgi:application --bind 0.0.0.0:8000 
