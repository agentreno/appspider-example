release: python api/manage.py makemigrations && python api/manage.py migrate
web: cd api && gunicorn api.wsgi --log-file -
