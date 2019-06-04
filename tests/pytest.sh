#!/bin/sh

set -o errexit

# run the project's tests
docker-compose -f local.yml run django pytest . -v --junitxml=pytest-report.xml
