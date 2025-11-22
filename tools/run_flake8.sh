#!/bin/bash -ex

if [[ -z $1 ]]
then
    SOURCE_DIRECTORY=$(realpath .)
else
    SOURCE_DIRECTORY=$(realpath $1)
fi

if [[ -z $2 ]]
then
    REPORT_DIRECTORY=$(realpath .)
else
    REPORT_DIRECTORY=$(realpath $2)
fi

cd "$(dirname "$0")"

IMAGE_NAME=core-common-tools

docker build -t ${IMAGE_NAME} .
docker run \
    -e PYTHONDONTWRITEBYTECODE=1 \
    -v ${PWD}:/usr/local/app \
    -v ${REPORT_DIRECTORY}:/usr/local/report \
    -v ${SOURCE_DIRECTORY}:/usr/local/src \
    ${IMAGE_NAME} \
    ./run_flake8_no_docker.sh /usr/local/src /usr/local/report
