# -*- coding:utf-8 -*-

class JsonRPC(object):
    def __init__(self,jsondata):
        self.jsondata = jsondata

    def execute(self):
        # 验证id
        response = Response()
        if self.jsondata.get("id",None) is None:
                response.error_code = 101
                response.error_message = "id不存在"
            return response
        # 验证jsondata
        if self.validata():

            # 通过:
            auth = self.jsonData.get("auth", None)
            module, func = self.jsondata.get("method","").split(".")
            res=self.callMethod(module, fun, params, auth)
        response.error_code = 102
        response.error_message = "加载失败"
        return response 
            # 不通过:
    def callMethod(self, module, func, params, auth):
        res = Response()
        at = AutoLoad(module)
        if not at.isValidModule():
            res.error_code = 201
            res.error_message = "模块不可以"
            return res
        if not at.isValidMethod(fun):
            res.error_code = 202
            res.error_message = "没有这个方法"
            return res

        # flag = requireAuthentication()  判断module, func 是否需要登录

        # 需要登录：
            # 有没有token
            # 权限权限:
            #     成功:
            #     失败:
            #         return res

        try:
            called = at.getCallMethod()
            if callable(called):
                data = called(**params)
                self.processresult(data)
            else:
                response.error_code = 203
                response.error_message = "无法调用" 
        except Exception, e:
            res.error_code = 204
            res.error_message = "不能加载"
            return res
        return res




    def validata(self):
        jsonrpc = self.jsondata.get("jsonrpc",None)
        method = self.jsondata.get("method",None)
        params = self.jsondata.get("params",None)
        response = Response()
        if not jsonrpc:
            response.error_message = "没有传递版本"
            response.error_code = "102"
            return False
        if not method:
            response.error_message = "没有传递方法"
            response.error_code = "103"
            return False
        if not params:
            response.error_message = "版本没有传递参数"
            response.error_code = "104"
            return False
        # 验证通过: 
        return True
        # 验证不通过: 
            # return False


    def requireAuthentication():
        # idc.get  需要登录
            return True

        # 不需要登录
            return False



class AutoLoad(object):
    # 1.动态加载模块
    # 2.执行成果加载的模块
    def __init__(self,module_name):
        DIR = os.path.abspath(os.path.dirname(__file__))
        self.moduleDir = os.path.join(os.path.dirname(DIR),"module")
        self.module_name = module_name
        self.method = None
    def _load_module():
        ret = False
        for filename in os.listdir(self.moduleDir):
            if filename.endwith(".py"):
                module_name = filename.rstrip(".py")
                if self.module_name == module_name:
                    if self.module_name == module_name:
                    fp, pathname, desc = imp.find_module(
                        module_name, [self.moduleDir])
                        try:
                            self.module = imp.load_module(module_name,fp,params,desc)
                            ret = True
                        except:
                            esponse.error_message = "加载失败"
                            response.error_code = 301
                            return response
                        finally:
                            fp.close()
                        break
        if not ret:
            response.error_message = "没有找到模块"
            response.error_code = 302
        return ret


    def isValidModule(self):
        # 验证模块是否存在(ls modules/idc.py)
        # 有:import idc
        if _load_module():
            return True
        # 没有:
        return False

    def isValidMethod(self,func=None):
        # 验证模块下有没有制定方法
        # 有:
        self.method = func
        if hasattr(self.module,self.method):
            return True
        # 没有:
        return False

    def getCallMethod(self):
        if hasattr(self.module, self.method):
            return getattr(self.module, self.method)
        return None
        # 模块成功加载
        # 加载失败
        # return None
        # # 加载成功
        # return idc.get()



class Response(object):
    """docstring for Response"""
    def __init__(self, error_code,error_message):
        self.error_code = error_code
        self.error_message = error_message
        self.res = {
            "error_code":error_code,
            "error_message":error_message

        }
    # data = None  # 执行后果
    # error_code = 0  # 错误码
    # error_code = None  # 错误信息
