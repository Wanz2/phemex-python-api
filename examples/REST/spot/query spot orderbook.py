# -*- coding=utf-8 -*-
# @Time: 2022/2/20 23:36
# @Author: Harper
# @File: query spot orderbook.py
# @Software: PyCharm

from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as utils

# Create a client
client = Client(False)

# 查询订单薄
try:
    print(client.query_spot_orderbook(utils.Symbol.BTCUSD))
except PhemexAPIException as e:
    print(e)
