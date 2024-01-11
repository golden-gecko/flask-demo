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
    -c "CREATE USER ${POSTGRES_USER} WITH ENCRYPTED PASSWORD '${POSTGRES_PASSWORD}'"

PGPASSWORD=${POSTGRES_ROOT_PASSWORD} psql \
    -h ${POSTGRES_HOST} \
    -U postgres \
    -d ${POSTGRES_DATABASE_NAME} \
    -c "ALTER DATABASE ${POSTGRES_DATABASE_NAME} OWNER TO ${POSTGRES_USER}"

PGPASSWORD=${POSTGRES_ROOT_PASSWORD} psql \
    -h ${POSTGRES_HOST} \
    -U postgres \
    -d ${POSTGRES_DATABASE_NAME} \
    -c "GRANT ALL ON DATABASE ${POSTGRES_DATABASE_NAME} TO ${POSTGRES_USER}"

python3 -m venv venv
venv/bin/pip3 install -r api/requirements.txt

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=api venv/bin/python3 -m flask db init
