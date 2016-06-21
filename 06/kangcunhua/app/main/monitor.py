#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-19 10:39:05
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-19 18:23:32
from app.base.zabbix import Zabbix, get_zabbix_data, zabbix_link_template
from . import main
import json
from app.utils import Treeview

from app.utils import api_action
from flask import render_template, request

"""
    获取zabbix里 所有的hostgroup
"""


@main.route("/monitor/ajax/get_zabbix_host_groups", methods=['POST'])
def monitor_get_zabbix_host_groups():
    zb = Zabbix()
    data = zb.get_hostgroup()
    return json.dumps(data)


"""
    zabbix 模版绑定
"""


@main.route("/monitor/zabbix", methods=['GET'])
def monitor_zabbix():
    zb = Zabbix()
    templates = zb.zb.template.get(output=["templateid", "name"])
    templates_data = []

    for temp in templates:
        templates_data.append({"label": temp['name'], "value": temp['templateid']})

    tv = Treeview()
    treeview = tv.get()
    print treeview
    return render_template("monitor/monitor_zabbix.html",
                           treeview=json.dumps(treeview), templates=json.dumps(templates_data))

"""
    获取zabbix的主机，以及已link的模版
"""


@main.route("/monitor/ajax/get_zabbix_data_by_group", methods=["POST"])
def monitor_get_zabbix_data_by_group():
    if request.method == "POST":
        params = request.form.to_dict()
        # {'server_purpose': u'3', 'service_id': u '1'}
        # 取出响应的server id [{'id': 1L}]

        hosts = api_action("server.get", {"output": ["id"], "where": {"server_purpose": params[
                           "server_purpose"], "service_id": params["service_id"]}})
        ret = get_zabbix_data(hosts)
        # print ret
        return json.dumps(ret)
    return ""

"""
    zabbix 模版解除绑定
"""


@main.route("/monitor/ajax/unlink_zabbix_template", methods=["POST"])
def monitor_unlink_zabbix_template():
    if request.method == "POST":
        params = request.form.to_dict()
        # print params
        # {'hostid': u'10113', 'templateid': u'10115'}
        zb = Zabbix()
        ret = zb.unlink_template(params['hostid'], params['templateid'])
        if ret:
            return "1"
        else:
            return ret


"""
    zabbix 模版绑定
"""


@main.route("/monitor/ajax/link_zabbix_template", methods=["POST"])
def monitor_link_zabbix_template():
    if request.method == "POST":
        params = request.form.to_dict()
        # {'hostids': u'10113','template_ids': u'10066'}
        templateids = params['template_ids'].split(",")
        hostids = params['hostids'].split(",")
        ret_data = zabbix_link_template(hostids, templateids)
        # [{u'hostids':[u'10113']}]
        # [('Code: -32602, Message: Invalid params., Data: Cannot find host interface on "reboot-ms-wet-01" for item key "ifDescr".',)]
        flag = True
        for ret in ret_data:
            if not isinstance(ret, dict):
                flag = False
        if flag:
            return "1"
        else:
            return json.dumps(ret_data)
