sh: sh -c 'cp busineme/settings/databases busineme/settings/databases.py'
sh: sh -c 'cp busineme/settings/security busineme/settings/security.py'
web: gunicorn --pythonpath busineme settings.wsgi --log-file -
