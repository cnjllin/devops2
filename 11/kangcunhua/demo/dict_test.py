#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-24 15:57:03
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-24 15:57:07
import json
import requests

headers = {'content-type': 'application/json'}
data = {"name": "wd", "age": "18"}
url = "http://localhost:5001/"

r = requests.post(url, headers=headers, json=data)
print r.status_code
print r.text
