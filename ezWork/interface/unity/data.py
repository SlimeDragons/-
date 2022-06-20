#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os.path as os


class Data():
    """配置数据"""

    def __init__(self):
        # 生成config对象
        self.conf = configparser.ConfigParser()
        # 解决调用读取不到文件路径
        BASE_DIR= os.dirname(os.abspath(__file__))
        # 用config对象读取配置文件
        self.conf.read(os.join(BASE_DIR,'config.ini'),encoding="utf-8")

    def read_sections(self):
        """获取sections列表"""
        # self.sections = self.conf.sections()
        return self.conf.sections()

    def read_item(self, item):
        """读取指定sections列表的全部数据"""
        # self.useritem = self.conf.items(item)
        return self.conf.items(item)

    def read_option(self, item, option, type='str'):
        """
        读取指定section，option读取值
        :param item:输入section的值
        :param option:输入option的值
        :param type:返回类型参数默认str，可选str、int、float、bool
        :return:返回类型默认str，可选str、int、float、bool
        """
        if type == "str":
            return self.conf.get(item, option)
        elif type == "int":
            return self.conf.getint(item, option)
        elif type == "float":
            return self.conf.getfloat(item, option)
        elif type == "bool":
            return self.conf.getboolean(item, option)


if __name__ == '__main__':
    a = Data()
    b = a.read_option('user','name')
    print(b)
