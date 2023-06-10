#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"netadmin@nida.ac.th"}

/opt/venv/bin/python manage.py makemigrations
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
/opt/venv/bin/python manage.py collectstatic --noinput