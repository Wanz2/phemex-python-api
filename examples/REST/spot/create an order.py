# -*- coding=utf-8 -*-
# @Time: 2022/3/10 20:57
# @Author: Harper
# @File: create an order.py
# @Software: PyCharm

import time
from phemex.client import Client
from phemex.exceptions import PhemexAPIException
import phemex.constant as utils

# Create a client
client = Client(False)

try:
    r = client.place_spot_order_by_post({
        "symbol": utils.Symbol.sBTCUSDT,
        "clOrdID": "JackTest1" + str(time.time()),
        # "clOrdID": str(uuid.uuid4()),
        "qtyType": utils.Trade.qtyType_ByBase,
        "side": utils.Trade.SIDE_BUY,
        "baseQtyEv": 1000_0000,         # price scale factor  以BTC为交易单位 实际下单数量为该数除以10^8
        # 'quoteQtyEv': 10_0000_0000,    # price scale factor  以USDT为交易单位 实际下单数量为该数除以10^8
        "priceEp": 3_7000_0000_0000,
        "ordType": utils.Trade.ORDER_TYPE_Limit,
        "timeInForce": utils.Trade.TIF_GOOD_TILL_CANCEL})
    print("response:" + str(r))
    ordid = r["data"]["orderID"]

except PhemexAPIException as e:
    print(e)
