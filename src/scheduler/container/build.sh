#!/bin/bash -xeu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "RUN CONTEXT: $DIR"

docker build \
    -t airflow-dev \
    -f $DIR/dev/airflow.dockerfile $DIR/dev
