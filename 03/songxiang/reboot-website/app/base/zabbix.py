#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "SONG Xiang"

from flask import current_app
from zabbix_client import ZabbixServerProxy
from app.models import db, Zbhost, Server
"""
    对zabbix的所有操作
    zbhost(中间表)的所有操作
"""

class Zabbix(object):
    def __init__(self):
        self.url = current_app.config.get("ZABBIX_API_UIL")
        self.username = current_app.config.get("ZABBIX_API_USER")
        self.password = current_app.config.get("ZABBIX_API_PASS")
        self._login()
    def _login(self):
        self.zb = ZabbixServerProxy(self.url)
        self.zb.user.login(user=self.username, password=self.password)

    def __del__(self):
        self.zb.user.logout()

    def get_hostgroup(self):
        return self.zb.hostgroup.get(output=["groupid","name"])

    def _create_host(self, params):
        try:
            return self.zb.host.create(**params)
        except Exception as e:
            return e.data

    def create_zb_host(self, hostname, ip, groupid=2):

        """
         创建zabbix 监控主机
        :return:
        """
        data = {
            "host": hostname,
            "interfaces":{
                "type":1,
                "main":1,
                "useip":1,
                "ip":ip,
                "dns":1,
                "port": "10050",
            },
            "groups": [
                {
                    "groupid": groupid
                }
            ]
        }
        return self._create_host(data)

    def get_hosts(self):
        return self.zb.host.get(output=["hostid","host"])

    def get_interfaces(self, ids):
        """
        获取host 的ip
        :param ids:
        :return:
        """
        interface = self.zb.hostinterface.get(hostids = ids, output=["hostid","ip"])
        ret = {}
        for it in interface:
            ret[it["hostid"]] = it["ip"]
        return ret

    def get_templates(self, ids):
        return self.zb.template.get(hostids = ids, output = ["templateid", "name"])

    def unlink_template(self, hostid, templateid):
        templates = [{"templateid": templateid}]
        return self.zb.host.update(hostid = hostid, templates_clear=templates)

    def replace_template(self, hostid, templateids):
        templates = []
        for id in templateids:
            templates.append({"templateid": id})
        try:
            ret = self.zb.host.update(hostid = hostid, templates = templates)
            return ret
        except Exception as e:
            return e.args



def rsync_zabbix_to_zbhost():
    """
    将zabbix里的host信息同步到zbhost里
    :return:
    """
    zb = Zabbix()
    # 1   从zabbix里取出所有的host信息(hostid, host, ip)
    zabbix_hosts = zb.get_hosts()
    zabbix_hosts_interface = zb.get_interfaces([z["hostid"] for z in zabbix_hosts])
    commit = False
    for host in zabbix_hosts:
        res = db.session.query(Zbhost).filter_by(hostid=host["hostid"]).all()
        if res:
            continue
        host["ip"] = zabbix_hosts_interface[host["hostid"]]
        db.session.add(Zbhost(**host))
        commit = True
    if commit:
        db.session.commit()
    # 2   将host信息更新到表中
    # 2.1 查询记录是否存在
    # 2.2 不存在,执行插入


def rsync_server_to_zbhost():
    """
    将cmdb里的host数据更新到缓存表中
    :return:
    """
    # 1 从服务表中把主机信息取出来(id ,ip)
    # 2 根据ip去更新zbhost表中的cmdb_hostid
    hosts = db.session.query(Zbhost).all()
    servers = db.session.query(Server).filter(Server.inner_ip.in_([h.ip for h in hosts])).all()
    server_info = {}
    for s in servers:
        server_info[s.inner_ip] = s.id
    print server_info
    for h in hosts:
        if not h.cmdb_hostid:
            db.session.query(Zbhost).filter(Zbhost.id == h.id).update({"cmdb_hostid":server_info[h.ip]})
            db.session.commit()

def get_zabbix_data(hosts):
    """
    取出zabbix的主机及模板信息
    :param hosts:
    :return:
    """
    zabbix_data = db.session.query(Zbhost).filter(Zbhost.cmdb_hostid.in_([h["id"] for h in hosts])).all()
    zb = Zabbix()
    ret = []
    for zb_host in zabbix_data:
        tmp = {}
        tmp["hostname"] = zb_host.host
        tmp["templates"] = zb.get_templates(zb_host.hostid)
        # print "*"
        # print tmp["templates"]
        # print "*"
        tmp["hostid"] = zb_host.hostid
        ret.append(tmp)
    return ret

def zabbix_link_template(hostids, templates):
    """
    绑定zabbix templates
    :param hostid:
    :param templates:
    :return:
    """
    zb = Zabbix()
    ret = []
    for hostid in hostids:
        linked_template_ids = [t["templateid"] for t in zb.get_templates(hostid)]
        linked_template_ids.extend(templates)
        tmp = zb.replace_template(hostid, linked_template_ids)
        ret.append(tmp)
    return ret













