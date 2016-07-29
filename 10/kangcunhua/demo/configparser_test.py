#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-26 10:03:04
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-26 10:28:30
"""使用ConfigParser的demo
"""
import ConfigParser


def getconfig(filename, section=''):
    """获取指定文件的配置项

    Args:
        filename (TYPE): 文件名
        section (str, optional): Description

    Returns:
        TYPE: list
    """
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    cf_items = dict(cf.items(section)) if cf.has_section(section) else {}

    return cf_items

if __name__ == '__main__':
    conf = getconfig('configparser_test.conf', 'web')
    print conf
    print conf['port']
    print conf.get('path')
""" output
(python27env) [vagrant@odweb-01 demo]$ python configparser_test.py 
{'path': '/data/web/log', 'port': '1002'}
1002
/data/web/log
"""
