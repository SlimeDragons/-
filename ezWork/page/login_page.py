#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.basePage import BasePage
from selenium.webdriver.common.by import By



class Login(BasePage):
    """登录页"""
    # 用户名
    ele_name = (By.CSS_SELECTOR, '#employess_number')
    # 密码
    ele_psw = (By.CSS_SELECTOR, '#employess_password')
    # 确定
    ele_click = (By.CSS_SELECTOR, '#login_btn')
    # 重复登录
    ele_hint = (By.CSS_SELECTOR,'#sureid')

    def input_name(self, name):
        """输入用户名"""
        self.input_text(self.ele_name, name)

    def input_psw(self, psw):
        """输入密码"""
        self.input_text(self.ele_psw, psw)

    def lohin_click(self):
        """登录确定"""
        self.element_click(self.ele_click)

    def is_repetition(self):
        """判断是否重复登录"""
        return self.is_element(self.ele_hint)

    def repetition_click(self):
        """重复登录后确定"""
        self.element_click(self.ele_hint)