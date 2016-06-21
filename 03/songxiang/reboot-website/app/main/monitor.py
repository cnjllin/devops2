#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "SONG Xiang"
from . import main
from app.base.zabbix import Zabbix, rsync_zabbix_to_zbhost, rsync_server_to_zbhost, get_zabbix_data, zabbix_link_template
import json
from flask import render_template, request
from app.utils import Treeview, api_action
"""
    获取zabbix
"""
@main.route("/monitor/ajax/get_zabbix_host_groups", methods = ["POST"])
def monitor_get_zabbix_host_groups():
    zb = Zabbix()
    data = zb.get_hostgroup()
    # print data
    return json.dumps(data)

"""
    text
"""
@main.route("/test/", methods = ["GET"])
def test():
    rsync_zabbix_to_zbhost()
    rsync_server_to_zbhost()
    return "ok"


"""
    zabbix 模板绑定
"""
@main.route("/monitor/zabbix", methods = ["GET"])
def monitor_zabbix():
    zb = Zabbix()
    templates = zb.zb.template.get(output=["templateid", "name"])
    templates_data = []
    for temp in templates:
        templates_data.append({"label": temp["name"], "value": temp["templateid"]})

    tv = Treeview()
    treeview = tv.get()
    return render_template("monitor/monitor_zabbix.html", treeview = json.dumps(treeview), templates = json.dumps(templates_data))
"""
    获取zabbix的主机, 以及已绑定的模板
"""

@main.route("/monitor/ajax/get_zabbix_data_by_group", methods=["POST"])
def monitor_get_zabbix_data_by_group():
    if request.method == "POST":
        params = request.form.to_dict()
        hosts = api_action("server.get", {"output": ["id"], "where": {"server_purpose": params["server_purpose"],
                                                               "service_id": params["service_id"]}})
        ret = get_zabbix_data(hosts)
        return json.dumps(ret)
    return ""


"""
    zabbix模板接触绑定
"""
@main.route("/monitor/ajax/unlink_zabbix_template", methods=["POST"])
def monitor_unlink_zabbix_template():
    if request.method == "POST":
        params = request.form.to_dict()
        zb = Zabbix()
        ret = zb.unlink_template(params["hostid"], params["templateid"])
        if ret:
            return "1"
        else:
            return ret

"""
    zabbix绑定模板
"""
@main.route("/monitor/ajax/link_zabbix_template", methods=["POST"])
def monitor_link_zabbix_template():
    if request.method == "POST":
        params = request.form.to_dict()
        templateids = params["template_ids"].split(",")
        hostids = params["hostids"].split(",")
        ret_data = zabbix_link_template(hostids, templateids)
        flag = True
        for ret in ret_data:
            if not isinstance(ret, dict):
                flag = False
        if flag:
            return "1"
        else:
            return json.dumps(ret_data)














