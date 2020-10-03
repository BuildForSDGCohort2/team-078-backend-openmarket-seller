# !/usr/bin/env bash

echo "=> Creating database migrations..."
python manage.py makemigrations

echo "=> Performing database migrations..."
python manage.py migrate