#!/bin/bash

postgres_host=postgres
postgres_port=5432
shift 2
cmd="$@"

# wait for the postgres docker to be running
while ! pg_isready -h $postgres_host -p $postgres_port -q -U postgres; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"




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
