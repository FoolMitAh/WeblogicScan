#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
from urllib.parse import urlparse

logging.basicConfig(filename='Weblogic.log',
                    format='%(asctime)s %(message)s',
                    filemode="w", level=logging.INFO)


class ManageProcessor(object):
    PLUGINS = {}

    def process(self, target, plugins=()):
        o = urlparse(target)
        ip = o.hostname
        port = o.port if o.port is not None else 80
        if plugins is ():
            for plugin_name in self.PLUGINS.keys():
                try:
                    print(Color.OKYELLOW + "[*]开始检测", ip, port, plugin_name + Color.ENDC)
                    if self.PLUGINS[plugin_name]().process(ip, port):
                        logging.info("[+] {} {} {}".format(ip, port, plugin_name))
                        print(Color.OKGREEN + "[+]", ip, port, plugin_name + Color.ENDC)
                except BaseException:
                    print(Color.WARNING + "[-]{} 未成功检测，请检查网络连接或或目标存在负载中间件".format(plugin_name) + Color.ENDC)
        else:
            for plugin_name in plugins:
                try:
                    print(Color.OKYELLOW + "[*]开始检测", ip, port, plugin_name + Color.ENDC)
                    self.PLUGINS[plugin_name]().process(ip, port)
                except BaseException:
                    print(Color.WARNING + "[-]{} 未成功检测，请检查网络连接或或目标存在负载中间件".format(plugin_name) + Color.ENDC)
        return

    @classmethod
    def plugin_register(cls, plugin_name):
        def wrapper(plugin):
            cls.PLUGINS.update({plugin_name: plugin})
            return plugin
        return wrapper


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[90m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\33[93m'
    WARNING = '\033[91m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
