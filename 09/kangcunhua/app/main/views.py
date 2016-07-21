#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-05-27 14:40:47
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-07 22:14:58
from __future__ import unicode_literals
from flask import request, current_app
from . import main
import json
from app.base import JsonRpc
from flask import render_template, redirect

# @main.route('/', methods=['GET', 'POST'])
# def index():
#     current_app.logger.debug("访问首页")
#     return 'index'


@main.route('/', methods=['GET', 'POST'])
def index():
    return redirect("/dashboard/")


@main.route("/dashboard/", methods=['GET'])
def dashboard():
    return render_template("public/dashboard.html")


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
        return ret
        # return json.dumps(ret, ensure_ascii=False)
    else:
        current_app.logger.debug("用户请求的content-type为： {}, 不予处理".format(request.content_type))
        return "200", 400
