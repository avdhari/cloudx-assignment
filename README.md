# Setup

## Create a python virtual environment and activate it
```
python -m venv <env_name>
```
or
```
mkvirtualenv <env_name> 
```
*depending on the virtualenv package used*

## Install requirements
```
cd local_path/coudx-assignment

pip install -r requirements.txt
```



## create `.env` file and set up config vars 
*refer `env.example`* and add secret, DB link etc.

- for generating new secret refer use `get_random_secret_key` from `django.core.management.utils`
- if you want to use a postgres DB:
*change `DATABASE` settings in `settings.py` to below one*
```python
DATABASES = {
    'default': env.db()
}
```
and update `.env` file

## Migrate database to apply changes
```
python manage.py migrate
```

## Start dev server
```
python manage.py runserver
```

## Create superuser to access `admin panel`
```
python manage.py createsuperuser
```