#!/bin/bash

echo "Starting example API"
python manage.py makemigrations
python manage.py migrate
exec gunicorn api.wsgi:application --bind 0.0.0.0:8000
