# -*- coding=utf-8 -*-
# @Time: 2022/4/2 16:50
# @Author: Harper
# @File: query contract orderbook.py
# @Software: PyCharm


from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as utils

# Create a client
client = Client(False)

# 查询合约订单薄
try:
    orderbook = client.query_contract_orderbook(utils.Symbol.BTCUSD)['result']['book']
    print(f'获取的订单薄为: {orderbook}')
    best_ask = orderbook['asks'][1]
    print(f'最低卖价价为:{best_ask}')
    best_bid = orderbook['bids'][1]
    print(f'最高买价为: {best_bid}')

except PhemexAPIException as e:
    print(e)
