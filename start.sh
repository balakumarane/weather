#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
python manage.py migrate
echo ....
exec gunicorn weather.wsgi:application \
	            --bind 0.0.0.0:8000 \
                --workers 1
# --log-file /tmp/gunicorn.log \
# --log-level INFO 

