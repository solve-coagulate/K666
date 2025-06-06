#!/bin/sh
# Simple helper to run the dev server without the broken k666-env

export DJANGO_SETTINGS_MODULE=k666.settings
export DEFAULT_DATABASE=sqlite3
export DEBUG=True

python manage.py migrate --noinput
exec python manage.py runserver "$@"
