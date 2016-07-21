#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-05-27 14:40:47
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-20 18:13:34
from __future__ import unicode_literals
from flask import render_template, request, current_app
from app.models import db, Zbhost, Server
from . import main
import app.utils
import json
from app.base.zabbix import Zabbix, rsync_zabbix_to_zbhost, rsync_server_to_zbhost
"""cmdb所有请求的路由定义
"""


@main.route("/resources/idc/", methods=["GET"])
def resources_idc():
    """IDC 列表页面

    Args:
        idc_id (TYPE): Description

    Returns:
        TYPE: Description
    """
    ret = app.utils.api_action("idc.get", {"where": {"status": 1}})
    return render_template("resources/server_idc_list.html",
                           title="IDC信息",
                           show_resource=True,
                           show_idc_list=True,
                           idcs=ret)


@main.route("/resources/idc/modify/<int:idc_id>", methods=["GET"])
def resources_idc_modify(idc_id):
    """修改IDC信息

    Args:
        idc_id (TYPE): Description

    Returns:
        TYPE: Description
    """
    ret = app.utils.api_action("idc.get", {"where": {"id": idc_id}})
    if ret:
        return render_template("resources/server_idc_modify.html",
                               title="修改IDC信息",
                               show_resource=True,
                               show_idc_list=True,
                               idc=ret[0])
    return render_template("404.html"), 404


@main.route("/resources/idc/update", methods=["POST"])
def resources_idc_update():
    """更新IDC信息

    Args:
        idc_id (TYPE): Description

    Returns:
        TYPE: Description
    """
    data = request.form.to_dict()
    id = data.pop("id")
    ret = app.utils.api_action("idc.update", {"data": data, "where": {"id": id}})
    if ret:
        return render_template("public/success.html", next_url="/resources/idc/")
    else:
        return render_template("public/error.html", next_url="/resources/idc/")


@main.route("/resources/idc/add/", methods=["GET"])
def resources_add_idc():
    """添加IDC信息

    Args:
        idc_id (TYPE): Description

    Returns:
        TYPE: Description
    """
    return render_template("resources/server_idc_add.html",
                           title="添加IDC",
                           show_resource=True,
                           show_idc_list=True)


@main.route("/resources/idc/doadd/", methods=["POST"])
def resources_doadd_idc():
    """执行添加IDC信息

    Args:
        idc_id (TYPE): Description

    Returns:
        TYPE: Description
    """
    params = request.form.to_dict()
    ret = app.utils.api_action("idc.create", params)
    if ret:
        return render_template("public/success.html", next_url="/resources/idc/", title="操作成功")
    else:
        return render_template("public/error.html", next_url="/resources/idc/", title="操作失败")


@main.route("/resources/idc/delete/", methods=["POST"])
def resources_idc_delete():
    """删除IDC信息：更新idc的状态为0"""
    id = request.form.get("id", 0)
    ret = app.utils.api_action("idc.update", {"where": {"id": id}, "data": {"status": 0}})
    return str(ret)


@main.route("/resources/server/list/", methods=["GET"])
def resources_server_list():
    """<FRESHLY_INSERTED>"""
    # ret = app.utils.api_action("server.get", {"where": {"status": 1}})
    ret = app.utils.api_action("server.get")
    return render_template("resources/server_list.html",
                           title="服务器信息",
                           show_resource=True,
                           show_serverlist=True,
                           servers=ret)

"""
    添加服务器
"""


