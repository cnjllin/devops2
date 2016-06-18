#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kangcunhua
# @Date:   2016-05-25 14:22:12
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-17 10:24:31
"""
    一个包是一个带有特殊文件 __init__.py 的目录。
    __init__.py 文件定义了包的属性和方法。其实它可以什么也不定义；可以只是一个空文件，但是必须存在。
    如果 __init__.py 不存在，这个目录就仅仅是一个目录，而不是一个包，它就不能被导入或者包含其它的模块和嵌套包。
    __init__.py 控制着包的导入行为。假如 __init__.py 为空，那么仅仅导入包是什么都做不了的。
"""
from app.utils import check_field_exists, check_output_field, check_order_by, check_limit, process_result, check_update
from app.models import db
from flask import current_app


class BaseDao(object):
    """docstring for BaseDao"""

    def __init__(self, Module):
        super(BaseDao, self).__init__()
        self.Module = Module

    def create(self, **kwargs):
        # 1. 获取参数
        # 2. 验证参数是否合法
        check_field_exists(self.Module, kwargs)
        idc = self.Module(**kwargs)
        db.session.add(idc)
        try:
            db.session.commit()
        except Exception as e:
            current_app.logger.warning("插入错误: {} ".format(e.message))
            raise Exception("commit error")
        # 3. 插入到数据库
        # 4. 返回插入的状态
        return idc.id

    def get(self, **kwargs):
        # 整理条件
        output = kwargs.get("output", [])
        limit = kwargs.get("limit", 10)
        order_by = kwargs.get("order_by", "id desc")
        where = kwargs.get("where", {})

        # 验证
        # 验证output
        check_output_field(self.Module, output)
        # 验证order_by
        check_order_by(self.Module, order_by)
        # 验证limit
        check_limit(limit)
        # order "id desc"
        tmp_order_by = order_by.split()
        # 比较奇怪的写法
        order_by_con = getattr(getattr(self.Module, tmp_order_by[0]), tmp_order_by[1])()
        # print "=========================="
        # print order_by_con
        data = db.session.query(self.Module).filter_by(**where).order_by(order_by_con).limit(limit).all()
        db.session.close()
        ret = process_result(data, output)
        return ret

    def update(self, **kwargs):
        data = kwargs.get("data", {})
        where = kwargs.get("where", {})
        check_update(self.Module, data, where)
        ret = db.session.query(self.Module).filter_by(**where).update(data)
        try:
            db.session.commit()
        except Exception as e:
            current_app.logger.warning("commit error: {}".format(e.message))
            raise Exception("commit error")
        return ret

    def delete(self, **kwargs):
        id = kwargs.get("id", None)
        if id is None:
            raise Exception("必须要有id")
        ret = db.session.query(self.Module).filter(self.Module.id == id).delete()
        try:
            db.session.commit()
            current_app.logger.debug("删除id为： {}的数据成功".format(id))
        except Exception as e:
            current_app.logger.warning("commit error: {}".format(e.message))
            raise Exception("commit error")
        return ret
