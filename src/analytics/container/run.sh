#!/bin/bash

docker rm -f superset > /dev/null
docker run -d --name superset -p 8088:8088 superset 

docker exec -it superset superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin

# Migrate local DB to latest
docker exec -it superset superset db upgrade

# Setup roles
docker exec -it superset superset init
