#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-13 11:01:26
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-17 10:49:42
from app.models import Manufacturers

from flask import current_app
from modules import BaseDao

current_app.logger.debug("初始化Manufacturers模块，准备开始调用指定方法：")
bdao = BaseDao(Manufacturers)


def create(**kwargs):
    return bdao.create(**kwargs)


def get(**kwargs):
    return bdao.get(**kwargs)


def update(**kwargs):
    return bdao.update(**kwargs)


def delete(**kwargs):
    return bdao.delete(**kwargs)
