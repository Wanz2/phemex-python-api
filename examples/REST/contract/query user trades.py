# -*- coding=utf-8 -*-
# @Time: 2022/3/26 13:08
# @Author: Harper
# @File: query user trades.py
# @Software: PyCharm

import time
import pandas as pd
from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as utils

# pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)  # 横向最多显示多少个字符
pd.set_option('display.max_colwidth', 1000)
pd.set_option('expand_frame_repr', False)  # False表示不允许换行
pd.set_option('display.max_rows', None)  # 显示所有行

# Create a client
client = Client(True)

try:
    r = client.query_user_trades({'symbol': utils.Symbol.ETHUSD,
                                  'tradeType': 'Trade',
                                  'start': 0,
                                  'end': 0,
                                  'limit': 50,  # default 50
                                  'offset': 0,
                                  'withCount': True})
    user_trades = r['data']['rows']

    if user_trades:
        user_trades = pd.DataFrame(user_trades)
        user_trades.columns = ['transactTimeNs', 'symbol', 'currency', 'action', 'side', 'tradeType', 'execQty',
                               'execPriceEp', 'orderQty', 'priceEp', 'execValueEv', 'feeRateEr', 'execFeeEv',
                               'closedSize', 'closedPnlEv', 'ordType',
                               'execID', 'orderID', 'clOrdID', 'execStatus']
        print(user_trades)    # 需要关掉pycharm的soft-warp
    else:
        print(f'获取到的历史成交订单为: {user_trades}')

except PhemexAPIException as e:
    print(e)
