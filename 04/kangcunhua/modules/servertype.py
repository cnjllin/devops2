#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-17 12:24:13
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-17 12:43:12
from app.models import ServerType

from flask import current_app
from modules import BaseDao

current_app.logger.debug("初始化 ServerType模块，准备开始调用指定方法：")
bdao = BaseDao(ServerType)


def create(**kwargs):
    return bdao.create(**kwargs)


def get(**kwargs):
    return bdao.get(**kwargs)


def update(**kwargs):
    return bdao.update(**kwargs)


def delete(**kwargs):
    return bdao.delete(**kwargs)
