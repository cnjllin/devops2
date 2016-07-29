#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-25 20:00:45
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-25 20:21:23
from datetime import datetime
import requests
import json

# 创建文档(表)
url = 'http://192.168.99.20:9200/baike/test/'
headers = {'content-type': 'application/json'}
data = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
}

r = requests.post(url, headers=headers, json=data)
print "插入document：" + r.text

# 搜索内容
search = {
    'query': {
        'match': {
            'text': 'cool'
        }
    }
}
url = 'http://192.168.99.20:9200/baike/_search'
r = requests.post(url, headers=headers, json=search)
print "搜索结果为：" + r.text
print "\n可以多执行几次本程序，查看搜索结果的命中率 hit 在上升"
