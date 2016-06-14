#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-13 11:01:26
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-14 19:35:15
from app.models import db, Manufacturers
from flask import current_app


from app.utils import check_field_exists, check_output_field, check_order_by, check_limit, process_result, check_update


def create(**kwargs):
    # 1. 获取参数
    # 2. 验证参数是否合法
    check_field_exists(Manufacturers, kwargs)
    manufacturers = Manufacturers(**kwargs)
    db.session.add(manufacturers)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning("插入错误: {} ".format(e.message))
        raise Exception("commit error")
    # 3. 插入到数据库
    # 4. 返回插入的状态
    return manufacturers.id


def get(**kwargs):
    # 整理条件
    output = kwargs.get("output", [])
    limit = kwargs.get("limit", 10)
    order_by = kwargs.get("order_by", "id desc")
    where = kwargs.get("where", {})

    # 验证
    # 验证output
    check_output_field(Manufacturers, output)
    # 验证order_by
    check_order_by(Manufacturers, order_by)
    # 验证limit
    check_limit(limit)
    # order "id desc"
    tmp_order_by = order_by.split()
    # 比较奇怪的写法
    order_by_con = getattr(getattr(Manufacturers, tmp_order_by[0]), tmp_order_by[1])()
    # print "=========================="
    # print order_by_con
    data = db.session.query(Manufacturers).filter_by(**where).order_by(order_by_con).limit(limit).all()
    db.session.close()
    ret = process_result(data, output)
    return ret


def update(**kwargs):
    data = kwargs.get("data", {})
    where = kwargs.get("where", {})
    check_update(Manufacturers, where, data)

    ret = db.session.query(Manufacturers).filter_by(**where).update(data)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning("commit error: {}".format(e.message))
        raise Exception("commit error")
    return ret


def delete(**kwargs):
    id = kwargs.get("id", None)
    if id is None:
        raise Exception("必须要有id")
    ret = db.session.query(Manufacturers).filter(Manufacturers.id == id).delete()
    try:
        db.session.commit()
        current_app.logger.debug("删除id为： {}的数据成功".format(id))
    except Exception as e:
        current_app.logger.warning("commit error: {}".format(e.message))
        raise Exception("commit error")
    return ret
