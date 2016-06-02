#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-05-27 14:40:47
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-02 10:25:36
from __future__ import unicode_literals
from flask import request, current_app
from . import main
import json
from app.base import JsonRpc


@main.route('/', methods=['GET', 'POST'])
def index():
    current_app.logger.debug("访问首页")
    return 'index'


@main.route("/api", methods=['GET', 'POST'])
def api():
    # application/jaon
    # application/json-rpc
    allowed_content = ["application/json", "application/json-rpc"]

    if request.content_type in allowed_content:
        jsonData = request.get_json()
        current_app.logger.debug("请求json数据为： {}".format(json.dumps(jsonData)))
        jsonrpc = JsonRpc(jsonData)
        jsonrpc.jsonData = jsonData
        ret = jsonrpc.execute()
        return json.dumps(ret, ensure_ascii=False)
    else:
        current_app.logger.debug("用户请求的content-type为： {}, 不予处理".format(request.content_type))
        return "200", 400
