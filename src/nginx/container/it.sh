#!/bin/bash

# set container name from args or default
CONTAINER_NAME=${1:-nginx}

docker exec -it $CONTAINER_NAME bash
