#!/bin/bash
APP_PORT=${PORT:-8000}

cd /app/
/opt/venv/bin/celery -A core worker -l INFO --autoscale=10,3