#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-03 10:18:14
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-12 20:54:57

import os
from app import create_app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app.models import Idc
app = create_app(os.getenv('FLASK_CONFIG') or 'development')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, idc=Idc)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
