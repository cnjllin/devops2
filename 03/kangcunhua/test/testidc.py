#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-04 23:26:01
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-06 20:26:08
import requests
import json

url = "http://127.0.0.1:8000/api"


def test_api():

    header = {
        "content-type": "application/json"
    }
    format_Request = {
        "jsonRpcVersion": "2.0",
        "id": "1",
        "method": "idc.create",
        "auth": "kch",
        "params": {
            "name": "yz8",
            "idc_name": "北京亦庄机房",
            "address": "北京亦庄开发区",
            "phone": "010-88886666",
            "email": "mdr@51reboot.com",
            "user_interface": "mdr",
            "user_phone": "18888888888",
            "rel_cabinet_num": 50,
            "pact_cabinet_num": 60

        }
    }

    print "======发送正常数据测试返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(format_Request))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)


def test_idc_get():

    header = {
        "content-type": "application/json"
    }
    format_Request = {
        "jsonRpcVersion": "2.0",
        "method": "idc.get",
        "id": 0,
        "auth": None,
        "params": {
            "output": ["name"]
        }
    }

    print "======发送正常数据测试返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(format_Request))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)
    # print json.loads(r.content)


def test_idc_update():

    header = {
        "content-type": "application/json"
    }
    format_Request = {
        "jsonRpcVersion": "2.0",
        "method": "idc.update",
        "id": 0,
        "auth": None,
        "params": {
            "data": {"name": "kang1"},
            "where": {"id": 3}
        }
    }

    print "======发送正常数据测试返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(format_Request))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)


def test_idc_delete():

    header = {
        "content-type": "application/json"
    }
    format_Request = {
        "jsonRpcVersion": "2.0",
        "method": "idc.delete",
        "id": 0,
        "auth": None,
        "params": {
            "id": 4
        }
    }

    print "======发送正常数据测试返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(format_Request))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)
if __name__ == '__main__':
    test_api()
    test_idc_get()
    test_idc_update()
    test_idc_delete()
# output
# (python27env) [vagrant@reboot-devops-02 test]$ python testidc.py
# ======发送正常数据测试返回执行结果：======
# response的状态：200
# response的内容：{
#     "jsonrpc": "2.0",
#     "result": 5,
#     "id": 1
# }
# ======发送正常数据测试返回执行结果：======
# response的状态：200
# response的内容：{
#     "jsonrpc": "2.0",
#     "result": [
#         {
#             "name": "yz8"
#         },
#         {
#             "name": "yz6"
#         },
#         {
#             "name": "yz2"
#         },
#         {
#             "name": "yz"
#         }
#     ],
#     "id": 1
# }
# ======发送正常数据测试返回执行结果：======
# response的状态：200
# response的内容：{
#     "jsonrpc": "2.0",
#     "result": 1,
#     "id": 1
# }
# ======发送正常数据测试返回执行结果：======
# response的状态：200
# response的内容：{
#     "jsonrpc": "2.0",
#     "result": 1,
#     "id": 1
# }
# (python27env) [vagrant@reboot-devops-02 test]$
