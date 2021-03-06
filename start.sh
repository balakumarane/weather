#!/bin/sh
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
echo ">> Postgres started Successfully"

# Start Gunicorn processes
echo Starting Gunicorn.
python manage.py migrate
echo ....
echo Starting Collectstatic
python manage.py collectstatic --noinput
echo Completed Collectstatic
# Prepare log files and start outputting logs to stdout
mkdir -p /code/logs
touch /code/logs/gunicorn.log
touch /code/logs/gunicorn-access.log
tail -n 0 -f /code/logs/gunicorn*.log &


exec gunicorn weather.wsgi:application \
	            --bind 0.0.0.0:8000 \
                --workers 1\
                --log-level=debug \
                --log-file=/code/logs/gunicorn.log \
                --access-logfile=/code/logs/gunicorn-access.log \
