## Requirements
- [x] ETL job scheduler (apache airflow)
- [ ] Data for charts and dashboards
    - [x] Price timeseries stats
    - [x] Assets
    - [x] Networks
    - [x] Trading Pairs
    - [x] Account watch list
        - [ ] assets/tokens
        - [ ] account balance
        - [ ] internal_txns
        - [ ] account type
        - [ ] account transactions  
- [x] Dataware house solution (postgres/TimescaleDB)
- [ ] Charts and Dashboards (apache superset)

## Project
- [x] setup development infrastructure
    - [x] apache airflow
    - [x] apache superset
    - [x] timescaleDb
    - [x] pgadmin4
    - [x] linux server
    - [x] nginx reverse proxy
- [x] document development setup
- [x] Create public subdomain for exposing resources for demo
- [x] Nginx setup, ssl configuration
- [x] Django ORM to manage table creation and table relations
- [x] REST Api for querying and managing database
- [ ] Apache Airflow Operator for interacting with API/DB
- [x] SQL scripts to inject inital datasets 
- [ ] DB backups for disaster recovery

## Nice to haves
- [x] Design an incremental data load which can be started/stopped anytime and rerun on demand 
- [ ] Incorporate data pipeline monitoring from start to end with alerting 
- [ ] Describe the necessary steps to maintain and evolve your data pipeline
- [ ] Implement quality checks 
- [ ] Build prediction models for the key metrics mentioned in the requirements and visualize the outcome