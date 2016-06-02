#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua@qq.com
# @Date:   2016-06-01 20:12:39
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-02 15:49:37
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
        "method": "idc.getIdc",
        "auth": "kch",
        "params": {"idcId": "2"}
    }
    # 发送测试用的错误数据
    header_err = {
        "content-type": "application/json_err"
    }
    format_Request_err = {
        "jsonRpcVersion": "1.0",
        "id": "2",
        "method": "idc.getIdc_err",
        "auth": "kch",
        "params": {"idcId": "2"}
    }

    print "======发送正常数据测试返回执行结果：======"
    r = requests.post(url, headers=header, data=json.dumps(format_Request))
    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)

    print "======发送错误json元素信息测试返回报错信息：======"
    r = requests.post(url, headers=header, data=json.dumps(format_Request_err))

    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)

    print "======测试错误头文件测试返回报错信息：======"
    r = requests.post(url, headers=header_err, data=json.dumps(format_Request_err))

    print "response的状态：{}".format(r.status_code)
    print "response的内容：{}".format(r.content)
if __name__ == '__main__':
    test_api()
