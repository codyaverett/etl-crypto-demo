#!/bin/bash

# Run server on port 8000 
gunicorn --bind 0.0.0.0:9001 --log-level=debug -w 5 --threads 5 project.wsgi
#gunicorn --bind unix:/tmp/etl-service.sock project.wsgi
