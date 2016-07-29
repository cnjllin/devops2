#!/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

url = "http://127.0.0.1:2000/api"


def rpc():
    headers = {'content-type': 'application/json'}
    '''
        #create请求
        data = {
                 'jsonrpc':'2.0',
                'method': 'user.create',      
                'id':'1',
                'params':{
                    'username':'dingzi',
                    'password':'123456',
                    'repwd':'123456',
                    'name':'dingzi',
                    'email':'787696331@qq.com',
                    'mobile':'121212121',
                    'r_id':'1,6',
                    'is_lock':0
                }
            }
        '''
    '''
        #get请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.get',      
                'id':'1',
                'params':{
                    'output':['id','username','name','email','mobile'],
                    'where':{'id':1}
                }
        }
        '''
    '''
        #getlist请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.getlist',      
                'id':'1',
                'params':{
                    'output':['id','username'],
                }
        }
        '''
    # getinfo请求
    data = {
        'jsonrpc': '2.0',
        'method': 'user.getinfo',
        'id': '1',
        'params': {
        }
    }
    '''
        #update请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.update',      
                'id':'1',
                'params':{
                    'data':{'name':'adminadmin'},
                    'where':{'id':'1'}
                }
        }
        '''
    '''
        #delete请求
        data = {
                'jsonrpc':'2.0',
                'method': 'user.delete',      
                'id':'1',
                'params':{
                    'where':{'username':'reboot'}
                }
        }
        '''
    '''
        #/git/password修改密码 
        data = {
            #'oldpassword':'123456',
            'user_id':1,
            'password':'123456'
        }
        r = requests.post("http://127.0.0.1:2000/api/password", headers=headers,json=data)
        '''
    r = requests.post(url, headers=headers, json=data)

    print r.status_code
    print r.text


rpc()
