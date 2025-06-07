#!/bin/bash

# See if we have wait-for-it installed
if ! [ -e wait-for-it ]; then
    git clone https://github.com/vishnubob/wait-for-it
fi

./wait-for-it/wait-for-it.sh postgres:5432

sleep 3

echo "Migrating Models"
python3 manage.py migrate

echo "Starting Dev Server"
python3 manage.py runserver 0.0.0.0:8000
