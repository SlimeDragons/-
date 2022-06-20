#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from common.basePage import BasePage
from selenium.webdriver.common.by import By
from common.commonElements import Elements

class Look(BasePage):
    """查看公告"""

    # 查看公告
    _ele_look = (By.XPATH,"//*[contains(text(),'查看公告')]")
    # 公告名称
    _ele_name = (By.ID,"nitname")
    # 状态
    _ele_state = (By.XPATH,"//td[contains(text(),'已查看')]")
    # 右侧iframe
    _ele_center = (By.XPATH, '//*[@id="tab_查看公告"]/iframe')
    # 富文本父级ifram
    _ele_father = (By.ID, "lookDetailIframe")
    # 已查看文本
    _ele_look_text = (By.XPATH,"//*[contains(text(),'已查看')]")

    def __init__(self):
        super().__init__()
        self.elements = Elements()
        time.sleep(1)

    def click_an(self):
        """点击首页公告"""
        an = self.elements.anElements.ele_an
        self.element_click(an)

    def click_lookan(self):
        """点击查看公告"""
        self.element_click(self.elements.anElements.ele_look)

    def center_iframe(self):
        """切换主体iframe"""
        self.cut_iframe(self._ele_center)

    def rich_father_iframe(self):
        """切换父级富文本iframe"""
        self.cut_iframe(self._ele_father)

    def input_title(self,text):
        """输入标题"""
        self.input_text(self._ele_name,text)

    def click_query(self):
        """点击查询"""
        self.element_click(self.elements.comElements.ele_query_button)

    def click_look(self):
        """点击查看"""
        self.element_click(self.elements.comElements.ele_detail)

    def click_close(self):
        """点击关闭"""
        self.element_click(self.elements.comElements.ele_close)

    def is_table(self):
        """判断是否查询出数据"""
        return self.is_element(self.elements.comElements.ele_tr)

    def is_text(self):
        """判断是否已查看公告"""
        return self.is_element(self._ele_look_text)
