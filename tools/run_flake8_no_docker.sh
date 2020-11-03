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

rm -fr ${REPORT_DIRECTORY}/report_flake8.log ${REPORT_DIRECTORY}/report_flake8.xml

set +e

python3 \
    -m flake8 \
    --benchmark \
    --doctests \
    --disable-noqa \
    --output-file ${REPORT_DIRECTORY}/report_flake8.log \
    --show-source \
    --statistics \
    --verbose \
    ${SOURCE_DIRECTORY} \
    "$@"

status=$?

set -e

if [[ ${status} -eq 0 ]]
then
    flake8_junit ${REPORT_DIRECTORY}/report_flake8.log ${REPORT_DIRECTORY}/report_flake8.xml
fi

exit ${status}
