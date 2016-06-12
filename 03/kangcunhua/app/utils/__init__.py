#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-07 10:10:54
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-07 22:56:45
from flask import current_app
from app.base import LazyImport
import requests
import json


def api_action(method="", params=None):
    """Summary

   Args:
        method (str, optional): 调用的(模块.方法)
        params (dict, optional): 参数

    Returns:
        json: 远程调用结果
    """
    if params is None:
        params = {}
    try:
        module, func = method.split(".")
    except ValueError as e:
        current_app.logger.warning("method传值错误: {}".format(e.message))
        return False

    lazyimport = LazyImport(module, func)
    if not lazyimport.isValidModule():
        current_app.logger.warning("{} 模块不可用".format(module))
        return False
    if not lazyimport.isValidMethod():
        current_app.logger.warning("{} 函数不可用".format(func))
        return False

    try:
        called = lazyimport.getCallMethod()
        if callable(called):
            return called(**params)
        else:
            current_app.logger.warning("{}.{} 函数不能被调用".format(module, func))
            return False

    except Exception as e:
        current_app.logger.warning("调用模块执行中出错: {}".format(e.message))
    return False


def api_action2(method="", params={}):
    """域外调用例子

    Args:
        method (str, optional): 调用的方法名
        params (dict, optional): 参数

    Returns:
        json: 远程调用结果
    """
    url = "http://127.0.0.1:5000/api"
    header = {
        "content-type": "application/json"
    }
    data = {
        "jsonrpc": 2.0,
        "method": method,
        "id": 0,
        "auth": None,
        "params": params
    }
    r = requests.post(url, headers=header, data=json.dumps(data))
    return r
