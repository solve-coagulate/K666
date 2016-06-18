#!/usr/bin/env bash

. ./env/bin/activate
./manage.py dumpdata --natural-foreign --natural-primary -a --indent 4 > fixtures.json
