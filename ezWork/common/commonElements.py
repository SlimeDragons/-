#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from munch import DefaultMunch
from selenium.webdriver.common.by import By


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Elements():
    def __init__(self):

        # 公共元素
        _comElements = {
            # 加载
            'ele_loadding': (By.ID, "loadding"),
            # 全选按钮
            'ele_checkAll': (By.ID, "checkChoose"),
            # 提交
            'ele_submit': (By.XPATH, "//a[contains(text(),'提交')]"),
            #提交成功
            'ele_succe':(By.XPATH,"//div[contains(text(),'提交成功！')]"),
            # 查询结果表格元素
            'ele_tr':(By.XPATH,'//*[@id="addtable"]/tr[1]'),
            # 查询按钮
            'ele_query_button':(By.XPATH, "//button[contains(text(),'查询')]"),
            # 列表选择
            'ele_choose':(By.XPATH,'//*[@id="addtable"]/tr[1]/td[1]/input'),
            # 删除按钮
            'ele_delete':(By.XPATH,'//*[@id="caozuobt"]/button[3]'),
            # 删除成功提示
            'ele_delete_succe':(By.XPATH,"//div[contains(text(),'删除成功')]"),
            # 确认按钮
            'ele_affirm':(By.XPATH,"//a[contains(text(),'确定')]"),
            # 修改按钮
            'ele_edit':(By.XPATH,'//*[@id="caozuobt"]/button[2]'),
            # 查看详情
            'ele_detail':(By.XPATH,'//*[@id="addtable"]/tr[1]/td[10]/button'),
            # 关闭
            'ele_close':(By.XPATH,"//button[contains(text(),'关闭')]")
        }
        # 公告公共元素
        _anElements ={
            # 首页公告
            'ele_an' : (By.XPATH, '//*[contains(text(),"首页公告")]'),
            # 公告管理
            'ele_manage' : (By.XPATH, '//*[contains(text(),"公告管理")]'),
            'ele_look' : (By.XPATH, "//a[contains(text(),'查看公告')]"),
        }

        # 字典转对象
        self.comElements = Struct(**_comElements)
        self.anElements = Struct(**_anElements)


