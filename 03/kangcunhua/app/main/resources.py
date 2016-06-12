#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-05-27 14:40:47
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-12 19:52:46
from __future__ import unicode_literals
from flask import render_template, request
from . import main
import app.utils


"""
    IDC 列表页面
"""


@main.route("/resources/idc/", methods=["GET"])
def resources_idc():
    ret = app.utils.api_action("idc.get", {"where": {"status": 1}})
    return render_template("resources/server_idc_list.html",
                           title="IDC信息",
                           show_resource=True,
                           show_idc_list=True,
                           idcs=ret)

"""
    修改IDC信息
"""


@main.route("/resources/idc/modify/<int:idc_id>", methods=["GET"])
def resources_idc_modify(idc_id):
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
    data = request.form.to_dict()
    id = data.pop("id")
    ret = app.utils.api_action("idc.update", {"data": data, "where": {"id": id}})
    if ret:
        return render_template("public/success.html", next_url="/resources/idc/")
    else:
        return render_template("public/error.html", next_url="/resources/idc/")


@main.route("/resources/idc/add/", methods=["GET"])
def resources_add_idc():
    return render_template("resources/server_add_idc.html",
                           title="添加IDC",
                           show_resource=True,
                           show_idc_list=True)


@main.route("/resources/idc/doadd/", methods=["POST"])
def resources_doadd_idc():
    params = request.form.to_dict()
    ret = app.utils.api_action("idc.create", params)
    if ret:
        return render_template("public/success.html", next_url="/resources/idc/", title="操作成功")
    else:
        return render_template("public/error.html", next_url="/resources/idc/", title="操作失败")


@main.route("/resources/idc/delete/", methods=["POST"])
def resources_idc_delete():
    id = request.form.get("id", 0)
    ret = app.utils.api_action("idc.update", {"where": {"id": id}, "data": {"status": 0}})
    return str(ret)


"""
    服务器列表页面
"""


@main.route("/resources/server/list/", methods=["GET"])
def resources_server_list():
    return render_template("resources/server_list.html",
                           title="服务器信息",
                           show_resource=True,
                           show_serverlist=True)

"""
    添加服务器
"""


@main.route("/resources/server/add/", methods=["GET"])
def resources_server_add():
    manufacturers = app.utils.api_action("manufacturers.get")

    return render_template("resources/server_add.html",
                           title="添加服务器",
                           manufacturers=manufacturers)


"""
    添加制造商
"""


@main.route("/resources/server/manufacturers/add/", methods=["GET"])
def resources_manufacturers_add():
    return render_template("resources/server_add_manufacturers.html",
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
