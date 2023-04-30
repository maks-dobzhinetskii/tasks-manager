# Tasks Manager

  

## Description

  

Tasks Manager allows you to manage all tasks that can be created by authorized users.

  

## Built with

* Django

* Docker

* PostgreSQL

  

## Getting Started Dev

  

In order to use this App: clone this repository to your machine, in terminal go to project directory and:

```

sudo chmod +x ./app/entrypoint.sh

docker compose up -d --build

docker compose exec web python manage.py migrate --noinput

```

## Usage Dev

After you started app you can follow this link http://localhost:8000/tasks/ there you can see all created tasks.

There are also two other endpoints:

http://127.0.0.1:8000/tasks/new/ - there you can create your own task.

http://127.0.0.1:8000/tasks/pk/ - displays detail info about your task.

http://127.0.0.1:8000/tasks/pk/edit/ - there you can update your task.

http://127.0.0.1:8000/tasks/pk/delete/ - there you can delete your task.
  

## Getting Started Prod

  

In order to use this App: clone this repository to your machine, in terminal go to project directory and:

Create .env file and fill it with data as shown below with changing marked variables:

```

DEBUG=1

SECRET_KEY=change_me

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql

SQL_DATABASE=tasks

SQL_USER=change_me

SQL_PASSWORD=change_me

SQL_HOST=db

SQL_PORT=5432

DATABASE=postgres

HOST_URL=https://localhost/

  

```
