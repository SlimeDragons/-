#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.unity.data import Data


class RdWebChat():
    def __init__(self):
        _URL = Data()
        self.ip = _URL.read_option('ip', 'url')

    def online(self):
        """在线状态"""
        return self.ip + '/RDWebChat/online.html'

    def waitSum(self):
        """获取排队信息"""
        return self.ip+'/RDWebChat/waitSum.html'

