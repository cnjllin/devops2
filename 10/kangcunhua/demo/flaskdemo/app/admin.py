#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-27 12:01:33
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-27 12:38:10

from . import app


@app.route('/admin')
def admin():
    return "I AM admin!\n"
