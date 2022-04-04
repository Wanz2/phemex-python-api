# -*- coding=utf-8 -*-
# @Time: 2022/2/20 23:10
# @Author: Harper
# @File: replace an order.py
# @Software: PyCharm

from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as constant

# Create a client
client = Client(False)

# Send replace if this order not filled yet
try:
    r = client.amend_order({
        'symbol': constant.Symbol.BTCUSD,
        'orderID': '6c50fa2d-bbf2-454e-b141-0aafd509a700',
        'priceEp': 820000})
    print("response:" + str(r))
except PhemexAPIException as e:
    print(e)

