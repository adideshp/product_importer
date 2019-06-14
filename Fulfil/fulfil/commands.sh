#!/bin/bash
celery worker --app=worker.worker.app --concurrency=1 --hostname=djangoapp@%h --loglevel=INFO &
daphne -b 0.0.0.0 -p $PORT fulfil.asgi:application
#gunicorn --chdir fulfil --bind :8000 fulfil.wsgi:application
#python manage.py runserver 0.0.0.0:8000
#daphne -b 0.0.0.0 -p 8001 app.asgi:channel_layer