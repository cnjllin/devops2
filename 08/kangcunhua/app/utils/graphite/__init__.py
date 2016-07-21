#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-03 15:21:42
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-03 16:16:40
import requests
import json
from flask import current_app


def get_graphite_keys():
    try:
        r = requests.get("{}metrics/index.json".format(current_app.config.get("GRAPHITE_SERVER")))
        metrics = json.loads(r.content)
        ret = [m[m.index(".") + 1:] for m in metrics if not m.startswith("carbon")]
        return list(set(ret))
    except Exception, e:
        return []
