#!/bin/sh

# Simple script to run the project's test suite.
# Currently the `comments` and `freek666` apps have tests.

export DJANGO_SETTINGS_MODULE=comments.test_settings
export DEFAULT_DATABASE=sqlite3
export DEBUG=1
export SECRET_KEY=dev-secret-key

python manage.py test comments freek666
