#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.basePage import BasePage
from selenium.webdriver.common.by import By
from common.commonElements import Elements


class Manage(BasePage):
    """公告管理"""

    # 右侧iframe
    _ele_center = (By.CLASS_NAME, 'iframeClass')
    # 新增
    _ele_update = (By.XPATH, '//*[@id="caozuobt"]/button[1]')
    # 修改
    _ele_edit = (By.XPATH, '//*[contains(text(),"修改")]')
    # 富文本父级ifram
    _ele_father = (By.ID,"lookDetailIframe")
    # 富文本iframe
    _ele_txt = (By.ID, 'ueditor_0')
    # 人员选择
    _ele_personnel = (By.ID, "companyPersonnel")
    # 公告名称
    _ele_addname = (By.ID, 'addname')
    # 富文本内容
    _ele_content = (By.XPATH, "//body//p")
    # 公告内容提交
    _ele_anSubmit = (By.XPATH, "//button[contains(text(),'提交')]")
    # 查询公告名称
    _ele_nitname = (By.ID,"nitname")


    def __init__(self):
        super().__init__()
        self.elements = Elements()

    def click_an(self):
        """点击首页公告"""
        an = self.elements.anElements.ele_an
        self.element_click(an)

    def click_manage(self):
        """点击公告管理"""
        an = self.elements.anElements.ele_manage
        self.element_click(an)

    def center_iframe(self):
        """切换主体iframe"""
        self.cut_iframe(self._ele_center)

    def click_update(self):
        """点击新增"""
        self.element_click(self._ele_update)

    def rich_father_iframe(self):
        """切换父级富文本iframe"""
        self.cut_iframe(self._ele_father)

    def rich_text_iframe(self):
        """切换富文本iframe"""
        self.cut_iframe(self._ele_txt)

    def rich_text(self, text):
        """富文本内容"""
        self.input_text(self._ele_content, text)

    def rich_text_submit(self):
        """富文本内容提交"""
        self.element_click(self._ele_anSubmit)

    def click_personnel(self):
        """点击人员选择"""
        self.element_click(self._ele_personnel)

    def staff(self):
        """选择全体员工"""
        self.element_click(self.elements.comElements.ele_checkAll)

    def submit(self):
        """提交部门人员"""
        self.element_click(self.elements.comElements.ele_submit)

    def title_name(self, text):
        """公告标题"""
        self.input_text(self._ele_addname, text)

    def is_loadding(self):
        """加载动画是否存在"""
        load = self.elements.comElements.ele_loadding
        print(load)
        self.isLoadding(loc=load, tm=15)

    def is_succe(self):
        """是否提交成功"""
        return self.is_element(self.elements.comElements.ele_succe,2)

    def query_name(self,text):
        """输入查询的标题名称"""
        self.input_text(self._ele_nitname,text)

    def click_query(self):
        """点击查询"""
        self.element_click(self.elements.comElements.ele_query_button)

    def is_table(self):
        """判断是否查询出数据"""
        return self.is_element(self.elements.comElements.ele_tr)

    def click_choose(self):
        """点击列表选择"""
        self.element_click(self.elements.comElements.ele_choose)

    def click_delect(self):
        """点击删除"""
        self.element_click(self.elements.comElements.ele_delete)

    def click_affirm(self):
        """点击确认"""
        self.element_click(self.elements.comElements.ele_affirm)

    def is_hint(self):
        """是否有提示"""
        return self.is_element(self.elements.comElements.ele_delete_succe)

    def click_edit(self):
        """点击修改"""
        self.element_click(self.elements.comElements.ele_edit)