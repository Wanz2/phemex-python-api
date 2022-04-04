# -*- coding=utf-8 -*-
# @Time: 2022/2/20 23:18
# @Author: Harper
# @File: cancel all orders.py
# @Software: PyCharm

from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as constant

# Create a client
client = Client(False)

# # Cancel all orders
try:
    client.cancel_all_contract_orders(constant.Symbol.uBTCUSD)

except PhemexAPIException as e:
    print(e)
