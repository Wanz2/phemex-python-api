# -*- coding=utf-8 -*-
# @Time: 2022/2/20 23:24
# @Author: Harper
# @File: query open orders.py
# @Software: PyCharm

from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as utils

# Create a client
client = Client(False)

#  query open orders
try:
    r = client.query_open_contract_orders(utils.Symbol.BTCUSD)
    print("response:" + str(r))
except PhemexAPIException as e:
    print(e)
