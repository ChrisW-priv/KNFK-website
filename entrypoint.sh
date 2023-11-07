#!/bin/sh

python manage.py collectstatic --no-input
gunicorn --workers 4 --bind unix:main.sock -m 007 KNFK_website.wsgi:application
