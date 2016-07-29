#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-26 16:52:33
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-28 18:51:46
import sys
sys.path.append('../')
import utils

utils.write_log('web').info('hello,kang!')
utils.write_log('api').info('hello,world!')

conf = utils.get_config('api')
print conf

token = utils.get_validate("wd", "1", "role", "123456")
print "token执行结果：" + token
print "utils.validate执行结果：" + utils.validate(token, "123456")
