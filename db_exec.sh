#!/bin/bash -ex

cd "$(dirname "$0")"

source .env
export $(cut -d= -f1 .env)

docker exec -it flask-demo_postgres_1 psql -h ${POSTGRES_HOST} -U ${POSTGRES_USER} -d ${POSTGRES_DATABASE_NAME}
