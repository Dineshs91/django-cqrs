#! /bin/bash

set -e

echo "Before postgres check'

until psql -h "postgres_db" -U "postgres" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done


echo "Testing1232"
echo "Hello"

ls -l

echo "howdie"

# Run python migrations
# python blog/manage.py migrate

# sh blog/demo/replay_three.sh

# python blog/manage.py runserver 0.0.0.0:8000
