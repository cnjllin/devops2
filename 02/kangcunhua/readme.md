#目录
[TOC]
#作业
##描述
+ 引入Flask，从web端发起RPC调用
+ 使用Flask的log插件记录操作日志；

##测试：
```shell
(python27env) [vagrant@OpsDev2 vagrant]$ cd test
(python27env) [vagrant@OpsDev2 test]$ python testAPI.py 

```
##输出
###webserver端输出

```shell
(python27env) [vagrant@OpsDev2 vagrant]$ python manage.py runserver -h 0.0.0.0 -p 8000
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 246-881-882
--------------------------------------------------------------------------------
DEBUG in views [/vagrant/app/main/views.py:28]:
请求json数据为： {"jsonRpcVersion": "2.0", "params": {"idcId": "2"}, "method": "idc.getIdc", "auth": "kch", "id": "1"}
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:37]:
======初始化：JsonRpc类======！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:210]:
初始化：Response_preform类！
--------------------------------------------------------------------------------
模块名：idc，函数名：getIdc
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:289]:
初始化：LazyImport类！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:185]:
验证函数入口execute;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:143]:
验证模块idc是否存在;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:153]:
当前延迟加载的类为：<module 'modules.idc' from '/vagrant/modules/idc.pyc'>！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:168]:
验证模块idc是否有此函数getIdc;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:171]:
当前模块idc查找函数getIdc成功;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:106]:
验证Json的id要素;
--------------------------------------------------------------------------------
id:1
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:109]:
验证Json的id要素成功;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:123]:
验证Json的jsonRpcVersion要素;
--------------------------------------------------------------------------------
jsonRpcVersion:2.0
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:127]:
验证Json的jsonRpcVersion要素成功;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:73]:
验证是否需要登录;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:77]:
该调用在白名单内，无需登录！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:192]:
验证通过execute;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:54]:
json数据通过验证，等待调用方法并返回结果！
--------------------------------------------------------------------------------
验证通过：等待调用方法！
测试getIdc()方法:返回传过来的参数{u'idcId': u'2'}
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:229]:
组装调用成功返回的json信息;
--------------------------------------------------------------------------------
127.0.0.1 - - [02/Jun/2016 21:37:10] "POST /api HTTP/1.1" 200 -
--------------------------------------------------------------------------------
DEBUG in views [/vagrant/app/main/views.py:28]:
请求json数据为： {"jsonRpcVersion": "1.0", "params": {"idcId": "2"}, "method": "idc.getIdc_err", "auth": "kch", "id": "2"}
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:37]:
======初始化：JsonRpc类======！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:210]:
初始化：Response_preform类！
--------------------------------------------------------------------------------
模块名：idc，函数名：getIdc_err
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:289]:
初始化：LazyImport类！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:185]:
验证函数入口execute;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:143]:
验证模块idc是否存在;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:153]:
当前延迟加载的类为：<module 'modules.idc' from '/vagrant/modules/idc.pyc'>！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:168]:
验证模块idc是否有此函数getIdc_err;
--------------------------------------------------------------------------------
2016-06-02 21:37:10 模块idc没有此函数getIdc_err
--------------------------------------------------------------------------------
ERROR in __init__ [/vagrant/app/base/__init__.py:175]:
当前模块idc查找函数getIdc_err失败;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:189]:
执行函数validata_hasFunction验证失败;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:106]:
验证Json的id要素;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
ERROR in __init__ [/vagrant/app/base/__init__.py:112]:
验证Json的id要素失败;
--------------------------------------------------------------------------------
2016-06-02 21:37:10 ID不正确，应该为1
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:189]:
执行函数validata_id验证失败;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:123]:
验证Json的jsonRpcVersion要素;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
ERROR in __init__ [/vagrant/app/base/__init__.py:132]:
验证Json的jsonRpcVersion要素失败;
--------------------------------------------------------------------------------
2016-06-02 21:37:10 jsonrpc版本不正确，应该为2.0
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:189]:
执行函数validata_version验证失败;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:73]:
验证是否需要登录;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
ERROR in __init__ [/vagrant/app/base/__init__.py:80]:
你需要登录后才能访问此方法！
--------------------------------------------------------------------------------
2016-06-02 21:37:10 你需要登录后才能访问此方法！
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:189]:
执行函数validata_withoutlogin验证失败;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
ERROR in __init__ [/vagrant/app/base/__init__.py:64]:
jsonrpc调用失败，详见系统后台日志！
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
DEBUG in __init__ [/vagrant/app/base/__init__.py:251]:
通过函数组装调用失败返回的json信息;
--------------------------------------------------------------------------------
127.0.0.1 - - [02/Jun/2016 21:37:10] "POST /api HTTP/1.1" 200 -
--------------------------------------------------------------------------------
DEBUG in views [/vagrant/app/main/views.py:34]:
用户请求的content-type为： application/json_err, 不予处理
--------------------------------------------------------------------------------
127.0.0.1 - - [02/Jun/2016 21:37:10] "POST /api HTTP/1.1" 400 -

```
###执行测试文件输出
```shell
(python27env) [vagrant@OpsDev2 ~]$ cd /vagrant 
(python27env) [vagrant@OpsDev2 vagrant]$ cd test
(python27env) [vagrant@OpsDev2 test]$ ls
testAPI.py
(python27env) [vagrant@OpsDev2 test]$ python testAPI.py 
======发送正常数据测试返回执行结果：======
response的状态：200
response的内容："{\n    \"jsonrpc\": \"2.0\", \n    \"result\": \"测试getIdc()方法:返回传过来的参数{u'idcId': u'2'}\", \n    \"id\": 1\n}"
======发送错误json元素信息测试返回报错信息：======
response的状态：200
response的内容："{\n    \"error_code\": 100, \n    \"jsonrpc\": \"2.0\", \n    \"id\": \"2\", \n    \"errmsg\": \"jsonrpc调用失败，详见系统后台日志！\"\n}"
======测试错误头文件测试返回报错信息：======
response的状态：400
response的内容：200
(python27env) [vagrant@OpsDev2 test]$ 

```
###flask.log的输出
```shell
(python27env) [vagrant@OpsDev2 vagrant]$ tail -f flask.log 
2016-06-02 21:37:10,733 - app - views.py- DEBUG - 请求json数据为： {"jsonRpcVersion": "2.0", "params": {"idcId": "2"}, "method": "idc.getIdc", "auth": "kch", "id": "1"}
2016-06-02 21:37:10,733 - app - __init__.py- DEBUG - ======初始化：JsonRpc类======！
2016-06-02 21:37:10,733 - app - __init__.py- DEBUG - 初始化：Response_preform类！
2016-06-02 21:37:10,734 - app - __init__.py- DEBUG - 初始化：LazyImport类！
2016-06-02 21:37:10,820 - app - __init__.py- DEBUG - 验证函数入口execute;
2016-06-02 21:37:10,820 - app - __init__.py- DEBUG - 验证模块idc是否存在;
2016-06-02 21:37:10,824 - app - __init__.py- DEBUG - 当前延迟加载的类为：<module 'modules.idc' from '/vagrant/modules/idc.pyc'>！
2016-06-02 21:37:10,824 - app - __init__.py- DEBUG - 验证模块idc是否有此函数getIdc;
2016-06-02 21:37:10,824 - app - __init__.py- DEBUG - 当前模块idc查找函数getIdc成功;
2016-06-02 21:37:10,825 - app - __init__.py- DEBUG - 验证Json的id要素;
2016-06-02 21:37:10,825 - app - __init__.py- DEBUG - 验证Json的id要素成功;
2016-06-02 21:37:10,825 - app - __init__.py- DEBUG - 验证Json的jsonRpcVersion要素;
2016-06-02 21:37:10,825 - app - __init__.py- DEBUG - 验证Json的jsonRpcVersion要素成功;
2016-06-02 21:37:10,826 - app - __init__.py- DEBUG - 验证是否需要登录;
2016-06-02 21:37:10,826 - app - __init__.py- DEBUG - 该调用在白名单内，无需登录！
2016-06-02 21:37:10,829 - app - __init__.py- DEBUG - 验证通过execute;
2016-06-02 21:37:10,829 - app - __init__.py- DEBUG - json数据通过验证，等待调用方法并返回结果！
2016-06-02 21:37:10,829 - app - __init__.py- DEBUG - 组装调用成功返回的json信息;
2016-06-02 21:37:10,834 - app - views.py- DEBUG - 请求json数据为： {"jsonRpcVersion": "1.0", "params": {"idcId": "2"}, "method": "idc.getIdc_err", "auth": "kch", "id": "2"}
2016-06-02 21:37:10,835 - app - __init__.py- DEBUG - ======初始化：JsonRpc类======！
2016-06-02 21:37:10,836 - app - __init__.py- DEBUG - 初始化：Response_preform类！
2016-06-02 21:37:10,836 - app - __init__.py- DEBUG - 初始化：LazyImport类！
2016-06-02 21:37:10,840 - app - __init__.py- DEBUG - 验证函数入口execute;
2016-06-02 21:37:10,840 - app - __init__.py- DEBUG - 验证模块idc是否存在;
2016-06-02 21:37:10,841 - app - __init__.py- DEBUG - 当前延迟加载的类为：<module 'modules.idc' from '/vagrant/modules/idc.pyc'>！
2016-06-02 21:37:10,841 - app - __init__.py- DEBUG - 验证模块idc是否有此函数getIdc_err;
2016-06-02 21:37:10,841 - app - __init__.py- ERROR - 当前模块idc查找函数getIdc_err失败;
2016-06-02 21:37:10,842 - app - __init__.py- DEBUG - 执行函数validata_hasFunction验证失败;
2016-06-02 21:37:10,842 - app - __init__.py- DEBUG - 验证Json的id要素;
2016-06-02 21:37:10,843 - app - __init__.py- ERROR - 验证Json的id要素失败;
2016-06-02 21:37:10,843 - app - __init__.py- DEBUG - 执行函数validata_id验证失败;
2016-06-02 21:37:10,844 - app - __init__.py- DEBUG - 验证Json的jsonRpcVersion要素;
2016-06-02 21:37:10,844 - app - __init__.py- ERROR - 验证Json的jsonRpcVersion要素失败;
2016-06-02 21:37:10,844 - app - __init__.py- DEBUG - 执行函数validata_version验证失败;
2016-06-02 21:37:10,845 - app - __init__.py- DEBUG - 验证是否需要登录;
2016-06-02 21:37:10,845 - app - __init__.py- ERROR - 你需要登录后才能访问此方法！
2016-06-02 21:37:10,846 - app - __init__.py- DEBUG - 执行函数validata_withoutlogin验证失败;
2016-06-02 21:37:10,847 - app - __init__.py- ERROR - jsonrpc调用失败，详见系统后台日志！
2016-06-02 21:37:10,848 - app - __init__.py- DEBUG - 通过函数组装调用失败返回的json信息;
2016-06-02 21:37:10,854 - app - views.py- DEBUG - 用户请求的content-type为： application/json_err, 不予处理

```
##笔记&&debug

