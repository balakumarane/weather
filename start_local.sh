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
echo ">> Postgres started Successfully"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:4444
