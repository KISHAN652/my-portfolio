#!/bin/bash

echo "📄 Running migrations..."
python manage.py migrate

echo "🚀 Starting Gunicorn..."
gunicorn portfolio_backend.wsgi:application
