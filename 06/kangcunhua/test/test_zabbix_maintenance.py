#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-21 15:24:10
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-21 15:33:31
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


def test_zabbix_maintenance_api():
    """创建一个维护，指定group为22的机子，在时间
        2016/6/21 15:19:12 ~ 2026/6/21 15:19:12期间
        每周日18点起，有一个小时的维护窗口
    """
    header = {
        "content-type": "application/json-rpc"
    }
    data = {
        "jsonrpc": "2.0",
        "method": "maintenance.create",
        "params": {
            "name": "Sunday maintenance",
            "active_since": 1466493552,
            "active_till": 1782026352,
            "groupids": [
                "2"
            ],
            "timeperiods": [
                {
                    "timeperiod_type": 3,
                    "every": 1,
                    "dayofweek": 64,
                    "start_time": 64800,
                    "period": 3600
                }
            ]
        },
        "auth": "48b645955401c0ec8c82b7f06c6cdf2f",
        "id": 1
    }

    print "======发送正常数据测试zabbix返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(data))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)
    # {"jsonrpc":"2.0","result":{"groupids":["18"]},"id":1}
    # dic = json.dumps(json.loads(r.content)["result"]["groupids"][0])
    dic = json.loads(r.content)["result"]["maintenanceids"][0]
    print "创建的maintenance id为：{}".format(dic)


if __name__ == '__main__':
    test_zabbix_maintenance_api()
