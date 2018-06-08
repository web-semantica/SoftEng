#!/bin/sh

echo "Creating migrations and insert into sqlite database"
python3 softeng/manage.py makemigrations
python3 softeng/manage.py migrate

echo "Run the server"
python3 softeng/manage.py runserver 0.0.0.0:8000
