web: bin/start-nginx bin/start-pgbouncer-stunnel gunicorn -c gunicorn.conf mobilify.wsgi:application -w 4 -t 120  --max-requests 1200  --env DJANGO_SETTINGS_MODULE='mobilify.settings'
worker: bin/start-pgbouncer-stunnel python manage.py qcluster