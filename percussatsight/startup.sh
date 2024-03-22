#!/bin/sh
python manage.py makemigrations
python manage.py migrate

export DJANGO_SUPERUSER_PASSWORD="password"
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_EMAIL="admin@example.com"

python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:8080
