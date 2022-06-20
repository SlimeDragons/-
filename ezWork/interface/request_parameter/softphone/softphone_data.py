#!/usr/bin/env python
# -*- coding: utf-8 -*-
from interface.unity.data import Data


class SoftphoneData():
    def __init__(self):
        self._URL = Data()
        self.ITEM = 'softphone'

    def login_from(self):
        """签入"""
        data = {
            'la': '0',
            'lb': self._URL.read_option(self.ITEM, 'job'),
            'lc': self._URL.read_option(self.ITEM, 'ext'),
            'ld': self._URL.read_option(self.ITEM, 'ext'),
        }
        return data

    def force_login_from(self):
        """强制签入"""
        data = {
            'la': '0',
            'lb': self._URL.read_option(self.ITEM, 'job'),
            'lc': self._URL.read_option(self.ITEM, 'ext'),
            'ld': self._URL.read_option(self.ITEM, 'ext'),
            # 强制登录
            'isforce': '1'
        }
        return data

    def signOff(self):
        """签出"""
        data = {
            'la': '1',
            'lb': '0',
            'lc': '0',
            'ld': self._URL.read_option(self.ITEM, 'ext'),
        }
        return data

    def outbound_from(self):
        """外呼"""
        data = {
            'la': '6',
            'lb': '1',
            # 外呼号码
            'lc': self._URL.read_option(self.ITEM, 'call_numbers'),
            'ld': self._URL.read_option(self.ITEM, 'ext'),
        }
        return data

    def hangUp_from(self):
        """挂断"""
        data = {
            'la': '8',
            'lb': '0',
            'lc': '0',
            'ld': self._URL.read_option(self.ITEM, 'ext'),
        }
        return data

    def ready(self):
        """就绪"""
        data = {
            'la': '7',
            'lb': '0',
            'lc': '101',
            'ld':self._URL.read_option(self.ITEM, 'ext'),
        }
        return data

    def call_back(self):
        """获取来电状态"""
        data = {
            'la': '9',
            'lb': '0',
            'lc': self._URL.read_option(self.ITEM, 'job'),
            'ld': self._URL.read_option(self.ITEM, 'ext'),
        }
        return data

    def ringResponse(self):
        """应答"""
        data = {
            'la': '2',
            'lb': '0',
            'lc': '0',
            'ld': self._URL.read_option(self.ITEM,'ext',type="int"),
        }
        return data

    def evaluate(self):
        """评价"""
        data = {
            'la': '3',
            'lb': '2',
            'lc': self._URL.read_option(self.ITEM, 'evaluate', type="int"),
            'ld': self._URL.read_option(self.ITEM, 'ext', type="int"),
        }
        return data





