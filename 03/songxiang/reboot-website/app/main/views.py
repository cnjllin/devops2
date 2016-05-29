#!/usr/bin/env python
# coding:utf-8
from __future__ import unicode_literals
from . import main
from flask import request, current_app
from app.base import JsonRpc
import json

@main.route('/', methods=['GET', 'POST'])
def index():
    current_app.logger.debug("访问日志")
    return 'index'






@main.route("/api", methods=["GET", "POST"])
def api():
    # application/json
    # application/json-rpc
    allowed_content = ["application/json", "application/json-rpc"]
    if request.content_type in allowed_content:
        jsonData = request.get_json()
        jsonrpc = JsonRpc()
        jsonrpc.jsonData = jsonData
        ret = jsonrpc.execute()
        return json.dumps(ret)
    else:
        return "error"
