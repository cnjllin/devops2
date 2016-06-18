#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kangcunhua
# @Date:   2016-05-25 10:38:51
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-17 10:49:45
from app.models import Idc
from flask import current_app
from modules import BaseDao

current_app.logger.debug("初始化Idc模块，准备开始调用指定方法：")
idc = BaseDao(Idc)


def create(**kwargs):
    return idc.create(**kwargs)


def get(**kwargs):
    return idc.get(**kwargs)


def update(**kwargs):
    return idc.update(**kwargs)


def delete(**kwargs):
    return idc.delete(**kwargs)


def getIdc(**args):
    return "测试getIdc()方法:返回传过来的参数" + str(args)
