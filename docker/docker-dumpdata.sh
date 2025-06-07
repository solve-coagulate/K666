#!/bin/sh

docker-compose exec freek666 python3 manage.py dumpdata --indent 4 > dump.fixtures.json
