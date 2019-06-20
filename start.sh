#!/bin/bash

echo "Starting example API"
exec gunicorn api.wsgi:application --bind 0.0.0.0:8000
