#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-27 11:59:53
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-27 12:01:03
from flask import Flask

app = Flask(__name__)

import views
import admin
