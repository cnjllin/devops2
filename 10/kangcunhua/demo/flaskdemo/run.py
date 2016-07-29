#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-27 12:02:10
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-27 12:03:06

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9898, debug=True)
