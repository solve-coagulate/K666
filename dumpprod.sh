#!/usr/bin/env bash

. ./env/bin/activate
export DJANGO_SETTINGS_MODULE="k666.settings"

./manage.py dumpdata --natural-foreign --natural-primary -a --indent 4 > fixtures.json
