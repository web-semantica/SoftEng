#!/bin/sh

# Waiting postgreSQL initialize
postgres_ready() {
python3 << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="", host="db")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgresql is unavailable - Waiting..."
  sleep 1
done

echo "Deleting migrations"
find . -path "softeng/*/migrations/*.pyc"  -delete
find . -path "softeng/*/migrations/*.py" -not -name "__init__.py" -delete

echo "Deleting staticfiles"
find . -path "softeng/settings/static/*"  -delete

echo "Creating migrations and insert into psql database"
python3 softeng/manage.py makemigrations
python3 softeng/manage.py migrate

echo "Run server"
gunicorn --bind 0.0.0.0:8000 --chdir softeng softeng.wsgi
