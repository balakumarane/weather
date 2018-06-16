#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
python manage.py migrate
echo ....
# Prepare log files and start outputting logs to stdout
mkdir -p /code/logs
touch /code/logs/gunicorn.log
touch /code/logs/gunicorn-access.log
tail -n 0 -f /code/logs/gunicorn*.log &


exec gunicorn weather.wsgi:application \
	            --bind 0.0.0.0:8000 \
                --workers 1\
                --log-level=info \
                --log-file=/code/logs/gunicorn.log \
                --access-logfile=/code/logs/gunicorn-access.log \
