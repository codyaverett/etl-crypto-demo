# Operational Data Store

Stores data related to operations and business needs.

- Starts a [timescaleDB](https://hub.docker.com/r/timescale/timescaledb) instance on port `5432` by default.
- Starts a [pgadmin 4](https://registry.hub.docker.com/r/dpage/pgadmin4#!) instance on port `5050`

## Setup

Create [./container/.env] with your settings

```ini
POSTGRES_USER=admin
POSTGRES_PASSWORD=postgres
POSTGRES_DB=crypto
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Build and run the containers

```shell
./container/setup.sh
```

Create database and user for airflow

## Todo

- Streamline setup/creation of airflow_db and airflow user by running creation scripts on startup
