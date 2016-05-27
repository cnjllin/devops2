#目录
[TOC]
# 写一个JsonRPC处理模块
JsonRPC简介
http://blog.csdn.net/mhmyqn/article/details/39718097
JSON-RPC是一个无状态的、轻量级的远程过程调用（RPC）协议。本规范主要围绕它的处理方式定义了几个数据结构和规则。这个概念可用于在同一进程中、套接字或HTTP之间、或其他很多消息传递的环境中传输数据。它使用JSON (RFC 4627)作为数据格式。
http://www.jsonrpc.org/specification

## errcode | errmsg
+ 101  模块不存在
+ 102  模块加载失败
+ 103  指定模块下的函数不存在
+ 104  jsonrpc版本不对，应该是2.0
+ 105  id不正确，应该是1

"""
## 发送的格式
```json
{
    "jsonrpc": "2.0",
    "method":"host.get",
    "id":1,
    "auth":None,
    "params":{}
}
```
## 返回的格式
```json
{
    "jsonrpc": "2.0",
    "result": response.data,
    "id": 1
}
```
## 出错时的格式
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "error_code": errno,
    "errmsg": data,
}
```

##测试 动态导入函数 __import__
```python
In [22]: mn = "tt.jsontest"

In [23]: module = __import__(mn)

In [24]: module
Out[24]: <module 'tt' from 'tt/__init__.pyc'>

In [25]: module = __import__(mn,fromlist=["jsontest"])

In [26]: module
Out[26]: <module 'tt.jsontest' from 'tt/jsontest.py'>

In [28]: module.getidc()
Out[28]: 'test getidc() suss!'

In [29]: !tree tt*
tt
├── __init__.py
└── jsontest.py

0 directories, 2 files

In [30]: !more tt/jsontest.py
def getidc():
    return "test getidc() suss!"
```

###__init__.py的作用
文件夹下面必须有此文件，该文件夹才会被识别成package
此时使用动态导入时，才不会报错，找不到**模块


#开发环境的搭建


##课程用到的软件
+ gliffy：轻快的流程绘图软件
+ CentOS 6/7
+ GIT：代码管理
+ PyCharm:开发IDE
+ Vagrant Manager 方便的 Vagrant 机器管理工具

##开发环境如何快速搭建
+ vagrant + virtual box
+ 不使用vagrant也可以，有linux运行环境即可

###安装
+ Virtual Box，添加到环境变量Path；
+ 安装vagrant；
+ 添加box镜像；

```log
cd F:\Dev_Soft\vagrant   //镜像所在目录
vagrant box add "centos6.6" centos-6.6-x86_64.box

vagrant box --help
vagrant box list
```
###关闭和移除的命令

+. vagrant halt // 关闭虚拟机镜像
+. vagrant box list
+. vagrant box remove "centos6.6" // 移除名字为"centos6.6"的镜像

##初始化开发环境目录
+. vagrant init "centos6.6"
+. vagrant up  //启动当前目录的vm
+. vagrant ssh //linux & mac可以直接登录vm了
+.             //windows 需要用客户端
+. vagrant halt //关机
+. vagrant global-status
+. vagrant reload //让配置生效
###修改对应的vagrant配置
+ vagrantfile 
+ config.vm.hostname = "OpsDev2"
+ # 文件同步目录
+ config.vm.synced_folder "../data", "/vagrant_data"
+ config.vm.synced_folder "../PythonHome/Python_DevOps2", "/PythonHome/wwwroot"
##修改默认镜像地址
+ 在VirtualBox中设置：管理-->全局设定-->常规-->默认虚拟电脑位置
+ 比如, F:\per5\Devops_centos
+ 再次添加镜像、初始化环境、初始化开发目录 
+ SSH连接测试本地和VM之间的地址映射是否正常


##修改镜像编码
+ sudo su - //切换到root用户
+ /etc/sysconfig/i18n
+ LANG="de_DE.UTF-8"
+ 改为：
+ LANG="en_US.UTF-8"

+ . /etc/sysconfig/i18n

##修改当前时区

```shell
[root@OpsDev2 ~]# date -R
Fri, 27 May 2016 03:31:41 +0200
[root@OpsDev2 ~]# /etc/localtime
-bash: /etc/localtime: Permission denied
[root@OpsDev2 ~]# date
Fri May 27 03:43:49 CEST 2016

[root@OpsDev2 ~]# vi /etc/sysconfig/clock
[root@OpsDev2 ~]# cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
cp: overwrite `/etc/localtime'? y
[root@OpsDev2 ~]# date
Fri May 27 10:01:58 CST 2016

```

##修改yum源
+ http://www.ruooo.com/VPS/594.html
+ CentOS系统更换软件安装源
+ 第一步：备份你的原镜像文件，以免出错后可以恢复。

+ mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
+ 第二步：下载新的CentOS-Base.repo 到/etc/yum.repos.d/
+ CentOS 5
+ wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo
+ CentOS 6
+ wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
+ 第三步：运行yum makecache生成缓存

+ yum makecache
##安装必要的依赖包

yum -y install gcc gcc-c++ zlib-devel openssl-devel readline-devel
+ zilib-devel MySQL安装需要
+ openssl-devel 通过easyinstall或pip 安装软件时走的是HTTPS协议

## 安装工具包 tree等
tree ，lasz
待补

##手动编译安装Python2.7
```shell
[root@bogon ~]# python -V
Python 2.6.6

[root@bogon ~]# cd /vagrant_data/
[root@bogon vagrant_data]# ls 
12.txt  pip-8.1.1.tar.gz  Python-2.7.11.tgz  setuptools-20.10.1.tar.gz
[root@bogon vagrant_data]# tar -xzf Python-2.7.11.tgz
[root@bogon vagrant_data]# cd Python-2.7.11

./configure --help
./configure --prefix=/usr/local/python27
make 
make install
python -V          # 查看版本
```
### 软连接
本地镜像没有过执行这两条命令

```shell
mv /usr/bin/python /usr/bin/python26
ln -s /usr/local/python27/bin/python /usr/bin/python
```
##安装python工具
```shell
tar -xzf setuptools-20.10.1.tar.gz 
cd setuptools-20.10.1
/usr/local/python27/bin/python setup.py install
```
### pip编译安装
```shell
/usr/local/python27/bin/python setup.py build
/usr/local/python27/bin/python setup.py install

/usr/local/python27/bin/pip install virtualenv
mkdir /data
/usr/local/python27/bin/virtualenv /data/python27env
source /data/python27env/bin/activate
pip list
pip install ipython
ipython
```
