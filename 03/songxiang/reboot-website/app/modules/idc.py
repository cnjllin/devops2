#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "SONG Xiang"
from flask import current_app
from app.models import Idc
from app import db


def create(**kwargs):
    # 1. 获取参数
    # 2. 验证参数是否合法
    for field in kwargs.keys():
        if not hasattr(Idc, field):
            current_app.logger.warning("参数错误, {} 不在idc表里".format(field))
            raise Exception("Params error: {} is not in this table".format(field))
        if not kwargs.get(field, None):
            current_app.logger.warning("参数错误, {} 不能为空".format(field))
            raise Exception("Params error: {} is empty".format(field))
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
    if not isinstance(output, list):
        current_app.logger.warning("output 必须是list")
        raise Exception("output 必须是list")
    for field in output:
        if not hasattr(Idc, field):
            current_app.logger.warning("{} 输出字段不存在".format(field))
            raise Exception("{} 输出字段不存在".format(field))
    # 验证order_by
    tmp_order_by = order_by.split()
    if len(tmp_order_by) != 2:
        current_app.logger.warning("order by 参数不正确")
        raise Exception("order by 参数不正确")

    order_by_list = ["desc", "asx"]
    if tmp_order_by[1].lower() not in order_by_list:
        current_app.logger.warning("排序参数不正确, 值可以为 {}".format(order_by_list))
        raise Exception("排序参数不正确, 值可以为 {}".format(order_by_list))
    if not hasattr(Idc, tmp_order_by[0].lower()):
        current_app.logger.warning("排序字段不在表中")
        raise Exception("排序字段不在表中")
    # 验证limit
    if not str(limit).isdigit():
        current_app.logger.warning("limit 值必须为数字")
        raise Exception("limit 值必须为数字")
    data = db.session.query(Idc).filter_by(**where).order_by \
        (getattr(getattr(Idc, tmp_order_by[0]), tmp_order_by[1])()).limit(limit).all()
    db.session.close()
    ret = []
    for obj in data:
        if output:
            tmp = {}
            for j in output:
                tmp[j] = getattr(obj, j)
            ret.append(tmp)
        else:
            tmp = obj.__dict__
            tmp.pop("_sa_instance_state")
            ret.append(tmp)

    return ret


def update(**kwargs):
    data = kwargs.get("data", {})
    where = kwargs.get("where", {})
    if not data:
        current_app.logger.warning("没有要更新数据")
        raise Exception("没有要更新数据")
    for field in data.keys():
        if not hasattr(Idc, field):
            current_app.logger.warning("需要更新的 {} 这个字段不存在".format(field))
            raise Exception("需要更新的 {} 这个字段不存在".format(field))
    if not where:
        current_app.logger.warning("需要提供where条件")
        raise Exception("需要提供where条件")
    if not where.get("id", None):
        current_app.logger.warning("需要提供ID作为更新条件")
        raise Exception("需要提供ID作为更新条件")
    if str(where.get("id")).isdigit():
        if int(where.get("id")) <= 0:
            current_app.logger.warning("id的值为大于0的整数")
            raise Exception("id的值为大于0的整数")
        else:
            where = {"id":where.get("id")}
    else:
        current_app.logger.warning("ID必须为数字")
        raise Exception("ID必须为数字")

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
    except Exception as e:
        current_app.logger.warning("commit error: {}".format(e.message))
        raise Exception("commit error")
    return ret
