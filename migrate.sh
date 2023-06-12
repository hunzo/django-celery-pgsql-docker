#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"netadmin@nida.ac.th"}

until /opt/venv/bin/python manage.py migrate --noinput
do
    echo "wait for database..."
    sleep 2
done

/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
/opt/venv/bin/python manage.py collectstatic --noinput