#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-26 15:56:07
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-26 17:42:29

import logging
import logging.config

# 绝对路径也可以
# logging.config.fileConfig("/vagrant/demo/logger.conf")
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("api")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
