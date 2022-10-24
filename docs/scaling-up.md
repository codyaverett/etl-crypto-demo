# Scaling up


## Airflow
- Implement Celery workers
- Management queue

## API

I implemented the api in a stateless way.
Process can be horizontally scaled


## Data warehouse

Given I chose to use postgres database there are a few approaches I might take to scale out performance of the database.

- Postgres supports replication for high availabiltiy
- Balance read loads across multiple nodes

There are some solutions that build on top of Postgres that might be worth considering.
- [Postgres-XL](https://www.postgres-xl.org/documentation/intro-whatis-postgres-xl.html) clusters. 
    - There are tradeoffs with using "Postgres-XL's forign key usage has some restrictions.  [CREATE_TABLE](https://www.postgres-xl.org/documentation/sql-createtable.html)
    - It also doesn't support triggers at this point in time.

- [TimescaleDB](https://docs.timescale.com/timescaledb/latest/)
    - Integrates into Postgres via plugin
    - Supports Time series functions for queries
    - Innovative sharding strategies
    - [Hypertables](https://docs.timescale.com/timescaledb/latest/how-to-guides/hypertables/)
    - High availabiltiy configurations