@main.route("/resources/server/add/", methods=["GET"])
def resources_server_add():
    # 取制造商信息
    manufacturers = app.utils.api_action("manufacturers.get")
    # 取业务线信息
    products = app.utils.api_action("product.get", {"where": {"pid": 0}})
    # 获取服务器状态
    status = app.utils.api_action("status.get")
    # 获取IDC状态
    idc_info = app.utils.api_action("idc.get", {"output": ["idc_name", "id"]})
    # 获取raids
    raids = app.utils.api_action("raid.get")
    # 获取raid类型
    raidtypes = app.utils.api_action("raidtype.get")
    # 获取电源功率
    powers = app.utils.api_action("power.get")
    # 远程管理卡型号
    managementcardtypes = app.utils.api_action('managementcardtype.get')
    # 获取供应商
    suppliers = app.utils.api_action("supplier.get")
    # 获取机柜号
    cabinets = app.utils.api_action("cabinet.get")
    return render_template("resources/server_add.html",
                           title="添加服务器",
                           manufacturers=manufacturers,
                           products=products,
                           status=status,
                           idc_info=idc_info,
                           raids=raids,
                           raidtypes=raidtypes,
                           powers=powers,
                           managementcardtypes=managementcardtypes,
                           suppliers=suppliers,
                           cabinets=cabinets,
                           show_resource=True,
                           show_serverlist=True)


"""
    添加制造商
"""


@main.route("/resources/server/manufacturers/add/", methods=["GET"])
def resources_manufacturers_add():
    return render_template("resources/server_manufacturers_add.html",
                           title="添加制造商")


"""
    执行添加制造商
"""


@main.route("/resources/server/manufacturers/doadd/", methods=["POST"])
def resources_manufacturers_doadd():
    params = request.form.to_dict()
    ret = app.utils.api_action("manufacturers.create", params)
    if ret:
        return render_template("public/success.html", next_url="/resources/server/manufacturers/add/")
    else:
        return render_template("public/error.html", next_url="/resources/server/manufacturers/add/")
"""
    添加制造商操作
"""


@main.route("/resources/server/manufacturers/doadd/", methods=["POST"])
def resources_doadd_manufacturers():
    params = request.form.to_dict()
    ret = app.utils.api_action("manufacturers.create", params)
    jump_url = "/resources/server/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)

"""
    添加服务器类型
"""


@main.route("/resources/server/servertype/add/", methods=["GET"])
def resources_server_type_add():
    manufacturers = app.utils.api_action("manufacturers.get")
    return render_template("resources/server_servertype_add.html",
                           title="添加服务器类型",
                           manufacturers=manufacturers)

"""
    执行添加服务器类型操作
"""


@main.route("/resources/server/servertype/doadd/", methods=["POST"])
def resources_doadd_servertype():
    params = request.form.to_dict()
    ret = app.utils.api_action("servertype.create", params)
    jump_url = "/resources/server/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)

"""
    ajax操作
    获取服务器型号
"""


@main.route("/resources/ajax/get/server/type/", methods=["GET"])
def resources_ajax_get_server_type():
    params = request.args.to_dict()
    if params:
        servertype = app.utils.api_action("servertype.get", {"where": params})
        return json.dumps(servertype)
    return ''


"""
    添加业务线或产品线
"""


@main.route("/resources/server/product/add/", methods=["GET"])
def resources_server_product_add():
    products = app.utils.api_action("product.get", {"where": {"pid": 0}})
    return render_template("resources/server_product_add.html",
                           products=products)

"""
    执行添加业务或产品线
"""


@main.route("/resources/server/product/doadd/", methods=["POST"])
def resources_server_doadd_product():
    params = request.form.to_dict()
    ret = app.utils.api_action("product.create", params)
    jump_url = "/resources/server/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)

"""
    ajax操作
    根据一级业务线,获取他的二级业务线
"""


@main.route("/resources/ajax/get/server/product/", methods=["GET"])
def resources_ajax_get_server_product():
    params = request.args.to_dict()
    print params
    if params:
        ret = app.utils.api_action("product.get", {"where": params, "output": ["id", "service_name", "pid"]})
        return json.dumps(ret)
    return ''

"""
    添加服务器状态
"""


@main.route("/resources/status/add/", methods=["GET"])
def resources_status_add():
    return render_template("resources/server_status_add.html")

"""
    执行添加服务器状态
"""


@main.route("/resources/status/doadd/", methods=["POST"])
def resources_doadd_status():
    params = request.form.to_dict()
    ret = app.utils.api_action("status.create", params)
    jump_url = "/resources/server/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)
"""
    添加raid状态
"""


@main.route("/resources/server/raid/add/", methods=["GET"])
def resources_server_raid_add():
    return render_template("resources/server_raid_add.html")

