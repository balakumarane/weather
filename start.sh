#!/bin/bash
echo ">> Waiting for postgres to start"
WAIT=0
while ! nc -z postgres_db 5432; do
    sleep 1
    WAIT=$(($WAIT + 1))
    if [ "$WAIT" -gt 15 ]; then
    echo "Error: Timeout wating for Postgres to start"
    exit 1
    fi
done
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
