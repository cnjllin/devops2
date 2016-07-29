#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-07-24 16:26:58
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-07-24 18:03:50

from flask import request
from . import app, jsonrpc
import json
import traceback
import utils

# 权限的CRUD

username = "wd"


@jsonrpc.method('power.create')
def create(**kwargs):
    try:
        data = request.get_json()['params']
        if not utils.check_name(data['name']):
            return json.dumps({'code': 1, 'errmsg': 'name must be string or num'})
        app.config['cursor'].execute_insert_sql('power', data)
        utils.write_log('api').info(username, "create power %s sucess" % data['name'])
        return json.dumps({'code': 0, 'result': 'create %s sucess' % data['name']})

    except Exception, e:
        utils.write_log('api').error('create power error:%s' % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': 'create power failed'})


@jsonrpc.method('power.delete')
def delete(**kwargs):
    try:
        data = request.get_json()['params']
        where = data.get('where', None)
        if not where:
            return json.dumps({'code': 1, 'errmsg': 'must need a condition'})
        result = app.config['cursor'].get_one_result('power', ['name'], where)

        if not result:
            return json.dumps({'code': 1, 'errmsg': 'data not exist'})
        app.config['cursor'].execute_delete_sql('power', where)
        utils.write_log('api').info(username, "delete power sucess")
        return json.dumps({'code': 0, 'result': "delete power sucess"})

    except Exception, e:
        utils.write_log('api').error('delete power error:%s' % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': 'delete power failed'})


@jsonrpc.method('power.getlist')
def getlist(**kwargs):
    try:
        output = ['id', 'name', 'name_cn', 'url', 'conment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        result = app.config['cursor'].get_results('power', fields)
        utils.write_log('api').info(username, "select permission list sucess")
        return json.dumps({'code': 0, 'result': result, 'count': len(result)})

    except Exception, e:
        utils.write_log('api').error('get list permission error:%s' % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': 'get power_list failed'})


@jsonrpc.method('power.get')
def getbyid(**kwargs):
    try:
        output = ['id', 'name', 'name_cn', 'url', 'comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        where = data.get('where', None)
        if not where:
            return json.dumps({'code': 1, 'errmsg': 'must need a condition'})
        result = app.config['cursor'].get_one_result('power', fields, where)

        if not result:
            return json.dumps({'code': 1, 'errmsg': 'data not exist'})

        utils.write_log('api').info(username, "select permission by id sucessed!")
        return json.dumps({'code': 0, 'result': result})

    except Exception, e:
        utils.write_log('api').error('select power by id error:%s' % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': 'get power failed'})


@jsonrpc.method('power.update')
def update(**kwargs):
    try:
        data = request.get_json()['params']
        where = data.get('where', None)
        data = data.get('data', None)
        if not where:
            return json.dumps({'code': 1, 'errmsg': 'must need a condition'})
        result = app.config['cursor'].execute_update_sql('power', data, where)

        if not result:
            return json.dumps({'code': 1, 'errmsg': 'data not exist'})
        utils.write_log('api').info(username, "update power sucessed!")
        return json.dumps({'code': 0, 'result': "update power sucessed!"})

    except Exception, e:
        utils.write_log('api').error('update error:%s' % traceback.format_exc())
        return json.dumps({'code': 1, 'errmsg': 'update power failed'})
