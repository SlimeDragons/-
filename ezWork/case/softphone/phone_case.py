#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from page.softphone.phone_page import SoftPhone
from case.login import login
from common.data import Data

class PhoneCase(unittest.TestCase):
    """软电话签入签出、呼出、呼入、评价、挂断"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.phone = SoftPhone()
        data = Data()
        ITEM = 'softphone'
        cls._ext = data.read_option(ITEM, 'ext')
        cls._call_numbers = data.read_option(ITEM, 'call_numbers')
        cls._out_time = data.read_option(ITEM, 'out_time',type='int')
        cls._wait_time = data.read_option(ITEM, 'wait_time',type='int')
        cls.STATE = "就绪"
        cls.OUT_STATE = "振铃"
        cls.END_STATE = "后续"
        cls.BUSY = "置忙"
        cls.CALL = "通话中"



    def tearDown(self) -> None:
        # 初始化
        self.phone.initialize()

    def test_1_phone_in(self):
        """软电话签入签出"""
        self.phone.click_icon()
        self.phone.input_ext(self._ext)
        self.phone.sign_in()
        time.sleep(1)
        self.phone.ready()
        time.sleep(1)
        now_state = self.phone.get_state()
        self.assertEqual(self.STATE, now_state, "签入失败")


    def test_2_call_out(self):
        """软电话外呼"""
        self.phone.click_icon()
        self.phone.input_ext(self._ext)
        self.phone.sign_in()
        time.sleep(1)
        now_state = self.phone.get_state()
        self.assertEqual(self.BUSY, now_state, "签入失败")
        self.phone.call_out_num(self._call_numbers)
        self.phone.dial()
        time.sleep(1)
        now_state = self.phone.get_state()
        self.assertEqual(self.OUT_STATE, now_state, "拨号失败")
        t_end =time.time()+self._out_time
        call_res = False
        while time.time()<t_end:
            now_state = self.phone.get_state()
            if now_state == self.CALL:
                call_res = True
                self.phone.evaluate()
                break
        if call_res == False:
            self.phone.hang_up()
        self.assertTrue(call_res,"外呼失败")

    def test_3_answer(self):
        """软电话接听"""
        self.test_1_phone_in()
        t_end = time.time() + self._wait_time
        call_res = False
        while time.time()<t_end:
            now_state = self.phone.get_state()
            if now_state ==self.OUT_STATE:
                call_res = True
                self.phone.reply()
                break
        self.assertTrue(call_res, "接听电话失败，没有振铃状态")

if __name__ == '__main__':
    unittest.main
