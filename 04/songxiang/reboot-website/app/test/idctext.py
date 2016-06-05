#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "SONG Xiang"


from __future__ import print_function
import requests
import json

url = "http://0.0.0.0:5000/api"


def test_api():
    headers = {"Content-Type": "application/json"}
    data = {
        "id": 12,
        "jsonrpc": "2.0",
        "method": "idc.create",
        "auth": None,
        "params": {
            'name':"songxiang",
            "idc_name":"香港沙田",
            "address":"香港",
            "phone":"1778887788",
            "email":"sx@123.com",
            "user_interface":"sx",
            "user_phone":"18888888888",
            "rel_cabinet_num":50,
            "pact_cabinet_num":60,
           },

    }
    r = requests.get(url, headers=headers, data=json.dumps(data))
    print(r.status_code)
    print(r.content)


# con = json.loads(r.content)
if __name__ == "__main__":
    test_api()