"""
    执行添加raid状态
"""


@main.route("/resources/server/raid/doadd/", methods=["POST"])
def resources_doadd_server_raid():
    params = request.form.to_dict()
    ret = app.utils.api_action("raid.create", params)
    jump_url = "/resources/server/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)

"""
    添加机柜号
"""


@main.route("/resources/cabinet/add/", methods=["GET"])
def resources_server_raid_type_add():
    idcs = app.utils.api_action("idc.get", {"output": ["idc_name", "id"]})
    powers = app.utils.api_action("power.get")
    return render_template("resources/server_cabinet_add.html",
                           idcs=idcs,
                           powers=powers)

"""
    执行添加机柜号
"""


@main.route("/resources/cabinet/doadd/", methods=["POST"])
def resources_doadd_cabinet_type():
    params = request.form.to_dict()
    ret = app.utils.api_action("cabinet.create", params)
    jump_url = "/resources/server/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)


"""
    添加功率
"""


@main.route("/resources/power/add/", methods=["GET"])
def resources_power_add():
    return render_template("resources/server_power_add.html")

"""
    执行添加功率
"""


@main.route("/resources/power/doadd/", methods=["POST"])
def resources_doadd_power():
    params = request.form.to_dict()
    ret = app.utils.api_action("power.create", params)
    jump_url = "/resources/power/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)


"""
    ajax操作
    获取机柜号
"""


@main.route("/resources/ajax/get/cabinet/", methods=["GET"])
def resources_ajax_get_cabinet():
    params = request.args.to_dict()
    print params
    if params:
        ret = app.utils.api_action("cabinet.get", {"where": params, "output": ["name", "id"]})
        return json.dumps(ret)
    return ''


"""
    添加raid类型
"""


@main.route("/resources/server/raidcardtype/add/", methods=["GET"])
def resources_server_raid_cardtype_add():
    return render_template("resources/server_raidcardtype_add.html",)

"""
    执行添加机柜号
"""


@main.route("/resources/server/raidcardtype/doadd/", methods=["POST"])
def resources_doadd_raidtype_type():
    params = request.form.to_dict()
    ret = app.utils.api_action("raidtype.create", params)
    jump_url = "/resources/server/raidcardtype/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)


"""
    添加远程管理卡
"""


@main.route("/resources/server/managementcardtype/add/", methods=["GET"])
def resources_server_managementcardtype_add():
    return render_template("resources/server_managementcardtype_add.html",)

"""
    执行添加远程管理卡
"""


@main.route("/resources/server/managementcardtype/doadd/", methods=["POST"])
def resources_doadd_raidtydpe_type():
    params = request.form.to_dict()
    ret = app.utils.api_action("managementcardtype.create", params)
    jump_url = "/resources/server/managementcardtype/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)


"""
    添加供应商
"""


@main.route("/resources/server/supplier/add/", methods=["GET"])
def resources_server_supplier_add():
    return render_template("resources/server_supplier_add.html",)

"""
    执行添加供应商
"""


@main.route("/resources/server/supplier/doadd/", methods=["POST"])
def resources_doadd_supplier():
    params = request.form.to_dict()
    ret = app.utils.api_action("supplier.create", params)
    jump_url = "/resources/server/supplier/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)

"""
    执行添加服务器
"""


@main.route("/resources/server/doadd/", methods=["POST"])
def resources_doadd_server():
    params = request.form.to_dict()
    ret = app.utils.api_action("server.create", params)
    jump_url = "/resources/server/add/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)


"""
    修改服务器
"""


