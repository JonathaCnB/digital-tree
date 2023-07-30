release: python3 manage.py collectstatic
release: python3 manage.py migrate
web: gunicorn digital_tree.wsgi --log-file -