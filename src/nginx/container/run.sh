#!/bin/bash

# set container name from args or default
CONTAINER_NAME=${1:-nginx}

# directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "RUN CONTEXT: $DIR"

docker rm -f $CONTAINER_NAME > /dev/null

docker run -d \
    --name $CONTAINER_NAME \
    -v $DIR/../content:/usr/share/nginx/html \
    -v $DIR/../logs:/var/logs/nginx \
    -v $DIR/../config:/etc/nginx/ \
    -p 80:80 \
    -p 433:433 \
    nginx