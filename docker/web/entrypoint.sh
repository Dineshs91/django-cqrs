#! /bin/bash

set -e

until psql -h "postgres_db" -U "postgres" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Run python migrations
python blog/manage.py migrate
python blog/manage.py runserver 0.0.0.0:8000