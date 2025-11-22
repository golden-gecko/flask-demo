#!/bin/bash -ex

cd "$(dirname "$0")"

source .env
export $(cut -d= -f1 .env)

PGPASSWORD=${POSTGRES_ROOT_PASSWORD} psql \
    -h ${POSTGRES_HOST} \
    -U postgres \
    -c "CREATE DATABASE ${POSTGRES_DATABASE_NAME}"

PGPASSWORD=${POSTGRES_ROOT_PASSWORD} psql \
    -h ${POSTGRES_HOST} \
    -U postgres \
    -d ${POSTGRES_DATABASE_NAME} \
    -c "CREATE USER ${POSTGRES_USER} WITH PASSWORD '${POSTGRES_PASSWORD}'"

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=api:common python3 db_manage.py db init
