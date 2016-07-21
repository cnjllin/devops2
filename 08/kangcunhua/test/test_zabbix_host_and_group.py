#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-20 18:29:05
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-20 21:03:05
import requests
import json

url = "http://192.168.99.14/zabbix/api_jsonrpc.php"

"""get authentication token
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbix"
        },
        "id": 1
    }
"""


def test_creat_hostgroup_api():

    header = {
        "content-type": "application/json-rpc"
    }
    data = {
        "jsonrpc": "2.0",
        "method": "hostgroup.create",
        "params": {
            "name": "Reboot-network"
        },
        "auth": "48b645955401c0ec8c82b7f06c6cdf2f",
        "id": 1
    }

    #     POST http://company.com/zabbix/api_jsonrpc.php HTTP/1.1
    # Content-Type: application/json-rpc

    # {"jsonrpc":"2.0","method":"apiinfo.version","id":1,"auth":null,"params":{}}

    print "======发送正常数据测试zabbix返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(data))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)
    # {"jsonrpc":"2.0","result":{"groupids":["18"]},"id":1}
    # dic = json.dumps(json.loads(r.content)["result"]["groupids"][0])
    dic = json.loads(r.content)["result"]["groupids"][0]
    print "创建的hostgroup id为：{}".format(dic)


def test_creat_host_api(ip, host):

    header = {
        "content-type": "application/json-rpc"
    }
    data_commonhost = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": host,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": "22"
                }
            ],
            "templates": [
                {
                    "templateid": "10110"
                }
            ],
            "inventory": {
                "macaddress_a": "01234",
                "macaddress_b": "56768"
            }
        },
        "auth": "48b645955401c0ec8c82b7f06c6cdf2f",
        "id": 1
    }
    data = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": "juniper-device-01",
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": "10.20.31.100",
                    "dns": "",
                    "port": "161"
                }
            ],
            "groups": [
                {
                    "groupid": "22"
                }
            ],
            "templates": [
                {
                    "templateid": "10066"
                }
            ],
            "inventory": {
                "macaddress_a": "01234",
                "macaddress_b": "56768"
            }
        },
        "auth": "48b645955401c0ec8c82b7f06c6cdf2f",
        "id": 1
    }

    #     POST http://company.com/zabbix/api_jsonrpc.php HTTP/1.1
    # Content-Type: application/json-rpc

    # {"jsonrpc":"2.0","method":"apiinfo.version","id":1,"auth":null,"params":{}}

    print "======发送正常数据测试zabbix返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(data_commonhost))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)


def test_get_host_api():

    header = {
        "content-type": "application/json-rpc"
    }
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": "extend",
            "filter": {
                "host": [
                    "ttt"
                ]
            }
        },
        "auth": "48b645955401c0ec8c82b7f06c6cdf2f",
        "id": 1
    }
    print "======发送正常数据测试zabbix返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(data))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)
if __name__ == '__main__':
    # test_creat_hostgroup_api()

    # test_get_host_api()

    hosts = [
        {"ip": "10.20.31.100", "host": "juniper-device-01"},
        {"ip": "10.20.31.101", "host": "juniper-device-02"},
        {"ip": "10.20.31.102", "host": "juniper-device-03"},
        {"ip": "10.20.31.103", "host": "juniper-device-04"},
        {"ip": "10.20.31.104", "host": "juniper-device-05"}
    ]
    # print hosts[0]["ip"]
    for x in hosts:
        test_creat_host_api(x["ip"], x["host"])

    # test_creat_host_api()
