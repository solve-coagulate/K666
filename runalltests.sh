#!/bin/sh

# Simple script to run the project's test suite.
# Currently only the `comments` app has tests.

export DJANGO_SETTINGS_MODULE=comments.test_settings
export DEFAULT_DATABASE=sqlite3
export DEBUG=1

python manage.py test comments
