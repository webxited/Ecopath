#!/bin/sh
sleep 2
python manage.py migrate --no-input
python manage.py createcachetable 

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py collectstatic --noinput
gunicorn Resort.wsgi:application --bind :8002

exec "$@"
