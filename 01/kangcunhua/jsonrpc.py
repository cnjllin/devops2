#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kangcunhua
# @Date:   2016-05-23 17:12:52
# @Last Modified by:   kangcunhua
# @Last Modified time: 2016-05-27 11:39:43

import json
import time


class JsonRPC(object):
    """[summary]

    [description]
    + 101  模块不存在
    + 102  模块加载失败
    + 103  指定模块下的函数不存在
    + 104  jsonrpc版本不对，应该是2.0
    + 105  id不正确，应该是1
    """

    def __init__(self, jsondata):
        self.jsondata = jsondata
        self.response_preform = Response_preform()
        self.module_name, self.funcname = self.jsondata.get("method", "").split(".")
        print "模块名：%s，函数名：%s" % (self.module_name, self.funcname)
        self.lazyImport = LazyImport(self.module_name)
        self.module = None
        self.err_dic = {
            101: "模块不存在",
            102: "模块加载失败",
            103: "指定模块下的函数不存在",
            104: "jsonrpc版本不对，应该是2.0",
            105: "id不正确，应该是1"
        }

    def execute(self):
        # 验证id # 验证jsondata
        if self.validata_all():
            print "验证通过：" + "等待调用方法！"
            result = getattr(self.module, self.funcname)(self.jsondata.get("params"))
            # result = self.lazyImport.(self.funcname)(self.jsondata.get("params")) # 这个直接调用不会写
            print result
            self.response = self.response_preform.processresult(result)
        else:
            self.response = self.response_preform.jsonError(self.jsondata["id"], 100, "jsonrpc调用失败，详见系统后台日志！")
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

    def validate_mandatory(self):
        """[summary]验证json的元素是否包括完整

        [description]Entropy同学的这段代码太精彩了，学习了
        """
        mandatory = ["jsonRpcVersion", "id", "auth", "method", "params"]
        validata_result = True
        for i in mandatory:
            if not self.jsondata.get(i, None):
                # self.response.error_message = "{0} is mandatory".format(i)
                self.response_preform.printlogs("{0} is mandatory".format(i))
                validata_result = False
        return validata_result

    def validata_id(self):
        if self.jsondata["id"] == "1":
            print "id:" + self.jsondata["id"]
            validata_result = True
        else:
            # self.response_preform.jsonError(self.jsondata["id"], 104, "ID不正确，应该为1")
            self.response_preform.printlogs("ID不正确，应该为1")
            validata_result = False
        return validata_result

    def validata_version(self):

        if self.jsondata["jsonRpcVersion"] == "2.0":
            print "jsonRpcVersion:" + self.jsondata["jsonRpcVersion"]
            # 通过：
            validata_result = True
        else:
            # self.response_preform.jsonError(self.jsondata["id"], errno, "jsonrpc版本不正确，应该为2.0")
            self.response_preform.printlogs("jsonrpc版本不正确，应该为2.0")
            validata_result = False

    def validata_HasModule(self):
        if self.module:
            # 已加载，不再重复加载，可以写日志：提示已经加载过了
            print self.module
            self.response_preform.printlogs("模块已导入过了。")
            validata_result = False
        else:
            try:
                self.module = self.lazyImport.setAndReturnModule()
                print self.module
                validata_result = True
            except Exception, e:
                # raise e
                self.response_preform.printlogs("导入模块报错：" + str(e))
                validata_result = False
        return validata_result

    def validata_hasFunction(self):
        # 这个条件判断意义不大(not self.module)
        if hasattr(self.module, self.funcname):
            validata_result = True
        else:
            self.response_preform.printlogs("模块" + self.module_name + "没有此函数" + self.funcname)
            validata_result = False
        return validata_result

    def validata_all(self):
        """[summary]验证json的元素是否正确

        [description]Entropy同学的这段代码太精彩了，学习了
        """
        validata_result = True
        for func in [self.validate_mandatory, self.validata_id, self.validata_HasModule, self.validata_hasFunction]:
            if not func():
                # self.response_preform.jsonError(self.jsondata["id"], errno, "jsonrpc调用失败，详见系统后台日志！")
                # print func()
                validata_result = False
        return validata_result

    def requiresAuthentication(self,):
        # idc.get  需要登陆 return True
        # user.login 不需要登陆 return False
        pass


