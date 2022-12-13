# Django template project

[![CI](https://github.com/nekeal/django-template-project/actions/workflows/backend.yml/badge.svg)](https://github.com/nekeal/django-template-project/actions)

Project based on cookiecutter template generated by cruft.

# Prerequisites

## Native way with virtualenv
- [Python3.10](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Docker way
- [Docker](https://docs.docker.com/engine/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)


## Local Development

## Native way with virtualenv

First create postgresql database:

```sql
create user django_template_project with createdb;
alter user django_template_project password 'django_template_project';
create database django_template_project owner django_template_project;
```

Now you can setup virtualenv and django:
```bash
virtualenv venv
source venv/bin/activate
pip install pip-tools
make bootstrap
```

## Docker way

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
