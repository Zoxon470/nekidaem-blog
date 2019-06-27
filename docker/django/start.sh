#!/usr/bin/env bash

python manage.py check
python manage.py migrate --noinput
uwsgi --ini docker/django/uwsgi.ini
