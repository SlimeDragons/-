#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.basePage import BasePage
from selenium.webdriver.common.by import By


class SoftPhone(BasePage):
    """软电话条"""
    # 软电话图标
    ele_phone_icon = (By.CSS_SELECTOR, "#yuyinimg")
    # 软电话iframe
    phone_iframe = (By.ID, "softphoneif")
    # 分机号
    ele_input_ext = (By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/input[1]")
    # 签入
    ele_in = (By.CSS_SELECTOR, "#in")
    # 就绪
    ele_re = (By.CSS_SELECTOR, "#re")
    # 应答
    ele_ab = (By.CSS_SELECTOR, "#ab")
    # 拨号
    ele_co = (By.CSS_SELECTOR, "#co")
    # 挂断
    ele_up = (By.CSS_SELECTOR, "#up")
    # 评价
    ele_sa = (By.CSS_SELECTOR, "#sa")
    # 外呼号码
    ele_input_phone = (By.CSS_SELECTOR, "#phone")
    # 软电话状态
    ele_state = (By.CSS_SELECTOR, "#ztdiv")
    def click_icon(self):
        """点击软电话"""
        self.element_click(self.ele_phone_icon)

    def input_ext(self, ext):
        """输入分机号"""
        self.cut_iframe(self.phone_iframe)
        self.element_click(self.ele_input_ext)
        self.input_text(self.ele_input_ext, ext)

    def sign_in(self):
        """签入"""
        self.element_click(self.ele_in)
        self.js_popUp()

    def ready(self):
        """就绪"""
        self.element_click(self.ele_re)

    def get_state(self):
        """获取软电话状态"""
        return self.js_element_text(self.ele_state)

    def call_out_num(self,num):
        """输出外呼号码"""
        self.element_click(self.ele_input_phone)
        self.input_text(self.ele_input_phone,num)

    def dial(self):
        """拨号"""
        self.element_click(self.ele_co)
    def hang_up(self):
        """挂断"""
        self.element_click(self.ele_up)
    def evaluate(self):
        """评价"""
        self.element_click(self.ele_sa)

    def initialize(self):
        """还原初始化页面"""
        self.sign_in()
        self.content_iframe()
        self.click_icon()

    def reply(self):
        """软电话应答"""
        self.element_click(self.ele_ab)