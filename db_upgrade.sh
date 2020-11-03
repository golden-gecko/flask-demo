#!/bin/bash -ex

cd "$(dirname "$0")"

source .env
export $(cut -d= -f1 .env)

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=api:common python3 db_manage.py db upgrade
