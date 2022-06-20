#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface.unity.data import Data


class TSoftphoneUrl():
    def __init__(self):
        _URL = Data()
        self.ip = _URL.read_option('ip', 'url')

    def tsoftphone_url(self):
        """软电话url"""
        return self.ip + '/AesdemoAlone/ChoiceDe'

    def callBlck_url(self):
        """获取振铃状态"""
        return self.ip + '/AesdemoAlone/callback'

    def startTraffic(self):
        """应答"""
        return self.ip + '/AesdemoAlone/startTraffic.html'


