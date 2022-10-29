#!/bin/bash

python manage.py makemigrations
python manage.py migrate

# Run server on port 9001
python manage.py runserver 9001
