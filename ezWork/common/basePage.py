#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import random
from case.login import login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    """
        page基类，所有page页面全部都要继承该类
    """

    def __init__(self, browser='chrome', tm=5,flag='t'):
        """

        :param browser: 浏览器类型(chrome、firefox、ie)
        :param tm: 等待时间
        :param flag: 是否要登录
        """
        self.driver = self.choose_browser(browser)
        self.driver.get('http://10.16.2.7')
        # 窗口放大
        self.driver.maximize_window()
        if flag == 't':
            login(self.driver)
        # 隐形等待
        self.driver.implicitly_wait(tm)

    def out(self):
        self.driver.quit()

    # def __del__(self):
    #     """关闭浏览器"""
    #     self.driver.quit()

    def choose_browser(self, browser):
        """选择浏览器类型"""
        if browser == "chrome":
            # self.driver = webdriver.Chrome(options=options)
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        return self.driver

    def find_element(self, *loc):
        """查找元素"""
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as msg:
            print("%s未能找到页面元素%s" % (loc, msg))

    def find_elements(self, *loc):
        """查找元素集合"""
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException as msg:
            print("%s未能找到页面元素集合%s" % (loc, msg))

    def element_click(self, loc):
        """点击元素"""
        try:
            self.find_element(*loc).click()
        except InvalidElementStateException as msg:
            print("%s元素不可点击%s" % (loc, msg))

    def elements_click(self, loc, index):
        """点击元素集合的某一项"""
        try:
            self.find_elements(*loc)[index].click()
        except IndexError as msg:
            print(msg, loc, index)

    def get_title(self):
        """获取标签栏"""
        return self.driver.title

    def get_url(self, second=1):
        """获取当前url"""
        time.sleep(second)
        return self.driver.current_url

    def input_text(self, loc, text, is_clear=True):
        """输入内容"""
        try:
            if is_clear:
                self.find_element(*loc).clear()
                # 解决了send_keys输入显示不完成问题，原理单个输入
                for str in text:
                    self.find_element(*loc).send_keys(str)
            else:
                for str in text:
                    self.find_element(*loc).send_keys(str)
        except InvalidElementStateException as msg:
            print("%s元素不可操作%s" % (loc, msg))

    def input_text_s(self, loc, index, text, is_clear=True):
        """集合中的一项输入内容"""
        try:
            if is_clear:
                self.find_elements(*loc)[index].clear()
                for str in text:
                    self.find_elements(*loc)[index].send_keys(str)
            else:
                for str in text:
                    self.find_elements(*loc)[index].send_keys(str)
        except InvalidElementStateException as msg:
            print("%s[%d]元素不可操作%s" % (loc, index, msg))

    def js_element_click(self, loc):
        """解决页面元素点击不了的问题"""
        ele = self.find_element(*loc)

        self.driver.execute_script("arguments[0].click()", ele)

    def js_elements_click(self, loc, index):
        """解决页面元素集点击不了的问题"""
        ele = self.find_elements(*loc)[index]
        self.driver.execute_script("arguments[0].click()", ele)

    def key_esc(self):
        """使用鼠标键盘ESC事件取消弹窗"""
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def js_element_text(self, loc):
        """获取元素文本"""
        return self.find_element(*loc).text

    def isLoadding(self,loc,tm=10):
        time_end = time.time()+tm
        # 判断是否在加载
        flag = True
        while time.time()<time_end:
            ele = self.driver.find_element(*loc).is_displayed()
            if not ele:
                flag = False
                break
        return flag

    def is_element(self, loc,tm=3) -> bool:
        """判断元素是否存在"""
        flag = True
        try:
            self.driver.implicitly_wait(tm)
            ele = self.driver.find_element(*loc).is_displayed()
        except:
            flag = False
            return flag
        else:
            return flag

    def get_pop_text(self):
        """获取弹窗信息"""
        # 弹窗元素
        ele_pop = (By.XPATH, "//p[contains(@class,'el-message__content')]")
        pop = [self.elemnen_text(ele_pop)]
        # print(pop)
        if len(pop) <= 1:
            return pop[0]
        else:
            return "弹窗元素过多无法判断"

    def inputKEY(self, loc):
        """元素进行回车"""
        self.find_element(*loc).send_keys(Keys.ENTER)

    def is_form_item_error(self):
        """判断表达数据格式是否正确"""
        ele_from_err = (By.CLASS_NAME, 'el-form-item__error')
        from_err = False
        fromDriver = self.driver
        try:
            fromDriver.implicitly_wait(1)
            self.driver.find_element(*ele_from_err)
        except:
            from_err = True
            return from_err
        else:
            return from_err

    def random_events(self, a, b, type='num'):
        """随机数字符串"""
        if type == 'num': return str(random.randint(a, b))

    def isQuery(self):
        """判断查询结果是否为暂无数据"""
        is_ele = True
        ele_result = (By.XPATH, '//*[contains(text(),"暂无数据")]')
        result = self.elemnen_text(ele_result)
        if result != '暂无数据':
            is_ele = False
        return is_ele

    def close(self):
        """使用鼠标键盘ESC事件取消弹窗"""
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def js_popUp(self,type="See a sample confirm"):
        """确认js弹窗"""
        # 等待js弹窗
        try:
            WebDriverWait(self.driver,5).until(EC.alert_is_present())
        # self.wait.until()
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass


    def cut_iframe(self,loc):
        """切换指定iframe"""
        self.driver.switch_to.frame(self.find_element(*loc))

    def content_iframe(self):
        """切换默认HTML页面"""
        self.driver.switch_to.default_content()

    def refresh(self):
        """刷新当前浏览器"""
        self.driver.refresh()