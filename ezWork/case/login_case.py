#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from page.login_page import Login
from common.data import Data


class LoginCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.loginPage = Login(flag='f')
        data = Data()
        ITEM = 'user'
        cls._name = data.read_option(ITEM, 'name')
        cls._psw = data.read_option(ITEM, 'password')
        cls._url = data.read_option(ITEM, 'url')

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._psw

    @property
    def url(self):
        return self._url

    def test_login(self):
        self.loginPage.input_name(self._name)
        self.loginPage.input_psw(self._psw)
        self.loginPage.lohin_click()
        time.sleep(0.3)
        flag = self.loginPage.is_repetition()
        if flag:
            self.loginPage.repetition_click()
        now_url = self.loginPage.get_url(second=2)
        self.assertEqual(now_url, self._url, "登录失败")


if __name__ == '__main__':
    unittest.main()
