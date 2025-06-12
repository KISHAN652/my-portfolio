#!/bin/bash

echo "Running database migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
gunicorn portfolio_backend.wsgi:application
