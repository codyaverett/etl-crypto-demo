#!/usr/bin/env python

# import api key from .env file
# from dotenv import load_dotenv
# load_dotenv()


# requests eth data from ethscan.io
# and writes it to a file

import requests

# get data from ethscan.io
r = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice&apikey=')

# write data to file
with open('ethData.txt', 'w') as f:
    f.write(r.text)
