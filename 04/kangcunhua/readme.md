#目录
[TOC]
#作业

完成各个模块
优化模块：抽出重复的代码，比如各个模块的CRUD抽象出来基类，对应模块CRUD操作继承基类即可


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

##进度
+ 首页： http://127.0.0.1:8000/dashboard/
+ IT资产-->IDC信息：  http://127.0.0.1:8000/resources/idc/ 
    - 列表，添加、修改、删除
+ IT资产-->服务器：  列表 http://127.0.0.1:8000/resources/server/list/
        - 添加页面 http://127.0.0.1:8000/resources/server/add/
        - 添加功能尚未完成

##其他开发日志：

##需要注意的地方


##输出
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