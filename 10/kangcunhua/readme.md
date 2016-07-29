[TOC]
# Panda老师课程简介
第七次课、第十次、第十一次、第十二次为Panda老师授课；


# Lesson 10
## 课程目标

+ 介绍讲课风格
+ 最后三天的讲课安排
+ git工作流及常用操作（一小时）
+ Configparser模块介绍及demo实现（十分钟）
+ logging介绍，三种常用的demo实现（半小时）
+ token介绍以及demo实现（20分钟）
+ mysql抽象类的讲解实现（半小时）
+ 公共基础设施编写
+ 在基础设施的基础上，实现生产环境下的用户登录和token生成 
+ rbac思想介绍

## 课程笔记

+ 01-ELK回顾及ik中文分词
    + 参见笔记  [2016.07.20ES使用Demo](document/note/2016.07.20ES使用Demo.md)
+ 02-mapping操作
    + 参见笔记  [2016.07.25_02-mapping操作](document/note/2016.07.25_02-mapping操作.md)
+ 03-es的api使用
    + 参见笔记  [2016.07.25_03-es的api使用](document/note/2016.07.25_03-es的api使用.md)
+ 04-项目演示及讲解
+ 05-configParse模块及列表字典生成式
    + 参见笔记  [2016.07.26_05-configParse模块及列表字典生成式](document/note/2016.07.26_05-configParse模块及列表字典生成式.md)
+ 06-将config和logging模块封装工具函数utils模块中
    + 参见笔记  [2017.07.26_06-将config和logging模块封装工具函数utils模块中](document/note/2017.07.26_06-将config和logging模块封装工具函数utils模块中.md)
    + 参见 demo/utils_test.py
+ 07-项目框架运行及配置flask配置文件加载详解
    + 参见笔记  [07-项目框架运行及配置flask配置文件加载详解](document/note/07-项目框架运行及配置flask配置文件加载详解.md)
+ 08-包组织代码I结构及token加密解密工具函数编写
    + 参见笔记 [2017.07.27_08-包组织代码I结构及token加密解密工具函数编写](document/note/2017.07.27_08-包组织代码I结构及token加密解密工具函数编写.md)
+ 09-框架跑通及讲解
    + 参见笔记 [2016.07.29_09-框架跑通及讲解](document/note/2016.07.29_09-框架跑通及讲解.md)

# Lesson 07
## 讲课风格

+ 是什么 -- what
    + 什么项目
    + 有哪些功能
    + 会用到哪些技术 
        + 会通过写demo的形式掌握，在正式开发时，按照项目文档拼接各种demo即可
+ 为什么 -- why
    + 项目解决了什么问题
    + 项目的使用场景介绍，及扩展
    + 离开应用场景谈技术，就是耍流氓
+ 怎么做 -- how
    + 思路--流程图、思维导图 ...
    + 实战--项目文档，功能代码分工开发
    + 代码review 代码优化
    + 项目总结，文档整理


## 课程大纲
ELK 安装配置应用

+ es的python模块及中文分词demo
+ 公共基础设施的编写
    + 配置文件管理 -- ConfigParser模块
    + 数据库连接、及工具函数抽象的类 -- 类的应用及字典和列表生成式
    + 统一日志设置 -- logging模块
    + token的创建和解码 -- md5 hashlib base64 模块 RBAC权限模型
+ 用户权限系统（RBAC） -- jsonrpc API + flask + jquery
    + 用户的增删改查-- 添加用户时必须选一个组，默认为test组
    + 组的CRUD-- admin组为超级管理员，有所有权限，其他角色定义不同的权限
    + 增删查改 -- 权限名称对应相应的URL
+ git代码管理系统
+ 代码发布系统
    + 项目的增删查改 -- 与git关联，权限和项目同表，权限不细分，简单些
    + 测试发布 -- 用户依据权限，只能操作有权限的项目
    + 申请发布 -- 根据角色，显示不同的页面
    + 发布列表 -- 所有用户可见



# 笔记链接
## [2016.06.26_ELK安装配置](document/note/2016.06.26_ELK安装配置.md)
## [2016.06.26logstash使用](document/note/2016.06.26logstash使用.md)
## [2016.06.26ES原理&插件介绍](document/note/2016.06.26ES原理&插件介绍.md)
## [2016.07.20ES使用Demo](document/note/2016.07.20ES使用Demo.md)
## [2016.07.20Kibana使用介绍](document/note/2016.07.20Kibana使用介绍.md)
## [2016.06.26Homework&sublimeconfig](document/note/2016.06.26Homework&sublimeconfig.md)
## [2016.07.25_02-mapping操作](document/note/2016.07.25_02-mapping操作.md)
## [2016.07.25_03-es的api使用](document/note/2016.07.25_03-es的api使用.md)
## [2016.07.26_05-configParse模块及列表字典生成式](document/note/2016.07.26_05-configParse模块及列表字典生成式.md)
## [2017.07.26_06-将config和logging模块封装工具函数utils模块中](document/note/2017.07.26_06-将config和logging模块封装工具函数utils模块中.md)
## [2017.07.26_07-项目框架运行及配置flask配置文件加载详解](document/note/2017.07.26_07-项目框架运行及配置flask配置文件加载详解.md)
## [2017.07.27_08-包组织代码I结构及token加密解密工具函数编写](document/note/2017.07.27_08-包组织代码I结构及token加密解密工具函数编写.md)
## [2016.07.29_09-框架跑通及讲解](document/note/2016.07.29_09-框架跑通及讲解.md)







