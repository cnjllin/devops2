#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-03 10:18:14
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-12 20:54:24
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)                           # 实例化flask
    app.config.from_object(config[config_name])     # 给flask加载配置文件
    config[config_name].init_app(app)               # 初始化
    db.init_app(app)                                # 初始化数据库服务
    # 注册蓝图
    from .main import main as main_blugprint
    app.register_blueprint(main_blugprint)
    return app
