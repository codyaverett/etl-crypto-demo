#!/bin/bash -xeu

# set container name from args or default
CONTAINER_NAME=${1:-nginx}

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "RUN CONTEXT: $DIR"

docker build \
    -t $CONTAINER_NAME \
    -f $DIR/dockerfile \
    $DIR/../
