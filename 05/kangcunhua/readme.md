#目录
[TOC]
#作业

##第五次作业：

### 作业1：批量创建主机，加入新建的network组，并指定模版
+ 创建一个Reboot-network组
+ 获取Reboot-network组id
+ 准备5台网络设置
+ 批量创建主机，并加入到network组 ,将这指机器加上  Template SNMP Device 这个模板


```shell
[
    {"ip","10.20.31.100", "host": "juniper-device-01"},
    {"ip","10.20.31.101", "host": "juniper-device-02"},
    {"ip","10.20.31.102", "host": "juniper-device-03"},
    {"ip","10.20.31.103", "host": "juniper-device-04"},
    {"ip","10.20.31.104", "host": "juniper-device-05"},
]
```

备注： 走snmp 端口为161

### 作业2： 将zb里的host同步缓存表(zb_host)
    字段信息
        hostid
        host
        ip
        port
        server_id

```shell
    host.get(output=['hostid', 'host', 'ip', "port"])   ip,port怎么取 ?
    [
        {
            "hostid": 10021,
            "host": "yz-ms-web-01",
            "ip": "192.168.99.13",
            "port": "10051"
            "server_id": 22
        }
        {
            "hostid": 10022,
            "host": "yz-ms-web-02",
            "ip": "192.168.99.14",
            "port": "10051"
            "server_id": 21
        }
    ]
```
### 作业3： 将CMDB里的信息同步到缓存表里

```shell
    server.get(output=["server_id", "hostname", "ip"])
```
+ 已知
    + 哪些host在zb里
        + pass
    + 哪些不在zb里
        + s.host.create()

+ 后续同步
    + 检查hostname, ip， port，有没有变更
    + s.host.update()
    + 更新缓存表


### 挑战1：  flask + uwsgi + nginx


### 挑战2： 一批机器突然故障，运维已知， 想要关掉报警， 但不能关数据采集
作业： 主机维护 

主机，维护的起始时间 ： 不触发报警，但是信息采集正常


##测试：
+ 启动vagrant
    - sublime 左栏Lesson03目录，右键“Open Glue Terminal”
    - vagrant up default
    - 注：因为是听到第五次课时，回头补上的第四次作业，所以vagrant虚拟机多了几个，此时启动要加上指定vm，此处是default
    - 同理，关闭vm也是 vagrant halt default
+ 启动MySQL
    - ssh 127.0.0.1 2222
    - sudo /etc/init.d/mysqld start
+ 启动webserver
    - ssh 127.0.0.1 2222
    - cd /vagrant
    - python manage.py runserver -h 0.0.0.0 -p 8000
+ 打印日志
    - 复制ssh隧道
    - cd /vagrant 
    - tail -f flask.log
##zabbix
+ 启动MySQL sudo /etc/init.d/mysqld start
+ 启动server sudo service zabbix-server start
+ 启动web管理界面 sudo /etc/init.d/httpd start

+ 启动agent    sudo service zabbix-agent start
+ 访问web管理 http://192.168.99.14/zabbix/
    - Admin/zabbix
+ 重启web sudo service httpd restart

##进度
+ cmdb
    + 首页： http://127.0.0.1:8000/dashboard/
    + IT资产-->IDC信息：  http://127.0.0.1:8000/resources/idc/ 
        - 列表，添加、修改、删除
    + IT资产-->服务器：  列表 http://127.0.0.1:8000/resources/server/list/
            - 添加页面 http://127.0.0.1:8000/resources/server/add/
            - 修改页面 http://127.0.0.1:8000/resources/server/modify/1
    + 修正server_edit.html模块的缺陷：如果不变更 制造商字段时，提交manufacturers空数据；
    + 修正models.py中的DB表定义：idc，server，cabinet中的idc.id字段由字符串改为整型；并修订对应模版缺陷；
    + 变更字段类型时，需先注释掉该字段，migrate & upgrade，然后加上修改后的字段，migrate & upgrade；最后登录数据库维护该字段即可；
    + 在modules的__init__.py中定义BaseDao类，将对各个模块的CRUD抽象封装；使用时只需传入对应的表models类即可
    + 其实让各模块操作类继承BaseDao最好，但是这么做就需要修订JsonRPC调用代码：得声明类对象。暂保持与大家代码的兼容；
+ 监控和zabbix
    + 采集监控信息 /test/collector/sysinfo.py
    + 测试zabbix，get版本信息 /test/testzabbix.py
    + 上报采集到的信息 /test/collector/sysinfo.py 
        + url = "http://192.168.99.10:8000/resources/server/reporting/"
+ 未全部完成 作业1：批量创建主机，加入新建的network组，并指定模版
    + 指定模版  Template SNMP Device 时报错，暂未能处理
        + response的内容：{"jsonrpc":"2.0","error":{"code":-32602,"message":"Invalid params.","data":"Cannot find host interface on \"juniper-device-01\" for item key \"ifDescr\"."},"id":1}
    + 指定普通模版 Reboot_template 没问题  
+ 完成 作业2： 将zb里的host同步缓存表(zb_host) 
+ 完成 作业3： 将CMDB里的信息同步到缓存表里


# 在cmdb服务器安装插件
pip install zabbix-client -i https://pypi.doubanio.com/simple/


