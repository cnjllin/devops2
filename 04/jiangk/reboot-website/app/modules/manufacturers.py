#!/usr/bin/python
# coding:utf-8

from app.models import Manufacturers
from flask import current_app
from app.models import db
from app.utils import check_field_exists
from app.utils import check_output_field
from app.utils import check_order_by
from app.utils import check_limit
from app.utils import process_result
from app.utils import check_update_params

def create(**kwargs):
    # 1 获取参数
    # print kwargs

    # 2 检查参数
    check_field_exists(Manufacturers, kwargs)

    # 3 插入到数据库
    manufacturers = Manufacturers(**kwargs)
    db.session.add(manufacturers)
    try:
        db.session.commit()
    except Exception, e:
        # logging
        current_app.logger.warning(
            "commit error: {}".format(e.message)
        )
        raise Exception("commit error")

    # 4 返回插入的状态
    return manufacturers.id


def get(**kwargs):
    # output: [manufacturers_name, user_interface, user_phone]
    # where: {
    #     id: 1
    # }
    # limit: 10
    # order_by: id
    # 1 整理条件
    output = kwargs.get("output", [])
    limit = kwargs.get("limit", 10)
    order_by = kwargs.get("order_by", "id desc")
    where = kwargs.get("where", {})

    # 2 验证
    # 验证output
    check_output_field(Manufacturers, output)

    # 验证 order_by，字符串分割，字段是否在表中   第二个字段必须为asc desc
    order_by_list = check_order_by(Manufacturers, order_by)

    # 验证 limit 必须为数字
    check_limit(limit)

    # 验证 where 条件，先不验证
    pass

    # print callable(getattr(getattr(Manufacturers, "id"), "desc"))
    # 函数对象
    # getattr(getattr(Manufacturers, tmp_order_by[0]), tmp_order_by[1])
    # 调用函数
    # getattr(getattr(Manufacturers, tmp_order_by[0]), tmp_order_by[1])()

    data = db.session.query(Manufacturers).filter_by(**where)\
        .order_by(getattr(getattr(Manufacturers, order_by_list[0]), order_by_list[1])())\
        .limit(limit).all()
    db.session.close()

    # process result
    return process_result(data, output)


def update(**kwargs):
    data = kwargs.get("data", {})
    where = kwargs.get("where", {})

    # # 1 验证data
    # # 2 验证where
    # # 3 更新必须提供id，只按照id更新
    # # id 要为数字且大于0的整数
    check_update_params(Manufacturers, data, where)

    # update
    # ret = db.session.query(Manufacturers).filter_by(**where).update(**data)
    # 调用模块执行出现错误：update() got an unexpected keyword argument 'rel_cabinet_num'
    ret = db.session.query(Manufacturers).filter_by(**where).update(data)
    try:
        db.session.commit()
    except Exception, e:
        # logging
        current_app.logger.warning("commit error: {}".format(e.message))
        raise Exception("commit error")

    # print ret
    return ret

