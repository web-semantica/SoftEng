#!/bin/sh

echo "Creating migrations and insert into sqlite database"
python3 fga_ontology/manage.py makemigrations
python3 fga_ontology/manage.py migrate

echo "Run the server"
python3 fga_ontology/manage.py runserver 0.0.0.0:8000
