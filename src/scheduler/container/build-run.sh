#!/bin/bash

# set container name from args or default
CONTAINER_NAME=${1:-airflow-dev}

# directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "RUN CONTEXT: $DIR"

bash $DIR/build.sh

$DIR/run.sh $CONTAINER_NAME