class Response_preform(object):
    """docstring for Response_preform
        对于返回值的组装预处理
        目前对于出错的情况存在覆盖现象，暂未处理合并
        一种办法是，详细报错记录到日志，合并一抽象报错信息返回调用端；
    """

    def __init__(self):
        super(Response_preform, self).__init__()
        # self.arg = arg
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

    def printlogs(self, errmsg):
        """[模拟记录日志]

        [简化打印至命令行]

        Arguments:
            args {[string]} -- [详细报错信息]
        """
        print "[" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "]" + errmsg


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
    调用__getattr__前，需先调用setAndReturnModule初始化module
    """
    #“单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
    #“双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据;
    # 1.带有单下划线的特性不会被 from module import *导入;
    # 2.单下划线是Python程序员使用类时的约定，表明程序员不希望类的用户直接访问属性。仅仅是一种约定！实际上，实例._变量，可以被访问

    def __init__(self, module_name):
        self.modules_package = "modules"
        self.module_name = module_name
        self.module = None

    def __getattr__(self, funcname):
        return getattr(self.module, funcname)

    def getFullPackage(self):
        return self.modules_package + "." + self.module_name

    def setAndReturnModule(self):
        self.module = __import__(self.getFullPackage(), fromlist=[self.module_name])
        return self.module


class Response(object):
    """[summary]
    思路，参考，此处 暂不用
    [description]
    """

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

    def __init__(self, testflag):
        self.testflag = testflag

    def sendRequest(self):
        # 发送测试用的正确数据
        format_Request = {
            "jsonRpcVersion": "2.0",
            "id": "1",
            "method": "idc.getIdc",
            "auth": "kch",
            "params": {"idcId": "2"}
        }
        # 发送测试用的错误数据
        # 多种出错合并已实现
        format_Request_err = {
            "jsonRpcVersion": "1.0",
            "id": "2",
            "method": "idc.getIdc_err",
            "auth": "kch",
            "params": {"idcId": "2"}
        }

        if self.testflag:
            return format_Request
        else:
            return format_Request_err


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


# 测试动态导入类
# tt = Test_imoprt("modulename")
# tt.get()
# 测试懒加载类
# tt1 = LazyImport("idc")
# print tt1.setAndReturnModule()
# print tt1.getIdc()

if __name__ == '__main__':

    print "===============发送正常数据测试返回执行结果：==============="
    requestTmp = Request(True)
    jsonrpcTmp = JsonRPC(requestTmp.sendRequest())
    print "测试execute方法：" + jsonrpcTmp.execute()

    print "===============测试报错信息测试返回报错信息：==============="
    requestTmp = Request(False)
    jsonrpcTmp = JsonRPC(requestTmp.sendRequest())
    print "测试execute方法：" + jsonrpcTmp.execute()


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

# 原因：getattr返回的是一个function，此时不能 在调用getattr函数中返回 其他值；

# output

# [vagrant@OpsDev2 Lesson01]$ python jsonrpc.py
# ===============发送正常数据测试返回执行结果：===============
# 模块名：idc，函数名：getIdc
# id:1
# <module 'modules.idc' from '/PythonHome/wwwroot/Lesson01/modules/idc.pyc'>
# 验证通过：等待调用方法！
# 测试getIdc()方法
# 测试execute方法：{
#     "jsonrpc": "2.0",
#     "result": "测试getIdc()方法",
#     "id": 1
# }
# ===============测试报错信息测试返回报错信息：===============
# 模块名：idc，函数名：getIdc_err
# [2016-05-27 11:31:41]ID不正确，应该为1
# <module 'modules.idc' from '/PythonHome/wwwroot/Lesson01/modules/idc.pyc'>
# [2016-05-27 11:31:41]模块idc没有此函数getIdc_err
# 测试execute方法：{
#     "error_code": 100,
#     "jsonrpc": "2.0",
#     "id": "2",
#     "errmsg": "jsonrpc调用失败，详见系统后台日志！"
# }
