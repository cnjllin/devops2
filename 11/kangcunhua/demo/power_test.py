#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-24 16:39:18
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-24 18:08:52
from __future__ import unicode_literals
import json
import requests

url = "http://127.0.0.1:2000/api"


def rpc():
    headers = {'content-type': 'application/json', }
    # create 请求

    data = {
        "jsonrpc": "2.0",
        "method": "power.create",
        "id": "1",
        "params": {
            "name": "cdntest",
            "name_cn": "cdn刷新123",
            "url": "http://cdn.com",
            "comment": "cdn刷新"
        }
    }
    data_get = {
        "jsonrpc": "2.0",
        "method": "power.get",
        "id": "1",
        "params": {
            "where": {
                "name": "cdntest",
            },
            "output": ["name", "name_cn"]
        }
    }
    data_getlist = {
        "jsonrpc": "2.0",
        "method": "power.getlist",
        "id": "1",
        "params": {
            "output": ["name", "name_cn"]
        }
    }
    data_delete = {
        "jsonrpc": "2.0",
        "method": "power.delete",
        "id": "1",
        "params": {
            "where": {
                "name": "cdntest"
            }
        }
    }

    r = requests.post(url, headers=headers, json=data_delete)
    print r.status_code
    print r.text
rpc()
