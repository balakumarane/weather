#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
gunicorn weather.wsgi:application \
	            --bind 0.0.0.0:8000 \
		                --workers 3

