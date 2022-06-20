#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from page.announcement.manage_page import Manage
from case.login import login
from common.data import Data


class ManageCase(unittest.TestCase):
    """公告管理"""

    @classmethod
    def setUpClass(cls) -> None:
        data = Data()
        ITEM = 'announcement'
        cls._annText = data.read_option(ITEM, 'content')
        cls._annName = data.read_option(ITEM, 'title')
        cls._edit_annText = data.read_option(ITEM, 'edit_content')
        cls._edit_annName = data.read_option(ITEM, 'edit_name')
        cls.an = Manage()
        cls.an.click_an()
        cls.an.click_manage()
        cls.an.center_iframe()

    def tearDown(self) -> None:
        time.sleep(1.5)
        # 还原iframe状态
        self.an.content_iframe()
        self.an.center_iframe()

    def test_1_update(self):
        """新增公告"""
        self.an.click_update()
        self.assertFalse(self.an.is_loadding(), "公告富文本加载失败")
        # 切换两次iframe到富文本
        self.an.rich_father_iframe()
        self.an.rich_text_iframe()
        self.an.rich_text(self._annText)
        #切换到页面按钮iframe
        self.an.content_iframe()
        self.an.center_iframe()
        self.an.rich_father_iframe()
        self.an.click_personnel()
        time.sleep(0.5)
        self.an.staff()
        self.an.submit()
        self.an.title_name(self._annName)
        self.an.rich_text_submit()
        self.assertTrue(self.an.is_succe(), "提交失败")

    def test_2_query(self):
        """查询公告"""
        self.an.query_name(self._annName)
        self.an.click_query()
        self.assertTrue(self.an.is_table(), "查询失败")
        pass

    def ttest_4_delete(self):
        """删除公告"""
        self.test_2_query()
        time.sleep(1)
        self.an.click_choose()
        self.an.click_delect()
        self.an.click_affirm()
        self.assertTrue(self.an.is_hint(), '删除失败')
        pass

    def test_3_edit(self):
        """修改公告"""
        self.test_2_query()
        time.sleep(1)
        self.an.click_choose()
        self.an.click_edit()
        # 切换两次iframe到富文本
        self.an.rich_father_iframe()
        self.an.rich_text_iframe()
        self.an.rich_text(self._edit_annText)
        #切换到页面按钮iframe
        self.an.content_iframe()
        self.an.center_iframe()
        self.an.rich_father_iframe()
        self.an.title_name(self._annName)
        self.an.rich_text_submit()
        self.assertTrue(self.an.is_succe(), "提交失败")



if __name__ == '__main__':
    unittest.main()