###vagrant用户下链接mysql报错：
(python27env) [vagrant@OpsDev2 Lesson02]$ mysql -uroot -proot123
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)
#### 数据库没有启动
http://www.cnblogs.com/eoiioe/archive/2008/12/28/1363947.html
####当前用户没有权限
(python27env) [vagrant@OpsDev2 Lesson02]$ mysql -uroot -proot123
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

##运行flask

  python manage.py runserver -h 0.0.0.0 -p 8000

###问题：在vagrant 中启动flask后，在宿主机上无法通过端口访问
原因：没有做宿主机到 vagrant虚拟机的端口映射
解决：编辑Vagrantfile，加入
  config.vm.network "forwarded_port", guest: 8000, host: 8000


##安装MySQL
sudo yum install mysql mysql-devel mysql-server -y
###
修改默认编码为utf8
mysql配置文件/etc/my.cnf中加入default-character-set=utf8

```shell
(python27env) [vagrant@OpsDev2 Lesson02]$ sudo su -
[root@OpsDev2 ~]# vi /etc/my.cnf

```

[root@OpsDev2 ~]# service mysqld start

mysqladmin -uroot password root1234
[root@OpsDev2 ~]# mysql -uroot -proot1234

##使用pip工具时提示没有权限
```shell
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/data/python27env/lib/python2.7/site-packages/sqlalchemy'
```
原因：当前vagrant用户对 /data/python27env/ 没有操作权限

