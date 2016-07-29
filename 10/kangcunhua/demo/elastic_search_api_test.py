#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-25 20:45:46
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-25 20:57:04

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(['192.168.99.20'])

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

# es.index传入一条数据
# res = es.index(index="baike", doc_type='baike',id=1, body=doc)
res = es.index(index="baike", doc_type='esbaike', body=doc)     # 不写id会自动生成
print res['created']

# es.get获取索引信息
#res = es.get(index="baike", doc_type='esbaike', id=1)
# print(res['_source'])

# 刷新索引数据
es.indices.refresh(index="baike")

# es.search，搜索数据
res = es.search(index="baike", doc_type='esbaike', body={
    "query": {
        "match": {
            'text': 'cool'
        }
    }
})

print "Got %d Hits:" % res['hits']['total']
for hit in res['hits']['hits']:
    print "%(timestamp)s %(author)s: %(text)s" % hit["_source"]
