#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.cunhua
# @Date:   2016-05-23 17:12:52
# @Last Modified by:   kang.cunhua@qq.com
# @Last Modified time: 2016-06-03 09:08:09

import json
import time
import inspect


class JsonRpc(object):
    """Summary
        接收post过来的json数据，进行验证后，执行指定调用，返回数据；
    Attributes:
        jsondata (Json): Json数据
        lazyImport (LazyImport): 延迟加载类
        module (Module): 模块
        params (dic): 接收传递过来的参数对
        response (json.dumps): 存储返回的json数据
        response_preform (Response_preform): 返回json数据格式化
    """

    def __init__(self, jsondata):
        """初始化JsonRpc类

        Args:
            jsondata (Json): Json数据
        """
        self.jsondata = jsondata
        self.response_preform = Response_preform()
        self.module_name, self.funcname = self.jsondata.get("method", "").split(".")
        print "模块名：%s，函数名：%s" % (self.module_name, self.funcname)
        self.lazyImport = LazyImport(self.module_name)
        self.module = None
        self.params = self.jsondata.get("params")

    def execute(self):
        """执行RPC调用总入口

        Returns:
            response (json.dumps): 存储返回的json数据
        """
        # 验证id # 验证jsondata
        if self.runAllValidata():
            print "验证通过：" + "等待调用方法！"
            result = getattr(self.module, self.funcname)(**self.params)
            # str1 = "{}.{}".format(self.module, self.funcname)
            # result = eval(str1)(**self.params)
            # result = self.lazyImport.(self.funcname)(self.jsondata.get("params")) #
            # 这个直接调用不会写
            print result
            self.response = self.response_preform.processresult(result)
        else:
            self.response = self.response_preform.jsonError(
                self.jsondata["id"], 100, "jsonrpc调用失败，详见系统后台日志！")
        return self.response

    def validata_withoutlogin(self):
        """
        不需要登陆也可直接访问的白名单列表
        """
        whitelist = ["idc.getIdc"]
        if "{}.{}".format(self.module_name, self.funcname) in whitelist:
            print "whitelist:" + "{}.{}".format(self.module_name, self.funcname)
            validata_result = True
        else:
            self.response_preform.printlogs("你需要登录后才能访问此方法！")
            validata_result = False
        return validata_result

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
        """Summary验证ID是否正确

        Returns:
            bool: 返回验证结果True or false
        """
        if self.jsondata["id"] == "1":
            print "id:" + self.jsondata["id"]
            validata_result = True
        else:
            # self.response_preform.jsonError(self.jsondata["id"], 104,
            # "ID不正确，应该为1")
            self.response_preform.printlogs("ID不正确，应该为1")
            validata_result = False
        return validata_result

    def validata_version(self):
        """Summary验证Json版本是否正确

        Returns:
            bool: 返回验证结果True or false
        """
        if self.jsondata["jsonRpcVersion"] == "2.0":
            print "jsonRpcVersion:" + self.jsondata["jsonRpcVersion"]
            # 通过：
            validata_result = True
        else:
            # self.response_preform.jsonError(self.jsondata["id"], errno,
            # "jsonrpc版本不正确，应该为2.0")
            self.response_preform.printlogs("jsonrpc版本不正确，应该为2.0")
            validata_result = False
        return validata_result

    def validata_HasModule(self):
        """Summary验证模块是否存在

        Returns:
            bool: 返回验证结果True or false
        """
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
        """Summary验证函数是否存在

        Returns:
            bool: 返回验证结果True or false
        """
        # 这个条件判断意义不大(not self.module)
        if hasattr(self.module, self.funcname):
            validata_result = True
        else:
            self.response_preform.printlogs("模块" + self.module_name + "没有此函数" + self.funcname)
            validata_result = False
        return validata_result

    def runAllValidata(self):
        """[summary]验证json的元素是否正确

        [description]手工维护validata list容易出错，改造成inspect
        [self.validate_mandatory, self.validata_id, self.validata_HasModule, self.validata_hasFunction]:
        Returns:
        bool: 返回验证结果True or false
        """
        validata_result = True
        for func in list(inspect.getmembers(self, predicate=inspect.ismethod)):
            if (func[0][:8] == 'validata') and (not func[1]()):
                # print "====" + str(func[1]())
                validata_result = False
        return validata_result


