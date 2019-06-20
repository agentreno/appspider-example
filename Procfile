release: python manage.py makemigrations && python manage.py migrate
web: cd api && gunicorn api.wsgi --log-file -