##其他开发日志：
###AssertionError: View function mapping is overwriting an existing endpoint function: main.resources_idc_modify
原因：app/main下对应的路由函数有重名
###Zabbix server is not running:the information displayed may not be current.
原因：明明是启动了的。是Selinx没有关闭，关掉即可；
##需要注意的地方
centos6.5关闭selinux、iptables、ipv6
http://blog.chinaunix.net/xmlrpc.php?r=blog/article&uid=29302591&id=4829027
1、关闭selinux
/usr/sbin/setenforce 0 立刻关闭selinux
/usr/sbin/getenforce 1 立刻开启selinux
永久更改
vim /etc/selinux/config
#SELINUX=enforcing
#SELINUXTYPE=targeted
SELINUX=disabled
重启系统
2、关闭防火墙
/sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT
/sbin/iptables -I INPUT -p tcp --dport 22 -j ACCEPT
/etc/rc.d/init.d/iptables save
永久性关闭防火墙：
#chkconfig --level 35 iptables off (注意中间的是两个英式小短线;重启)
3、关闭ipv6
1）、vim /etc/sysconfig/network     追加
NETWORKING_IPV6=no
2）、vim /etc/hosts
#::1    localhost localhost6 localhsot6.localdomai6
3）、新建/etc/modprobe/ipv6off.conf文件（名字随便取）
添加内容
alias net-pf-10 off
options ipv6 disable=1

##输出
### 采集监控信息
```shell
(python27env) [vagrant@reboot-devops-02 collector]$ python sysinfo.py 
======测试get sysinfo:======
{'server_disk': '9', 'ipinfo': '[{"ip": "192.168.99.10", "mac": "08:00:27:d3:fb:d0"}]', 'server_type': 'VirtualBox', 'server_cpu': 'Intel(R) Core(TM) i5-4300M CPU @ 2.60GHz 1', 'hostname': 'reboot-devops-02', 'vm_status': 0, 'manufacturers': 'innotek GmbH', 'server_mem': 996, 'sn': '0', 'os': 'CentOS 6.6 Final', 'manufacture_date': '2006-12-01', 'uuid': '50FB326E-361B-4F0C-938C-A73D06902989'}
(python27env) [vagrant@reboot-devops-02 collector]$ 

```
### 测试zabbix
```shell
(python27env) [vagrant@reboot-devops-02 test]$ python testzabbix.py 
======发送正常数据测试zabbix返回执行结果：======
response的状态：200
response的内容：{"jsonrpc":"2.0","result":"2.4.8","id":1}
(python27env) [vagrant@reboot-devops-02 test]$ 

```
###webserver端输出
```shell


```
###日志输出
```shell


```
###mysql输出
```sql


```

##笔记
###Alembic cannot automatically detect

    http://stackoverflow.com/questions/12409724/no-changes-detected-in-alembic-autogeneration-of-migrations-with-flask-sqlalchem
    Alembic cannot automatically detect table or column renames. By default it will not look for column type changes either, but the compare_type option can be enabled for this.

    Excerpt from the Alembic documentation:

    Autogenerate will by default detect:

    Table additions, removals.
    Column additions, removals.
    Change of nullable status on columns.
    Autogenerate can optionally detect:

    Change of column type. This will occur if you set compare_type=True on EnvironmentContext.configure(). The feature works well in most cases, but is off by default so that it can be tested on the target schema first. It can also be customized by passing a callable here; see the function’s documentation for details.
    Change of server default. This will occur if you set compare_server_default=True on EnvironmentContext.configure(). This feature works well for simple cases but cannot always produce accurate results. The Postgresql backend will actually invoke the “detected” and “metadata” values against the database to determine equivalence. The feature is off by default so that it can be tested on the target schema first. Like type comparison, it can also be customized by passing a callable; see the function’s documentation for details.
    Autogenerate can not detect:

    Changes of table name. These will come out as an add/drop of two different tables, and should be hand-edited into a name change instead.
    Changes of column name. Like table name changes, these are detected as a column add/drop pair, which is not at all the same as a name change.
    Special SQLAlchemy types such as Enum when generated on a backend which doesn’t support ENUM directly - this because the representation of such a type in the non-supporting database, i.e. a CHAR+ CHECK constraint, could be any kind of CHAR+CHECK. For SQLAlchemy to determine that this is actually an ENUM would only be a guess, something that’s generally a bad idea. To implement your own “guessing” function here, use the sqlalchemy.events.DDLEvents.column_reflect() event to alter the SQLAlchemy type passed for certain columns and possibly sqlalchemy.events.DDLEvents.after_parent_attach() to intercept unwanted CHECK constraints.
    Autogenerate can’t currently, but will eventually detect:

    Free-standing constraint additions, removals, like CHECK, UNIQUE, FOREIGN KEY - these aren’t yet implemented. Right now you’ll get constraints within new tables, PK and FK constraints for the “downgrade” to a previously existing table, and the CHECK constraints generated with a SQLAlchemy “schema” types Boolean, Enum.
    Index additions, removals - not yet implemented.
    Sequence additions, removals - not yet implemented.
    UPDATE: some of the items in this last list are supported in the Alembic 0.7.x releases.