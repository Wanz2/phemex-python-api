# -*- coding=utf-8 -*-
# @Time: 2022/2/22 16:22
# @Author: Harper
# @File: websocketbase.py
# @Software: PyCharm

from phemex.websocketbase import WebsocketBase
import unittest


class Test(unittest.TestCase):
    def test_connection(self):   # 函数名必须以test开头
        new_ws = WebsocketBase(False)
        status = new_ws.ws.getstatus()  # 获取连接状态
        # ws.settimeout(10)  # 设置超时时间
        # print(ws.gettimeout())  # 获取超时时间
        new_ws.send_heartbeat(1234, [])
        self.assertEqual(101, status, msg='websocket连接错误')  # 断言连接状态


if __name__ == "__main__":
    unittest.main()


