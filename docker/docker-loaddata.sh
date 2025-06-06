#!/bin/sh

docker-compose exec freek666 python3 manage.py loaddata dump.fixtures.json
