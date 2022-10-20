#!/bin/bash

# Get current working directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Load environment variables from .env file
set -o allexport
source $DIR/.env
set +o allexport

# Function to expect env variables to be set
function expect_env() {
    if [ -z "${!1}" ]; then
        echo "ERROR: $1 is not set"
        exit 1
    fi
}

# Use expect_env function to check if required env variables are set
expect_env POSTGRES_DB
expect_env POSTGRES_USER
expect_env POSTGRES_PASSWORD

# container names
DB_CONTAINER_NAME="${POSTGRES_DB}_db"
DB_ADMIN_CONTAINER_NAME="${POSTGRES_DB}_pgadmin"

# Pull latest postgres and pgadmin images
docker pull postgres
docker pull dpage/pgadmin4

# Stop and remove containers if they exist
docker rm -f $DB_CONTAINER_NAME $DB_ADMIN_CONTAINER_NAME > /dev/null

# Create temporary directory for postgres data if it doesn't exist
# This is where the database data will be stored
LOCAL_DATA_DIR="$DIR/.$DB_CONTAINER_NAME"
mkdir -p $LOCAL_DATA_DIR

# Run postgres container
# with a local volume for data persistence
# and a local port for access
docker run -d \
--name $DB_CONTAINER_NAME \
-e POSTGRES_DB=$POSTGRES_DB \
-e POSTGRES_USER=$POSTGRES_USER \
-e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
-v $LOCAL_DATA_DIR:/var/lib/postgresql/data \
-p $POSTGRES_PORT:$POSTGRES_PORT \
postgres

# Run pgadmin container
# with a local port for access
docker run -d \
--name $DB_ADMIN_CONTAINER_NAME \
-e PGADMIN_DEFAULT_USER=$POSTGRES_USER \
-e PGADMIN_DEFAULT_EMAIL=$POSTGRES_USER@local.com \
-e PGADMIN_DEFAULT_PASSWORD=$POSTGRES_PASSWORD \
-p 5050:80 \
dpage/pgadmin4

# Wait for postgres to start
while ! docker exec $DB_CONTAINER_NAME pg_isready > /dev/null 2>&1; do
    echo "Waiting for postgres to start..."
    sleep 1
done

# Print success message
echo "--------------------------------------------------"
echo "Database started on port $POSTGRES_PORT"
echo "pgAdmin started on port 5050"
echo
echo "To stop or remove the database containers, run either:"
echo "docker stop $DB_CONTAINER_NAME $DB_ADMIN_CONTAINER_NAME"
echo "docker rm -f $DB_CONTAINER_NAME $DB_ADMIN_CONTAINER_NAME"
echo
echo "Database: $POSTGRES_DB"
echo "User: $POSTGRES_USER"
echo "Password: $POSTGRES_PASSWORD"
echo "Local IP: $(ipconfig getifaddr en0)"
echo "Connection String: postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@localhost:$POSTGRES_PORT/$POSTGRES_DB"
echo
echo "Access pgAdmin at http://localhost:5050 as $POSTGRES_USER@local.com with password '$POSTGRES_PASSWORD'"
echo "--------------------------------------------------"
