#!/usr/bin/env python
# -*- coding: utf-8 -*-

def repeat(times):
    """重复执行方法"""
    def repeatHelper(f):
        def callHelper(*args):
            for i in range(0, times):
                f(*args)
        return callHelper
    return repeatHelper