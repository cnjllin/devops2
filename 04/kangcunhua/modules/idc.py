#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kangcunhua
# @Date:   2016-05-25 10:38:51
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-14 09:59:23
from app.models import db, Idc
from flask import current_app
from app.utils import check_field_exists, check_output_field, check_order_by, check_limit, process_result, check_update


def getIdc(**args):
    return "测试getIdc()方法:返回传过来的参数" + str(args)


def create(**kwargs):
    # 1. 获取参数
    # 2. 验证参数是否合法
    check_field_exists(Idc, kwargs)
    idc = Idc(**kwargs)
    db.session.add(idc)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning("插入错误: {} ".format(e.message))
        raise Exception("commit error")
    # 3. 插入到数据库
    # 4. 返回插入的状态
    return idc.id


def get(**kwargs):
    # 整理条件
    output = kwargs.get("output", [])
    limit = kwargs.get("limit", 10)
    order_by = kwargs.get("order_by", "id desc")
    where = kwargs.get("where", {})

    # 验证
    # 验证output
    check_output_field(Idc, output)
    # 验证order_by
    check_order_by(Idc, order_by)
    # 验证limit
    check_limit(limit)
    # order "id desc"
    tmp_order_by = order_by.split()
    # 比较奇怪的写法
    order_by_con = getattr(getattr(Idc, tmp_order_by[0]), tmp_order_by[1])()
    # print "=========================="
    # print order_by_con
    data = db.session.query(Idc).filter_by(**where).order_by(order_by_con).limit(limit).all()
    db.session.close()
    ret = process_result(data, output)
    return ret


def update(**kwargs):
    data = kwargs.get("data", {})
    where = kwargs.get("where", {})
    check_update(Idc, data, where)
    ret = db.session.query(Idc).filter_by(**where).update(data)
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
    ret = db.session.query(Idc).filter(Idc.id == id).delete()
    try:
        db.session.commit()
        current_app.logger.debug("删除id为： {}的数据成功".format(id))
    except Exception as e:
        current_app.logger.warning("commit error: {}".format(e.message))
        raise Exception("commit error")
    return ret
