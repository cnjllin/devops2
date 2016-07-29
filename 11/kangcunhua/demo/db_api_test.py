#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-24 12:08:39
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-24 12:15:46

import utils


def _insert_sql(table_name, data):
    fields, values = [], []
    for k, v in data.items():
        fields.append(k)
        values.append("'%s'" % v)
    sql = "INSERT INTO %s (%s) VALUES  (%s) " % (table_name, ",".join(fields), ','.join(values))
    utils.write_log('api').info("Insert sql: %s" % sql)
    print sql
    return sql


def execute_insert_sql(table_name, data):
    sql = _insert_sql(table_name, data)
    return "ok"

data = {"name": "wd", "age": "18", "job": "devops"}
execute_insert_sql("user", data)
