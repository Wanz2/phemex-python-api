# -*- coding=utf-8 -*-
# @Time: 2022/3/29 10:59
# @Author: Harper
# @File: query sub-main spot transfer.py
# @Software: PyCharm

import time
from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as utils

client = Client(False)

try:
    r = client.query_sub_to_main_spot_transfer(
        {'currency': utils.Currency.BTC, 'start': 0, 'end': int(time.time() * 1000), 'limit': 50, 'offset': 0})
    print(r)

except PhemexAPIException as e:
    print(e)