class Response_preform(object):
    """docstring for Response_preform
    对于返回值的组装预处理
    目前对于出错的情况存在覆盖现象，暂未处理合并
    一种办法是，详细报错记录到日志，合并一抽象报错信息返回调用端；

    Attributes:
        result (json): 格式化后的json数据
    """

    def __init__(self):
        """Summary 初始化返回数据预处理类
        """
        super(Response_preform, self).__init__()
        # self.arg = arg
        self.result = None

    def processresult(self, data):
        """Summary格式化成功调用后的返回结果

        Args:
            data (dic): RPC调用执行结果

        Returns:
            json: 格式化成功调用后的返回结果
        """
        format_sucess = {
            "jsonrpc": "2.0",
            "result": data,
            "id": 1
        }
        self.result = json.dumps(format_sucess, ensure_ascii=False, indent=4)
        return self.result

    def jsonError(self, id, errno, data=None):
        """Summary格式化调用失败后的返回结果

        Args:
            id (string): jsonRPC的id元素
            errno (String): jsonRPC的errno元素
            data (None, optional): 调用函数返回的dic

        Returns:
            json: 格式化调用失败后的返回结果
        """
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
            errmsg (string): Description
            args {[string]} -- [详细报错信息]
        """
        print time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())) + errmsg


class LazyImport(object):
    """[summary]延迟加载类

    [description]
    调用__getattr__前，需先调用setAndReturnModule初始化module

    Attributes:
        module (Module): 延迟加载的模块
        module_name (str): 模块名
        modules_package (str): 包名
    """
    #“单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
    #“双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据;
    # 1.带有单下划线的特性不会被 from module import *导入;
    # 2.单下划线是Python程序员使用类时的约定，表明程序员不希望类的用户直接访问属性。仅仅是一种约定！实际上，实例._变量，可以被访问

    def __init__(self, module_name):
        """Summary

        Args:
            module_name (str): 模块名
        """
        # 加入相对路径，来查找modules路径
        # sys.path.append('../../')
        self.modules_package = "modules"
        self.module_name = module_name
        self.module = None

    def __getattr__(self, funcname):
        """Summary

        Args:
            funcname (str): 函数名

        Returns:
            func: 函数
        """
        return getattr(self.module, funcname)

    def getFullPackage(self):
        """Summary

        Returns:
            str: 返回附加包名的模块名
        """
        return "{}.{}".format(self.modules_package, self.module_name)

    def setAndReturnModule(self):
        """Summary延迟加载类，并初始化加载后的模块

        Returns:
            TYPE: Description
        """
        self.module = __import__(self.getFullPackage(), fromlist=[self.module_name])
        return self.module


class Request(object):
    """Summary模拟发送请求的类

    Attributes:
        testflag (bool): 测试开关
    """

    def __init__(self, testflag):
        """Summary

        Args:
            testflag (bool): 测试开关
        """
        self.testflag = testflag

    def sendRequest(self):
        """Summary模拟发送测试数据

        Returns:
            json: 测试用的json数据
        """
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


if __name__ == '__main__':

    print "===============发送正常数据测试返回执行结果：==============="
    requestTmp = Request(True)
    jsonrpcTmp = JsonRpc(requestTmp.sendRequest())
    print "测试execute方法：" + jsonrpcTmp.execute()

    print "===============测试报错信息测试返回报错信息：==============="
    requestTmp = Request(False)
    jsonrpcTmp = JsonRpc(requestTmp.sendRequest())
    print "测试execute方法：" + jsonrpcTmp.execute()
