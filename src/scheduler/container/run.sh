#!/bin/bash

# set container name from args or default
CONTAINER_NAME=${1:-airflow-dev}

# directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "RUN CONTEXT: $DIR"

docker rm -f $CONTAINER_NAME > /dev/null

docker run -d \
    --name $CONTAINER_NAME \
    -v $DIR/../dags:/home/airflow/dags \
    -v $DIR/../logs:/home/airflow/logs \
    -p 8080:8080 \
    airflow-dev