# -*- coding=utf-8 -*-
# @Time: 2022/2/20 23:12
# @Author: Harper
# @File: cancel one order.py
# @Software: PyCharm

from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as constant

# Create a client
client = Client(False)

# Cancel one order
try:
    orderID = ''
    r = client.cancel_order(constant.Symbol.BTCUSD, orderID)
    print("response:" + str(r))

except PhemexAPIException as e:
    print(e)
