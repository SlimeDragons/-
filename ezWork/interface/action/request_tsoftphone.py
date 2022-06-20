#!/usr/bin/env python
# -*- coding: utf-8 -*-
from interface.unity.headers import general
from interface.request_parameter.softphone.softphone_data import SoftphoneData
from interface.url.tsoftphone_url import TSoftphoneUrl
from interface.unity.data import Data
import requests.utils as utils

import requests


class PhoneActi:
    """软电话请求方法"""

    def __init__(self):
        self.ini = Data()
        self._header = general()
        self._data = SoftphoneData()
        phone = TSoftphoneUrl()
        self._url = phone.tsoftphone_url()
        self._call_url = phone.callBlck_url()
        self._cookies = {'agentId':self.ini.read_option('softphone','job')}

    def login(self):
        """签入"""
        result = requests.post(self._url, data=self._data.login_from())
        self._cookies.update(utils.dict_from_cookiejar(result.cookies))
        print('签入：'+result.text)
        return result

    def force_login(self):
        """强制签入"""
        result = requests.post(self._url, data=self._data.force_login_from())
        self._cookies.update(utils.dict_from_cookiejar(result.cookies))
        print("强制签入："+result.text)
        return result

    def sign_off(self):
        """登出"""
        result = requests.post(self._url, data=self._data.signOff(), cookies=self._cookies)
        print("登出："+result.text)
        return result

    def outbound(self):
        """外呼"""
        result = requests.post(self._url, data=self._data.outbound_from(), cookies=self._cookies)
        print("外呼："+result.text)
        return result

    def ready(self):
        """就绪"""
        result = requests.post(self._url, data=self._data.ready(), cookies=self._cookies)
        print("就绪："+result.text)
        return result

    def hang_up(self):
        """挂断"""
        result = requests.post(self._url, data=self._data.hangUp_from(), cookies=self._cookies)
        print("挂断：" + result.text)
        return result

    def call_end(self,is_evaluate=False):
        """
        挂断or评价
        :param is_evaluate:是否点击评价结束
        :return:
        """
        if is_evaluate:
            return self.evaluate()
        else:
            return self.hang_up()

    def callBack(self):
        """获取振铃状态"""
        result = requests.post(self._call_url, data=self._data.call_back(), cookies=self._cookies)
        print("获取状态："+result.text)
        return result

    def ringResponse(self):
        """应答"""
        result = requests.post(self._url, data=self._data.ringResponse(), cookies=self._cookies)
        print('应答：'+result.text)
        return result

    def evaluate(self):
        """评价"""
        result = requests.post(self._url, data=self._data.ringResponse(), cookies=self._cookies)
        print('评价：' + result.text)
        return result
