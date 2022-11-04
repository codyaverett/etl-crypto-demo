from airflow.models import Variable
from airflow.decorators import dag, task
from etherscan import Etherscan
from datetime import datetime, timedelta
import requests

eth = Etherscan(Variable.get("ETHERSCAN_SECRET_KEY"))
serviceAPI = Variable.get("SERVICE_API")


@dag(
    schedule="* * * * *",
    start_date=datetime(2022, 10, 29),
    catchup=False,
    default_args={
        "retries": 2
    },
    max_active_runs=1,
    dagrun_timeout=timedelta(seconds=50),
    tags=['price'])
def eth_prices_dag():
    """
    This DAG simply retrieves and stores the current ETH price in USD and BTC.
    """
    
    @task()
    def get_latest_eth_prices():
        return eth.get_eth_last_price()
    
    @task()
    def log_eth_prices(prices, pair):
        response = requests.post(serviceAPI + "prices/", 
            json={"pair": 1, 
                  "price": float(prices[pair]),
                  "time": datetime
                    .utcfromtimestamp(int(prices[f"{pair}_timestamp"]))
                    .strftime('%Y-%m-%dT%H:%M:%S')})
        
        if(response.status_code != 201):
            raise Exception(response.text)
        
        return response.text
    
    # Call the task functions to infer dependencies
    prices = get_latest_eth_prices()
    log_eth_prices.partial(prices = prices).expand(pair = ["ethusd", "ethbtc"])

# Call the dag function to register the DAG
eth_prices_dag = eth_prices_dag()