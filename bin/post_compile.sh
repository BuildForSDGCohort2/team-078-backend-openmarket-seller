# !/usr/bin/env bash

echo "=> Creating database migrations..."
python manage.py makemigrations api accounts

echo "=> Performing database migrations..."
python manage.py migrate