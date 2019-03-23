#!/bin/bash
echo "Make migrations"
python manage.py makemigrations
echo "Migrating"
python manage.py migrate
exec "$@"