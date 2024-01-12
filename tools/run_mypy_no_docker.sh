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

rm -fr ${SOURCE_DIRECTORY}/report_mypy.xml

set +e

mypy \
    --cache-dir /dev/null \
    --ignore-missing-imports \
    --junit-xml ${REPORT_DIRECTORY}/report_mypy.xml \
    --skip-version-check \
    ${SOURCE_DIRECTORY}

status=$?

set -e

exit ${status}
