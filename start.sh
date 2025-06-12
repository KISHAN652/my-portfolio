#!/bin/bash

echo "📦 Installing dependencies..."
pip install -r reqs.txt

echo "📄 Running migrations..."
python manage.py migrate

echo "🚀 Starting Gunicorn..."
gunicorn portfolio_backend.wsgi:application