@main.route("/resources/server/modify/<int:id>", methods=["GET"])
def resources_server_modify(id):
    # 获取此服务器信息
    server = app.utils.api_action("server.get", {"where": {"id": id}})[0]
    print server
    # 取制造商信息
    manufacturers = app.utils.api_action("manufacturers.get")
    # 取业务线信息
    products = app.utils.api_action("product.get", {})
    # 获取服务器状态
    statuses = app.utils.api_action("status.get")
    # 获取IDC状态
    idcs = app.utils.api_action("idc.get", {"output": ["idc_name", "id"]})
    # 获取raids
    raids = app.utils.api_action("raid.get")
    # 获取raid类型
    raidtypes = app.utils.api_action("raidtype.get")
    # 获取电源功率
    powers = app.utils.api_action("power.get")
    # 远程管理卡型号
    managementcardtypes = app.utils.api_action('managementcardtype.get')
    # 获取供应商
    suppliers = app.utils.api_action("supplier.get")
    # 获取机柜号
    cabinets = app.utils.api_action("cabinet.get")
    return render_template("resources/server_edit.html",
                           title="修改服务器",
                           server=server,
                           manufacturers=manufacturers,
                           products=products,
                           statuses=statuses,
                           idcs=idcs,
                           raids=raids,
                           raidtypes=raidtypes,
                           powers=powers,
                           managementcardtypes=managementcardtypes,
                           suppliers=suppliers,
                           cabinets=cabinets,
                           show_resource=True,
                           show_serverlist=True)

"""
    执行修改服务器
"""


@main.route("/resources/server/update/", methods=["POST"])
def resources_doadd_modify_server():
    params = request.form.to_dict()
    current_app.logger.debug("提交的数据为： {}".format(params))

    server_id = request.form.get('id')
    resource = {"data": params, "where": {"id": server_id}}
    ret = app.utils.api_action("server.update", resource)
    jump_url = "/resources/server/list/"
    return app.utils.jump(ret, success_url=jump_url, error_url=jump_url)


@main.route("/resources/server/reporting/", methods=['POST'])
def resurce_server_reporting():
    """
    服务器信息自动上报
    """
    params = request.form.to_dict()
    where = {}
    if params.get("st", None)and len(params['st']) > 3:

        where['st'] = params.pop('st')
    else:
        where['uuid'] = params.pop('uuid')
    host = app.utils.api_action("server.get", {"where": where})
    if host:
        # update
        app.utils.api_action("server.update", {"data": params, 'where': {'id': host[0]['id']}})
    else:
        # create
        params.update(where)
        app.utils.api_action("server.create", params)
    return ""

"""
    ajax获取不在zabbix中的主机
"""


@main.route("/resource/monitor/ajax/get_sync_zabbix_hosts", methods=['POST'])
def get_sync_zabbix_hosts():
    # 1 取出在zabbix里的所有主机
    zabbix_hosts = db.session.query(Zbhost).all()
    # 2 组合条件，ip
    host_ips = [zb.ip for zb in zabbix_hosts]
    # 3 取出不在zabbix里的所有主机（条件：ip（在zabbix里的所有主机））
    servers = db.session.query(Server).filter(~Server.inner_ip.in_(host_ips)).all()
    print servers
    return json.dumps([{"hostname": s.hostname, "id": s.id} for s in servers])


"""
    ajax 操作， 同步主机到zabbix
"""


@main.route("/resource/monitor/ajax/sync_host_to_zabbix", methods=['POST'])
def resurce_sync_host_to_zabbix():
    """<FRESHLY_INSERTED>"""
    if request.method == "POST":
        params = request.form.to_dict()
    # {'hostid': u'1,2', 'groupid': u'2'}
        hostids = params['hostids'].split(',')
        servers = db.session.query(Server).filter(Server.id.in_(hostids)).all()
        data = {}

        zb = Zabbix()
        flag = True

        for server in servers:
            ret = zb.create_zb_host(server.hostname, server.inner_ip, params['groupid'])

            # {u'hostids': [u'10108']}
            if isinstance(ret, dict) and ret.get("hostids", None):

                data[server.hostname] = True
            else:
                flag = False
                data[server.hostname] = ret
        # 同步到缓存表
        rsync_zabbix_to_zbhost()
        rsync_server_to_zbhost()
        if flag:
            return "1"
        else:
            return json.dumps(data)
    return "500"
"""
    test /test_zabbix
"""


@main.route("/test_zabbix", methods=["GET"])
def test_zabbix():
    rsync_zabbix_to_zbhost()
    rsync_server_to_zbhost()
    return "1"
