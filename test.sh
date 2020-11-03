#!/bin/bash -ex

cd "$(dirname "$0")"

source .env
export $(cut -d= -f1 .env)

python3 -m venv test/venv

test/venv/bin/pip3 install \
    --disable-pip-version-check \
    --isolated \
    --no-cache-dir \
    --requirement api/requirements.txt \
    --requirement test/requirements.txt

PYTHONDONTWRITEBYTECODE=1 test/venv/bin/python3 -m pytest \
    --durations=0 \
    --junitxml=report.xml \
    --html=report.html \
    --self-contained-html \
    --showlocals \
    -p no:cacheprovider \
    -s \
    -vv \
    "$@"
