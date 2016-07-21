[TOC]
#ELK应用场景
+ 中小型应用场景

```shell
Logs of service #1,#2,#3[Skipper] 
--copy logs using logst-->Redis[Broker] 
--Read data from Redis-->Logstash[Indexer] 
--Stores data in Elasticsearch-->Elasticsearch 
--Reads data from ES-->Kibana
```

+ 分布式应用中用Kafka替代Redis

```shell
logs(Scribe|Fluent|Flume|Logstash|Rsyslog|Scripts|...) 
--> Kafka集群 
--> Logstash集群
--> Elasticsearch集群
--> Kibana展示
```

#安装配置
##logstash安装准备
+ 源码安装Java8。（不推荐yum安装：中文分词会有问题；配置环境变量）
    + http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
    + mkdir /usr/local/java
    + 解压即可 tar -zxf jdk-8u45-linux-x64.tar.gz -C /usr/local/java/

### 配置环境变量
vi .bash_profile

```shell
export JAVA_HOME=/usr/local/java/jdk1.8.0_45
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$CLASSPATH
```

+ 检查Java环境是否配置成功
    + java -version
+ 下载logstash
    + https://download.elastic.co/logstash/logstash/logstash-2.2.0.tar.gz 

## 安装logstash
    + 解压的对应目录即可，例如：/usr/local下：
    + tar -zxf logstash-2.2.0.tar.gz -C /usr/local/
## 安装Elasticsearch
    + https://www.elastic.co/ 官网
    + https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-2.2.0.tar.gz
    + 解压的对应目录即可，例如：/usr/local下：
## 安装kibana
    + https://download.elastic.co/kibana/kibana/kibana-4.4.0-linux-x64.tar.gz
    + 解压的对应目录即可，例如：/usr/local下：
    + tar -zxf kibana-4.4.0-linux-x64.tar.gz -C /usr/local/

##启动ELK
###启动logstash

+ /usr/local/logstash-2.2.0/bin/logstash -e 'input { stdin {} } output { stdout {} }'
+ 可以指定格式化输出：codec =>rubydebug
+ /usr/local/logstash-2.2.0/bin/logstash -e  'input { stdin{} } output { stdout { codec=>rubydebug} }'


```shell
hello
{
       "message" => "hello",
      "@version" => "1",
    "@timestamp" => "2016-07-14T02:14:20.405Z",
          "host" => "localhost.localdomain"
}
```

###启动es
```shell
[es@localhost ~]$ cd /usr/local/elasticsearch-2.2.0/bin
[es@localhost bin]$ ls
elasticsearch      elasticsearch.in.bat  elasticsearch-service-mgr.exe  elasticsearch-service-x86.exe  plugin.bat
elasticsearch.bat  elasticsearch.in.sh   elasticsearch-service-x64.exe  plugin                         service.bat
[es@localhost bin]$ ./elasticsearch -d
```
###启动kabina
```shell
[vagrant@localhost ~]$ sudo /usr/local/kibana-4.4.0-linux-x64/bin/kibana
  log   [10:41:00.370] [info][status][plugin:sense] Status changed from uninitialized to green - Ready
  log   [10:41:00.380] [info][status][plugin:kibana] Status changed from uninitialized to green - Ready
  log   [10:41:00.419] [info][status][plugin:elasticsearch] Status changed from uninitialized to yellow - Waiting for Elasticsearch
  log   [10:41:00.453] [info][status][plugin:kbn_vislib_vis_types] Status changed from uninitialized to green - Ready
  log   [10:41:00.467] [info][status][plugin:markdown_vis] Status changed from uninitialized to green - Ready
  log   [10:41:00.487] [info][status][plugin:metric_vis] Status changed from uninitialized to green - Ready
  log   [10:41:00.508] [info][status][plugin:spyModes] Status changed from uninitialized to green - Ready
  log   [10:41:00.521] [info][status][plugin:statusPage] Status changed from uninitialized to green - Ready
  log   [10:41:00.537] [info][status][plugin:table_vis] Status changed from uninitialized to green - Ready
  log   [10:41:00.569] [info][status][plugin:elasticsearch] Status changed from yellow to green - Kibana index ready
  log   [10:41:00.577] [info][listening] Server running at http://0.0.0.0:5601

```
## es用户修改密码
默认新建用户不知道密码

```shell
[vagrant@localhost ~]$ sudo su -
[root@localhost ~]# passwd es
chown -R es:es /usr/local/elasticsearch-2.2.0
```

# 笔记链接
## [2016.06.26logstash使用](document/note/2016.06.26logstash使用.md)
## [2016.06.26ES原理&插件介绍](document/note/2016.06.26ES原理&插件介绍.md)
## [2016.07.20ES使用Demo](document/note/2016.07.20ES使用Demo.md)
## [2016.07.20Kibana使用介绍](document/note/2016.07.20Kibana使用介绍.md)
## [2016.06.26Homework&sublimeconfig](document/note/2016.06.26Homework&sublimeconfig.md)




