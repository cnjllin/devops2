#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-24 14:53:51
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-24 15:01:19


from __future__ import unicode_literals
import json
import requests

headers = {'content-type': 'application/json'}
url = "http://127.0.0.1:5001/api"
data = {
    "jsonrpc": "2.0",
    "method": "App.user",
    "id": "1",
    "params": {
        "name": "wd",
        "age": "18"
    }
}
r = requests.post(url, headers=headers, json=data)
print r.status_code
print r.text
