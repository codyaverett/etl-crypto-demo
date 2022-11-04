# Scaling up

This document depicts the steps I would recommend taking to continue to develop and scale the project to support more features in the future.

## Airflow
- Implement Celery workers
- Implement Redis Queue
- Standardize interactions with the service layer 

## Database (DataWarehouse)

- I started with a standard postgres instance, but swapped it out for a timescalDB instance.
- [TimescaleDB](https://docs.timescale.com/timescaledb/latest/)
    - Integrates into Postgres via plugin
    - Supports Time series functions for queries
    - Innovative sharding strategies
    - [Hypertables](https://docs.timescale.com/timescaledb/latest/how-to-guides/hypertables/)
    - Hypertables can be distributed across clusters of timescaleDB instances
    - High availability configurations

## Service

- Continue to build models using Django ORM?  OR  Look into using DBT to manage tables instead?
- Implement api routes that accept multiple update artifacts
- Use atomic transactions in the api layer to minimize calls to the database
- There is a trade-off where django's admin panel would not be available if I chose to use sql alchemy across the board
- Process can be horizontally scaled


## Superset

- Set up docker container volume to prevent loss of dashboard/chart configuration
- 