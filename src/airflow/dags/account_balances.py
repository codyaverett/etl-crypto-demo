from collections import ChainMap
from airflow.models import Variable
from airflow.decorators import dag, task
from datetime import datetime, timedelta
from etherscan import Etherscan
import requests

eth = Etherscan(Variable.get("ETHERSCAN_SECRET_KEY"))
serviceAPI = Variable.get("SERVICE_API")


@dag(
    schedule="5 * * * *",
    start_date=datetime(2022, 10, 29),
    catchup=False,
    default_args={
        "retries": 2
    },
    max_active_runs=1,
    max_active_tasks=5,
    tags=['price'])
def account_balances_dag():
    """
    This DAG simply retrieves and stores the current account balances for a list of accounts.
    """
    
    @task()
    def get_list_of_accounts(**kwargs) -> list:
        """
        _summary_: Fetch the list of watched accounts
        Returns:
            list: List of account addresses
        """
        ti = kwargs['ti']
        
        # TODO: Add filter in api to only return watched accounts
        response = requests.get(serviceAPI + "accounts").json()
        
        watchedAccounts = list(filter(lambda x: x["watch"], response))
        
        for item in watchedAccounts:
            address = item["address"]
            id = item["id"]
            ti.xcom_push(key=address, value=id)
  
        accounts = list(map(lambda x: x["address"], watchedAccounts))
        return accounts
    
    
    @task()
    def create_list_groups(items: list, groupSize: int) -> list:
        """
        _summary_: Bucket the list items into groups of <groupSize>
        Returns:
            list: List of items grouped in lists of size <groupSize>
        """
        groups = []
        for i in range(0, len(items), groupSize):
            groups.append(items[i:i + groupSize])

        return groups
           
    
    @task()
    def fetch_account_balances(accounts: list) -> list:
        """
        _summary_: Fetch the balances for each account in the list of accounts
        Args:
            accounts (list): List of lists of at most <groupSize> accounts
        """
        return eth.get_eth_balance_multiple(accounts)
            
    
    @task()
    def store_account_balances(**kwargs):
        """
        _summary_: Store the balances in the database via the service API
        """
        ti = kwargs["ti"]
        
        accounts = []
        for items in ti.xcom_pull(key="return_value", task_ids="fetch_account_balances"):
            for item in items:
                accounts.append(item)
        
        print(accounts)
        
        for item in accounts:
            account = item["account"]
            balance = item["balance"]
            
            accountId = ti.xcom_pull(key=account, task_ids="get_list_of_accounts")
            r = requests.post(serviceAPI + "balances/", 
                json={"account": accountId, 
                    "amount": balance,
                    "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')})
            print(r.text)

    # Call the task functions to infer dependencies
    accounts = get_list_of_accounts()
    groups = create_list_groups(accounts, 20)
    fetch_account_balances.expand(accounts = groups) >> store_account_balances()

# Call the dag function to register the DAG
account_balances_dag = account_balances_dag()