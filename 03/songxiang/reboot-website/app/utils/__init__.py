#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "SONG Xiang"

from flask import current_app
from app.base import AutoLoad


def api_action(method="", params=None):
    if params is None:
        params = {}
    try:
        module, func = method.split(".")
    except ValueError as e:
        current_app.logger.warning("method传值错误: {}".format(e.message))
        return False

    at = AutoLoad()
    if not at.isValidModule(module):
        current_app.logger.warning("{} 模块不可用".format(module))
        return False
    if not at.isValidMethod(func):
        current_app.logger.warning("{} 函数不可用".format(func))
        return False

    try:
        called = at.getCallMethod()
        if callable(called):
            return called(**params)
        else:
            current_app.logger.warning("{}.{} 函数不能被调用".format(module, func))
            return False

    except Exception as e:
        current_app.logger.warning("调用模块执行中出错: {}".format(e.message))
    return False
