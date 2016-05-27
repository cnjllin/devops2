#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kangcunhua
# @Date:   2016-05-26 20:44:01
# @Last Modified by:   kangcunhua
# @Last Modified time: 2016-05-26 20:44:12


import json


class JsonRPC(object):
    """[summary]

    [description]
    """

    def __init__(self, jsondata):
        self.jsondata = jsondata

    def execute(self):
        # 验证id # 验证jsondata
        if self.validata_id() and self.validata_version():
            # res = callMethod(module, fun, params, auth)
            self.processresult("测试正常结果！")
            print "验证通过：" + "等待调用方法！"
        else:
            # print "验证不通过：" + self.response
            self.processresult("验证不通过！")

        return self.response

    def callMethod(self, module, fun, params, auth):
        res = Response()
        at = AutoLoad(module)
        at.isValidModule
        res.error_code = 10
        res.error_message = "模块不可用"
        return res
        at.isValidMethod()
        return res
        flag = requiresAuthentication()  # 判断module, func 是否需要登陆

        # 需要登陆：
        #     有没有token
        #     验证权限
        #         失败： return res
        try:
            called = at.getCallMethod()
            res.data = called(**params)
        except Exception, e:
            res.error_code = 30
            res.error_message = e.message
            return res

    def validata_id(self):
        if self.jsondata["id"] == "1":
            print "id:" + self.jsondata["id"]
            validata_result = True
        else:
            self.jsonError(self.jsondata["id"], 104, "ID不正确，应该为1")
            validata_result = False
        return validata_result

    def validata_version(self):

        if self.jsondata["jsonRpcVersion"] == "2.0":
            print "jsonRpcVersion:" + self.jsondata["jsonRpcVersion"]
            # 通过：
            validata_result = True

        else:
            self.jsonError(self.jsondata["id"], errno, "jsonrpc版本不正确，应该为2.0")
            validata_result = False

    def validata_HasModuleAndFunction(self):
        pass

    def requiresAuthentication(self,):
        # idc.get  需要登陆 return True
        # user.login 不需要登陆 return False
        pass


class Response_preform(object):
    """docstring for Response_preform"""

    def __init__(self, arg):
        super(Response_preform, self).__init__()
        self.arg = arg
        self.result = None

    def processresult(self, data):

        format_sucess = {
            "jsonrpc": "2.0",
            "result": data,
            "id": 1
        }
        self.result = json.dumps(format_sucess, ensure_ascii=False, indent=4)
        return self.result

    def jsonError(self, id, errno, data=None):
        format_error = {
            "jsonrpc": "2.0",
            "id": id,
            "error_code": errno,
            "errmsg": data
        }
        # self.response = format_error
        self.result = json.dumps(format_error, ensure_ascii=False, indent=4)
        return self.result


class AutoLoad(object):
    """[summary]
    思路，参考，此处 暂不用
    [description]
    """
    # 1 动态加载模块
    # 2 执行成功加载的模块
    # idc.get()

    def _load_module(self,):
        # 加载模块
        pass

    def isValidMethod(self,):
        # 验证模块下有没有指定方法
        # 有：return True
        # 没有： return False
        pass

    def isValidModule(self,):
        # 验证模块是否存在（ls modules / idc.py）
        # 有： import idc(这里会有导入失败)
        self.module
        return True
        # 没有：
        return False

    def getCallMethod(self,):
        # 模块成功加载
        # 加载失败 return none
        # 加载成功 return idc.get()
        pass


class LazyImport(object):
    """[summary]

    [description]
    """
    #“单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
    #“双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据;
    # 1.带有单下划线的特性不会被 from module import *导入;
    # 2.单下划线是Python程序员使用类时的约定，表明程序员不希望类的用户直接访问属性。仅仅是一种约定！实际上，实例._变量，可以被访问

    def __init__(self, module_name):
        self.modules_package = "modules"
        self.module_name = module_name
        self.module = None
        self.errMsg = None
        self.result = None

    def __getattr__(self, funcname):
        # if self.module is None:
        #     self.module = __import__(self.module_name)
        #     print(self.module)
        # return getattr(self.module, funcname)

        try:
            print "self.module：" + self.getFullPackage()
            print "self.module_name:" + self.module_name
            self.module = __import__(self.getFullPackage(), fromlist=[self.module_name])
            self.mr_result = True

            if hasattr(self.module, self.funcname):
                return getattr(self.module, funcname)
            else:
                pass
                # 写入日志？
        except Exception, e:
            # raise e
            self.mr_result = False

        if self.mr_result:
            print "test import sucess!"
            pass
        else:
            print "test import failed!"
            # self.errMsg = "test import failed!"
            # return self.errMsg
        # print "getattr(self.module, funcname):" + getattr(self.module, funcname)

    def getFullPackage(self):
        return self.modules_package + "." + self.module_name

    def getModule():
        self.module = __import__(self.getFullPackage(), fromlist=[self.module_name])
        rerurn self.module


class Response(object):

    def __init__(self):
        self.userName = None
        self.id = None
        self.result = None
        self.errorCode = None
        self.errorMessage = None

    def toResponse(self):
        if self.errorMessage:
            return {"jsonrpc": "2.0", "id": self.id, "error_code": self.error_msg, "error_msg": self.error_message}
        else:
            return {"jsonrpc": "2.0", "id": self.id, "result": self.result}


class Request(object):

    def __init__(self):
        pass

    def sendRequest(self):
        format_Request = {
            "jsonRpcVersion": "2.0",
            "id": "1",
            "module": "idc",
            "auth": "kch",
            "params": {"idcId": "2"}
        }

        return format_Request


class Test_imoprt(object):
    """docstring for Test_imoprt"""

    def __init__(self, arg):
        super(Test_imoprt, self).__init__()
        self.arg = arg

    def get(self):

        # mn = "modules.idc"
        mn = "modules.idc_err"
        try:
            module = __import__(mn)
            self.mr_result = True
        except Exception, e:
            # raise e
            self.mr_result = False

        # import tt.jsontest
        if self.mr_result:
            print "test import sucess!"
        else:
            print "test import failed!"
        return self.mr_result

requestTmp = Request()
# print "测试Request类：" + str(requestTmp.sendRequest())
jsonrpcTmp = JsonRPC(requestTmp.sendRequest())
print "测试execute方法" + jsonrpcTmp.execute()

# 测试动态导入类
# tt = Test_imoprt("modulename")
# tt.get()
# 测试懒加载类
tt1 = LazyImport("idc")
print tt1.getIdc()


# errlog

# Traceback (most recent call last):
#   File "jsonrpc.py", line 242, in <module>
#     tt1.get()
# TypeError: 'bool' object is not callable

# Traceback(most recent call last):
#     File "jsonrpc.py", line 247, in < module >
#         print tt1.getIdc()
# TypeError:
#     'str' object is not callable
