#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-27 11:55:58
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-27 11:59:38

from . import app


@app.route('/views')
def views():
    return "I AM VIEWs!\n"
