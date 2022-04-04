# -*- coding=utf-8 -*-
# @Time: 2022/2/20 22:49
# @Author: Harper
# @File: query account & position.py
# @Software: PyCharm

import pprint
import json
from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as utils

# Create a client
client = Client(False)

# Get account and positions
try:
    response = client.query_account_and_positions(utils.Currency.USD)
    pprint.pprint(response)
    # with open('query_account_and_positions.txt', 'w') as fp:
    #     fp.write(json.dumps(response, indent=4))

except PhemexAPIException as e:
    print(e)