```shell
(python27env) [vagrant@OpsDev2 python27env]$ sudo su -
[root@OpsDev2 ~]# pwd
/root
[root@OpsDev2 ~]# chown -R vagrant /data/python27env/
[root@OpsDev2 ~]# exit
logout
(python27env) [vagrant@OpsDev2 python27env]$ pwd
/data/python27env
(python27env) [vagrant@OpsDev2 python27env]$ ls -la
total 28
drwxr-xr-x. 6 vagrant root 4096 May 15 02:37 .
drwxr-xr-x. 3 root    root 4096 May 15 02:36 ..
drwxr-xr-x. 2 vagrant root 4096 May 15 02:37 bin
drwxr-xr-x. 2 vagrant root 4096 May 15 02:36 include
drwxr-xr-x. 3 vagrant root 4096 May 15 02:36 lib
-rw-r--r--. 1 vagrant root   60 May 15 02:36 pip-selfcheck.json
drwxr-xr-x. 3 vagrant root 4096 May 15 02:37 share
```
##扩展阅读
基于virtualenv 可以很好的完成环境隔离，保证对每个应用的环境是干净的。而且对一个干净的环境可以通过：
pip freeze > requirements.txt将包依赖信息保存在requirements.txt文件
pip install -r requirements.txt会自动从网上下载并安装所有包
##扩展阅读
如果你希望 python 将一个文件夹作为 package 对待，那么这个文件夹中必须包含一个名为 __init__.py 的文件，即使它是空的。 参见： Packages 
如果你需要 python 讲一个文件夹作为 package 执行，那么这个文件夹中必须包含一个名为 __main__.py 的文件，

##扩展阅读
Anaconda
打造python IDE
 
Anaconda turns your Sublime Text 3 in a full featured Python development IDE including autocompletion, code linting, IDE features, autopep8 formating, McCabe complexity checker and Vagrant for Sublime Text 3



