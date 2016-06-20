#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua
# @Email: kang.cunhua@qq.com
# @Date:   2016-05-27 14:40:47
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-19 10:45:00
import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get("SECRET_KDY") or "abcdefg"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLACHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:root1234@127.0.0.1/reboot"
    ZABBIX_API_URL = "http://192.168.99.14/zabbix"
    ZABBIX_API_USER = "Admin"
    ZABBIX_API_PASS = "zabbix"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s- %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(os.path.join(basedir, 'flask.log'))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
