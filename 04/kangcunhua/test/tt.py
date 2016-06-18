#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-17 08:10:11
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-17 08:54:15


class ft(object):
    """docstring for ft"""

    def __init__(self):
        super(ft, self).__init__()
        print "fffffffffff"

    def tf(self):
        print "ffff=tttttt"

    def __hhh__(self):
        print("测试")


class Lt(ft):
    """docstring for Lt"""

    def __init__(self, **arg):
        super(Lt, self).__init__()
        self.arg = arg
        print self.arg

    def tf(self):
        print "llllll=tttttt"


class cc(object):
    """docstring for cc"""

    def test(self, t):
        t.tf()
tt = cc()
tt.test(ft())
tt.test(Lt())
ft().hhh
