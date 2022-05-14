# Setup

## Create a python virtual environment and activate it
```
python -m venv <env_name>
```
*or*
```
mkvirtualenv <env_name> 
```
*depending on the virtualenv package used*

activate the env
```
source <env_name>/bin/activate
```
*or*
```
workon <env_name>
``` 

## Install requirements
```
cd local_path/cloudx-assignment

pip install -r requirements.txt
```

<br>
<br>

## Create postgres database
```
create database <db_name>
```
## Grant ALL privilleges for the user for the database
```
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

<br>
<br>

## Create `.env` file and set up config vars 
*refer `env.example`* and add secret_key, DB link etc.

- for generating new secret key use `get_random_secret_key` from `django.core.management.utils`
and update `.env` file
```
DJANGO_SECRET_KEY=<your_key>
DATABASE_URL=postgres://<user>:<password>@localhost:5432/<dbname>
```


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