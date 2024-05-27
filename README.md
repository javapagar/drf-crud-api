# drf-crud-api
CRUD API REST created with Django Rest Framework

## Virtual env
### Create
```
python -m venv .venv
```
### with Poetry
```
poetry install
```
### with requirements.txt
Before activate .venv
```
python -m pip install -r requirements.txt
```

## Run Django app

```
poetry run python manage.py makemigrations
```

```
poetry run python manage.py migrate
```

```
poetry run python manage.py runserver
```

## URL API ROOT

```
http://127.0.0.1:8000/api/v1/to-do/
```