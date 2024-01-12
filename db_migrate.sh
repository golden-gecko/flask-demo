#!/bin/bash -ex

cd "$(dirname "$0")"

source .env
export $(cut -d= -f1 .env)

python3 -m venv venv
venv/bin/pip3 install -r src/requirements.txt

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src venv/bin/python3 -m flask db migrate
