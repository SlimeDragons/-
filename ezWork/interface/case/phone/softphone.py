#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.unity.tools import repeat
from interface.unity.data import Data
from interface.action.request_tsoftphone import PhoneActi
import time
import unittest
import sys





class PhoneCase(unittest.TestCase):

    def setUp(self) -> None:
        self.login = self.acti.login()
        # 判断坐席是否已经签入
        if "600" in self.login.text:
            self.login = self.acti.force_login()
            print('重新登录成功')
        elif "500" in self.login.text:
            print('分机号不存在')
            sys.exit()
        else:
            print("坐席签入成功")
        self.ready = self.acti.ready()

    @classmethod
    def setUpClass(cls) -> None:
        cls.acti = PhoneActi()
        cls.data = Data()
        cls._await = cls.data.read_option('softphone', 'ringing', type='int')
        cls._evaluate = cls.data.read_option('softphone','evaluate',type='bool')

    def tearDown(self) -> None:
        self.acti.sign_off()

    # @repeat(50)
    def ttest_1_vdnQueue(self):
        outbound = self.acti.outbound()
        if "200" in outbound.text:
            print("外呼成功")
            time.sleep(self.data.read_option('softphone', 'queue', type='int'))
            self.acti.call_end(self._evaluate)
        elif "500" in outbound.text:
            print("外呼失败")

    def test_2_response(self):
        if '3' in self.ready.text:
            print("未就绪，程序退出")
            sys.exit()
        t_end = time.time() + self._await
        while time.time() < t_end:
            back = self.acti.callBack()
            if 'ringing' in back.text:
                self.acti.ringResponse()
                time.sleep(20)
                self.acti.call_end(self._evaluate)
                break



if __name__ == '__main__':
    unittest.main()
